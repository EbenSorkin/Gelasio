from __future__ import print_function, division, absolute_import
from PIL import Image, ImageChops
import requests
import os
from glob import glob
from ntpath import basename
import json
import time
import shutil
import logging

from diffbrowsers.gfregression import GFRegression, GF_PRODUCTION_URL
from diffbrowsers.browsers import test_browsers
from diffbrowsers.screenshot import ScreenShot
from diffbrowsers.utils import (
    load_browserstack_credentials,
    NoBrowserStackAuthFile
)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

class DiffBrowsers(object):
    """Class to control GF Regression and Browser Stack api."""
    def __init__(self,
                 auth=None,
                 dst_dir=None,
                 browsers=test_browsers['all_browsers'],
                 gfr_instance_url=GF_PRODUCTION_URL,
                 gfr_is_local=False):

        if not auth:
            auth = load_browserstack_credentials()
            if not auth:
                raise NoBrowserStackAuthFile

        if gfr_instance_url.endswith('/'):
            gfr_instance_url = gfr_instance_url[:-1]

        self.gf_regression = GFRegression(
            instance_url=gfr_instance_url
        )
        self.browserstack_settings = browsers
        if gfr_is_local:
            self.browserstack_settings['local'] = True
        self.screenshot = ScreenShot(auth=auth, config=self.browserstack_settings)

        self.dst_dir = dst_dir if dst_dir else 'out'
        self.stats = {'views': {},
                      'fonts': []}
        self._mkdir(self.dst_dir)

    def new_session(self, fonts_before, fonts_after):
        """Upload fonts to gfregression"""
        self.gf_regression.new_session(fonts_before, fonts_after)
        logger.info("Posting fonts to GF Regression. Be patient.")
        self.stats['fonts'] = self.gf_regression.info['fonts']

    def load_session(self, url):
        """Load a previous gf regression session"""
        self.gf_regression.load_session(url)
        self.stats['fonts'] = self.gf_regression.info['fonts']

    def diff_view(self, screenshot_view, pt=None, gen_gifs=True):
        """Return before and after images from a GF Regression view.

        Use PIL to calculate the amount of different pixels and save
        the images."""
        if not self.gf_regression.info['uuid']:
            raise Exception("Cannot make diff. Upload or load fonts first")
        view_dir = '{}_{}pt'.format(screenshot_view, pt) if pt \
                   else screenshot_view
        view_path = os.path.join(self.dst_dir, view_dir)
        self._mkdir(view_path, overwrite=True)

        logger.info('Generating {} before images'.format(screenshot_view))
        before_url = self.gf_regression.url(screenshot_view, 'before', pt)
        before_path = os.path.join(view_path, 'before')
        self._mkdir(before_path, overwrite=True)
        self.screenshot.take(before_url, before_path)

        logger.info('Generating {} after images'.format(screenshot_view))
        after_url = self.gf_regression.url(screenshot_view, 'after', pt)
        after_path = os.path.join(view_path, 'after')
        self._mkdir(after_path, overwrite=True)
        self.screenshot.take(after_url, after_path)

        diff_dir = os.path.join(view_path, 'diff')
        self._mkdir(diff_dir, overwrite=True)

        comparison = self._compare_images(before_path, after_path, diff_dir)
        r_view = '{}_{}pt'.format(screenshot_view, pt) if pt else screenshot_view
        self.stats['views'][r_view] = comparison

        if gen_gifs:
            logger.info('Generating {} gifs'.format(screenshot_view))
            gif_dir = os.path.join(view_path, 'gifs')
            self._mkdir(gif_dir, overwrite=True)
            self._gen_gifs(before_path, after_path, gif_dir)
        return comparison

    def _mkdir(self, path, overwrite=False):
        """Create a directory, if overwrite enabled rm -rf the dir"""
        if not os.path.isdir(path):
            os.mkdir(path)
        if overwrite:
            shutil.rmtree(path)
            os.mkdir(path)

    def _gen_gifs(self, dir1, dir2, out_dir):
        shared_imgs = self._matched_filenames_in_dirs(dir1, dir2, 'jpg')
        for img in shared_imgs:
            gif_filename = img[:-4] + '.gif'
            dir1_img_path = os.path.join(dir1, img)
            dir2_img_path = os.path.join(dir2, img)
            if not self._valid_imgs([dir1_img_path, dir2_img_path]):
                logger.warning(("Skipping {}. Before/after images are "
                             "corrupt").format(gif_filename))
                continue
            with Image.open(dir1_img_path) as dir1_img, \
                 Image.open(dir2_img_path) as dir2_img:
                dir1_img.save(
                    os.path.join(out_dir, gif_filename),
                    save_all=True,
                    append_images=[dir2_img],
                    loop=10000,
                    duration=1000
                )

    def _matched_filenames_in_dirs(self, dir1, dir2, ext):
        """find matching filenames in two different dirs which have a specific
        extension"""
        dir1_items = {basename(n): n for n in glob('%s/*.%s' % (dir1, ext))}
        dir2_items = {basename(n): n for n in glob('%s/*.%s' % (dir2, ext))}
        return set(dir1_items) & set(dir2_items)

    def _compare_images(self, dir1, dir2, diff_dir):
        """Compare two folders of images against each other."""
        comparisons = []

        shared_imgs = self._matched_filenames_in_dirs(dir1, dir2, 'jpg')
        for img in shared_imgs:
            dir1_img_path = os.path.join(dir1, img)
            dir2_img_path = os.path.join(dir2, img)
            diff_img_path = os.path.join(diff_dir, img)
            if not self._valid_imgs([dir1_img_path, dir2_img_path]):
                logger.warning(("Skipping {}. Before/after images are "
                             "corrupt").format(diff_img_path))
                continue
            with Image.open(dir1_img_path) as dir1_img, \
                Image.open(dir2_img_path) as dir2_img:
                comparison = compare_image(dir1_img, dir2_img, diff_img_path)
            comparisons.append((img, comparison))
        return comparisons

    def update_browsers(self, browsers):
        self.screenshot.config['browsers'] = browsers['browsers']

    def _valid_imgs(self, imgs_paths):
        for img_path in imgs_paths:
            if os.path.getsize(img_path) == 0:
                return False
        return True


def compare_image(img1, img2, out_img=None,
                  ignore_first_px_rows=200, ignore_right_px_cols=40):
    """Compare two images and return the amount of different pixels.

    ignore_first_px_rows param will ignore the first n pixel rows. This is
    useful if the images contain text which shouldn't be diffed and may
    change such as a header.

    ignore_right_px_cols param will ignore the last n pixel columns. GF Regression
    shows before and after labels in the right hand margin. We don't want these
    labels to be included in the pixel count."""
    img_diff = ImageChops.difference(img1, img2)

    pixels = list(img_diff.getdata())
    width, height = img_diff.size
    pixels = [pixels[i * width:(i + 1) * width] for i in range(height)]

    px_diff = 0
    for line in pixels[ignore_first_px_rows:]:
        for px in line[:-ignore_right_px_cols]:
            # ignore image alpha channel if exists
            r, g, b = px[:3]
            if r != 0 or g != 0 or b != 0:
                px_diff += 1
    if out_img:
        img_diff_rgb = img_diff.convert('RGB')
        img_diff_rgb.save(out_img[:-4] + '.png')
    img_diff.close()
    return px_diff

from __future__ import division, absolute_import
import logging
import browserstack_screenshots
import os
import time
from diffbrowsers.utils import download_file


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

class ScreenShot(browserstack_screenshots.Screenshots):
    """Expansion for browserstack screenshots Lib. Adds ability to
    download files"""

    def take(self, url, dst_dir):
        """take a screenshot from a url and save it to the dst_dir"""
        self.config['url'] = url
        logger.info('Taking screenshot for url: %s' % url)
        generate_resp_json = self.generate_screenshots()
        job_id = generate_resp_json['job_id']

        logger.info('Browserstack is processing: '
                    'http://www.browserstack.com/screenshots/%s' % job_id)
        screenshots_json = self.get_screenshots(job_id)
        while screenshots_json == False: # keep refreshing until browerstack is done
            time.sleep(3)
            screenshots_json = self.get_screenshots(job_id)
        for screenshot in screenshots_json['screenshots']:
            filename = self._build_filename_from_browserstack_json(screenshot)
            base_image = os.path.join(dst_dir, filename)
            try:
                download_file(screenshot['image_url'], base_image)
            except:
                logger.info('Skipping {} BrowserStack timed out'.format(
                    screenshot['image_url'])
                )

    def _build_filename_from_browserstack_json(self, j):
        """Build useful filename for an image from the screenshot json
        metadata"""
        filename = ''
        device = j['device'] if j['device'] else 'Desktop'
        if j['state'] == 'done' and j['image_url']:
            detail = [device, j['os'], j['os_version'],
                      j['browser'], j['browser_version'], '.jpg']
            filename = '_'.join(item.replace(" ", "_") for item in detail if item)
        else:
            logger.info('screenshot timed out, ignoring this result')
        return filename

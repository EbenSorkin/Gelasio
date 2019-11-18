"""
Compare VFs against static family on GF.

Test all glyphs at text sizes
"""
import argparse
import os
import logging
from diffbrowsers.gfregression import GF_PRODUCTION_URL, VIEWS
from diffbrowsers.diffbrowsers import DiffBrowsers
from diffbrowsers.browsers import test_browsers

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--fonts', nargs="+", required=True)
    parser.add_argument('-u', '--gfr-url', default=GF_PRODUCTION_URL,
                        help="Url to GFR instance")
    parser.add_argument('-l', '--gfr-local', action="store_true", default=False)
    parser.add_argument('-o', '--output-dir', help="Directory for output images",
                        required=True)
    args = parser.parse_args()

    browsers_to_test = test_browsers['vf_browsers']
    if not os.path.isdir(args.output_dir):
        os.mkdir(args.output_dir)

    diffbrowsers = DiffBrowsers(gfr_instance_url=args.gfr_url,
                                gfr_is_local=args.gfr_local,
                                dst_dir=args.output_dir,
                                browsers=browsers_to_test)

    diffbrowsers.new_session("from-googlefonts", args.fonts)
    logger.info("Generating waterfall diff")
    diffbrowsers.diff_view("waterfall")
    for pt_size in [13, 14, 15, 16]:
        logger.info("Generating images for glyphs_all at {}".format(pt_size))
        diffbrowsers.diff_view("glyphs_all", pt=pt_size)
    logger.info("Images saved to {}".format(args.output_dir))


if __name__ == '__main__':
    main()

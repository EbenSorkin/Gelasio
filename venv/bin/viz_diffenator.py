"""
Visualize any differences found with fontdiffenator
"""
import argparse
from diffbrowsers.gfregression import GF_PRODUCTION_URL, VIEWS
from diffbrowsers.diffbrowsers import DiffBrowsers
from diffbrowsers.browsers import test_browsers
import os
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('fonts_after', nargs="+", help="Fonts after paths")
    before_group = parser.add_argument_group(title="Fonts before input")
    before_input_group = before_group.add_mutually_exclusive_group(required=True)
    before_input_group.add_argument('-fb', '--fonts-before', nargs="+",
                                    help="Fonts before paths")
    before_input_group.add_argument('-gf', '--from-googlefonts', action='store_true',
                               help="Diff against GoogleFonts instead of fonts_before")


    parser.add_argument('-u', '--gfr-url', default=GF_PRODUCTION_URL,
                        help="Url to GFR instance")
    parser.add_argument('-l', '--gfr-local', action="store_true", default=False)
    parser.add_argument('-o', '--output-dir', help="Directory for output images",
                               required=True)
    args = parser.parse_args()

    browsers_to_test = test_browsers['safari_latest']

    diffbrowsers = DiffBrowsers(gfr_instance_url=args.gfr_url,
                                gfr_is_local=args.gfr_local,
                                dst_dir=args.output_dir,
                                browsers=browsers_to_test)

    fonts_before = 'from-googlefonts' if args.from_googlefonts \
                    else args.fonts_before

    diffbrowsers.new_session(fonts_before, args.fonts_after)

    views_to_diff = diffbrowsers.gf_regression.info['diffs']
    logger.info("Following diffs have been found [%s]. Genning images." % ', '.join(views_to_diff))
    for view in views_to_diff:
        logger.info("Generating images for {}".format(view))
        if view not in VIEWS:
            logger.info("Skipping view {}".format(view))
        else:
            diffbrowsers.diff_view(view, pt=32)

    logger.info("Images saved to {}".format(args.output_dir))


if __name__ == '__main__':
    main()

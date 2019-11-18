"""
Hardcore tests for families with manual hinting. This should also be run for
popular families.

"""
from __future__ import print_function, division, absolute_import, unicode_literals
import argparse
import os
import time
import logging
from diffbrowsers.diffbrowsers import DiffBrowsers
from diffbrowsers.utils import load_browserstack_credentials, cli_reporter
from diffbrowsers.browsers import test_browsers

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    
    parser.add_argument('fonts_after', nargs="+", help="Fonts after paths")
    before_group = parser.add_argument_group(title="Fonts before input")
    before_input_group = before_group.add_mutually_exclusive_group(required=True)
    before_input_group.add_argument('-fb', '--fonts-before', nargs="+",
                                  help="Fonts before paths")
    before_input_group.add_argument('-gf', '--from-googlefonts', action='store_true',
                               help="Diff against GoogleFonts instead of fonts_before")
    parser.add_argument('-o', '--output-dir', help="Directory for output images",
                        required=True)

    args = parser.parse_args()
    auth = load_browserstack_credentials()

    browsers_to_test = test_browsers['all_browsers']

    fonts_before = 'from-googlefonts' if args.from_googlefonts \
                    else args.fonts_before

    diffbrowsers = DiffBrowsers(dst_dir=args.output_dir, browsers=browsers_to_test)
    diffbrowsers.new_session(fonts_before, args.fonts_after)

    for pt in [7, 12, 24]:
        diffbrowsers.diff_view('glyphs-all', pt, gen_gifs=True)
        logger.info("Sleeping for 10 secs. Giving Browserstack api a rest")
        time.sleep(10)

    diffbrowsers.diff_view('waterfall', gen_gifs=True)
    logger.info("Sleeping for 10 secs. Giving Browserstack api a rest")
    time.sleep(10)

    diffbrowsers.browsers = test_browsers['osx_browser']
    diffbrowsers.diff_view('glyphs-modified', gen_gifs=True)

    report = cli_reporter(diffbrowsers.stats)
    report_path = os.path.join(args.output_dir, 'report.txt')
    with open(report_path, 'w') as doc:
        doc.write(report)

    print(report)


if __name__ == '__main__':
    main()

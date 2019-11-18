#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Browserdiff
~~~~~~~~~~~

Compare two sets of fonts for regressions

Caveats, script is incredibly slow due to the Browserstack api. Fonts are
matched by filenames.

See README.md for further info

Basic Usage:
gfdiffbrowsers new [fonts_after] -fb [fonts_before] -o ~/Desktop/font_img_dir

Compare against family hosted on Google Fonts:
gfdiffbrowsers new [fonts_after] -gf -o ~/Desktop/font_img_dir

Load a previous session:
gfdiffbrowsers load <url> -o ~/Desktop/font_img_dir
"""
from __future__ import print_function, division, absolute_import, unicode_literals
import argparse
import os

from diffbrowsers.diffbrowsers import DiffBrowsers
from diffbrowsers.browsers import test_browsers
from diffbrowsers.gfregression import GF_PRODUCTION_URL, VIEWS
from diffbrowsers.utils import cli_reporter
import logging

logging.basicConfig(level=logging.INFO)


def main():
    parent_parser = argparse.ArgumentParser(add_help=False)
    parent_parser.add_argument('-u', '--gfr-url', default=GF_PRODUCTION_URL,
                               help="Url to GFR instance")
    parent_parser.add_argument('-l', '--gfr-local', action="store_true", default=False,
                               help="Enable this if GFR is being run locally.")
    parent_parser.add_argument('-o', '--output-dir', help="Directory for output images",
                            required=True)
    parent_parser.add_argument('-pt', '--type-point-size',
                            help="In some views, users can control type sample size")
    parent_parser.add_argument('-b', '--browsers',
                        choices=list(test_browsers.keys()),
                        default='all_browsers',
                        help="Which set of browsers to test on")
    parent_parser.add_argument('-v', '--view', choices=VIEWS, default='waterfall')
    parent_parser.add_argument('-gif', '--output-gifs', action='store_true', default=True,
                        help="Output before and after gifs")

    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='command')

    upload_parser = subparsers.add_parser('new', parents=[parent_parser])
    upload_parser.add_argument('fonts_after', nargs="+", help="Fonts after paths")
    before_group = upload_parser.add_argument_group(title="Fonts before input")
    before_input_group = before_group.add_mutually_exclusive_group(required=True)
    before_input_group.add_argument('-fb', '--fonts-before', nargs="+",
                                  help="Fonts before paths")
    before_input_group.add_argument('-gf', '--from-googlefonts', action='store_true',
                               help="Diff against GoogleFonts instead of fonts_before")

    load_parser = subparsers.add_parser('load', parents=[parent_parser])
    load_parser.add_argument("url")

    args = parser.parse_args()

    browsers_to_test = test_browsers[args.browsers]

    diffbrowsers = DiffBrowsers(gfr_instance_url=args.gfr_url,
                                gfr_is_local=args.gfr_local,
                                dst_dir=args.output_dir,
                                browsers=browsers_to_test)

    if args.command == 'new':
        fonts_before = 'from-googlefonts' if args.from_googlefonts \
                       else args.fonts_before
        diffbrowsers.new_session(fonts_before, args.fonts_after)
    elif args.command == 'load':
        diffbrowsers.load_session(args.url)

    diffbrowsers.diff_view(args.view, args.type_point_size, args.output_gifs)

    report_path = os.path.join(args.output_dir, 'report.txt')
    with open(report_path, 'w') as doc:
        report = cli_reporter(diffbrowsers.stats)
        doc.write(report)
        print(report)


if __name__ == '__main__':
    main()

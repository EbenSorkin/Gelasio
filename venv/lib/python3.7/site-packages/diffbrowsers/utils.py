import shutil
import requests
import os
try:
    from configparser import ConfigParser
except ImportError:
    from ConfigParser import ConfigParser


CONFIG_FILE = '~/.browserstack-api-config'


class NoBrowserStackAuthFile(Exception):
    def __init__(self):
        super(NoBrowserStackAuthFile, self).__init__(
            "~/.browserstack-api-config file is missing. See README.md"
    )


def load_browserstack_credentials():
    """Load the credentials to use Browserstack's screenshot api."""
    config = ConfigParser()
    config_filepath = os.path.expanduser(CONFIG_FILE)

    if os.path.isfile(config_filepath):
        config.read(config_filepath)
        credentials = config.items('Credentials')
        return credentials[0][1], credentials[1][1]
    return None

def cli_reporter(report):
    """Simple output for report dict

    input: {'view-name' [(platform, px_difference)]}

    output: str

    e.g

    >>> reporter(diffbrowsers.report)

    Regression Report:
    Fonts: [fonts]

    View: Glyphs-All
    WARNING: Desktop_Windows_7_chrome_50.0 is different by 100px,
    WARNING: Desktop_OS_X_Yosemite_safari_8.0 is different by 80px

    View: Waterfall
    PASSED: Desktop_Windows_7_chrome_50.0 is different is the same
    PASSED: Desktop_OS_X_Yosemite_safari_8.0 is different is the same

    TODO (M Foley) this needs more work
    """
    doc = []
    doc.append('Regression Report:\n\n')
    doc.append('Fonts: ["{}"]\n'.format('", "'.join(report['fonts'])))
    for view in report['views']:
        doc.append('\nView: {}\n'.format(view))
        for platform, px_diff in report['views'][view]:
            if px_diff != 0:
                doc.append('WARNING: {} is different by {} pixels\n'.format(
                    platform, px_diff
                ))
            else:
                doc.append('PASSED: {} is the same\n'.format(platform))
    return ''.join(doc)


def download_file(url, dst_path=None):
    """Download a file from a url. If no url is specified, store the file
    as a StringIO object"""
    try:
        request = requests.get(url, stream=True)
        if not dst_path:
            return StringIO(request.content)
        with open(dst_path, 'wb') as downloaded_file:
            shutil.copyfileobj(request.raw, downloaded_file)
    except requests.exceptions.MissingSchema:
        raise Exception("url {} is not a valid file".format(url))

from __future__ import division, absolute_import
import logging
import requests
import json


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

GF_PRODUCTION_URL = 'http://www.gf-regression.com'

VIEWS = (
    'waterfall',
    'glyphs_all', 'glyphs_new', 'glyphs_missing', 'glyphs_modified',
    'marks_new', 'marks_missing', 'marks_modified',
    'mkmks_new', 'mkmks_missing', 'mkmks_modified',
    'kerns_new', 'kerns_missing', 'kerns_modified',
    'metrics_modified',
)


class UnknownGFRegressionViewError(Exception):
    def __init__(self):
        super(UnknownGFRegressionViewError, self).__init__(
        'View is not valid. Choose from [%s]' % ', '.join(VIEWS)
    )


class GFRegression:
    """Simple client for GF Regression"""
    def __init__(self, instance_url=GF_PRODUCTION_URL):
        self.instance_url = instance_url
        self._validate_instance(self.instance_url)
        self.info = {}

    def new_session(self, fonts_before, fonts_after):
        """Post fonts to GF Regression site using the api.

        If fonts_before == 'from-googlefonts', compare against fonts hosted
        on Google Fonts.

        If the fonts uploaded successfully, GF Regression will return a uuid.
        This can be used to form urls to view endpoints."""
        logger.info("Posting fonts to GF Regression")
        if fonts_before == 'from-googlefonts':
            url_upload = self.instance_url + '/api/upload/googlefonts'
            payload = [('fonts_after', open(f, 'rb')) for f in fonts_after]
        else:
            url_upload = self.instance_url + '/api/upload/user'
            payload = [('fonts_after', open(f, 'rb')) for f in fonts_after] + \
                      [('fonts_before', open(f, 'rb')) for f in fonts_before]
        request = requests.post(url_upload, files=payload)
        self.info = request.json()
        logger.info("Fonts have been uploaded, uuid: %s" % self.info['uuid'])

    def load_session(self, url):
        """Load fonts which were previously posted to GF Regression"""
        uuid = self._extract_uuid(url)
        self.info = self._session_info(uuid)

    def url(self, view, font_type, pt=None):
        """Return a url from a user's input params."""
        if view not in VIEWS:
            raise UnknownGFRegressionViewError()
        if not self.info['uuid']:
            raise Exception('No fonts uploaded or previous uuid defined')
        url = '%s/screenshot/%s/%s/%s' % (self.instance_url,
                                          self.info['uuid'], view, font_type)
        if pt:
            url = url + '/%s' % pt
        return url

    @staticmethod
    def _extract_uuid(url):
        """Extract a uuid4 subpath from a url.

        http://127.0.0.1:5000/compare/a3ec8a52-690d-4faf-b567-13a488125c62/fonts
        -->
        a3ec8a52-690d-4faf-b567-13a488125c62
        """
        segments = url.split('/')
        for idx, segment in enumerate(segments):
            dash_count = 0
            for char in segment:
                if char == '-':
                    dash_count += 1
            if dash_count == 4:
                return segments[idx]
        raise Exception('Url does not contain a valid uuid4')

    def _session_info(self, uuid):
        """Return info about the current session"""
        url = "%s/api/info/%s" % (self.instance_url, uuid)
        request = requests.get(url)
        if request.status_code != 200:
            raise Exception('url %s is invalid' % url)
        return request.json()

    def _validate_instance(self, url):
        """Confirm instance_url is a working instance of GFRegression"""
        request = requests.get(url)
        if 'Google Fonts Regression' not in request.text and \
           'Compare fonts' not in request.text:
            raise Exception(('instance_url %s is not an instance of '
                             'GF Regression' % url))

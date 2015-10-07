# -*- coding: utf-8 -*-

""" This is an integration "unit" test.
https://github.com/propertyshelf/pspolicy.homes4.base/blob/master/src/pspolicy/homes4/base/tests/test_settings.py

"""

from acaeslanoticia.policy.config import DEPENDENCIES as ZOPE2_STYLE_PRODUCTS
from acaeslanoticia.policy.config import PROFILE_ID
from acaeslanoticia.policy.config import PROJECTNAME
from acaeslanoticia.policy.testing import FUNCTIONAL_TESTING
from acaeslanoticia.policy.testing import INTEGRATION_TESTING

from plone import api
from plone.app.testing import TEST_USER_ID
from plone.app.testing import setRoles
from plone.testing.z2 import Browser

import unittest

DEPENDENCIES = [
    'brasil.gov.tiles',
    # 'acaeslanoticia.theme',
    'collective.cover',
    'collective.disqus',
    # 'collective.googlenews',
    'collective.nitf',
    'collective.opendata',
    'collective.polls',
    'collective.sitelogo',
    'collective.upload',
    'plone.api',
    'plone.app.caching',
    'ftw.avatar',
    'sc.social.like',
] + ZOPE2_STYLE_PRODUCTS


class BaseTestCase(unittest.TestCase):
    """ Base test case to be used by other tests. """

    layer = INTEGRATION_TESTING

    profile = PROFILE_ID

    def setUp(self):
        self.portal = self.layer['portal']
        self.qi = self.portal['portal_quickinstaller']
        self.p_properties = self.portal['portal_properties']
        self.wt = self.portal['portal_workflow']
        self.st = self.portal['portal_setup']


class InstallTestCase(BaseTestCase):
    """ Ensure product is properly installed. """

    def test_installed(self):
        """ This method test the default GenericSetup profile of this package. """
        self.assertTrue(self.qi.isProductInstalled(PROJECTNAME))

    def test_dependencies_installed(self):
        """ This method test that dependencies products are installed of this package. """
        expected = set(DEPENDENCIES)
        installed = self.qi.listInstalledProducts(showHidden=True)
        installed = set([product['id'] for product in installed])
        result = sorted(expected - installed)

        self.assertTrue(
            result,
            'These dependencies are not installed: ' + ', '.join(result)
        )

    def test_version(self):
        """ This method test that last version for profile of this package. """
        self.assertEqual(
            self.st.getLastVersionForProfile(PROFILE_ID), (u'1000',))


class DependenciesSettingsTestCase(BaseTestCase):
    """ Ensure package dependencies are properly configured. """

    def test_collective_upload_settings(self):
        expected = 'gif, jpeg, jpg, png, pdf, txt, ods, odt, odp, html, csv, zip, tgz, bz2'
        self.assertEqual(
            api.portal.get_registry_record(
                'collective.upload.interfaces.IUploadSettings.upload_extensions'),
            expected
        )
        self.assertEqual(
            api.portal.get_registry_record(
                'collective.upload.interfaces.IUploadSettings.max_file_size'),
            10485760
        )
        self.assertEqual(
            api.portal.get_registry_record(
                'collective.upload.interfaces.IUploadSettings.resize_max_width'),
            1024
        )
        self.assertEqual(
            api.portal.get_registry_record(
                'collective.upload.interfaces.IUploadSettings.resize_max_height'),
            768
        )

    def test_nitf_settings(self):
        self.assertEqual(
            api.portal.get_registry_record(
                'collective.nitf.controlpanel.INITFSettings.available_genres'),
            [u'Actuality', u'Anniversary', u'Current', u'Exclusive', u'From the Scene', u'Interview', u'Opinion', u'Profile']
        )
        self.assertEqual(
            api.portal.get_registry_record(
                'collective.nitf.controlpanel.INITFSettings.available_sections'),
            set([
                u'Local',
                u'Nacional',
                u'Internacional',
                u'Economía',
                u'Cultura',
                u'Opinión',
                u'Educación',
                u'Formación',
                u'Ciencia y Tecnología',
                u'Medio ambiente',
                u'Deportes',
                u'Institucionales',
                u'Anuncia con Nosotros'
            ])
        )
        self.assertEqual(
            api.portal.get_registry_record(
                'collective.nitf.controlpanel.INITFSettings.default_genre'),
            u'Current'
        )
        self.assertEqual(
            api.portal.get_registry_record(
                'collective.nitf.controlpanel.INITFSettings.default_section'),
            u'Local'
        )

    # def test_nitf_google_news(self):
    #     self.assertEqual(
    #         api.portal.get_registry_record(
    #             'collective.googlenews.interfaces.GoogleNewsSettings.portal_types'),
    #         ['collective.nitf.content']
    #     )

    def test_disqus_settings(self):
        self.assertEqual(
            api.portal.get_registry_record(
                'collective.disqus.interfaces.IDisqusSettings.activated'),
            True
        )
        self.assertEqual(
            api.portal.get_registry_record(
                'collective.disqus.interfaces.IDisqusSettings.developer_mode'),
            False
        )
        self.assertEqual(
            api.portal.get_registry_record(
                'collective.disqus.interfaces.IDisqusSettings.forum_short_name'),
            'acaeslanoticia'
        )
        self.assertEqual(
            api.portal.get_registry_record(
                'collective.disqus.interfaces.IDisqusSettings.access_token'),
            # '15796f758e24404bb965521fe85f9aa8'
            None
        )
        self.assertEqual(
            api.portal.get_registry_record(
                'collective.disqus.interfaces.IDisqusSettings.app_public_key'),
            # 'iroSK4ud2I2sLMYAqMNI56tqI1fjbCm3XQ8T5HhZGTSQfAnj9m7yBNr9GqcycA8M'
            None
        )
        self.assertEqual(
            api.portal.get_registry_record(
                'collective.disqus.interfaces.IDisqusSettings.app_secret_key'),
            # 'q3xfSJDNYvi5uwMq9Y6Whyu3xy6luxKN9PFsruE2X2qMz98xuX23GK7sS5KnIAtb'
            None
        )

    def test_social_like_settings(self):
        """Validate sc.social.like settings."""
        sp = self.p_properties.get('sc_social_likes_properties')
        self.assertTrue(sp)
        self.assertEqual('acaeslanoticia', getattr(sp, 'twittvia'))

        plugins = getattr(sp, 'plugins_enabled', [])
        self.assertIn('Facebook', plugins)
        self.assertIn('Google+', plugins)
        self.assertIn('LinkedIn', plugins)
        self.assertIn('Pinterest', plugins)
        self.assertIn('Twitter', plugins)

        p_types = getattr(sp, 'enabled_portal_types', [])
        self.assertIn('File', p_types)
        self.assertIn('Folder', p_types)
        self.assertIn('Image', p_types)
        self.assertIn('Link', p_types)
        self.assertIn('collective.nitf.content', p_types)
        self.assertIn('Document', p_types)


class NonInstallableTestCase(unittest.TestCase):
    """Ensure non installable packages are available."""

    layer = FUNCTIONAL_TESTING

    def setUp(self):
        self.portal = self.layer['portal']

    def test_opendata_available(self):
        portal_url = self.portal.absolute_url()
        browser = Browser(self.layer['app'])

        opendata_url = '{0}/{1}'.format(portal_url, '/open-data')
        browser.open(opendata_url)
        # self.assertIn('Open Data', browser.contents)

        apidata_url = '{0}/{1}'.format(portal_url, '/apidata/cms/site_info')
        browser.open(apidata_url)
        self.assertIn('Portal A.C.A. es la Noticia', browser.contents)


class UninstallTestCase(BaseTestCase):
    """ Ensure product is properly uninstalled. """

    def setUp(self):
        BaseTestCase.setUp(self)
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.qi.uninstallProducts(products=[PROJECTNAME])

    def test_uninstalled(self):
        """ This method test the uninstall GenericSetup profile of this package. """
        self.assertFalse(self.qi.isProductInstalled(PROJECTNAME))

    def test_dependencies_uninstalled(self):
        """ This method test that dependencies products are uninstalled. """
        pass

# -*- coding: utf-8 -*-

""" This is an integration "unit" test for Site Settings """

from acaeslanoticia.policy.testing import INTEGRATION_TESTING
from plone import api

import unittest


class SiteSettingsTestCase(unittest.TestCase):
    """ The class that tests the Plone Site Settings. """

    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.request = self.layer['request']
        self.portal_memberdata = api.portal.get_tool(name='portal_memberdata')
        self.portal_properties = api.portal.get_tool(name='portal_properties')
        self.mailhost = api.portal.get_tool(name='MailHost')

    def test_portal_title(self):
        """ This method test that ensure the portal title is the same. """
        self.assertTrue('Portal A.C.A. es la Noticia', self.portal.getProperty('title'))

    def test_portal_description(self):
        """ This method test that ensure the portal description is the same. """
        self.assertTrue('Portal de ACA es la Noticia (Agencia Comunicacional Alternativa)',
                        self.portal.getProperty('description'))

    def test_utf8_is_default_charset(self):
        """ This method test that the default charset is utf8. """
        self.assertEqual(self.portal_properties.site_properties.default_charset, 'utf-8')
        self.assertEqual(self.portal.email_charset, 'utf-8')

    def test_portal_memberdata_language(self):
        """ This method test that ensure the memberdata language is the same. """
        self.assertTrue('es', self.portal_memberdata.getProperty('language'))

    def test_local_time_format(self):
        """ This method test that ensure the local time format is the same. """
        self.assertEqual(self.portal_properties.site_properties.localTimeFormat, '%d %b %Y')

    def test_default_language(self):
        """ This method test that ensure the default language is the same. """
        self.assertEqual(self.portal_properties.site_properties.default_language, 'es')

    def test_livesearch_is_disabled(self):
        """ This method test that ensure the livesearch is disabled. """
        self.assertFalse(self.portal_properties.site_properties.enable_livesearch)

    def test_mailhost_smtp_host(self):
        """ This method test that ensure the mail host is the same. """
        self.assertTrue(self.mailhost.smtp_host, 'localhost')

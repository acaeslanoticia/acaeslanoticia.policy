# -*- coding: utf-8 -*-

""" This is an integration "unit" test for Site Structure """

from acaeslanoticia.policy.testing import INTEGRATION_TESTING

from plone import api

import unittest


class SiteStructureTestCase(unittest.TestCase):
    """ The class that tests the Plone Site Structure was created. """

    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        # self.member_folder = self.portal['Member']
        self.existing = self.portal.objectIds()

    def test_default_content_exclude_from_navigation(self):
        """ This method test that the default content are exclude from navigation. """
        # self.assertIn('Member', self.existing)
        # self.assertEqual(self.member_folder.getExcludeFromNav(), True)
        pass
        # self.assertEqual(self.member_folder.getExcludeFromNav(), True)

    def test_default_content_is_removed(self):
        """ This method test that the default content is removed. """
        existing = self.portal.objectIds()
        self.assertTrue('events' not in existing)
        self.assertTrue('front-page' not in existing)
        self.assertTrue('news' not in existing)

    def test_root_folders(self):
        """ This method test if the root folders are existing. """
        existing = self.portal.objectIds()
        self.assertIn('articulos', existing)
        self.assertIn('imagenes', existing)
        self.assertIn('local', existing)
        self.assertIn('nacional', existing)
        self.assertIn('internacional', existing)
        self.assertIn('economia', existing)
        self.assertIn('cultura', existing)
        self.assertIn('comunidad', existing)
        self.assertIn('opinion', existing)
        self.assertIn('educacion', existing)
        self.assertIn('formacion', existing)
        self.assertIn('ciencia-y-tecnologia', existing)
        self.assertIn('ecosocialismo-y-biodiversidad', existing)
        self.assertIn('deportes-a-c-a', existing)
        self.assertIn('logros-en-revolucion', existing)
        self.assertIn('colabora-con-a-c-a-es-la-noticia', existing)

    def test_site_default_page_defined(self):
        """ This method test if the site default page is defined. """
        self.assertEqual(self.portal.getDefaultPage(), 'portada')

    def test_articulos_folder(self):
        """ This method test if the items children of articulos folder are existing. """
        folder = self.portal['articulos']
        self.assertEqual(folder.title, u'Artículos')
        types = ('Folder', 'File', 'Image', 'Link', 'collective.nitf.content')
        self.assertEqual(folder.getImmediatelyAddableTypes(), types)
        self.assertEqual(folder.getLocallyAllowedTypes(), types)
        self.assertEqual(folder.getExcludeFromNav(), True)
        self.assertEqual(api.content.get_state(folder), 'published')

    def test_imagenes_folder(self):
        """ This method test if the items children of imagenes folder are existing. """
        folder = self.portal['imagenes']
        self.assertEqual(folder.title, u'Imágenes')
        types = ('Folder', 'Image')
        self.assertEqual(folder.getImmediatelyAddableTypes(), types)
        self.assertEqual(folder.getLocallyAllowedTypes(), types)
        self.assertEqual(folder.getExcludeFromNav(), True)
        self.assertEqual(api.content.get_state(folder), 'published')

    def test_footer_defined(self):
        """ This method test if the footer item is defined. """
        self.assertIn('pie-de-pagina', self.existing)

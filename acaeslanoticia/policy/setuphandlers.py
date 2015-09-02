# -*- coding: utf-8 -*-

from Products.ATContentTypes.lib import constraintypes
from Products.CMFPlone import interfaces as st_interfaces
from Products.CMFQuickInstallerTool import interfaces as qi_interfaces

from acaeslanoticia.policy.config import DEFAULT_CONTENT
from acaeslanoticia.policy.config import DEPENDENCIES
from acaeslanoticia.policy.config import HIDDEN_PRODUCTS
from acaeslanoticia.policy.config import HIDDEN_PROFILES
from acaeslanoticia.policy.config import MAILHOST_CONFIGURATION
from acaeslanoticia.policy.config import PROFILE_ID as PROFILE_NAME
from acaeslanoticia.policy.config import PROJECTNAME
from acaeslanoticia.policy.config import SITE_STRUCTURE

from plone import api
from zope.interface import implements

import logging
logger = logging.getLogger(PROJECTNAME)


class HiddenProducts(object):
    """ Hidden Products in portal_quickinstaller """
    implements(qi_interfaces.INonInstallable)

    def getNonInstallableProducts(self):
        products = []
        products = [p for p in HIDDEN_PRODUCTS]
        return products


class HiddenProfiles(object):
    """ Hidden profiles from the home screen to create the site """
    implements(st_interfaces.INonInstallable)

    def getNonInstallableProfiles(self):
        return HIDDEN_PROFILES


def constrain_types(folder, allowed_types):
    """ Constrain addable types in folder. """

    folder.setConstrainTypesMode(constraintypes.ENABLED)
    folder.setImmediatelyAddableTypes(allowed_types)
    folder.setLocallyAllowedTypes(allowed_types)


def createContentType(type, folder, title, subject, state, exclude_from_nav):
    """ Create common Content Types. """

    obj = api.content.create(type=type, title=title, container=folder)
    obj.setTitle(title)
    obj.reindexObject('Title')

    if subject is not None:
        obj.setSubject(subject)
        obj.reindexObject('Subject')
        logger.info('The subjects is done!')

    if exclude_from_nav is not False:
        obj.setExcludeFromNav(True)
        logger.info('The element was excluded from navigation')

    if state is not None:
        api.content.transition(obj, state)
        logger.info('The workflow transition is done')
    else:
        pass

    logger.info('Created the {0} item'.format(obj))


def disable_mail_host(site):
    """ Disabling configured smtp host before reinstalling """

    smtphost = ''
    try:
        mailHost = api.portal.get_tool('MailHost')

        if mailHost is not None:
            smtphost = mailHost.smtp_host
            mailHost.smtp_host = ''
            logger.info('Disabling configured smtp host before reinstalling: {0}'.format(smtphost,))
    except AttributeError:
        smtphost = ''

    return smtphost


def install_dependencies(site):
    """ Install Products dependencies. """

    qi = api.portal.get_tool(name='portal_quickinstaller')
    for product in DEPENDENCIES:
        if not qi.isProductInstalled(product):
            qi.installProduct(product)
            logger.info('Instalado {0}'.format(product))
        else:
            qi.reinstallProducts([product])
            logger.info('Reinstalado {0}'.format(product))


def exclude_from_navigation_default_content(site):
    """ Exclude from navigation "Members" section. """

    members = site['Members']
    members.setExcludeFromNav(True)
    # site['Members'].setExcludeFromNav(True)
    logger.info('Excluded from Nav {0} item'.format(site))


def remove_default_content(site):
    """ Remove the default Plone content. """

    for item in DEFAULT_CONTENT:
        if hasattr(site, item):
            try:
                api.content.delete(obj=site[item])
                logger.info('Deleted {0} item'.format(item))
            except AttributeError:
                logger.info('No {0} item detected. Hmm... strange. Continuing...'.format(item))


def create_site_structure(site, structure):
    """ Create and publish new site structure as defined in config.py."""

    for item in structure:
        id = item['id']
        title = item['title']
        description = item.get('description', u'')
        subject = item.get('subjects', u'')
        if id not in site:
            obj = api.content.create(site, **item)
            # publish private content or make a workflow transition
            if item['type'] not in ['Image', 'File']:
                if '_transition' not in item and api.content.get_state(obj) == 'private':
                    api.content.transition(obj, 'publish')
                elif item.get('_transition', None):
                    api.content.transition(obj, item['_transition'])
            # constrain types in folder?
            if '_addable_types' in item:
                constrain_types(obj, item['_addable_types'])
            # the content has more content inside? create it
            if '_children' in item:
                create_site_structure(obj, item['_children'])
            # add an image to all news items
            if obj.portal_type == 'News Item':
                if 'image' in item:
                    obj.setImage(item['image'])
            # set the default view to object
            if '_layout' in item:
                obj.setLayout(item['_layout'])
            # XXX: workaround for https://github.com/plone/plone.api/issues/99
            obj.setTitle(title)
            obj.setDescription(description)
            obj.setSubject(subject)
            obj.reindexObject()
            logger.debug(u'{0} fue creado y publicado'.format(title))
        else:
            logger.debug(u'Sin crear elemento \'{0}\'; ya existente este contenido'.format(title))
    logger.info('Toda la estructura del sitio creada!!!')


def set_site_default_page(site):
    """ Set front page as site default page. """
    site.setDefaultPage('portada')
    # site.manage_changeProperties(**{"default_page": 'portada'})
    logger.info(u'Definido elemento como pagina predeterminada para el Portal')


def set_footer_site(site):
    """ Rename the doormat item as "Pie de pagina" section. """

    obj = site['doormat']
    api.content.rename(obj=obj, new_id='pie-de-pagina')
    title = u'Pie de pagina'
    obj.setTitle(title)
    obj.reindexObject('Title')
    obj.setShowTitle(False)
    api.content.transition(obj, 'publish')
    logger.info('Renamed the {0} item'.format(obj))

    # Column 1
    title = u'Columna 1'
    obj = site['pie-de-pagina']['column-1']
    api.content.rename(obj=obj, new_id='columna-1')
    obj.setTitle(title)
    obj.reindexObject('Title')
    obj.setShowTitle(False)
    api.content.transition(obj, 'publish')
    logger.info('Renamed the {0} item'.format(obj))

    obj = site['pie-de-pagina']['columna-1']['section-1']
    api.content.rename(obj=obj, new_id='seccion-1')
    title = u'Sección 1'
    obj.setTitle(title)
    obj.reindexObject('Title')
    api.content.transition(obj, 'publish')
    logger.info('Renamed the {0} item'.format(obj))

    obj = site['pie-de-pagina']['columna-1']['seccion-1']['document-1']
    api.content.delete(obj=obj)
    logger.info('Deleted the {0} item'.format(obj))

    title = u'Local'
    obj_target = site['pie-de-pagina']['columna-1']['seccion-1']
    createContentType('DoormatReference', obj_target, title, None, 'publish', False)

    # Column 2
    title = u'Columna 2'
    obj_target = site['pie-de-pagina']
    obj = api.content.create(type='DoormatColumn', title=title, container=obj_target)
    obj.setTitle(title)
    obj.reindexObject('Title')
    obj.setShowTitle(False)
    api.content.transition(obj, 'publish')
    logger.info('Created the {0} item'.format(obj))

    title = u'Sección 1'
    obj_target = site['pie-de-pagina']['columna-2']
    createContentType('DoormatSection', obj_target, title, None, 'publish', False)

    title = u'Nacional'
    obj_target = site['pie-de-pagina']['columna-2']['seccion-1']
    createContentType('DoormatReference', obj_target, title, None, 'publish', False)

    # Column 3
    title = u'Columna 3'
    obj_target = site['pie-de-pagina']
    obj = api.content.create(type='DoormatColumn', title=title, container=obj_target)
    obj.setTitle(title)
    obj.reindexObject('Title')
    obj.setShowTitle(False)
    api.content.transition(obj, 'publish')
    logger.info('Created the {0} item'.format(obj))

    title = u'Sección 1'
    obj_target = site['pie-de-pagina']['columna-3']
    createContentType('DoormatSection', obj_target, title, None, 'publish', False)

    title = u'Internacional'
    obj_target = site['pie-de-pagina']['columna-3']['seccion-1']
    createContentType('DoormatReference', obj_target, title, None, 'publish', False)

    # Column 3
    title = u'Columna 3'
    obj_target = site['pie-de-pagina']
    obj = api.content.create(type='DoormatColumn', title=title, container=obj_target)
    obj.setTitle(title)
    obj.reindexObject('Title')
    obj.setShowTitle(False)
    api.content.transition(obj, 'publish')
    logger.info('Created the {0} item'.format(obj))

    title = u'Sección 1'
    obj_target = site['pie-de-pagina']['columna-3']
    createContentType('DoormatSection', obj_target, title, None, 'publish', False)

    title = u'Economía'
    obj_target = site['pie-de-pagina']['columna-3']['seccion-1']
    createContentType('DoormatReference', obj_target, title, None, 'publish', False)

    # Column 4
    title = u'Columna 4'
    obj_target = site['pie-de-pagina']
    obj = api.content.create(type='DoormatColumn', title=title, container=obj_target)
    obj.setTitle(title)
    obj.reindexObject('Title')
    obj.setShowTitle(False)
    api.content.transition(obj, 'publish')
    logger.info('Created the {0} item'.format(obj))

    title = u'Sección 1'
    obj_target = site['pie-de-pagina']['columna-4']
    createContentType('DoormatSection', obj_target, title, None, 'publish', False)

    title = u'Cultura'
    obj_target = site['pie-de-pagina']['columna-4']['seccion-1']
    createContentType('DoormatReference', obj_target, title, None, 'publish', False)

    # Column 5
    title = u'Columna 5'
    obj_target = site['pie-de-pagina']
    obj = api.content.create(type='DoormatColumn', title=title, container=obj_target)
    obj.setTitle(title)
    obj.reindexObject('Title')
    obj.setShowTitle(False)
    api.content.transition(obj, 'publish')
    logger.info('Created the {0} item'.format(obj))

    title = u'Sección 1'
    obj_target = site['pie-de-pagina']['columna-5']
    createContentType('DoormatSection', obj_target, title, None, 'publish', False)

    title = u'Comunidad'
    obj_target = site['pie-de-pagina']['columna-5']['seccion-1']
    createContentType('DoormatReference', obj_target, title, None, 'publish', False)

    # Column 6
    title = u'Columna 6'
    obj_target = site['pie-de-pagina']
    obj = api.content.create(type='DoormatColumn', title=title, container=obj_target)
    obj.setTitle(title)
    obj.reindexObject('Title')
    obj.setShowTitle(False)
    api.content.transition(obj, 'publish')
    logger.info('Created the {0} item'.format(obj))

    title = u'Sección 1'
    obj_target = site['pie-de-pagina']['columna-6']
    createContentType('DoormatSection', obj_target, title, None, 'publish', False)

    title = u'Opinión'
    obj_target = site['pie-de-pagina']['columna-6']['seccion-1']
    createContentType('DoormatReference', obj_target, title, None, 'publish', False)

    # Column 7
    title = u'Columna 7'
    obj_target = site['pie-de-pagina']
    obj = api.content.create(type='DoormatColumn', title=title, container=obj_target)
    obj.setTitle(title)
    obj.reindexObject('Title')
    obj.setShowTitle(False)
    api.content.transition(obj, 'publish')
    logger.info('Created the {0} item'.format(obj))

    title = u'Sección 1'
    obj_target = site['pie-de-pagina']['columna-7']
    createContentType('DoormatSection', obj_target, title, None, 'publish', False)

    title = u'Educación'
    obj_target = site['pie-de-pagina']['columna-7']['seccion-1']
    createContentType('DoormatReference', obj_target, title, None, 'publish', False)

    # Column 8
    title = u'Columna 8'
    obj_target = site['pie-de-pagina']
    obj = api.content.create(type='DoormatColumn', title=title, container=obj_target)
    obj.setTitle(title)
    obj.reindexObject('Title')
    obj.setShowTitle(False)
    api.content.transition(obj, 'publish')
    logger.info('Created the {0} item'.format(obj))

    title = u'Sección 1'
    obj_target = site['pie-de-pagina']['columna-8']
    createContentType('DoormatSection', obj_target, title, None, 'publish', False)

    title = u'Formación'
    obj_target = site['pie-de-pagina']['columna-8']['seccion-1']
    createContentType('DoormatReference', obj_target, title, None, 'publish', False)

    # Column 9
    title = u'Columna 9'
    obj_target = site['pie-de-pagina']
    obj = api.content.create(type='DoormatColumn', title=title, container=obj_target)
    obj.setTitle(title)
    obj.reindexObject('Title')
    obj.setShowTitle(False)
    api.content.transition(obj, 'publish')
    logger.info('Created the {0} item'.format(obj))

    title = u'Sección 1'
    obj_target = site['pie-de-pagina']['columna-9']
    createContentType('DoormatSection', obj_target, title, None, 'publish', False)

    title = u'Ciencia y Tecnología'
    obj_target = site['pie-de-pagina']['columna-9']['seccion-1']
    createContentType('DoormatReference', obj_target, title, None, 'publish', False)

    # Column 10
    title = u'Columna 10'
    obj_target = site['pie-de-pagina']
    obj = api.content.create(type='DoormatColumn', title=title, container=obj_target)
    obj.setTitle(title)
    obj.reindexObject('Title')
    obj.setShowTitle(False)
    api.content.transition(obj, 'publish')
    logger.info('Created the {0} item'.format(obj))

    title = u'Sección 1'
    obj_target = site['pie-de-pagina']['columna-10']
    createContentType('DoormatSection', obj_target, title, None, 'publish', False)

    title = u'Ecosocialismo y biodiversidad'
    obj_target = site['pie-de-pagina']['columna-10']['seccion-1']
    createContentType('DoormatReference', obj_target, title, None, 'publish', False)

    # Column 11
    title = u'Columna 11'
    obj_target = site['pie-de-pagina']
    obj = api.content.create(type='DoormatColumn', title=title, container=obj_target)
    obj.setTitle(title)
    obj.reindexObject('Title')
    obj.setShowTitle(False)
    api.content.transition(obj, 'publish')
    logger.info('Created the {0} item'.format(obj))

    title = u'Sección 1'
    obj_target = site['pie-de-pagina']['columna-11']
    createContentType('DoormatSection', obj_target, title, None, 'publish', False)

    title = u'Deportes A.C.A.'
    obj_target = site['pie-de-pagina']['columna-11']['seccion-1']
    createContentType('DoormatReference', obj_target, title, None, 'publish', False)

    # Column 12
    title = u'Columna 12'
    obj_target = site['pie-de-pagina']
    obj = api.content.create(type='DoormatColumn', title=title, container=obj_target)
    obj.setTitle(title)
    obj.reindexObject('Title')
    obj.setShowTitle(False)
    api.content.transition(obj, 'publish')
    logger.info('Created the {0} item'.format(obj))

    title = u'Sección 1'
    obj_target = site['pie-de-pagina']['columna-12']
    createContentType('DoormatSection', obj_target, title, None, 'publish', False)

    title = u'Logros en Revolución'
    obj_target = site['pie-de-pagina']['columna-12']['seccion-1']
    createContentType('DoormatReference', obj_target, title, None, 'publish', False)

    # Column 13
    title = u'Columna 13'
    obj_target = site['pie-de-pagina']
    obj = api.content.create(type='DoormatColumn', title=title, container=obj_target)
    obj.setTitle(title)
    obj.reindexObject('Title')
    obj.setShowTitle(False)
    api.content.transition(obj, 'publish')
    logger.info('Created the {0} item'.format(obj))

    title = u'Sección 1'
    obj_target = site['pie-de-pagina']['columna-13']
    createContentType('DoormatSection', obj_target, title, None, 'publish', False)

    title = u'Colabora con A.C.A es la Noticia'
    obj_target = site['pie-de-pagina']['columna-13']['seccion-1']
    createContentType('DoormatReference', obj_target, title, None, 'publish', False)

    logger.info(u'Set the footer item for Portal')


def configure_site_properties(site):
    """ Set the Site Title, Description and Properties """

    properties = api.portal.get_tool(name='portal_properties')
    memberdata = api.portal.get_tool(name='portal_memberdata')

    # Site Title and Description.
    if site.title is None or site.title is not None:
        site.title = 'Portal A.C.A. es la Noticia'
        site.description = 'Portal de ACA es la Noticia (Agencia Comunicacional Alternativa)'
        logger.info('Titulo y descripción del sitio ha sido configurado!')
    else:
        logger.info('Site title has already been changed, so NOT changing site title or description.')

    # Site properties.
    properties.site_properties.enable_livesearch = False
    properties.site_properties.localTimeFormat = '%d %b %Y'
    properties.site_properties.default_language = 'es'
    properties.site_properties.use_email_as_login = True
    properties.site_properties.enable_sitemap = True
    properties.site_properties.exposeDCMetaTags = True
    logger.info('Propiedades del sitio configuradas!')

    # Member data properties.
    memberdata.language = 'es'
    logger.info('Propiedades de datos del usuario configurados!')


def configure_mail_host(site):
    """ Configuration for MailHost tool """

    try:
        mailHost = api.portal.get_tool('MailHost')

        if MAILHOST_CONFIGURATION['configure']:
            logger.info('Starting Mail Configuration changes')
            if mailHost.smtp_host == '':
                mailHost.smtp_host = MAILHOST_CONFIGURATION['smtphost']
                logger.info(mailHost.smtp_host)
            if mailHost.smtp_port is None:
                mailHost.smtp_port = MAILHOST_CONFIGURATION['smtpport']
                logger.info(mailHost.smtp_port)
            if site.email_from_name == '':
                site.email_from_name = MAILHOST_CONFIGURATION['fromemailname']
                logger.info(site.email_from_name)
            if site.email_from_address == '':
                site.email_from_address = MAILHOST_CONFIGURATION['fromemailaddress']
                logger.info(site.email_from_address)
            logger.info('Configuracion de correo fue realizada!')

    except AttributeError:
        pass


def enable_mail_host(site, smtphost):
    """ Enabling SMTP configuration host """

    try:
        mailHost = api.portal.get_tool('MailHost')

        if mailHost is not None and smtphost != '':
            mailHost.smtp_host = smtphost
            logger.info('Enabling configured smtp host after reinstallation: {0}'.format(smtphost,))
    except AttributeError:
        pass


def setup_nitf_settings():
    """ Custom settings for collective.nitf """

    api.portal.set_registry_record(
        'collective.nitf.controlpanel.INITFSettings.available_genres',
        [u'Actuality', u'Anniversary', u'Current', u'Exclusive', u'From the Scene', u'Interview', u'Opinion', u'Profile']
    )
    api.portal.set_registry_record(
        'collective.nitf.controlpanel.INITFSettings.available_sections',
        set([
            u'Local',
            u'Nacional',
            u'Internacional',
            u'Economía',
            u'Cultura',
            u'Comunidad',
            u'Opinión',
            u'Educación',
            u'Formación',
            u'Ciencia y Tecnología',
            u'Ecosocialismo y biodiversidad',
            u'Deportes A.C.A.',
            u'Logros en Revolución',
            u'Colabora con A.C.A es la Noticia'
        ])
    )
    api.portal.set_registry_record(
        'collective.nitf.controlpanel.INITFSettings.default_genre',
        u'Current'
    )
    api.portal.set_registry_record(
        'collective.nitf.controlpanel.INITFSettings.default_section',
        u'Local'
    )

    logger.info('Configurado el tipo de contenido collective.nitf')


# def setup_nitf_google_news():
    # """ Setup collective.nitf content type in Google News """

    # api.portal.set_registry_record(
    #     'collective.googlenews.interfaces.GoogleNewsSettings.portal_types',
    #     ['collective.nitf.content']
    # )
    # logger.info('Configurado el producto collective.nitf con collective.googlenews')


# def setup_google_analytics():
    # """ Custom settings for collective.googleanalytics """

    # analytics_tool = api.portal.get_tool('portal_analytics')
    # pass


def setup_cache_settings():
    """ Custom settings for Plone caching """

    api.portal.set_registry_record(
        'plone.caching.interfaces.ICacheSettings.enabled',
        True
    )


def setup_syndication_settings():
    """ Custom settings for Plone syndication """

    api.portal.set_registry_record(
        'Products.CMFPlone.interfaces.syndication.ISiteSyndicationSettings.allowed',
        True
    )

    api.portal.set_registry_record(
        'Products.CMFPlone.interfaces.syndication.ISiteSyndicationSettings.render_body',
        True
    )

    api.portal.set_registry_record(
        'Products.CMFPlone.interfaces.syndication.ISiteSyndicationSettings.show_syndication_button',
        True
    )

    api.portal.set_registry_record(
        'Products.CMFPlone.interfaces.syndication.ISiteSyndicationSettings.show_syndication_link',
        True
    )

    logger.info('Configurado la sindicacion en Plone')


def setup_upload_settings():
    """ Custom settings for collective.upload """

    api.portal.set_registry_record(
        'collective.upload.interfaces.IUploadSettings.max_file_size',
        int(10485760)
    )

    api.portal.set_registry_record(
        'collective.upload.interfaces.IUploadSettings.upload_extensions',
        u'gif, jpeg, jpg, png, pdf, txt, ods, odt, odp, html, csv, zip, tgz, bz2'
    )

    api.portal.set_registry_record(
        'collective.upload.interfaces.IUploadSettings.resize_max_height',
        int(768)
    )

    api.portal.set_registry_record(
        'collective.upload.interfaces.IUploadSettings.resize_max_width',
        int(1024)
    )

    logger.info('Configurado el producto collective.upload')


def setup_disqus_settings():
    """ Custom settings for collective.disqus """

    api.portal.set_registry_record(
        'collective.disqus.interfaces.IDisqusSettings.activated',
        True
    )
    api.portal.set_registry_record(
        'collective.disqus.interfaces.IDisqusSettings.developer_mode',
        False
    )
    api.portal.set_registry_record(
        'collective.disqus.interfaces.IDisqusSettings.forum_short_name',
        'acaeslanoticia'
    )
    # api.portal.set_registry_record(
    #     'collective.disqus.interfaces.IDisqusSettings.access_token',
    #     u'15796f758e24404bb965521fe85f9aa8'
    # )
    # api.portal.set_registry_record(
    #     'collective.disqus.interfaces.IDisqusSettings.app_public_key',
    #     u'iroSK4ud2I2sLMYAqMNI56tqI1fjbCm3XQ8T5HhZGTSQfAnj9m7yBNr9GqcycA8M'
    # )
    # api.portal.set_registry_record(
    #     'collective.disqus.interfaces.IDisqusSettings.app_secret_key',
    #     u'q3xfSJDNYvi5uwMq9Y6Whyu3xy6luxKN9PFsruE2X2qMz98xuX23GK7sS5KnIAtb'
    # )
    logger.info('Configurado el producto collective.disqus')


def setup_social_likes_settings():
    """ Custom settings for sc.social.likes """

    properties = api.portal.get_tool(name='portal_properties')
    properties.sc_social_likes_properties.enabled_portal_types = [u'Folder', u'File', u'Image', u'Link', u'Document', u'collective.nitf.content']
    properties.sc_social_likes_properties.twittvia = 'acaeslanoticia'
    properties.sc_social_likes_properties.plugins_enabled = [u'Facebook', u'Google+', u'LinkedIn', u'Pinterest', u'Twitter']

    logger.info('Configurado el producto sc.social.likes')


def import_registry_settings():
    """ Import registry settings; we need to do this before other stuff here,
    like using a cover layout defined there.

    XXX: I don't know if there is other way to do this on ZCML or XML.
    """
    PROFILE_ID = 'profile-{0}'.format(PROFILE_NAME)
    setup = api.portal.get_tool('portal_setup')
    setup.runImportStepFromProfile(PROFILE_ID, 'plone.app.registry')
    logger.info('Imported registry settings from GenericSetup profile.')


def clear_and_rebuild_catalog(site):
    """ Clear and rebuild catalog """

    pcatalog = api.portal.get_tool(name='portal_catalog')
    pcatalog.clearFindAndRebuild()
    logger.info('Limpiado y construido de nuevo el catalogo!')


def setupVarious(context):
    """ Miscellaneous import steps for setup """
    # Ordinarily, GenericSetup handlers check for the existence of XML files.
    # Here, we are not parsing an XML file, but we use this text file as a
    # flag to check that we actually meant for this import step to be run.
    # The file is found in profiles/default.

    if context.readDataFile('acaeslanoticia.policy_various.txt') is None:
        return

    # Add additional setup code here
    portal = api.portal.get()

    # Do this first so that reinstallation will not fire any notifications if any
    old_smtphost = disable_mail_host(portal)
    install_dependencies(portal)
    exclude_from_navigation_default_content(portal)
    remove_default_content(portal)
    create_site_structure(portal, SITE_STRUCTURE)
    set_site_default_page(portal)
    set_footer_site(portal)
    configure_site_properties(portal)
    configure_mail_host(portal)
    # Do this last so that mail smtp host configured before reinstallation will be maintained.
    enable_mail_host(portal, old_smtphost)
    setup_nitf_settings()
    # setup_nitf_google_news()
    # setup_google_analytics()
    setup_cache_settings()
    setup_syndication_settings()
    setup_upload_settings()
    setup_disqus_settings()
    setup_social_likes_settings()
    # import_registry_settings()
    clear_and_rebuild_catalog(portal)

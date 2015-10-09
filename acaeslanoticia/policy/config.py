# -*- coding: utf-8 -*-

""" Contains constants used by setuphandler.py """

from acaeslanoticia.policy.utils import _add_id

PROJECTNAME = 'acaeslanoticia.policy'
PROFILE_ID = '{0}:default'.format(PROJECTNAME)

# content created at Plone's installation
DEFAULT_CONTENT = ('front-page', 'news', 'events')

DEPENDENCIES = [
    'CMFPlacefulWorkflow',
    'Doormat',
]

HIDDEN_PRODUCTS = [
    'Doormat',
    'acaeslanoticia.theme',
    'brasil.gov.tiles',
    'collective.cover',
    'collective.disqus',
    # 'collective.googlenews',
    'collective.nitf',
    'collective.js.galleria',
    'collective.js.jqueryui',
    #'collective.newsticker',
    'collective.nitf.upgrades.v1007',
    'collective.polls',
    #'collective.plonetruegallery',
    #'collective.sitelogo',
    'collective.upload',
    'collective.z3cform.colorpicker',
    'collective.z3cform.datetimewidget',
    'collective.z3cform.widgets',
    'plone.app.blocks',
    'plone.app.caching',
    'plone.app.collection',
    'plone.app.drafts',
    'plone.app.debugtoolbar',
    'plone.app.dexterity',
    'plone.app.jquery',
    'plone.app.jquerytools',
    'plone.app.intid',
    'plone.app.iterate',
    'plone.app.openid',
    'plone.app.referenceablebehavior',
    'plone.app.relationfield',
    'plone.app.tiles',
    'plone.app.theming',
    'plone.formwidget.autocomplete',
    'plone.formwidget.contenttree',
    'plone.session',
    'plonetheme.classic',
    'sc.social.like'
]

HIDDEN_PROFILES = [
    'Products.CMFPlacefulWorkflow:base',
    'Products.DataGridField:default',
    'Products.Doormat:default',
    'Products.Doormat:uninstall',
    'acaeslanoticia.theme:default',
    'brasil.gov.tiles:default',
    'collective.cover:default',
    'collective.cover:testfixture',
    'collective.cover:uninstall',
    'collective.disqus:test_fixture',
    'collective.disqus:default',
    'collective.disqus:upgrade',
    'collective.disqus:uninstall',
    #'collective.newsticker:default',
    #'collective.newsticker:uninstall',
    'collective.nitf:default',
    'collective.js.galleria:default',
    'collective.js.jqueryui:default',
    # 'collective.googlenews:uninstall',
    'collective.polls:default',
    #'collective.plonetruegallery:default',
    #'collective.plonetruegallery:uninstall',
    #'collective.plonetruegallery:upgrade_to_0_8a1',
    #'collective.sitelogo:default',
    #'collective.sitelogo:uninstall',
    'collective.upload:default',
    'collective.upload:testfixture',
    'collective.z3cform.colorpicker:default',
    'collective.z3cform.widgets:default',
    'collective.z3cform.widgets:test',
    'collective.z3cform.widgets:upgrade_1_to_2',
    'collective.z3cform.widgets:uninstall',
    'plone.app.caching:default',
    'plone.app.blocks:default',
    'plone.app.debugtoolbar:uninstall',
    'plone.app.dexterity:default',
    'plone.app.drafts:default',
    'plone.app.iterate:plone.app.iterate',
    'plone.app.querystring:upgrade_to_3',
    'plone.app.querystring:upgrade_to_5',
    'plone.app.openid:default',
    'plone.app.referenceablebehavior:default',
    'plone.app.relationfield:default',
    'plone.app.tiles:default',
    'plone.app.theming:default',
    'plone.formwidget.autocomplete:default',
    'plone.formwidget.contenttree:default',
    'plone.session:default',
    'sc.social.like:default'
]

MAILHOST_CONFIGURATION = {
    'configure': True,
    'smtphost': 'smtp.gmail.com',
    'smtpport': 587,
    'fromemailname': 'Portal A.C.A. es la Noticia',
    'fromemailaddress': 'acaeslanoticia@gmail.com'
}

# new site structure; this dictionary defines the objects that are going to be
# created on the root of the site; it also includes information about folder
# constraints and objects to be created inside them
SITE_STRUCTURE = [
    dict(
        type='collective.cover.content',
        title=u'Portada',
        description=u'Objeto que componen la página principal del sitio. (Atención: Este objeto no debe suprimirse)',
        # template_layout='ACA es la Noticia Principal',
        excludeFromNav=True,
    ),
    dict(
        type='Folder',
        title=u'Artículos',
        description=u'Artículos de noticias del sitio Web',
        _addable_types=['Folder', 'File', 'Image', 'Link', 'collective.nitf.content'],
        excludeFromNav=True,
    ),
    dict(
        type='Folder',
        title=u'Imágenes',
        description=u'Imágenes de los artículos de noticias del sitio Web',
        _addable_types=['Folder', 'Image'],
        excludeFromNav=True,
    ),
    dict(
        type='Collection',
        title=u'Lo más reciente',
        description=u'Las últimas noticias publicadas.',
        # _transition='private',
        _transition=None,
        excludeFromNav=True,
        sort_reversed=True,
        sort_on=u'effective',
        limit=1000,
        query=[
            dict(
                i='portal_type',
                o='plone.app.querystring.operation.selection.is',
                v='collective.nitf.content',
            ),
            dict(
                i='path',
                o='plone.app.querystring.operation.string.relativePath',
                v='../articulos',
            ),
            dict(
                i='review_state',
                o='plone.app.querystring.operation.selection.is',
                v=['published'],
            ),
        ],
        subjects=(u'Barra', u'Últimas', u'Noticias')
    ),
    dict(
        type='Collection',
        title=u'Local',
        description=u'Sección de noticias Local.',
        sort_reversed=True,
        sort_on=u'effective',
        limit=1000,
        query=[
            dict(
                i='portal_type',
                o='plone.app.querystring.operation.selection.is',
                v='collective.nitf.content',
            ),
            dict(
                i='path',
                o='plone.app.querystring.operation.string.relativePath',
                v='../articulos',
            ),
            dict(
                i='review_state',
                o='plone.app.querystring.operation.selection.is',
                v=['published'],
            ),
            dict(
                i='section',
                o='plone.app.querystring.operation.selection.is',
                v=['Local'],
            ),
            dict(
                i='genre',
                o='plone.app.querystring.operation.selection.is',
                v=[u'Current'],
            ),
        ],
        subjects=(u'Sección', u'Noticias', u'Local')
    ),
    dict(
        type='Collection',
        title=u'Nacional',
        description=u'Sección de noticias Nacional.',
        sort_reversed=True,
        sort_on=u'effective',
        limit=1000,
        query=[
            dict(
                i='portal_type',
                o='plone.app.querystring.operation.selection.is',
                v='collective.nitf.content',
            ),
            dict(
                i='path',
                o='plone.app.querystring.operation.string.relativePath',
                v='../articulos',
            ),
            dict(
                i='review_state',
                o='plone.app.querystring.operation.selection.is',
                v=['published'],
            ),
            dict(
                i='section',
                o='plone.app.querystring.operation.selection.is',
                v=['Nacional'],
            ),
            dict(
                i='genre',
                o='plone.app.querystring.operation.selection.is',
                v=[u'Current'],
            ),
        ],
        subjects=(u'Sección', u'Noticias', u'Nacional')
    ),
    dict(
        type='Collection',
        title=u'Internacional',
        description=u'Sección de noticias Internacional.',
        sort_reversed=True,
        sort_on=u'effective',
        limit=1000,
        query=[
            dict(
                i='portal_type',
                o='plone.app.querystring.operation.selection.is',
                v='collective.nitf.content',
            ),
            dict(
                i='path',
                o='plone.app.querystring.operation.string.relativePath',
                v='../articulos',
            ),
            dict(
                i='review_state',
                o='plone.app.querystring.operation.selection.is',
                v=['published'],
            ),
            dict(
                i='section',
                o='plone.app.querystring.operation.selection.is',
                v=['Internacional'],
            ),
            dict(
                i='genre',
                o='plone.app.querystring.operation.selection.is',
                v=[u'Current'],
            ),
        ],
        subjects=(u'Sección', u'Noticias', u'Internacional')
    ),
    dict(
        type='Collection',
        title=u'Economía',
        description=u'Sección de noticias Economía.',
        sort_reversed=True,
        sort_on=u'effective',
        limit=1000,
        query=[
            dict(
                i='portal_type',
                o='plone.app.querystring.operation.selection.is',
                v='collective.nitf.content',
            ),
            dict(
                i='path',
                o='plone.app.querystring.operation.string.relativePath',
                v='../articulos',
            ),
            dict(
                i='review_state',
                o='plone.app.querystring.operation.selection.is',
                v=['published'],
            ),
            dict(
                i='section',
                o='plone.app.querystring.operation.selection.is',
                v=['Economía'],
            ),
            dict(
                i='genre',
                o='plone.app.querystring.operation.selection.is',
                v=[u'Current'],
            ),
        ],
        subjects=(u'Sección', u'Noticias', u'Economía')
    ),
    dict(
        type='Collection',
        title=u'Cultura',
        description=u'Sección de noticias Cultura.',
        sort_reversed=True,
        sort_on=u'effective',
        limit=1000,
        query=[
            dict(
                i='portal_type',
                o='plone.app.querystring.operation.selection.is',
                v='collective.nitf.content',
            ),
            dict(
                i='path',
                o='plone.app.querystring.operation.string.relativePath',
                v='../articulos',
            ),
            dict(
                i='review_state',
                o='plone.app.querystring.operation.selection.is',
                v=['published'],
            ),
            dict(
                i='section',
                o='plone.app.querystring.operation.selection.is',
                v=['Cultura'],
            ),
            dict(
                i='genre',
                o='plone.app.querystring.operation.selection.is',
                v=[u'Current'],
            ),
        ],
        subjects=(u'Sección', u'Noticias', u'Cultura')
    ),
    dict(
        type='Collection',
        title=u'Opinión',
        description=u'Sección de noticias Opinión.',
        sort_reversed=True,
        sort_on=u'effective',
        limit=1000,
        query=[
            dict(
                i='portal_type',
                o='plone.app.querystring.operation.selection.is',
                v='collective.nitf.content',
            ),
            dict(
                i='path',
                o='plone.app.querystring.operation.string.relativePath',
                v='../articulos',
            ),
            dict(
                i='review_state',
                o='plone.app.querystring.operation.selection.is',
                v=['published'],
            ),
            dict(
                i='section',
                o='plone.app.querystring.operation.selection.is',
                v=['Opinión'],
            ),
            dict(
                i='genre',
                o='plone.app.querystring.operation.selection.is',
                v=[u'Current'],
            ),
        ],
        subjects=(u'Sección', u'Noticias', u'Opinión')
    ),
    dict(
        type='Collection',
        title=u'Educación',
        description=u'Sección de noticias Educación.',
        sort_reversed=True,
        sort_on=u'effective',
        limit=1000,
        query=[
            dict(
                i='portal_type',
                o='plone.app.querystring.operation.selection.is',
                v='collective.nitf.content',
            ),
            dict(
                i='path',
                o='plone.app.querystring.operation.string.relativePath',
                v='../articulos',
            ),
            dict(
                i='review_state',
                o='plone.app.querystring.operation.selection.is',
                v=['published'],
            ),
            dict(
                i='section',
                o='plone.app.querystring.operation.selection.is',
                v=['Educación'],
            ),
            dict(
                i='genre',
                o='plone.app.querystring.operation.selection.is',
                v=[u'Current'],
            ),
        ],
        subjects=(u'Sección', u'Noticias', u'Educación')
    ),
    dict(
        type='Collection',
        title=u'Formación',
        description=u'Sección de noticias Formación.',
        sort_reversed=True,
        sort_on=u'effective',
        limit=1000,
        query=[
            dict(
                i='portal_type',
                o='plone.app.querystring.operation.selection.is',
                v='collective.nitf.content',
            ),
            dict(
                i='path',
                o='plone.app.querystring.operation.string.relativePath',
                v='../articulos',
            ),
            dict(
                i='review_state',
                o='plone.app.querystring.operation.selection.is',
                v=['published'],
            ),
            dict(
                i='section',
                o='plone.app.querystring.operation.selection.is',
                v=['Formación'],
            ),
            dict(
                i='genre',
                o='plone.app.querystring.operation.selection.is',
                v=[u'Current'],
            ),
        ],
        subjects=(u'Sección', u'Noticias', u'Formación')
    ),
    dict(
        type='Collection',
        title=u'Ciencia y Tecnología',
        description=u'Sección de noticias Ciencia y Tecnología.',
        sort_reversed=True,
        sort_on=u'effective',
        limit=1000,
        query=[
            dict(
                i='portal_type',
                o='plone.app.querystring.operation.selection.is',
                v='collective.nitf.content',
            ),
            dict(
                i='path',
                o='plone.app.querystring.operation.string.relativePath',
                v='../articulos',
            ),
            dict(
                i='review_state',
                o='plone.app.querystring.operation.selection.is',
                v=['published'],
            ),
            dict(
                i='section',
                o='plone.app.querystring.operation.selection.is',
                v=['Ciencia y Tecnología'],
            ),
            dict(
                i='genre',
                o='plone.app.querystring.operation.selection.is',
                v=[u'Current'],
            ),
        ],
        subjects=(u'Sección', u'Noticias', u'Ciencia y Tecnología')
    ),
    dict(
        type='Collection',
        title=u'Medio ambiente',
        description=u'Sección de noticias Medio ambiente.',
        sort_reversed=True,
        sort_on=u'effective',
        limit=1000,
        query=[
            dict(
                i='portal_type',
                o='plone.app.querystring.operation.selection.is',
                v='collective.nitf.content',
            ),
            dict(
                i='path',
                o='plone.app.querystring.operation.string.relativePath',
                v='../articulos',
            ),
            dict(
                i='review_state',
                o='plone.app.querystring.operation.selection.is',
                v=['published'],
            ),
            dict(
                i='section',
                o='plone.app.querystring.operation.selection.is',
                v=['Medio ambiente'],
            ),
            dict(
                i='genre',
                o='plone.app.querystring.operation.selection.is',
                v=[u'Current'],
            ),
        ],
        subjects=(u'Sección', u'Noticias', u'Medio ambiente')
    ),
    dict(
        type='Collection',
        title=u'Deportes',
        description=u'Sección de noticias Deportes.',
        sort_reversed=True,
        sort_on=u'effective',
        limit=1000,
        query=[
            dict(
                i='portal_type',
                o='plone.app.querystring.operation.selection.is',
                v='collective.nitf.content',
            ),
            dict(
                i='path',
                o='plone.app.querystring.operation.string.relativePath',
                v='../articulos',
            ),
            dict(
                i='review_state',
                o='plone.app.querystring.operation.selection.is',
                v=['published'],
            ),
            dict(
                i='section',
                o='plone.app.querystring.operation.selection.is',
                v=['Deportes'],
            ),
            dict(
                i='genre',
                o='plone.app.querystring.operation.selection.is',
                v=[u'Current'],
            ),
        ],
        subjects=(u'Sección', u'Noticias', u'Deportes')
    ),
    dict(
        type='Collection',
        title=u'Institucionales',
        description=u'Sección de noticias Institucionales.',
        sort_reversed=True,
        sort_on=u'effective',
        limit=1000,
        query=[
            dict(
                i='portal_type',
                o='plone.app.querystring.operation.selection.is',
                v='collective.nitf.content',
            ),
            dict(
                i='path',
                o='plone.app.querystring.operation.string.relativePath',
                v='../articulos',
            ),
            dict(
                i='review_state',
                o='plone.app.querystring.operation.selection.is',
                v=['published'],
            ),
            dict(
                i='section',
                o='plone.app.querystring.operation.selection.is',
                v=['Institucionales'],
            ),
            dict(
                i='genre',
                o='plone.app.querystring.operation.selection.is',
                v=[u'Current'],
            ),
        ],
        subjects=(u'Sección', u'Noticias', u'Institucionales')
    ),
    dict(
        type='Folder',
        title=u'Galería',
        description=u'Sección creada para mostrar, las fotos más destacadas de eventos.',
        # _layout='atct_album_view',
        _layout='galleryview',
        _addable_types=['Folder', 'Image'],
    ),
    dict(
        type='Collection',
        title=u'Anuncia con Nosotros',
        description=u'Sección de noticias Anuncia con Nosotros.',
        sort_reversed=True,
        sort_on=u'effective',
        limit=1000,
        query=[
            dict(
                i='portal_type',
                o='plone.app.querystring.operation.selection.is',
                v='collective.nitf.content',
            ),
            dict(
                i='path',
                o='plone.app.querystring.operation.string.relativePath',
                v='../articulos',
            ),
            dict(
                i='review_state',
                o='plone.app.querystring.operation.selection.is',
                v=['published'],
            ),
            dict(
                i='section',
                o='plone.app.querystring.operation.selection.is',
                v=['Anuncia con Nosotros'],
            ),
            dict(
                i='genre',
                o='plone.app.querystring.operation.selection.is',
                v=[u'Current'],
            ),
        ],
        subjects=(u'Sección', u'Noticias', u'Anuncia con Nosotros')
    ),
]

SITE_STRUCTURE = _add_id(SITE_STRUCTURE)

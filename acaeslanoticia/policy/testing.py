# -*- coding: utf-8 -*-

from plone.app.robotframework.testing import AUTOLOGIN_LIBRARY_FIXTURE
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2


class Fixture(PloneSandboxLayer):

    """
    This layer is the Test class base.

    Check out all tests on this package:

    ./bin/test -s acaeslanoticia.policy --list-tests
    """

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        """
            http://iswwwup.com/t/4f0cd268f62d/plone-unit-tests-do-not-load-dependency-package-profile.html
            https://github.com/collective/collective.rcse/blob/master/collective/rcse/testing.py
        """
        # Load ZCML

        import Products.Doormat
        self.loadZCML(package=Products.Doormat)

        import acaeslanoticia.policy
        self.loadZCML(package=acaeslanoticia.policy)

        # import acaeslanoticia.theme
        # self.loadZCML(package=acaeslanoticia.theme)

        import brasil.gov.tiles
        self.loadZCML(package=brasil.gov.tiles)

        import collective.cover
        self.loadZCML(package=collective.cover)

        import collective.googlenews
        self.loadZCML(package=collective.googlenews)

        import collective.disqus
        self.loadZCML(package=collective.disqus)

        import collective.newsticker
        self.loadZCML(package=collective.newsticker)

        import collective.nitf
        self.loadZCML(package=collective.nitf)

        import collective.opendata
        self.loadZCML(package=collective.opendata)

        import collective.polls
        self.loadZCML(package=collective.polls)

        import collective.plonetruegallery
        self.loadZCML(package=collective.plonetruegallery)

        import collective.sitelogo
        self.loadZCML(package=collective.sitelogo)

        import collective.upload
        self.loadZCML(package=collective.upload)

        import plone.app.caching
        self.loadZCML(package=plone.app.caching)

        import sc.social.like
        self.loadZCML(package=sc.social.like)

        # import Products.my
        # self.loadZCML(package=Products.my)
        # z2.installProduct(app, 'Products.my')  # initialize

        # Install products that use an old-style initialize() function
        z2.installProduct(app, 'Products.CMFPlacefulWorkflow')
        z2.installProduct(app, 'Products.Doormat')
        z2.installProduct(app, 'acaeslanoticia.policy')

    def setUpPloneSite(self, portal):
        # Install into Plone site using portal_setup

        # set the default workflow
        workflow_tool = portal['portal_workflow']
        workflow_tool.setDefaultChain('simple_publication_workflow')
        # XXX: plone-content profiles installs also portlets
        #      it should be better just to add the portlets instead
        #      of adding all content and then deleting it
        self.applyProfile(portal, 'Products.CMFPlone:plone-content')
        # install the policy package
        self.applyProfile(portal, 'acaeslanoticia.policy:default')

    def tearDownZope(self, app):
        # Uninstall products installed above
        z2.uninstallProduct(app, 'Products.CMFPlacefulWorkflow')
        z2.uninstallProduct(app, 'Products.Doormat')
        z2.uninstallProduct(app, 'acaeslanoticia.policy')

FIXTURE = Fixture()

"""
We use this base for all the tests in this package. If necessary,
we can put common utility or setup code in here. This applies to unit
test cases.
"""
INTEGRATION_TESTING = IntegrationTesting(
    bases=(FIXTURE,),
    name='acaeslanoticia.policy:Integration'
)

"""
We use this for functional integration tests. Again, we can put basic
common utility or setup code in here.
"""
FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(FIXTURE,),
    name='acaeslanoticia.policy:Functional'
)

"""
We use this for functional integration tests with robot framework. Again,
we can put basic common utility or setup code in here.
"""
ROBOT_TESTING = FunctionalTesting(
    bases=(FIXTURE, AUTOLOGIN_LIBRARY_FIXTURE, z2.ZSERVER_FIXTURE),
    name='acaeslanoticia.policy:Robot',
)

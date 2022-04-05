# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import (
    applyProfile,
    FunctionalTesting,
    IntegrationTesting,
    PloneSandboxLayer,
)
from plone.testing import z2

import senaite.indexer


class SenaiteIndexerLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=senaite.indexer)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'senaite.indexer:default')


SENAITE_INDEXER_FIXTURE = SenaiteIndexerLayer()


SENAITE_INDEXER_INTEGRATION_TESTING = IntegrationTesting(
    bases=(SENAITE_INDEXER_FIXTURE,),
    name='SenaiteIndexerLayer:IntegrationTesting',
)


SENAITE_INDEXER_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(SENAITE_INDEXER_FIXTURE,),
    name='SenaiteIndexerLayer:FunctionalTesting',
)


SENAITE_INDEXER_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        SENAITE_INDEXER_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='SenaiteIndexerLayer:AcceptanceTesting',
)

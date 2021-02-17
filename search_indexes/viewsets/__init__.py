from .address import AddressDocumentViewSet, FrontAddressDocumentViewSet
from .author import AuthorDocumentViewSet
from .book import (
    BookCompoundFuzzySearchBackendDocumentViewSet,
    BookCompoundSearchBackendDocumentViewSet,
    BookCompoundSearchBoostSearchBackendDocumentViewSet,
    BookCustomDocumentViewSet,
    BookDefaultFilterLookupDocumentViewSet,
    BookDocumentViewSet,
    BookFrontendDocumentViewSet,
    BookFunctionalSuggesterDocumentViewSet,
    BookIgnoreIndexErrorsDocumentViewSet,
    BookMoreLikeThisDocumentViewSet,
    BookMoreLikeThisNoOptionsDocumentViewSet,
    BookMultiMatchOptionsPhasePrefixSearchFilterBackendDocumentViewSet,
    BookMultiMatchSearchFilterBackendDocumentViewSet,
    BookOrderingByScoreCompoundSearchBackendDocumentViewSet,
    BookOrderingByScoreDocumentViewSet,
    BookPermissionsDocumentViewSet,
    BookSimpleQueryStringBoostSearchFilterBackendDocumentViewSet,
    BookSimpleQueryStringSearchFilterBackendDocumentViewSet,
    BookSourceSearchBackendDocumentViewSet,
    QueryFriendlyPaginationBookDocumentViewSet,
)
from .city import CityDocumentViewSet, CityCompoundSearchBackendDocumentViewSet
from .journal import JournalDocumentViewSet
from .location import LocationDocumentViewSet
from .publisher import PublisherDocumentViewSet
# from .tag import TagDocumentViewSet

__all__ = (
    'AddressDocumentViewSet',
    'AuthorDocumentViewSet',
    'BookCompoundFuzzySearchBackendDocumentViewSet',
    'BookCompoundSearchBackendDocumentViewSet',
    'BookCompoundSearchBoostSearchBackendDocumentViewSet',
    'BookCustomDocumentViewSet',
    'BookDefaultFilterLookupDocumentViewSet',
    'BookDocumentViewSet',
    'BookFrontendDocumentViewSet',
    'BookFunctionalSuggesterDocumentViewSet',
    'BookIgnoreIndexErrorsDocumentViewSet',
    'BookMoreLikeThisDocumentViewSet',
    'BookMoreLikeThisNoOptionsDocumentViewSet',
    'BookMultiMatchOptionsPhasePrefixSearchFilterBackendDocumentViewSet',
    'BookMultiMatchSearchFilterBackendDocumentViewSet',
    'BookOrderingByScoreCompoundSearchBackendDocumentViewSet',
    'BookOrderingByScoreDocumentViewSet',
    'BookPermissionsDocumentViewSet',
    'BookSimpleQueryStringBoostSearchFilterBackendDocumentViewSet',
    'BookSimpleQueryStringSearchFilterBackendDocumentViewSet',
    'BookSourceSearchBackendDocumentViewSet',
    'CityCompoundSearchBackendDocumentViewSet',
    'CityDocumentViewSet',
    'JournalDocumentViewSet',
    'FrontAddressDocumentViewSet',
    'LocationDocumentViewSet',
    'PublisherDocumentViewSet',
    'QueryFriendlyPaginationBookDocumentViewSet',
    # 'TagDocumentViewSet',
)

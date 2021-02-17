from django_elasticsearch_dsl_drf.filter_backends import (
    DefaultOrderingFilterBackend,
    FacetedSearchFilterBackend,
    FilteringFilterBackend,
    HighlightBackend,
    IdsFilterBackend,
    SimpleQueryStringSearchFilterBackend,
    OrderingFilterBackend,
    PostFilterFilteringFilterBackend,
    SuggesterFilterBackend,
)

from .default import BookDocumentViewSet

__all__ = (
    'BookSimpleQueryStringBoostSearchFilterBackendDocumentViewSet',
)


class BookSimpleQueryStringBoostSearchFilterBackendDocumentViewSet(
    BookDocumentViewSet
):
    """Same as BookDocumentViewSet, but simple query string and boost."""

    filter_backends = [
        FilteringFilterBackend,
        PostFilterFilteringFilterBackend,
        IdsFilterBackend,
        OrderingFilterBackend,
        DefaultOrderingFilterBackend,
        SimpleQueryStringSearchFilterBackend,
        FacetedSearchFilterBackend,
        HighlightBackend,
        SuggesterFilterBackend,
    ]

    # Using dedicated search fields here
    simple_query_string_search_fields = {
        'title': None,
        'summary': None,
        'description': None,
    }
    ordering = ('_score', 'id', 'title', 'price',)

    simple_query_string_options = {
        "default_operator": "and",
    }

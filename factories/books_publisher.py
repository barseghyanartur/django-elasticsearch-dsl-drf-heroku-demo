import random

from factory import LazyAttribute
from factory.django import DjangoModelFactory

from books.models import Publisher

from .factory_faker import Faker

__all__ = (
    'PublisherFactory',
    'PublisherWithUniqueNameFactory',
    'LimitedPublisherFactory',
    'SinglePublisherFactory',
)


class BasePublisherFactory(DjangoModelFactory):
    """Base publisher factory."""

    name = Faker('company')
    address = Faker('address')
    city = Faker('city')
    state_province = Faker('province')
    country = Faker('country')
    website = Faker('url')
    latitude = -32.23421
    longitude = 43.23411

    class Meta(object):
        """Meta class."""

        model = Publisher
        abstract = True


class PublisherFactory(BasePublisherFactory):
    """Publisher factory."""


class PublisherWithUniqueNameFactory(BasePublisherFactory):
    """Publisher factory with unique name attribute."""

    class Meta(object):
        """Meta class."""

        django_get_or_create = ('name',)


class LimitedPublisherFactory(BasePublisherFactory):
    """Publisher factory, but limited to 20 publishers."""

    id = LazyAttribute(
        lambda __x: random.randint(1, 20)
    )

    class Meta(object):
        """Meta class."""

        django_get_or_create = ('id',)


class SinglePublisherFactory(BasePublisherFactory):
    """Publisher factory, but limited to a single publisher."""

    id = 999999
    name = "GWW"
    address = "Schuitendiep 3"
    city = "Groningen"
    state_province = "Groningen"
    country = "NL"
    website = "https://gw20e.com"

    class Meta(object):
        """Meta class."""

        django_get_or_create = ('id',)

import factory

from apps.schedules.models import CustomOnCallShift, OnCallScheduleCalendar, OnCallScheduleICal
from common.utils import UniqueFaker


class OnCallScheduleFactory(factory.DjangoModelFactory):
    name = UniqueFaker("sentence", nb_words=2)

    @classmethod
    def get_factory_for_class(cls, klass):
        factory_classes = OnCallScheduleFactory.__subclasses__()
        for factory_class in factory_classes:
            if issubclass(klass, factory_class._meta.model):
                return factory_class


class OnCallScheduleICalFactory(OnCallScheduleFactory):
    class Meta:
        model = OnCallScheduleICal


class OnCallScheduleCalendarFactory(OnCallScheduleFactory):
    class Meta:
        model = OnCallScheduleCalendar


class CustomOnCallShiftFactory(factory.DjangoModelFactory):
    name = UniqueFaker("sentence", nb_words=2)

    class Meta:
        model = CustomOnCallShift

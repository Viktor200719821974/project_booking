from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import DestroyAPIView

from .selializers import DateSelectionModelSerializer
from .models import DateSelectionModel


@method_decorator(name='delete',
                  decorator=swagger_auto_schema(operation_id='Delete date arrival and departure',
                                                operation_summary='Delete date'))
class DateSelectionDestroyView(DestroyAPIView):
    """
    delete:
        delete select date
    """
    queryset = DateSelectionModel.objects.all()
    serializer_class = DateSelectionModelSerializer

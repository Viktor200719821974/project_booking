from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.generics import DestroyAPIView, GenericAPIView, ListAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from bookingApps.utils.jwt_utils import JwtUtils
from enums.action_token import ActionTokenEnum
from .selializers import DateSelectionModelSerializer
from .models import DateSelectionModel
from bookingApps.utils.type_token_utils import TypeToken


class YesRentView(GenericAPIView):
    permission_classes = (AllowAny,)
    queryset = DateSelectionModel.objects.all()
    serializer_class = DateSelectionModelSerializer

    def get(self, *args, **kwargs):
        token = kwargs.get('token_yes')
        token_type = JwtUtils(ActionTokenEnum.YES.token_type).validate_apartment_token(token)
        TypeToken.type_token(token_type)
        return Response(status=status.HTTP_200_OK)


class NoRentView(GenericAPIView):
    permission_classes = (AllowAny,)
    queryset = DateSelectionModel.objects.all()
    serializer_class = DateSelectionModelSerializer

    def get(self, *args, **kwargs):
        token = kwargs.get('token_no')
        token_type = JwtUtils(ActionTokenEnum.NO.token_type).validate_apartment_token(token)
        TypeToken.type_token(token_type)
        return Response(status=status.HTTP_200_OK)


@method_decorator(name='get',
                  decorator=swagger_auto_schema(operation_id='get all date arrival and departure',
                                                operation_summary='Get all date'))
class DateSelectionListView(ListAPIView):
    """
    get all:
        get all select date
    """
    queryset = DateSelectionModel.objects.all()
    serializer_class = DateSelectionModelSerializer

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

from rest_framework.response import Response
from rest_framework.views import exception_handler

from enums.error import ErrorEnum


def custom_exception_handler(exc, content) -> Response:
    handlers = {
        'JwtException': _jwt_validate_error,
        'Vle1Exception': _vle1_valid_error,
        'Vle2Exception': _vle2__error,
        'Vle3Exception': _vle3_error,
        'REQUESTException': _request_error,
        'BadDateException': _bad_day_error,
        'AuthenticatedCommentApartment': _aunticated_comment_apartment_error,
        'AuthenticatedCommentUser': _aunticated_comment_user_error,
        'NoRentException': _no_rent_error,
        'AddDeleteApartmentException': _add_delete_apartment_error,
        'BadDateRequestException': _bad_date_request_error,
    }
    response = exception_handler(exc, content)
    exc_class = exc.__class__.__name__

    if exc_class in handlers:
        return handlers[exc_class](exc, content)

    return response


def _jwt_validate_error(exc, content) -> Response:
    print(exc.__class__)
    print(content)
    return Response(ErrorEnum.JWT.msg, ErrorEnum.JWT.code)


def _vle1_valid_error(exc, content) -> Response:
    print(exc.__class__)
    print(content)
    return Response(ErrorEnum.VLE1.msg, ErrorEnum.VLE1.code)


def _vle2__error(exc, content) -> Response:
    print(exc.__class__)
    print(content)
    return Response(ErrorEnum.VLE2.msg, ErrorEnum.VLE2.code)


def _vle3_error(exc, content) -> Response:
    print(exc.__class__)
    print(content)
    return Response(ErrorEnum.VLE3.msg, ErrorEnum.VLE3.code)


def _request_error(exc, content) -> Response:
    print(exc.__class__)
    print(content)
    return Response(ErrorEnum.REQUEST.msg, ErrorEnum.REQUEST.code)


def _bad_day_error(exc, content) -> Response:
    print(exc.__class__)
    print(content)
    return Response(ErrorEnum.BADDATE.msg, ErrorEnum.BADDATE.code)


def _aunticated_comment_apartment_error(exc, content) -> Response:
    print(exc.__class__)
    print(content)
    return Response(ErrorEnum.AUTHCOMAPARTMENT.msg, ErrorEnum.AUTHCOMAPARTMENT.code)


def _aunticated_comment_user_error(exc, content) -> Response:
    print(exc.__class__)
    print(content)
    return Response(ErrorEnum.AUTHCOMUSER.msg, ErrorEnum.AUTHCOMUSER.code)


def _no_rent_error(exc, content) -> Response:
    print(exc.__class__)
    print(content)
    return Response(ErrorEnum.NORENT.msg, ErrorEnum.NORENT.code)


def _add_delete_apartment_error(exc, content) -> Response:
    print(exc.__class__)
    print(content)
    return Response(ErrorEnum.ADDDELAPART.msg, ErrorEnum.ADDDELAPART.code)


def _bad_date_request_error(exc, content) -> Response:
    print(exc.__class__)
    print(content)
    return Response(ErrorEnum.BADDATEREQUEST.msg, ErrorEnum.BADDATEREQUEST.code)

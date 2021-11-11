from enums.error import ErrorEnum
from rest_framework.response import Response
from rest_framework.views import exception_handler


def custom_exception_handler(exc, content) -> Response:
    handlers = {
        'JwtException': _jwt_validate_error,
        'Vle1Exception': _vle1_valid_error,
        'Vle2Exception': _vle2__error,
        'Vle3Exception': _vle3_error,
        'BoolException': _bool_error

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


def _bool_error(exc, content) -> Response:
    print(exc.__class__)
    print(content)
    return Response(ErrorEnum.BOOLE.msg, ErrorEnum.BOOLE.code)
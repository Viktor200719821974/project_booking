from datetime import timedelta

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=10),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
    'AUTH_HEADER_TYPES': ('Bearer',),
}
DOMAIN = 'localhost:3000'
SITE_NAME = 'BookingApp'
DJOSER = {
    'PASSWORD_RESET_CONFIRM_URL': '#/password/reset/confirm/{uid}/{token}',
    'USERNAME_RESET_CONFIRM_URL': '#/username/reset/confirm/{uid}/{token}',
    'ACTIVATION_URL': 'register/activate/{uid}/{token}',
    'SEND_ACTIVATION_EMAIL': True,
    'SERIALIZERS': {"user_create": "apps.users.serializers.UserModelSerializer"}
}
# custom serializer},
#         "user": "djoser.serializers.UserSerializer",
#         "current_user": "djoser.serializers.UserSerializer",
#         "user_delete": "djoser.serializers.UserSerializer",
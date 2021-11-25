class TypeToken:
    token_type = ' '

    @classmethod
    def type_token(cls, token_type):
        cls.token_type = token_type

    @classmethod
    def send_email_user(cls):
        type = cls.token_type
        return type

from rest_auth.serializers import PasswordResetSerializer


class CustomPasswordResetSerializer(PasswordResetSerializer):
    def get_email_options(self):
        email_context = {
            'front_password_reset_url': 'http://localhost:8000/api/v1/password/reset/confirm/'
        }
        # 本文のテンプレートパスと email の追加コンテキストを返す
        return {

            'email_template_name': 'account/email/password_reset_key_message.txt',
            'extra_email_context': email_context,
        }

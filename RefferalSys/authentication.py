from django.contrib.auth import get_user_model
from rest_framework_simplejwt.authentication import JWTAuthentication


User = get_user_model()


class CustomJWTAuthentication(JWTAuthentication):
    def get_user(self, validated_token):
        try:
            return User.objects.get(pk=validated_token['user_id'])
        except User.DoesNotExist:
            return None

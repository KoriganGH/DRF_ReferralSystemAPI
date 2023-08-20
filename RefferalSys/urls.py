from django.urls import path, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from .views import (
    InviteActivationView,
    SendVerificationCodeView,
    UserProfileView,
    VerifyCodeView, UserListProfileView,
)

schema_view = get_schema_view(
    openapi.Info(
        title="Реферальная система",
        default_version='v1',
        contact=openapi.Contact(name='daw'),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('auth_code/send/', SendVerificationCodeView.as_view(), name='send_code'),
    path('auth_code/verify/', UserProfileView.as_view(), name='verify'),
    path('user/profile/<int:pk>/', UserProfileView.as_view(), name='user-profile'),
    path('user/list/', UserListProfileView.as_view(), name='users'),
    path('user/activate_invite/<int:pk>/', InviteActivationView.as_view(), name='activate-invite'),
    path('swagger<str:format>', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc')
]

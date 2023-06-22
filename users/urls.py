from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from users.views import MyObtainTokenPairView, RegisterView, UserApiListView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('user/<int:pk>', UserApiListView.as_view(), name='user'),
]

from django.urls import path
from packages.views import PackageList
from sms.views import SmsSubscriptionList
from performance.views import PerformanceMetrics
# from mikrotik.views import add_user
from .views import RegisterView, LoginView, LogoutView, UserMe, ActiveUsers, TokenObtainPair, TokenRefresh
from . import views



urlpatterns = [
    path('me/', views.UserMe.as_view(), name='user-me'),
    path('token/', views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', views.TokenRefreshView.as_view(), name='token_refresh'),
    path('active/', views.ActiveUsers.as_view(), name='active-users'),
    path('packages/', PackageList.as_view(), name='package-list'),  
    path('performance/', PerformanceMetrics.as_view(), name='performance-index'),
    # path('mikrotik/reset/',  name='mikrotik-reset'), 
    path('sms/subscriptions/', SmsSubscriptionList.as_view(), name='sms-subscriptions'),
    path('login/', views.LoginView.as_view(), name='user-login'), 
    path('register/', views.RegisterView.as_view(), name='user-register'),
    ]
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from users.views import SignupView, ProfileView, VerifyEmailView, ProfileEditView

app_name = "users"

urlpatterns = [
    path('login/', LoginView.as_view(template_name="users/login.html"), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('signup/', SignupView.as_view(), name="signup"),
    path('profile/', ProfileView.as_view(), name="profile"),
    path('profile_edit/', ProfileEditView.as_view(), name="profile_edit"),
    path('verify_email/<str:uid>/<str:token>/', VerifyEmailView.as_view(), name='verify_email'),

]

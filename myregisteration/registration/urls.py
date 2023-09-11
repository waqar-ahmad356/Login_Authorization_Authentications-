from django.urls import path
from django.contrib.auth import views as auth_view
from .forms import LoginForm,UserPasswordChangeForm,UserPasswordSetForm,UserPasswordResetForm
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('login/',auth_view.LoginView.as_view(template_name='login.html',authentication_form=LoginForm,success_url='/'),name='login'),
    path('registration/',views.UserRegistrationView.as_view(),name='registration'),
    path('passwordchange/',auth_view.PasswordChangeView.as_view(template_name='passwordchange.html',form_class=UserPasswordChangeForm,success_url='/passwordchangedone'),name='passwordchange'),
    path('passwordchangedone/',auth_view.PasswordChangeDoneView.as_view(template_name='passwordchangedone.html'),name='passwordchangedone'),
    path('logout/',auth_view.LogoutView.as_view(next_page='login'),name='logout'),
    path('passwordreset/',auth_view.PasswordResetView.as_view(template_name='passwordreset.html',form_class=UserPasswordResetForm,success_url='/passwordresetdone/done'),name='passwordreset'),
    path('passwordresetdone/done/',auth_view.PasswordResetDoneView.as_view(template_name='passwordresetdone.html'),name='passwordresetdone'),
    path('passwordresetconfirm/<uidb64>/<token>',auth_view.PasswordResetConfirmView.as_view(template_name='passwordresetconfirm.html',form_class=UserPasswordSetForm),name='passwordset'),
    path('passwordresetcomplete/',auth_view.PasswordResetCompleteView.as_view(template_name='passwordresetcomplete.html'),name='passwordresetcomplete')
]
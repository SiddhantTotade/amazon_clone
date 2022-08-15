from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from app import views
from django.contrib.auth import views as auth_views
from .forms import LoginForm, MyPasswordChangeForm, MyPasswordResetForm, MySetPasswordForm

urlpatterns = [
    path('', views.ProductView.as_view(), name='home'),
    path('product-detail/<int:pk>',
         views.ProductDetailView.as_view(), name='product-detail'),
    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
    path('cart/', views.show_cart, name='showcart'),
    path('pluscart/', views.plus_cart, name='pluscart'),
    path('minuscart/', views.minus_cart, name='minuscart'),
    path('removecart/', views.remove_cart, name='removecart'),
    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('address/', views.address, name='address'),
    path('editaddress/<int:pk>', views.edit_address, name='editaddress'),
    path('deleteaddress/<int:pk>',
         views.delete_address, name='deleteaddress'),
    path('addaddress/', views.AddAddressView.as_view(), name='addaddress'),
    path('editname/', views.edit_name, name='editname'),
    path('editemail/', views.edit_email, name='editemail'),
    path('selectaddress/<int:pk>',
         views.SelectAddress.as_view(), name='selectaddress'),
    path('orders/', views.orders, name='orders'),
    path('passwordchangedone/', auth_views.PasswordChangeDoneView.as_view(
        template_name='app/passwordchangedone.html'), name='passwordchangedone'),
    path('passwordchange/', auth_views.PasswordChangeView.as_view(template_name='app/passwordchange.html',
         form_class=MyPasswordChangeForm, success_url='/profile/'), name='passwordchange'),
    path('product-list/', views.product_list, name='productlist'),
    path('product-not-found/', views.no_product, name='noproduct'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='app/login.html',
         authentication_form=LoginForm), name='login'),
    path('account/', views.account, name='account'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('registration/', views.CustomerRegistrationView.as_view(),
         name='customerregistration'),
    path('password-reset/',
         auth_views.PasswordResetView.as_view(template_name='app/password_reset.html', form_class=MyPasswordResetForm), name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='app/password_reset_done.html'), name='password_reset_done'),
    path('password-reset/complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='app/password_reset_complete.html'), name='password_reset_complete'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='app/password_reset_confirm.html', form_class=MySetPasswordForm), name='password_reset_confirm'),
    path('checkout/', views.checkout, name='checkout'),
    path('payment/<int:pk>', views.payment, name='payment'),
    path('paymentdone/', views.payment_done, name='paymentdone'),
    path('uploaddetails/', views.ProductUpload.as_view(), name='saveproduct'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

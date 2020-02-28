"""shopping_model URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views
from django.contrib import admin
from django.urls import path,include
from users import views as user_views
from users.forms import CustomAuthForm
from django.contrib.auth import views as authentication_view
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import RedirectView

favicon_view = RedirectView.as_view(url='/static/favicon.ico', permanent=True)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name='index'),
    path(r'favicon\.ico', favicon_view),
    path('<int:id>/', views.detail,name='detail'),
    path('add-to-cart/<int:id>/', views.add_to_cart,name='add-to-cart'),
    path('order-summary/', views.OrderSummaryView.as_view(),name='OrderSummaryView'),
    path('remove-from-cart/<int:id>/', views.remove_cart,name='remove-from-cart'),
    path('checkout/', views.checkout,name='checkout'),
    path('remove-single-item-from-cart/<int:id>/', views.remove_single_item_from_cart,name='remove_single_item_from_cart'),

    path('register/',user_views.register,name='register'),

    path('login/',authentication_view.LoginView.as_view(template_name='users/login.html', authentication_form=CustomAuthForm ),name='login'),
    path('logout/',authentication_view.LogoutView.as_view(template_name='users/logout.html'),name='logout'),
]

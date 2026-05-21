"""
URL configuration for signal_assignment project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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

from core.views import (
    test_signal_behavior,
    test_transaction_behavior,
    test_rectangle_iterator,
    display_home_page
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', display_home_page, name='home_page'),
    path('test-signal/', test_signal_behavior, name='test_signal'),
    path('test-transaction/', test_transaction_behavior, name='test_transaction'),
    path('test-rectangle/',test_rectangle_iterator, name='test_rectangle'),
]

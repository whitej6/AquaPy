from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register('wemo', views.WemoSwitchViewset)

app_name = 'power'
urlpatterns = [
    path('wemo/discover/', views.WemoSwitchViewset.as_view({'post': 'discover'})),
    path('', include(router.urls))
]
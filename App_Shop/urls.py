
from django.urls import path,include

app_name="App_Shop"

from rest_framework import routers
from .views import userview,ProductView,OrderViewSet

router = routers.DefaultRouter()
router.register(r'products', ProductView,basename='products')
router.register(r'orders', OrderViewSet,basename='orders')
urlpatterns = [
  path("user/",userview.as_view(),name='user')
 
]
urlpatterns = router.urls
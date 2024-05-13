from django.urls import path
from .views import Home, SprenList, SprenDetail

urlpatterns = [
  path('', Home.as_view(), name = 'home'),
  path('spren/',SprenList.as_view(), name = 'spren-list'),
  path('spren/<int:id>', SprenDetail.as_view(), name = 'spren-detail')
]
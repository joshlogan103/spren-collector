from django.urls import path
from .views import Home, SprenList, SprenDetail, FeedingListCreate, FeedingDetail, PowerList, PowerDetail

urlpatterns = [
  path('', Home.as_view(), name = 'home'),
  path('spren/', SprenList.as_view(), name = 'spren-list'),
  path('spren/<int:id>', SprenDetail.as_view(), name = 'spren-detail'),
  path('spren/<int:spren_id>/feedings/', FeedingListCreate.as_view(), name = 'feeding-list-create'),
  path('spen/<int:spren_id>/feedings/<int:id>/', FeedingDetail.as_view(), name = 'feeding-detail'),
  path('powers/', PowerList.as_view(), name = 'power-list'),
  path('powers/<int:id>/', PowerDetail.as_view(), name = 'power-detail')
]
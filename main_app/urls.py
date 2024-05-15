from django.urls import path
from .views import Home, SprenList, SprenDetail, FeedingListCreate, FeedingDetail, PowerList, PowerDetail, AddPowerToSpren, RemovePowerFromSpren, RadiantList, RadiantDetail, InteractionList, InteractionDetail, CreateUserView, LoginView, VerifyUserView

urlpatterns = [
  # Home
  path('', Home.as_view(), name = 'home'),

  # Spren
  path('spren/', SprenList.as_view(), name = 'spren-list'),
  path('spren/<int:id>/', SprenDetail.as_view(), name = 'spren-detail'),

  # Feedings
  path('spren/<int:spren_id>/feedings/', FeedingListCreate.as_view(), name = 'feeding-list-create'),
  path('spen/<int:spren_id>/feedings/<int:id>/', FeedingDetail.as_view(), name = 'feeding-detail'),

  # Powers
  path('powers/', PowerList.as_view(), name = 'power-list'),
  path('powers/<int:id>/', PowerDetail.as_view(), name = 'power-detail'),
  path('spren/<int:spren_id>/add-power/<int:power_id>/', AddPowerToSpren.as_view(), name = 'add-power-to-spren'),
  path('spren/<int:spren_id>/remove-power/<int:power_id>/', RemovePowerFromSpren.as_view(), name = 'remove-power-from-spren'),

  # Radiants
  path('radiants/', RadiantList.as_view(), name = 'radiant-list'),
  path('radiants/<int:id>/', RadiantDetail.as_view(), name = 'radiant-detail'),

  # Interactions
  path('spren/<int:spren_id>/radiants/<int:radiant_id>/interactions/', InteractionList.as_view(), name = 'interactions-list'),
  path('spren/<int:spren_id>/radiants/<int:radiant_id>/interactions/<int:interaction_id>/', InteractionDetail.as_view(), name = 'interaction-detail'),

  # Users
  path('users/register/', CreateUserView.as_view(), name='register'),
  path('users/login/', LoginView.as_view(), name='login'),
  path('users/token/refresh/', VerifyUserView.as_view(), name='token_refresh')
]
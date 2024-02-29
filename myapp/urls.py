from django.urls import path
from .views import GetCardStatus

urlpatterns = [
    path('api/get_card_status/', GetCardStatus.as_view(), name="get_card_status")
]
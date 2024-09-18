from django.urls import path
from .views import *

urlpatterns = [
    path('products/',ProductViews.as_view()),
    path('auction_start/',AuctionCreate.as_view()),
    path('auction_list/',AuctionList.as_view()),
    path('bid/',BidCreate.as_view()),
    path('bid_list/',BidList.as_view()),
    path('find_winner/<int:pk>/',AuctionWinner.as_view())
]

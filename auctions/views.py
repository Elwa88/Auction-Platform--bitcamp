from rest_framework import generics
from .models import *
from .serializers import *
from rest_framework.permissions import IsAdminUser, IsAuthenticated

class ProductViews(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminUser]

class AuctionCreate(generics.CreateAPIView):
    queryset = Auction.objects.all()
    serializer_class = AuctionSerializer
    permission_classes = [IsAdminUser]

class AuctionList(generics.ListAPIView):
    queryset = Auction.objects.all()
    serializer_class = AuctionSerializer
    permission_classes = [IsAuthenticated]

class BidCreate(generics.CreateAPIView):
    queryset = Bid.objects.all()
    serializer_class = BidSerializer
    def perform_create(self, serializer):
        serializer.save(bidder=self.request.user)
    permission_classes = [IsAuthenticated]

class BidList(generics.ListAPIView):
    queryset = Bid.objects.all()
    serializer_class = BidSerializer
    permission_classes = [IsAdminUser]

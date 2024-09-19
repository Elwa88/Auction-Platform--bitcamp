from django.utils import timezone
from django.core.mail import EmailMessage
from rest_framework import generics
from rest_framework.response import Response
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

class AuctionWinner(generics.RetrieveAPIView):
    queryset = Auction.objects.all()
    serializer_class = AuctionSerializer
    permission_classes = [IsAdminUser]

    def get(self,request,*args, **kwargs):
        request_time = timezone.now()
        auction = self.get_object()
        highest_bid = Bid.objects.filter(auction=auction).order_by('-bid').first()
        if auction.end_date < request_time:
            email = EmailMessage(
                subject='Won Auction',
                body=f'Congratulations you won the auction on {auction.product}. You owe us {auction.current_bid}. Pay now pretty please :)',
                to = [highest_bid.bidder.email],
            )
            #email.send(fail_silently=False)
            auction.delete()

            return Response({"message" : "E-mail sent to the winner, auction has been removed"})
        
        return Response({"message" : "Auction is still ongoing"})

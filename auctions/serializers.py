from rest_framework import serializers
from .models import *

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class AuctionSerializer(serializers.ModelSerializer):

    product = ProductSerializer()

    class Meta:
        model = Auction
        fields = ['id', 'product','listing_date','end_date','min_bid','current_bid']

class BidSerializer(serializers.ModelSerializer):
    auction = serializers.PrimaryKeyRelatedField(queryset = Auction.objects.all())

    class Meta:
        model = Bid
        fields = ['id', 'auction', 'bidder', 'bid', 'placing_time']
        read_only_fields = ['bidder']

    def validate(self,data):
        auction = data['auction']

        if data['bid'] - auction.current_bid < auction.min_bid:
            raise serializers.ValidationError(f"Minimum increment amount is {auction.min_bid}! current bid is {auction.current_bid}.")
        
        return data
    
    def create(self, validated_data):
        
        bid = Bid.objects.create(**validated_data)
        validated_data['auction'].current_bid = bid.bid 
        validated_data['auction'].save()

        return bid
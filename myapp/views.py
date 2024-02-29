from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Card, Delivered, DeliveryException, Pickup, Returned
from .serializers import DeliveredSerializer, DeliveryExceptionSerializer, PickupSerializer, ReturnedSerializer

class GetCardStatus(APIView):
    def get(self, request):
        query_param = request.query_params.get('query') 
        if not query_param:
            return Response({"error": "Query parameter is required"}, status=status.HTTP_400_BAD_REQUEST)
            
        card = Card.objects.filter(card_id=query_param).first()
        if not card:
            card = Card.objects.filter(user_contact=query_param).first()

        if not card:
            return Response({"error": "Card not found"}, status=status.HTTP_404_NOT_FOUND)
                
        card_status = {}
        if Delivered.objects.filter(card=card).exists():
            card_status['Delivered'] = DeliveredSerializer(Delivered.objects.filter(card=card), many=True).data
        if DeliveryException.objects.filter(card=card).exists():
            card_status['DeliveryException'] = DeliveryExceptionSerializer(DeliveryException.objects.filter(card=card), many=True).data
        if Pickup.objects.filter(card=card).exists():
            card_status['Pickup'] = PickupSerializer(Pickup.objects.filter(card=card), many=True).data
        if Returned.objects.filter(card=card).exists():
            card_status['Returned'] = ReturnedSerializer(Returned.objects.filter(card=card), many=True).data

        return Response(card_status)

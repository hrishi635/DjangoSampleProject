from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser 
from .serializers import TransactionSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .models import Transaction
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
import logging
from django.core.mail import send_mail

logging.basicConfig(filename="transaction_logs.log",
                    format='%(asctime)s %(message)s'
                    )
# Creating an object
logger = logging.getLogger()
# Setting the threshold of logger to DEBUG
logger.setLevel(logging.INFO)

@csrf_exempt
@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def addTransaction(request):
    if request.method == 'POST':
        serializer=TransactionSerializer(data=request.data,many=True)
        
        if serializer.is_valid():
            serializer.save()
            res={'msg':"Data Created Successfully"} 
            logging.info("Data Created Successfully")
            json=JSONRenderer().render(res)
            return HttpResponse(json,content_type='application/json',status=201)
        json=JSONRenderer().render(serializer.errors)
        logging.info(json)
        return HttpResponse(json,content_type='application/json',status=400)
        # return Response(serializer.errors,status=status.HTTP_401)
    

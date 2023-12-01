#from django.shortcuts import redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
#from rest_framework import status
from .serializer import ProfileSerializer
#from .models import profile
# Create your views here.

@api_view(['POST'])
def add_profile(request):
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':200, 'payload':serializer.data, 'message': ' Your data has been saved in Database'})
        else:
            return Response({'status':403, 'message': ' Your data has not been saved in Database'})

@api_view(['GET'])
def see_profile(request):
    prof = profile.objects.all()
    serializer = ProfileSerializer(prof, many=True)
    return Response({'status': 200, 'payload': serializer.data, 'message': ' All data of your Database is here !'})

@api_view(['DELETE'])
def del_prof(request, id):
    try:
        prof = profile.objects.get(id=id)
        prof.delete()
        return Response({'status':200, 'message': ' Profile has been Deleted !'})
    except:
        return Response({'status':403, 'message': ' Something went Wrong, Data cant Delete !'})

@api_view(['PUT'])
def update_prof(request, id):
    try:
        prof = profile.objects.get(id=id)
        serializer = ProfileSerializer(prof, data=request.data, partial=True)
        if not serializer.is_valid():
            return Response({'status': 403, 'error': serializer.error, 'message':' Profile has not been Updated !'})
        serializer.save()
        return Response({'status': 200, 'payload': serializer.data, 'message': ' Profile has been Updated !'})
    except:
        return Response({'status':403, 'message': ' Something went Wrong, Data cant Delete !'})

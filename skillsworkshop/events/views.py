from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status, generics, permissions
from .permissions import IsOrganizerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend 

from .models import Event
from .serializers import EventSerializer


class EventList(generics.ListCreateAPIView):

    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request):
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(organizer=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# PUBLIC LIST OF EVENTS 
class EventListPublic(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    


class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                         
                          ]
    queryset =  Event.objects.all()
    serializer_class = EventSerializer
    
    ## generics.RetrieveUpdateDestroyAPIView OVERRIDES THE NEED FOR BELOW ##
    
    # def get_object(self, pk):
    #     try:
    #         event = Event.objects.get(pk=pk)
    #         self.check_object_permissions(self.request, event)
    #         return event
    #     except event.DoesNotExist:
    #         raise Http404

    # def get(self, request, pk):  # this is will run
    #     event = self.get_object(pk)
    #     serializer = EventSerializer(event)
    #     return Response(serializer.data)

    # def put(self, request, pk):
    #     event = self.get_object(pk)
    #     data = request.data
    #     serializer = EventSerializer(
    #         instance = event,
    #         data=data,
    #         partial=True
    #     )
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors)

    # def delete(self, request, pk):
    #     snippet = self.get_object(pk)
    #     snippet.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from  responder.models import Content
from responder.serializers import ContentSerializer
from django.http import Http404


class ContentList(APIView):

    def get(self,request):
        contentlist=Content.objects.all()
        serializer=ContentSerializer(contentlist,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer=ContentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)






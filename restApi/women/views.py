from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated

from .Permissios import *
from .models import Women
from .serializers import WomenSerializer
from rest_framework.views import APIView

class WomenPaginationAPIListView(PageNumberPagination):
    page_size = 1
    page_size_query_param = 'page_size'
    max_page_size = 10000

class WomenViewSet(viewsets.ModelViewSet):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsAuthenticated, )

class WomenAPIListView(generics.ListCreateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsAuthenticated, )
    pagination_class = WomenPaginationAPIListView

class WomenAPIUpdateView(generics.UpdateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer

class WomenAPIUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer

class WomenAPIDestroyView(generics.RetrieveDestroyAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsAdminReadOnly, )




class WomenAPIView(APIView):
    def get(self, request):
        women = Women.objects.all().values()
        data = WomenSerializer(women, many=True).data
        response = Response({'posts': data})
        return response
        # lst = Women.objects.all().values()
        # return Response({'posts': list(lst)})

    def post(self, request):
        serializer = WomenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save() #вызывает меток create в сириализаторе
        data = serializer.data
        response = Response({'post': data})
        return response
    # post_new = Women.objects.create(
    #     title=request.data['title'],
    #     content=request.data['content'],
    #     cat_id=request.data['cat_id'],
    # )
    # return Response({'post': WomenSerializer(post_new).data})
    # post_new = Women.objects.create(
    #     title=request.data['title'],
    #     content=request.data['content'],
    #     cat_id=request.data['cat_id'],
    # )
    # return Response({'post': model_to_dict(post_new)})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({"error": "Method PUT not alowed"})
        try:
            instatnce = Women.objects.get(pk=pk)
        except:
             return Response({"error": "no object"})

        serializer = WomenSerializer(data=request.data, instance=instatnce)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"post": " put success"})

# class WomenAPIView(generics.ListAPIView):
#    queryset = Women.objects.all()
#    serializer_class = WomenSerializer
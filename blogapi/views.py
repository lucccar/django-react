from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from blog.models import Post
from .serializers import PostSerializer

@api_view(("POST", "GET"))
def post_view(request):

    if request.method == 'GET':
        queryset = Post.postobjects.all()
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(("DELETE", "GET"))
def post_detail(request, pk):
    if request.method == 'GET':
        queryset = Post.postobjects.filter(pk=pk)
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)
    
from rest_framework.decorators import api_view
from blog.models import Post
from .serializers import PostSerializer

@api_view(("POST", "GET"))
def post_view(request):
    queryset = Post.postobjects.all()

    pass

@api_view(("POST", "GET"))
def post_detail(request):
    pass
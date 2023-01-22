from rest_framework.generics import *
from books.models import *

from .serializers import BookSerializer

# Create your views here.
class BookAPIView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

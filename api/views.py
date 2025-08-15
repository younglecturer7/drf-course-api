from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer

# Create your views here.
class ProductListView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        serializer.save()  # You can add custom logic here if needed

import base64
import json

from cryptography.fernet import Fernet
from django.utils.translation import get_language
from rest_framework.generics import CreateAPIView, ListAPIView, ListCreateAPIView
from rest_framework.response import Response

from product.models import Product, Test
from product.serializers import ProductTranslatableModelSerializer, TestSerializer


class ProductCreateAPIView(CreateAPIView):
    """
     Create a new product

     Example Request Body:
     ```json
     {
       "translations": {
         "ru": {
           "name": "яблоко",
           "description": "большое яблоко"
         },
       "price": "20.00",
       "image": null
       }
     }
     ```
     """
    serializer_class = ProductTranslatableModelSerializer


class ProductListAPIView(ListAPIView):
    """
        List a products

        Example Request Body:
        ```text
        Enter language prefix in the url to get the product in the desired language
        ```
        """

    serializer_class = ProductTranslatableModelSerializer

    def get_queryset(self, *args, **kwargs):
        language_code = self.kwargs.get('language_prefix', get_language())
        return Product.objects.filter(translations__language_code=language_code)


class TestDataListView(ListCreateAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)

        # Use a static key
        key = base64.urlsafe_b64encode(b'nmadrnma'.ljust(32))  # Replace with your actual key

        # Initialize the Fernet class with the key
        fernet = Fernet(key)

        # Encrypt the serialized data
        encrypted_data = fernet.encrypt(json.dumps(serializer.data).encode())

        return Response(encrypted_data)
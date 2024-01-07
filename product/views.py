from django.http import Http404
from django.utils.translation import get_language, gettext as _
from rest_framework.generics import CreateAPIView, ListAPIView

from product.models import Product
from product.serializers import ProductTranslatableModelSerializer
from root import settings


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
     ```
     """
    serializer_class = ProductTranslatableModelSerializer


class ProductListAPIView(ListAPIView):
    """
    Enter language prefix in the url to get the product in the desired language
    """
    serializer_class = ProductTranslatableModelSerializer

    def get_queryset(self, *args, **kwargs):
        language_code = self.kwargs.get('language_prefix', get_language())

        if language_code not in [language['code'] for language in settings.PARLER_LANGUAGES[None]]:
            raise Http404(_("Language code is not valid"))

        return Product.objects.filter(translations__language_code=language_code)

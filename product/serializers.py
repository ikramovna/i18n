from parler_rest.serializers import TranslatableModelSerializer
from parler_rest.fields import TranslatedFieldsField

from product.models import Product


class ProductTranslatableModelSerializer(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=Product)

    class Meta:
        model = Product
        fields = ('id', 'translations', 'price', 'image')

    def create(self, validated_data):
        translations_data = validated_data.pop('translations')
        product = Product.objects.create(**validated_data)
        for language_code, translation_data in translations_data.items():
            product.create_translation(language_code, **translation_data)
        return product

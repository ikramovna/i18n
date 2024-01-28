from django.urls import path

from product.views import ProductCreateAPIView, ProductListAPIView, TestDataListView

urlpatterns = [
    path('product', ProductCreateAPIView.as_view()),

    path('test', TestDataListView.as_view()),

    path('product/<str:language_prefix>', ProductListAPIView.as_view()),
]

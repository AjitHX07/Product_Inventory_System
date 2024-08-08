from django.shortcuts import render

# Create your views here.
# inventory/views.py
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Products, Variants, SubVariants
from .serializers import ProductSerializer
from rest_framework.decorators import action
from rest_framework import status # type: ignore

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        variants_data = data.pop('variants')
        product = Products.objects.create(**data)

        for variant_data in variants_data:
            sub_variants_data = variant_data.pop('sub_variants')
            variant = Variants.objects.create(product=product, **variant_data)

            for sub_variant_data in sub_variants_data:
                SubVariants.objects.create(variant=variant, **sub_variant_data)

        serializer = self.get_serializer(product)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer

    @action(detail=True, methods=['post'])
    def add_stock(self, request, pk=None):
        product = self.get_object()
        variant_id = request.data.get('variant_id')
        sub_variant_id = request.data.get('sub_variant_id')
        stock_to_add = request.data.get('stock')

        try:
            sub_variant = SubVariants.objects.get(pk=sub_variant_id, variant__product=product, variant__id=variant_id)
            sub_variant.stock += float(stock_to_add)
            sub_variant.save()
            return Response({'status': 'stock added'}, status=status.HTTP_200_OK)
        except SubVariants.DoesNotExist:
            return Response({'error': 'Sub-variant not found'}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['post'])
    def remove_stock(self, request, pk=None):
        product = self.get_object()
        variant_id = request.data.get('variant_id')
        sub_variant_id = request.data.get('sub_variant_id')
        stock_to_remove = request.data.get('stock')

        try:
            sub_variant = SubVariants.objects.get(pk=sub_variant_id, variant__product=product, variant__id=variant_id)
            if sub_variant.stock >= float(stock_to_remove):
                sub_variant.stock -= float(stock_to_remove)
                sub_variant.save()
                return Response({'status': 'stock removed'}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Insufficient stock'}, status=status.HTTP_400_BAD_REQUEST)
        except SubVariants.DoesNotExist:
            return Response({'error': 'Sub-variant not found'}, status=status.HTTP_400_BAD_REQUEST)
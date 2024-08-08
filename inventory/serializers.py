from rest_framework import serializers # type: ignore
from .models import Products, Variants, SubVariants

class SubVariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubVariants
        fields = ['id', 'name', 'stock']

class VariantSerializer(serializers.ModelSerializer):
    sub_variants = SubVariantSerializer(many=True)

    class Meta:
        model = Variants
        fields = ['id', 'name', 'sub_variants']

class ProductSerializer(serializers.ModelSerializer):
    variants = VariantSerializer(many=True)

    class Meta:
        model = Products
        fields = ['id', 'ProductID', 'ProductCode', 'ProductName', 'ProductImage', 'CreatedDate', 'UpdatedDate', 'CreatedUser', 'IsFavourite', 'Active', 'HSNCode', 'TotalStock', 'variants']

from django.db import models

# Create your models here.

import uuid
from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

class Products(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)    
    ProductID = models.BigIntegerField(unique=True)    
    ProductCode = models.CharField(max_length=255, unique=True)
    ProductName = models.CharField(max_length=255)    
    ProductImage = ProcessedImageField(
        upload_to='uploads/',
        processors=[ResizeToFill(500, 500)],
        format='JPEG',
        options={'quality': 100},
        blank=True,
        null=True
    )   
    CreatedDate = models.DateTimeField(auto_now_add=True)
    UpdatedDate = models.DateTimeField(blank=True, null=True)
    CreatedUser = models.ForeignKey("auth.User", related_name="user%(class)s_objects", on_delete=models.CASCADE)    
    IsFavourite = models.BooleanField(default=False)
    Active = models.BooleanField(default=True)    
    HSNCode = models.CharField(max_length=255, blank=True, null=True)    
    TotalStock = models.DecimalField(default=0.00, max_digits=20, decimal_places=8, blank=True, null=True)

    class Meta:
        db_table = "products_product"
        unique_together = (("ProductCode", "ProductID"),)
        ordering = ("-CreatedDate", "ProductID")


class Variants(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product = models.ForeignKey(Products, related_name="variants", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    
    class Meta:
        db_table = "products_variant"


class SubVariants(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    variant = models.ForeignKey(Variants, related_name="sub_variants", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    stock = models.DecimalField(default=0.00, max_digits=20, decimal_places=8)

    class Meta:
        db_table = "products_subvariant"

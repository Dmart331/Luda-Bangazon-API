from rest_framework import serializers
from Bangazon_api.models import *
from django.contrib.auth import models
from django.contrib.auth.models import User







class ProductSerializer(serializers.HyperlinkedModelSerializer):
    """
    Class for data serialization of a specific Model: Product
    """  

    class Meta:
        model = Product
        fields = ('id', 'url', 'name', 'description', 'price', 'quantity_available', 'product_category_id', 'user_id',)


class ProductCategorySerializer(serializers.HyperlinkedModelSerializer):
    """
    Class for data serialization of a specific Model: ProductCategory
    """
    class Meta:
        model = ProductCategory
        fields = ('id', 'url', 'name',)


class ProductOrderSerializer(serializers.HyperlinkedModelSerializer):
    """
    Class for data serialization of a specific Model: ProductOrder
    """
    class Meta:
        model = ProductOrder
        fields = ('id', 'url', 'product_id', 'order_id',)      
  

class OrderSerializer(serializers.ModelSerializer):
    """
    Class for data serialization of a specific Model: Order
    Added ProductOorderSerializer to make nested serializers in the OrderSerializer
    """
    product_orders = ProductOrderSerializer(many=True, read_only=True)
    
    class Meta:
        model = Order
        fields = ('id', 'url','created', 'active', 'payment_method_id', 'user_id', 'product_orders')
        

class UserSerializer(serializers.HyperlinkedModelSerializer):
    """
    Class for data serialization of a specific Model: User
    If user is not staff, This UserSerializer will be picked up on the ViewSet
    """
    orders = OrderSerializer(many=True, read_only=True)

    
    class Meta:
        model = User
        fields = ('id', 'url', 'first_name', 'last_name', 'username','orders','email',)

        extra_kwargs = {'email': {'write_only': True}, 'username': {'write_only': True}}

class UserStaffSerializer(serializers.HyperlinkedModelSerializer):
    """
    Class for data serialization of a specific Model: User
    If user is_staff, This UserStaffSerializer will be picked up on the ViewSet
    Added Orderserializer to make nested serializers in the UserStaffSerializer
    """
    orders = OrderSerializer(many=True, read_only=True)

    class Meta:

        model= User 
        fields = ('id', 'url', 'first_name', 'last_name', 'email', 'username', 'orders')
      
class PaymentMethodSerializer(serializers.HyperlinkedModelSerializer):
    
    """
    Class for data serialization of a specific Model: Payment Method
    Sets user serializer to only show sensitive imformation to superusers
    """
    class Meta:
        model = PaymentMethod
        fields = ('id', 'url', 'name', 'account_number', 'user_id',)

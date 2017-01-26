from rest_framework import serializers
from Bangazon_api.models import *

class UserSerializer(serializers.HyperlinkedModelSerializer):
    """
    Class for data serialization of a specific Model: User
    """
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'date_of_birth')

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    """
    Class for data serialization of a specific Model: Product
    """
    # product_category_id = serializers.HyperlinkedIdentityField(view_name='Bangazon:ProductCategoryViewSet-detail')

    # user_id = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     read_only=True,
    #     view_name='User-detail'
    # )

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price', 'quantity_available', 'product_category_id', 'user_id',)


class ProductCategorySerializer(serializers.HyperlinkedModelSerializer):
    """
    Class for data serialization of a specific Model: ProductCategory
    """
    class Meta:
        model = ProductCategory
        fields = ('id', 'name',)


class ProductOrderSerializer(serializers.HyperlinkedModelSerializer):
    """
    Class for data serialization of a specific Model: ProductOrder
    """
    class Meta:
        model = ProductOrder
        fields = ('id', 'product_id', 'order_id',)      
  

class OrderSerializer(serializers.HyperlinkedModelSerializer):
    """
    Class for data serialization of a specific Model: Order
    """
    class Meta:
        model = Order
        fields = ('id', 'active', 'payment_method_id', 'user_id',)

        
class PaymentMethodSerializer(serializers.HyperlinkedModelSerializer):
    """
    Class for data serialization of a specific Model: Payment Method
    """
    class Meta:
        model = PaymentMethod
        fields = ('id','name', 'account_number', 'user_id',)

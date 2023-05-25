from rest_framework import serializers
from .models import DepositProducts, DepositOptions, InstallmentOptions, InstallmentProducts
# from ..accounts.models import User

# Form -> forms.Form / forms.ModelForm
# serializers -> Serializer / ModelSerializer

# Model이 붙으면 -> 정의한 필드에 대해서 입출력
# 안붙으면 -> 사용자가 원하는 필드를 추가로 입력 받거나, 출력함

class DepositOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositOptions
        fields = '__all__'
        read_only_fields=('fin_prdt_cd',)

class DepositProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositProducts
        fields = '__all__'
    
class InstallmentProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstallmentProducts
        fields = '__all__'
    
class InstallmentOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstallmentOptions
        fields = '__all__'
        read_only_fields = ('fin_prdt_cd',)
        
        
class SubInstSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstallmentProducts
        fields = ('sub_user',)
        # read_only_fields
class SubDepoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositProducts
        fields = ('sub_user',)
        
        
# class ProductSerializer(serializers.ModelSerializer):
#     class UserSerializer(serializers.ModelSerializer):
#         class Meta:
#             model = User
#             fields = ('financial_product',)

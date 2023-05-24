from django.shortcuts import render
from .models import User
from rest_framework.decorators import api_view, permission_classes
from .serializers import UserSerializer,ProfileSerializer,RecommendSerializer
from rest_framework.permissions import *
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
import json
import pandas as pd

# 회원탈퇴
@api_view(['POST'])
@permission_classes([IsAuthenticated]) # 인증된 사용자만 권한 허용
def user_delete(request):
    request.user.delete()
    data = {
            'content': f'{request.user}님은 탈퇴하셨군요',
        }
    
    return Response(data, status=status.HTTP_204_NO_CONTENT)

# @permission_classes([IsAuthenticated]) # 인증된 사용자만 권한 허용
# def userproductchange(request):
#     pass

@api_view(['GET'])
@permission_classes([IsAuthenticated]) # 인증된 사용자만 권한 허용
def userproductget(request,user_pk):
    user = get_object_or_404(User, pk=user_pk)
    serializer = UserSerializer(user)
    return Response(serializer.data)



# Create your views here.
@api_view(['POST'])
@permission_classes([IsAuthenticated]) # 인증된 사용자만 권한 허용
def userchange(request):
    serializer = ProfileSerializer(instance=request.user,data=request.data, partial=True)
    #   print(serializer,'asdsadsad')
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_200_OK)



# 성별, 나이, 연봉, 자산이 비슷한 사람들이 가입한 상품을 출력
@api_view(['GET'])
@permission_classes([IsAuthenticated]) # 인증된 사용자만 권한 허용
def userrecommend(request, user_pk):
    user_data_json = open('C:/Users/SSAFY/Desktop/21321/AB_finalpjt/back/bank/accounts/fixtures/accounts/user_data.json', encoding='UTF8')
    user_data_list = json.load(user_data_json)
    product_json = open('C:/Users/SSAFY/Desktop/21321/AB_finalpjt/back/bank/accounts/fixtures/accounts/depo_info_data326.json', encoding='UTF8')
    product_list = json.load(user_data_json)
    # 사용자가 가입한 상품 선택
    # Users = get_object_or_404(User,pk=user_pk)
    # serializer = RecommendSerializer(Users)
    
    # 사용자가 가입한 상품 제거 필요
    
    df = pd.DataFrame(product_list)
    print(df.to_json())
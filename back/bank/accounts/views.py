from django.shortcuts import render
from .models import User
from rest_framework.decorators import api_view, permission_classes
from .serializers import UserSerializer
from rest_framework.permissions import *
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
@api_view(['PUT'])
@permission_classes([IsAuthenticated]) # 인증된 사용자만 권한 허용
def userchange(request, username):
    Users = get_object_or_404(User, username=username)
    print(request.data,'readsad')
    if request.user == Users:
      serializer = UserSerializer(instance=Users,data=request.data)
      print(serializer,'asdsadsad')
      if serializer.is_valid(raise_exception=True):
          serializer.save()
          serializer = UserSerializer(Users)
          return Response(serializer)
        
# 회원탈퇴
@api_view(['POST'])
@permission_classes([IsAuthenticated]) # 인증된 사용자만 권한 허용
def userdelete(request):
    request.user.delete()
    data = {
            'content': f'{request.user}님은 탈퇴하셨군요',
        }
    return Response(data, status=status.HTTP_204_NO_CONTENT)
     
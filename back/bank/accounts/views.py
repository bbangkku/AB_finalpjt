from django.shortcuts import render
from .models import User
from rest_framework.decorators import api_view, permission_classes
from .serializers import UserSerializer
from rest_framework.permissions import *
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
from collections import Counter


# 회원탈퇴
@api_view(['DELETE'])
@permission_classes([IsAuthenticated]) # 인증된 사용자만 권한 허용
def user_delete(request):
    user = User.object.get(id=request.user.id)
    if user:
        user.delete()
        data = {
            'content': f'{request.user}님은 탈퇴하셨군요',
        }
    return Response(data, status=status.HTTP_204_NO_CONTENT)


@api_view(['put'])
@permission_classes([IsAuthenticated]) # 인증된 사용자만 권한 허용
def userproductput(request,user_pk):
    user = get_object_or_404(User, pk=user_pk)
    serializer = UserSerializer(user,data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['delete'])
@permission_classes([IsAuthenticated]) # 인증된 사용자만 권한 허용
def userproductdelete(request,user_pk):
    user = get_object_or_404(User, pk=user_pk)
    serializer = UserSerializer(user,data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_200_OK)


# Create your views here.
@api_view(['PUT'])
@permission_classes([IsAuthenticated]) # 인증된 사용자만 권한 허용
def userchange(request):
    user = request.user
    updated_data = request.data
    serializer = UserSerializer(user,data=updated_data,partial=True)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_200_OK)


db_data = {}
def getuser(user_pk):
    user = get_user_model().objects.get(id=user_pk)

    serializer = UserSerializer(user)
    db_data = serializer.data
    print(db_data)
    return db_data
# db user는 잘 저장되었고,, 


# 성별, 나이, 연봉, 자산이 비슷한 사람들이 가입한 상품을 출력
@api_view(['GET'])
@permission_classes([IsAuthenticated]) # 인증된 사용자만 권한 허용

def userrecommend(request, user_pk):
    # 파일 로드
    db_data = getuser(user_pk)
    print(db_data)
    
    product_json = open('C:/Users/rkdmf/OneDrive/바탕 화면/jjj/AB_finalpjt/back/bank/accounts/fixtures/accounts/depo_info_data326.json', encoding='UTF8')
    product_list = json.load(product_json)
    json_file_path = 'C:/Users/rkdmf/OneDrive/바탕 화면/jjj/AB_finalpjt/back/bank/accounts/fixtures/accounts/user_data.json'
    with open(json_file_path, 'r', encoding='UTF8') as file:
        user_data = json.load(file)

    
    # 로그인된 유저 성별 숫자로 바꿔주고
    if db_data['gender'] == "F":
        db_data['gender'] = 2
    else:
        db_data['gender'] = 1
    if db_data['financial_products'] == []:
        db_data['financial_products'] = ""
    # DB 데이터를 JSON 데이터에 추가
    user_data.append(db_data)
    # 이전에 열었던 파일 객체 닫기

    
    # JSON 파일에 쓰기
    with open(json_file_path, 'w', encoding='UTF8') as file:
        json.dump(user_data, file, ensure_ascii=False, indent=4)
    

    # 각 항목의 평균을 계산해서 중심점을 잡아줄 것
    genders = []
    ages = []
    moneys = []
    salaries = []
    print('assssssssssssssssssssssssssssssssssssssssssss')
    for data in user_data:
        genders.append(int(data['gender']))
        ages.append(int(data['age']))
        moneys.append(int(data['money']))
        salaries.append(int(data['salary']))

    # 각 항목의 평균 계산
    gender_mean = np.mean(genders)
    age_mean = np.mean(ages)
    money_mean = np.mean(moneys)
    salary_mean = np.mean(salaries)

    # 평균의 평균 계산
    init_centers = np.array([[gender_mean, age_mean, money_mean, salary_mean]] * 4)
    print('assssssssssssssssssssssssssssssssssssssssssss')


    ## 엘보우 기법 
    # Elbow = []
    df_user = pd.DataFrame(user_data)
    data = df_user[['age','gender','salary','money']]

    # for k in range(1,11):
    #   kmeans = KMeans(n_clusters=k)
    #   kmeans.fit(data)
    #   Elbow.append(kmeans.inertia_)

    # plt.plot(range(1, 11), Elbow)
    # plt.xlabel('Number of Clusters')
    # plt.ylabel('SSE')
    # plt.title('Elbow Curve')
    # plt.show()
    # 보니까 4개

    # KMeans 클러스터링 사용
    k = 4
    
    kmeans = KMeans(n_clusters=k,init=init_centers,random_state=0,n_init=10)
    kmeans.fit(data)
    print('assssssssssssssssssssssssssssssssssssssssssss')

    labels = kmeans.labels_
    centroids = kmeans.cluster_centers_


    # 각 인원들이 어느라벨에 속하는지 볼게
    df_user['cluster_label'] = labels

    # 해당 유저는 가장 마지막에 추가되었으므로 마지막 클러스터 값을 가져온다 !!
    user_cluster = df_user['cluster_label'].iloc[-1]

    # 유저랑 같은 군집에 있는 애들의 가입된 상품 가져오기
    financial_products = df_user.loc[df_user['cluster_label'] == user_cluster, 'financial_products']

    # 리스트를 딕셔너리로 변환하여 상품 개수 세기
    product_count = dict(Counter(list(financial_products)))

    # 정렬 해주고
    sorted_products = sorted(product_count.items(), key=lambda x: x[1], reverse=True)

    # 가장 많이 가입한 상위 3개 출력 >> 그게 추천 (처음은 가입안한 갯수가나옴 거의 '')
    recommend_list = []
    for product, count in sorted_products[:4]:
        recommend_list.append((product,count))
        # print(f"Product: {product}, Count: {count}")
    # print(product_list)
    print(recommend_list)
    user_recommend_list_list = []
    for i in product_list:
        user_recommend_list = {}
        for j in recommend_list:
            if i['id']==j[0]:
                user_recommend_list['id'] = i['id']
                user_recommend_list['product'] = i['product']
                user_recommend_list_list.append(user_recommend_list)
                break
    print(user_recommend_list_list)

    return Response(user_recommend_list_list)

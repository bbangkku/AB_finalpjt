from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import *
import requests
from django.shortcuts import get_object_or_404
from accounts.models import User
from rest_framework import status


BASE_URL = 'http://finlife.fss.or.kr/'
API_KEY = settings.API_KEY
API_URL = 'finlifeapi/depositProductsSearch.json'
API_URL_INSTALL = 'finlifeapi/savingProductsSearch.json'

# 적금
def save_deposit_products(request):
    # API 돌리기
    URL = BASE_URL + API_URL
    params = {
        'auth' : API_KEY,
        'topFinGrpNo' : '020000',
        'pageNo' : '1'
    }
    response = requests.get(URL, params=params).json()
    
    # product 저장
    for item in response['result']['baseList']:
        form = DepositProductsSerializer(data=item)
        if form.is_valid():
            if DepositProducts.objects.filter(fin_prdt_cd=item['fin_prdt_cd']).exists():
                continue
            form.save()
            
    # option 저장
    for item in response['result']['optionList']:
        if item['intr_rate'] is None:
            item['intr_rate'] = -1
        form = DepositOptionsSerializer(data=item)
        if form.is_valid(raise_exception=True):
            # cd 가져오기 -> ORM을 python으로 바꾸기
            x = DepositProducts.objects.filter(fin_prdt_cd=item['fin_prdt_cd']).first()
            # 이미 있는 데이터면 걸러주는 코드 추가
            if DepositOptions.objects.filter(
                    intr_rate = item['intr_rate'],
                    intr_rate2 = item['intr_rate2'],
                    save_trm = item['save_trm'],
                    fin_prdt_cd_id = x.pk,
                ).exists():
                continue
            form.save(fin_prdt_cd=x)
    # =========================================================================
    # front로 보내기용 정리
    result_list = []
    # product
    baselist = response['result']['baseList']
    # option
    optionlist = response['result']['optionList']
    for product in baselist:
        test = {}
        for option in optionlist:
            # product와 cd가 겹치는 option 뽑기
            if product['fin_prdt_cd'] == option['fin_prdt_cd']:
                # 개월 당 최고 우대금리 dict로 묶어서 넣기
                test[option['save_trm']+'개월'] =  option['intr_rate2']
        # 특정 개월이 없는 상품은 0으로 채워주기
        trm = ['6개월', '12개월', '24개월', '36개월']
        for v in trm:
            if v not in test.keys():
                test[v] = 0
        # 은행 이름 첨부
        test['bank'] = product['kor_co_nm']
        # 상품 이름 첨부
        test['product'] = product['fin_prdt_nm']
        # ID 추가
        test['id'] = product['fin_prdt_cd']
        result_list.append(test)
        # print(result_list)
    return JsonResponse({'response':result_list})


def save_installment_products(request):
    URL = BASE_URL + API_URL_INSTALL
    params = {
        'auth' : API_KEY,
        'topFinGrpNo' : '020000',
        'pageNo' : '1'
    }
    response = requests.get(URL, params=params).json()
    for item in response['result']['baseList']:
        form = InstallmentProductsSerializer(data=item)
        if form.is_valid():
            if InstallmentProducts.objects.filter(fin_prdt_cd=item['fin_prdt_cd']).exists():
                continue
            form.save()
            
    for item in response['result']['optionList']:
        if item['intr_rate'] is None:
            item['intr_rate'] = -1
        form = InstallmentOptionsSerializer(data=item)
        if form.is_valid(raise_exception=True):
            # cd 가져오기
            x = InstallmentProducts.objects.filter(fin_prdt_cd=item['fin_prdt_cd']).first()
            # 이미 있는 데이터면 걸러주는 코드 추가
            if InstallmentOptions.objects.filter(
                    intr_rate = item['intr_rate'],
                    intr_rate2 = item['intr_rate2'],
                    save_trm = item['save_trm'],
                    intr_rate_type_nm = item['intr_rate_type_nm'],
                    rsrv_type_nm = item['rsrv_type_nm'],
                    fin_prdt_cd_id = x.pk,
                ).exists():
                continue
            form.save(fin_prdt_cd=x)
            
            
    # front로 보내기용 정리
    result_list = []
    # product
    baselist = response['result']['baseList']
    # option
    optionlist = response['result']['optionList']
    for product in baselist:
        test = {}
        test2 = {}
        for option in optionlist:
            # product와 cd가 겹치는 option 뽑기
            if product['fin_prdt_cd'] == option['fin_prdt_cd']:
                if option['rsrv_type_nm'] == '자유적립식':
                    # 개월 당 최고 우대금리 dict로 묶어서 넣기
                    test2[option['save_trm']+'개월'] =  option['intr_rate2']
                    test2['type'] = option['rsrv_type_nm']
                    # 이자 방식 첨부
                    test2['intr_rate_type_nm'] = option['intr_rate_type_nm']
                if option['rsrv_type_nm'] == '정액적립식':
                    # 개월 당 최고 우대금리 dict로 묶어서 넣기
                    test[option['save_trm']+'개월'] =  option['intr_rate2']
                    test['type'] = option['rsrv_type_nm']
                    # 이자 방식 첨부
                    test['intr_rate_type_nm'] = option['intr_rate_type_nm']
        # 특정 개월이 없는 상품은 0으로 채워주기
        trm = ['6개월', '12개월', '24개월', '36개월']
        if len(test2) != 0 :
            for v in trm:
                if v not in test2.keys():
                    test2[v] = 0
            # 은행 이름 첨부
            test2['bank'] = product['kor_co_nm']
            # 상품 이름 첨부
            test2['product'] = product['fin_prdt_nm']
        if len(test) != 0:
            for v in trm:
                if v not in test.keys():
                    test[v] = 0
            # 은행 이름 첨부
            test['bank'] = product['kor_co_nm']
            # 상품 이름 첨부
            test['product'] = product['fin_prdt_nm']
        if len(test) >= 8 :
            test['id1'] = product['fin_prdt_cd']
            result_list.append(test)
        if len(test2) >= 8 :
            test2['id1'] = product['fin_prdt_cd']
            result_list.append(test2)
                
    return JsonResponse({'response':result_list})


def d_detail(request, product_id):
    if request.method == 'GET':
        try:
            product = DepositProducts.objects.get(fin_prdt_cd=product_id)
            serializer = DepositProductsSerializer(product)
            print(serializer.data,'sssssssssssssssssssssss')
            return JsonResponse({'success': True, 'product': serializer.data})
        # 일치하는 상품이 없을 경우 예외처리
        except DepositProducts.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Product not found'})
    return JsonResponse({'success': False, 'error': 'Invalid request'})


def i_detail(request, product_id):
    if request.method == 'GET':
        try:
            product = InstallmentProducts.objects.get(fin_prdt_cd=product_id)
            serializer = InstallmentProductsSerializer(product)
            return JsonResponse({'success': True, 'product': serializer.data})
        # 일치하는 상품이 없을 경우 예외처리
        except InstallmentProducts.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Product not found'})
    return JsonResponse({'success': False, 'error': 'Invalid request'})



# 유저가 가입한 상품 조회 및 수정

# @api_view(['PUT','POST','DELETE','GET'])
# def userproductchange(request,user_pk,product1_pk):
#     user = get_object_or_404(User, pk=user_pk)
#     product = get_object_or_404(DepositProducts,)
    # product = 
    # serializer = UserSerializer(user)
    # return Response(serializer.data)


# @api_view(['GET','POST','PUT','DELETE'])
# def subscribe(request, product_id, username):
#     product = InstallmentProducts.objects.get(id=product_id)
#     product1 = DepositProducts.objects.get(id=product_id)

#     user = User.objects.get(username=username)
#     if request.method == "GET":
#         pass
#     elif request.method == "POST":
#         serializer = SubInstSerializer(data=request.data)
#         serializer1 = SubDepoSerializer(data=request.data)
        # if serializer.is_valid() or serializer1.is_valid():
        # serializers = InstallmentProductsSerializer(product)
        # print(serializers)
        # if serializers.is_valid(raise_exception=True):
            # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
     
    # user = User.objects.get(pk=user_id)
    
    # if user.financial_products.filter(pk=request.user_id).exists():
    #     user.financial_products.remove(request.user)
    # else:
    #     user.financial_products.add(request.user)
        
        
        
        
@api_view(['GET','POST','PUT','DELETE'])
def like(request, user_id):
    user = User.objects.get(pk=user_id)
    
    if user.like_financial_products.filter(pk=request.user_id).exists():
        user.like_financial_products.remove(request.user)
    else:
        user.like_financial_products.add(request.user)



@api_view(['POST','GET'])
def addproduct(request,fin_prdt_cd,user_pk):
    if request.method == 'POST':
        if request.data['pro'] == 'i':
            product = InstallmentProducts.objects.get(fin_prdt_cd=fin_prdt_cd)
            if product.sub_user.filter(pk=user_pk).exists():
                product.sub_user.remove(request.user)
            elif product.sub_user.filter(pk=user_pk).exists():
                product.sub_user.add(request.user)
            sub_user_list = list(product.sub_user.values())  # sub_user 필드의 데이터 추출
            return  JsonResponse({'sub_user' : sub_user_list})           
                
        else:
            product1 = DepositProducts.objects.get(fin_prdt_cd=fin_prdt_cd)
            if product1.sub_user.filter(pk=user_pk).exists():
                product1.sub_user.remove(request.user)
            if not product1.sub_user.filter(pk=user_pk).exists():
                product1.sub_user.add(request.user)
            sub_user_list = list(product1.sub_user.values())  # sub_user 필드의 데이터 추출

            return  JsonResponse({'sub_user' : sub_user_list})           

            
        
    #     if serializer.is_valid(raise_exception=True):
    #         serializer.save()
    #         return Response(data=serializer.data, status=status.HTTP_200_OK)
    # elif request.method == "DELETE":
        
    
        # sub_user = request.user.username
        # if serializers.data['sub_user']:
        #     serializers.data['sub_user'].append(sub_user)
        # else:
        #     serializers.data['sub_user'] = sub_user

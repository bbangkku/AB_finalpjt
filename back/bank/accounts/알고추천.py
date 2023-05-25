
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
from collections import Counter
# user_data_json = open('C:/Users/SSAFY/Desktop/21321/AB_finalpjt/back/bank/accounts/fixtures/accounts/user_data.json', encoding='UTF8')
# user_data_list = json.load(user_data_json)

# # 파일 로드
# product_json = open('C:/Users/SSAFY/Desktop/21321/AB_finalpjt/back/bank/accounts/fixtures/accounts/depo_info_data326.json', encoding='UTF8')
# product_list = json.load(product_json)
# json_file = 'C:/Users/SSAFY/Desktop/21321/AB_finalpjt/back/bank/accounts/fixtures/accounts/user_data.json'
# with open(json_file, 'r', encoding='UTF8') as file:
#     user_data = json.load(file)

# # 현재 로그인된 유저를 가져오기,,
# db_data = {    "id": 7,
#     "nickname": "bbbkkk",
#     "username": "병국병국",
#     "gender": "M",
#     "age": "50",
#     "money": "698491",
#     "salary": "65156498",
#     "bank": "KEB하나은행",
#     "financial_products": [],
#     "like_financial_products": []}
# # def userrecommend(request):

# # 성별 숫자로 바꿔주고
# if db_data['gender'] == "F":
#   db_data['gender'] = 2
# else:
#   db_data['gender'] = 1

# if db_data['financial_products'] == []:
#   db_data['financial_products'] = ""


# # 각 항목의 평균을 계산해서 중심점을 잡아줄 것
# genders = []
# ages = []
# moneys = []
# salaries = []

# for data in user_data:
#     genders.append(int(data['gender']))
#     ages.append(int(data['age']))
#     moneys.append(int(data['money']))
#     salaries.append(int(data['salary']))

# # 각 항목의 평균 계산
# gender_mean = np.mean(genders)
# age_mean = np.mean(ages)
# money_mean = np.mean(moneys)
# salary_mean = np.mean(salaries)

# # 평균의 평균 계산
# init_centers = np.array([[gender_mean, age_mean, money_mean, salary_mean]] * 4)

# # DB 데이터를 JSON 데이터에 추가
# user_data.append(db_data)

# # JSON 파일에 쓰기
# with open(json_file, 'w', encoding='UTF8') as file:
#     json.dump(user_data, file, ensure_ascii=False, indent=4)

# print("데이터가 JSON 파일에 성공적으로 추가되었습니다.")

# df = pd.DataFrame(product_list)
# df_user = pd.DataFrame(user_data)
# data = df_user[['age','gender','salary','money']]

# ## 엘보우 기법 
# # Elbow = []

# # for k in range(1,11):
# #   kmeans = KMeans(n_clusters=k)
# #   kmeans.fit(data)
# #   Elbow.append(kmeans.inertia_)

# # plt.plot(range(1, 11), Elbow)
# # plt.xlabel('Number of Clusters')
# # plt.ylabel('SSE')
# # plt.title('Elbow Curve')
# # plt.show()
# # 보니까 4개


# # KMeans 클러스터링 사용
# k = 4
# kmeans = KMeans(n_clusters=k,init=init_centers ,random_state=0,n_init=10)
# kmeans.fit(data)

# labels = kmeans.labels_
# centroids = kmeans.cluster_centers_


# # 각 인원들이 어느라벨에 속하는지 볼게
# df_user['cluster_label'] = labels

# # 해당 유저는 가장 마지막에 추가되었으므로 마지막 클러스터 값을 가져온다 !!
# user_cluster = df_user['cluster_label'].iloc[-1]

# # cluster_label이 0~3 (0,1,2,3) 인 값들의 financial_products 파악하기 !!!!
# cluster_products = {}

# # 유저랑 같은 군집에 있는 애들의 가입된 상품 가져오기
# financial_products = df_user.loc[df_user['cluster_label'] == user_cluster, 'financial_products']

# # 리스트를 딕셔너리로 변환하여 상품 개수 세기
# product_count = dict(Counter(list(financial_products)))

# # 정렬 해주고
# sorted_products = sorted(product_count.items(), key=lambda x: x[1], reverse=True)

# # 가장 많이 가입한 상위 3개 출력 >> 그게 추천 (처음은 가입안한 갯수가나옴 거의 '')
# recommend_list = []
# for product, count in sorted_products[:4]:
#     recommend_list.append((product,count))
#     # print(f"Product: {product}, Count: {count}")

# user_recommend_list = []
# for i in product_list:
#   for j in recommend_list:
#       if i['id']==j[0]:
#           user_recommend_list.append(i['product'])
# print(user_recommend_list)
#           # print(i['product'])
#           # j[0] = i['product']
#           # break
# # print(j)
      














# # 상위 3개 출력 >> 그게 추천 (처음은 0이나옴, (상품가입을안한사람이 더 많으니까))
# # for product, count in cluster_products.items():
# #   # 개수가 많은 순서로 정렬하여 상품 순서대로 나열
# #   sorted_products = sorted(product_count.items(), key=lambda x: x[1], reverse=True)
# #   top_products = [product for product, count in sorted_products[:2]]
# #   cluster_products[cluster] = top_products

# # print(sorted_products)
# # 이제 출력하자
# # for cluster, recommended_products in cluster_products.items():
# #     print(f"Cluster {cluster}: {recommended_products}")





# #     recommend_list.append((product,count))
# #     # print(f"Product: {product}, Count: {count}")
# # print(recommend_list)

# # Print the recommended products for each cluster
# # for cluster, recommended_products in cluster_products.items():
# #     print(f"Cluster {cluster}: {recommended_products}")

# # for i in product_list:
# #   for j in recommend_list:
# #       if i['id']==j[0]:
# #           print(i['product'])
# #           # j[0] = i['product']
# #           # break
# # print(j)

      


# # 나를 가장 마지막에 넣어서 내 cluster_label을 확인하고 가장 많이 가입한 상품 상위 3개를 출력해서 전환하기



# # for user in df_user:
# #   print(user)
# #   print(user['cluster_label'])
# #   if user['cluster_label']==1:
# #     print(user['financial_products'])


# # for user in (df_user.fields):
# #   print(user['age'])
# # kmeans = KMeans(n_clusters=3)
# # kmeans.fit(df_user['age'])
# # labels = kmeans.labels_



# 파일 로드

product_json = open('C:/Users/SSAFY/Desktop/21321/AB_finalpjt/back/bank/accounts/fixtures/accounts/depo_info_data326.json', encoding='UTF8')
product_list = json.load(product_json)
json_file_path = 'C:/Users/SSAFY/Desktop/21321/AB_finalpjt/back/bank/accounts/fixtures/accounts/user_data.json'
with open(json_file_path, 'r', encoding='UTF8') as file:
    user_data = json.load(file)



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


# 엘보우 기법 
df_user = pd.DataFrame(user_data)
data = df_user[['age','gender','salary','money']]

Elbow = []

for k in range(1,11):
  kmeans = KMeans(n_clusters=k)
  kmeans.fit(data)
  Elbow.append(kmeans.inertia_)

plt.plot(range(1, 11), Elbow)
plt.xlabel('Number of Clusters')
plt.ylabel('SSE')
plt.title('Elbow Curve')
plt.show()
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

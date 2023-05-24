
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
from collections import Counter

user_data_json = open('C:/Users/SSAFY/Desktop/21321/AB_finalpjt/back/bank/accounts/fixtures/accounts/user_data.json', encoding='UTF8')
user_data_list = json.load(user_data_json)
product_json = open('C:/Users/SSAFY/Desktop/21321/AB_finalpjt/back/bank/accounts/fixtures/accounts/depo_info_data326.json', encoding='UTF8')
product_list = json.load(product_json)
# print(product_list)
# product_data = product_list['product']

# for product in product_list:
  # print(product['product'])
df = pd.DataFrame(product_list)
df_user = pd.DataFrame(user_data_list)
data = df_user[['age','gender','salary','money']]
kmeans = KMeans(n_clusters=2)
kmeans.fit(data)

labels = kmeans.labels_
centroids = kmeans.cluster_centers_

df_user['cluster_label'] = labels
# print(labels)
# print(df_user['cluster_label']==1)

# cluster_label이 1인 값들의 financial_products 파악하기 !!!! 
financial_products = df_user.loc[df_user['cluster_label'] == 1, 'financial_products']
# print(list(financial_products))

# 파악했으면 뭐가 가장 많은지 확인해야지 !!!!

# 리스트를 딕셔너리로 변환하여 상품 개수 세기
product_count = dict(Counter(list(financial_products)))

# 개수가 많은 순서로 정렬하여 상품 순서대로 나열
sorted_products = sorted(product_count.items(), key=lambda x: x[1], reverse=True)

# 결과 출력
# for product, count in sorted_products:
    # print(f"Product: {product}, Count: {count}")
    
    
# 상위 3개 출력 >> 그게 추천 (처음은 가입안한 갯수가나옴 거의)
recommend_list = []
for product, count in sorted_products[:5]:
    recommend_list.append((product,count))
    # print(f"Product: {product}, Count: {count}")
print(recommend_list)

for i in product_list:
  for j in recommend_list:
      if i['id']==j[0]:
          print(i['product'])
          # j[0] = i['product']
          # break
print(j)
      
      


# 나를 가장 마지막에 넣어서 내 cluster_label을 확인하고 가장 많이 가입한 상품 상위 3개를 출력해서 전환하기



# for user in df_user:
#   print(user)
  # print(user['cluster_label'])
  # if user['cluster_label']==1:
    # print(user['financial_products'])


# for user in (df_user.fields):
#   print(user['age'])
# kmeans = KMeans(n_clusters=3)
# kmeans.fit(df_user['age'])
# labels = kmeans.labels_
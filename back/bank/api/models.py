from django.db import models
from django.conf import settings

class DepositProducts(models.Model):
    fin_prdt_cd = models.TextField(unique=True)
    kor_co_nm = models.TextField()
    fin_prdt_nm = models.TextField()
    etc_note = models.TextField()
    join_deny = models.IntegerField()
    join_member = models.TextField()
    join_way =  models.TextField()
    spcl_cnd = models.TextField()
    # 가입한 유저
    sub_user = models.ManyToManyField(settings.AUTH_USER_MODEL,blank=True, null=True)

class DepositOptions(models.Model):
    fin_prdt_cd = models.ForeignKey(DepositProducts, on_delete=models.CASCADE, related_name='depositoption')
    # 저축 금리 유형명
    intr_rate_type_nm = models.TextField(max_length=100)
    # 저축 금리
    intr_rate = models.FloatField(default=-1,null=True,blank=True)
    # 최고 우대금리
    intr_rate2 = models.FloatField()
    # 저축 기간
    save_trm = models.FloatField()
    # 저축 금리 유형
    intr_rate_type = models.TextField()
    
class InstallmentProducts(models.Model):
    fin_prdt_cd = models.TextField(unique=True)
    # 은행명
    kor_co_nm = models.TextField()
    # 상품명
    fin_prdt_nm = models.TextField()
    # 기타 유의사항
    etc_note = models.TextField()
    # 가입조건 // 1:제한X 2:서민전용 3:일부제한
    join_deny = models.IntegerField()
    # 가입대상
    join_member = models.TextField()
    # 가입방법
    join_way =  models.TextField()
    # 우대조건
    spcl_cnd = models.TextField()
    # 만기 후 이자율
    mtrt_int = models.TextField()
    # 가입한 유저
    sub_user = models.ManyToManyField(settings.AUTH_USER_MODEL,blank=True, null=True)
        
class InstallmentOptions(models.Model):
    fin_prdt_cd = models.ForeignKey(InstallmentProducts, on_delete=models.CASCADE, related_name='installmentoption')
    # 저축 금리 유형명
    intr_rate_type_nm = models.TextField(max_length=100)
    # 저축 금리
    intr_rate = models.FloatField(default=-1,null=True,blank=True)
    # 최고 우대 금리
    intr_rate2 = models.FloatField(default=-1,null=True,blank=True)
    # 저축 기간 (단위 : 개월)
    save_trm = models.FloatField()
    # 적립 유형명
    rsrv_type_nm = models.TextField()

class Subscribe_Products(models.Model):
    user_id = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='sdeposit')
    fin_prdt_cd = models.TextField()

class Like_Products(models.Model):
    user_id = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='ldeposit')
    fin_prdt_cd = models.TextField()

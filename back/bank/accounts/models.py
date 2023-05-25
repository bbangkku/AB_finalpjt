from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from django.db import models
from django.utils.translation import ugettext_lazy as _
from api.models import Subscribe_Products,Like_Products
class UserManager(BaseUserManager):
    def create_user(self, username, password, **other):
        user = self.model(
        username=username,
        **other
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **other):
        user = self.create_user(username, password, **other)
        user.is_superuser = True
        user.is_active = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    GENDER_CHOICES = (
        ('M', '남성'),
        ('F', '여성'),
    )
    BANK_CHOICES = (
        ('KEB하나은행','KEB하나은행'),
        ('SC제일은행','SC제일은행'),
        ('국민은행','국민은행'),
        ('신한은행','신한은행'),
        ('외환은행','외환은행'),
        ('우리은행','우리은행'),
        ('한국시티은행','한국시티은행'),
        ('경남은행','경남은행'),
        ('광주은행','광주은행'),
        ('부산은행','부산은행'),
        ('전북은행','전북은행'),
        ('제주은행','제주은행'),
        ('기업은행','기업은행'),
        ('농협','농협'),
        ('수협','SC제일은행'),
        ('한국산업은행','한국산업은행'),
        ('한국수출입은행','한국수출입은행'),
        ('기타','기타')
    )   
    USERNAME_FIELD = 'username'
    # REQUIRED_FIELDS = []
    email = models.EmailField(max_length=254, blank=True, null=True)
    objects = UserManager()
    username = models.CharField(max_length=30,unique=True)
    nickname = models.CharField(max_length=10)
    gender = models.CharField(max_length=3, choices=GENDER_CHOICES)
    age = models.CharField(max_length=3)
    money = models.CharField(max_length=30)
    salary = models.CharField(max_length=15)
    bank = models.CharField(max_length=10,choices=BANK_CHOICES)
    financial_products = models.ManyToManyField(Subscribe_Products,blank=True, null=True)
    like_financial_products = models.ManyToManyField(Like_Products,blank=True, null=True)

    # superuser fields
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    
    def __str__(self): 
        return self.username


# 상속 받아서 구현해보기
from allauth.account.adapter import DefaultAccountAdapter

class CustomAccountAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=True):

        from allauth.account.utils import user_email, user_field, user_username
        data = form.cleaned_data
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        email = data.get("email")
        username = data.get("username")
        # 나머지 필드
        nickname = data.get("nickname")
        gender = data.get("gender")
        age = data.get("age")
        money = data.get("money")
        salary = data.get("salary")
        financial_products = data.get("financial_products")
        # like_financial_products = data.get("like_financial_products")

        bank = data.get("bank")

        user_email(user, email)
        user_username(user, username)
        if first_name:
            user_field(user, "first_name", first_name)
        if last_name:
            user_field(user, "last_name", last_name)
        # 닉네임 필드 추가
        if nickname:
            user_field(user, "nickname", nickname)
        if gender:
            user_field(user, "gender", gender)
        if age:
            user_field(user, "age", age)
        if money:
            user_field(user, "money", money)
        if bank:
            user_field(user, "bank", bank)
        if salary:
            user_field(user, "salary", salary)
        if financial_products:
            financial_products = user.financial_products.split(',')
            financial_products.append(financial_products)
            if len(financial_products) > 1:
                financial_products = ','.join(financial_products)
            user_field(user, "financial_products", financial_products)
        # if like_financial_products:
        #     like_financial_products = user.like_financial_products.split(',')
        #     like_financial_products.append(like_financial_products)
        #     if len(like_financial_products) > 1:
        #         like_financial_products = ','.join(like_financial_products)
        #     user_field(user, "like_financial_products", like_financial_products)


        if "password1" in data:
            user.set_password(data["password1"])
        else:
            user.set_unusable_password()
            
        self.populate_username(request, user)
        if commit:
            # Ability not to commit makes it easier to derive from
            # this adapter by adding
            user.save()
        return user


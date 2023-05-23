from django.core.exceptions import ValidationError as DjangoValidationError
from rest_framework import serializers
from allauth.utils import email_address_exists, get_username_max_length
from allauth.account import app_settings as allauth_account_settings
from allauth.account.adapter import get_adapter,DefaultAccountAdapter
from allauth.account.utils import setup_user_email
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
# from rest_framework_simplejwt.tokens import RefreshToken
from .models import User
# 유저 정보 조회
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'nickname','username', 'gender', 'age', 'money','salary', 'bank',]
        extra_kwargs = {'password': {'write_only': True}}

#     def create(self, validated_data):
#         password = validated_data.pop('password1')
#         user = User(**validated_data)
#         user.set_password(password)
#         user.save()
#         return user

    # def save(self, request=None):
    #     # allauth 의 기본 adaper 를 가져옴
    #     adapter = get_adapter()
    #     user = adapter.new_user(request)
    #     self.cleaned_data = self.get_cleaned_data()
    #     # 기본 adapter 의 save_user 는 nickname 필드를 저장하지 않는다!
    #     user = adapter.save_user(request, user, self, commit=False)
    #     if "password1" in self.cleaned_data:
    #         try:
    #             adapter.clean_password(self.cleaned_data['password1'], user=user)
    #         except DjangoValidationError as exc:
    #             raise serializers.ValidationError(
    #                 detail=serializers.as_serializer_error(exc)
    #             )
    #     user.save()
    #     self.custom_signup(request, user)
    #     setup_user_email(request, user, [])
    #     return user
    
    # def create(self, validated_data):
    #     password = validated_data.pop('password')
    #     member = User(**validated_data)
    #     member.set_password(password)
    #     member.save()
    #     return member


# 회원가입 로직 중 일부
# def create(self, validated_data):
#     # 토큰 발급
#     user = self.Meta.model.objects.create_user(**validated_data)
#     refresh = RefreshToken.for_user(user)

#     return {
#         'user': user,
#         'refresh': str(refresh),
#         'access': str(refresh.access_token),
#     }


# 유저 회원 가입시 사용

class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(
        max_length=get_username_max_length(),
        min_length=allauth_account_settings.USERNAME_MIN_LENGTH,
        required=allauth_account_settings.USERNAME_REQUIRED,
    )
    # email = serializers.EmailField(max_length=50)
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)
    nickname = serializers.CharField(max_length=50)
    gender = serializers.CharField(max_length=5)
    age = serializers.CharField(max_length=10)
    money = serializers.CharField(max_length=15)
    salary = serializers.CharField(max_length=15)
    bank = serializers.CharField(max_length=15)
    financial_products = serializers.ListField(child=serializers.IntegerField(), required=False)
    like_financial_products = serializers.ListField(child=serializers.IntegerField(), required=False)

    def validate_username(self, username):
        username = get_adapter().clean_username(username)
        return username

    def validate_password1(self, password):
        return get_adapter().clean_password(password)

    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError(_("The two password fields didn't match."))
        return data

    def custom_signup(self, request, user):
        pass


    def get_cleaned_data(self):
        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),            
            # 'email': self.validated_data.get('email', ''),
            'nickname': self.validated_data.get('nickname', ''),
            'gender': self.validated_data.get('gender', ''),
            'age': self.validated_data.get('age', ''),
            'money': self.validated_data.get('money', ''),
            'salary': self.validated_data.get('salary', ''),
            'available_amount': self.validated_data.get('available_amount', ''),
            'bank': self.validated_data.get('bank', ''),
            'financial_products': self.validated_data.get('financial_products', ''),
            'like_financial_products': self.validated_data.get('like_financial_products', ''),
    
            }

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        user = adapter.save_user(request, user, self, commit=False)
        if "password1" in self.cleaned_data:
            try:
                adapter.clean_password(self.cleaned_data['password1'], user=user)
            except DjangoValidationError as exc:
                raise serializers.ValidationError(
                    detail=serializers.as_serializer_error(exc)
            )
        user.save()
        self.custom_signup(request, user)
        setup_user_email(request, user, [])
        return
    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        adapter.save_user(request, user, self)
        self.custom_signup(request, user)
        return user
    

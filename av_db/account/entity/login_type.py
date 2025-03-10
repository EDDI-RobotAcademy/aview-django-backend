from django.db import models

class LoginType(models.TextChoices):
    KAKAO = 'KAKAO', 'Kakao'
    GOOGLE = 'GOOGLE', 'google'
    NAVER = 'NAVER', 'naver'
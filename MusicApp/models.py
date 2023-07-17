from django.db import models

class User(models.Model):
    createAt = models.DateTimeField(auto_now_add=True) # 생성 시간을 자동으로 기입
    updateAt = models.DateTimeField(auto_now=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    nickname = models.CharField(max_length=100)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.nickname

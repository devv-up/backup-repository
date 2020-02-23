from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class MyUserManager(BaseUserManager):
    def _create_user(self, username, email, password, **extra_fields):
        if not email:
            raise ValueError('이메일은 필수입니다.')
        elif not username:
            raise ValueError('유저네임은 필수입니다.')
        elif not password:
            raise ValueError('비밀번호는 필수입니다.')
        email = self.normalize_email(email)
        username = self.normalize_username(username)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email, password, **extra_fields):
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(username, email, password, **extra_fields)


class Member(AbstractUser):
    verification = models.BooleanField(default=False)
    verification_key = models.CharField(max_length=256, null=True)

    bookmarks = models.ManyToManyField('Board')

    objects = MyUserManager()

    def __str__(self):
        return self.username


class Category(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title


class Board(models.Model):
    title = models.CharField(max_length=30, db_index=True)
    contents = models.TextField(db_index=True)
    created_date = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=75)
    meeting_capacity = models.IntegerField()
    meeting_date = models.DateTimeField()
    meeting_times_of_day = models.IntegerField()

    author = models.ForeignKey(Member, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Comment(models.Model):
    comments = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    comment_id = models.ForeignKey('self', on_delete=models.SET_NULL, null=True)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)

    def __str__(self):
        return self.comments


class Tag(models.Model):
    title = models.CharField(max_length=30)

    board_tags = models.ManyToManyField(Board)

    def __str__(self):
        return self.title


# class Type(models.Model):
#     type_name = models.CharField(max_length=30)
#
#     def __str__(self):
#         return self.type_name


class Photo(models.Model):
    photo_name = models.CharField(max_length=255)
    photo_type = models.CharField(max_length=30)
    photo_info = models.IntegerField(null=True)

    def __str__(self):
        return self.photo_name

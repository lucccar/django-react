from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post, Category

class TestCreatePost(TestCase):

    @classmethod
    def setUpTestData(cls) -> None:
        return super().setUpTestData()


# Create your tests here.

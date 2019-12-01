from django.test import TestCase

# Create your tests here.
import json
#
# import requests
from decouple import config
# from django.test import TestCase
#
# from .models import Label
# with open("test.json") as f:
#     data = json.load(f)
from django.urls import reverse

from .models import img
from django.contrib.auth.models import User
from django.test import Client

header = {
    'HTTP_AUTHORIZATION': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTc1MzUzMjI2LCJqdGkiOiJmY2RjNGMzNDYzM2M0ZjI4YTU2MGU1ZDA0NTFkOTQ5NyIsInVzZXJfaWQiOjN9.ZYu0e4RTjkFOQvoTwuGddS0yhulsC0BjDxBsdcSuQ80'}
# headers = {
#    'Content_Type': "application/json",
#    'Authorization': "TEST_TOKEN"
# }
BASE_URL = config('BASE_URL')
# Create your tests here.
# import requests
# import json
#
# with open("/home/admin1/noothan/project/fundoo_notes/users/test.json") as f:
#     data = json.load(f)
#
# print(data)
#
#
# class Test_Registration:

#     def test_Registration_validinput(self):
#         url = "http://127.0.0.1:8000/accounts/register"
#         user = data['register'][0]
#         Response = requests.post(url, user)
#
#         assert Response.status_code == 200
#
#     def test_Registration_nullinput(self):
#         url = "http://127.0.0.1:8000/accounts/register"
#         user = data['register'][1]
#         Response = requests.post(url, user)
#         assert Response.status_code == 404
#
#
# class Test_Login:
#     def test_Login_validinput(self):
#         url = "http://127.0.0.1:8000/accounts/login"
#         user = data['login'][0]
#         Response = requests.post(url, user)
#         assert Response.status_code == 200
#
#     def test_Login_nullinput(self):
#         url = "http://127.0.0.1:8000/accounts/login"
#         user = data['login'][1]
#         Response = requests.post(url, user)
#         assert Response.status_code == 404
#
#
# class Test_ForgotPassword:
#     def test_ForgotPassword_validinput(self):
#         url = "http://127.0.0.1:8000/accounts/forgotpassword"
#         user = data['forgotpassword'][0]
#         Response = requests.post(url, user)
#         assert Response.status_code == 200
#
#     def test_ForgotPassword_nullinput(self):
#         url = "http://127.0.0.1:8000/accounts/forgotpassword"
#         user = data['forgotpassword'][1]
#         Response = requests.post(url, user)
#         assert Response.status_code == 404
#
#
# if __name__ == "__main__":
#     Test_Registration()

class LoginTest(TestCase):

    fixtures = ['fixtures/db']
    def test_login1(self):
        url = BASE_URL + reverse('login_view')
        data = {'username':'admin','password':'admin'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code,200)
    def test_login2(self):
        url = BASE_URL + reverse('login_view')
        data = {'username':'admin','password':''}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code,400)


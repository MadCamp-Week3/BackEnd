from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import User
from .serializers import UserSerializer
from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.sessions.backends.db import SessionStore

# Create your views here.

def main(request):
    message = request.GET.get('abc')
    print(message)

    return HttpResponse("안녕?")


# @api_view(['POST'])
# def signup(request):
#     serializer = UserSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def signup(request):
    if request.method == 'POST':
        data = json.loads(request.body) # JSON 데이터 파싱
        email = data.get('email')
        password = data.get('password')
        nickname = data.get('nickname')
        # print(request.POST)
        # email = request.POST.get('email')
        # password = request.POST.get('password')
        # nickname = request.POST.get('nickname')

        session = SessionStore()
        session['email'] = email
        session['nickname'] = nickname
        session.save()

        # 받은 데이터를 처리하고 필요한 로직을 구현합니다.
        # 예를 들어, 회원 가입 로직을 수행하거나 새로운 사용자를 데이터베이스에 저장할 수 있습니다.

        # 응답 데이터를 생성합니다.
        response_data = {
            'message': 'Signup successful',
            'email': email,
            'nickname': nickname,
        }
        print(email)
        print(password)
        print(nickname)

        if not User.objects.filter(email=email).exists():
            user = User(email=email, password=password, nickname=nickname)
            user.save()
            return HttpResponse("Signup successful")
        else:
            return HttpResponse("User with this email already exists.")
    else:
        return HttpResponse("Only POST requests allowed.")


# @api_view(['POST'])
@csrf_exempt
def login(request):
    # email = request.data.get('email')
    # password = request.data.get('password')

    # user = authenticate(request, email=email, password=password)

    # if user is not None:
    #     login(request, user)
    #     serializer = UserSerializer(user)
    #     return Response(serializer.data, status=status.HTTP_200_OK)
    # return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    if request.method == "POST":
        data = json.loads(request.body)
        email = data.get('email')
        password = data.get('password')

        try:
            user = User.objects.get(email=email)
            if user.password == password:
                # 세션 생성
                session = SessionStore()
                session['email'] = email
                session['nickname'] = user.nickname
                session.save()
                print("login success")
                return HttpResponse(f"{user.id}")
            else:
                print("Invalid username or password.")
                return HttpResponseBadRequest("Invalid username or password.")
        except User.DoesNotExist:
            print("User does not exist.")
            return HttpResponseBadRequest("User does not exist.")
    else:
        print("Only POST requests allowed.")
        return HttpResponseBadRequest("Only POST requests allowed.")

# from rest_framework import status
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from .models import User
# from .serializers import UserSerializer, UserSerializer2
# from django.contrib.auth import authenticate
# from django.views.decorators.csrf import csrf_exempt

# # Create your views here.

# @api_view(['POST'])
# @csrf_exempt
# def signup(request):
#     if request.method == 'POST':
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             email = serializer.validated_data.get('email')
#             password = serializer.validated_data.get('password')
#             nickname = serializer.validated_data.get('nickname')
#             print(email)
#             print(password)
#             print(nickname)

#             if not User.objects.filter(email=email).exists():
#                 user = User(email=email, password=password, nickname=nickname)
#                 user.save()

#                 return Response({'message': 'Signup successful'}, status=status.HTTP_201_CREATED)
#             else:
#                 return Response({'error': 'User with this email already exists.'}, status=status.HTTP_400_BAD_REQUEST)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     else:
#         return Response({'error': 'Only POST requests allowed.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


# # @api_view(['POST'])
# # @csrf_exempt
# # def login(request):
# #     if request.method == 'POST':
# #         serializer = UserSerializer2(data=request.data)
# #         if serializer.is_valid():
# #             email = serializer.validated_data.get('email')
# #             password = serializer.validated_data.get('password')
# #             print(email)
# #             print(password)
# #             # print(nickname)
# #             print("여기는 되나?")
# #             user = authenticate(request, email=email, password=password)    
# #             print("여기는 안되나?")
# #             if user is not None:
# #                 print("user is not none")
# #                 # 세션 생성
# #                 request.session['email'] = email
# #                 # request.session['nickname'] = user.nickname
# #                 request.session.save()

# #                 return Response({'user_id': user.id}, status=status.HTTP_200_OK)
# #             else:
# #                 print("user is none")
# #                 return Response({'error': 'Invalid username or password.'}, status=status.HTTP_401_UNAUTHORIZED)
# #         else:
# #             print("Serializer 문제")
# #             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# #     else:
# #         return Response({'error': 'Only POST requests allowed.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
# # @api_view(['POST'])
# @csrf_exempt
# def login(request):
#     # email = request.data.get('email')
#     # password = request.data.get('password')

#     # user = authenticate(request, email=email, password=password)

#     # if user is not None:
#     #     login(request, user)
#     #     serializer = UserSerializer(user)
#     #     return Response(serializer.data, status=status.HTTP_200_OK)
#     # return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

    
#     if request.method == "POST":
#         data = json.loads(request.body)
#         email = data.get('email')
#         password = data.get('password')

#         try:
#             user = User.objects.get(email=email)
#             if user.password == password:
#                 # 세션 생성
#                 session = SessionStore()
#                 session['email'] = email
#                 session['nickname'] = user.nickname
#                 session.save()
#                 print("login success")
#                 return HttpResponse(f"{user.id}")
#             else:
#                 print("Invalid username or password.")
#                 return HttpResponseBadRequest("Invalid username or password.")
#         except User.DoesNotExist:
#             print("User does not exist.")
#             return HttpResponseBadRequest("User does not exist.")
#     else:
#         print("Only POST requests allowed.")
#         return HttpResponseBadRequest("Only POST requests allowed.")
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import User
from .serializers import UserSerializer

# Create your views here.


@api_view(['GET'])
def getUsers(request):
  person = {'name':'Dennis', 'age':28}

  users = User.objects.all() # query the User table

  serializer = UserSerializer(users, many=True)

  return Response(serializer.data) # changes python data into json

@api_view(['POST'])
def addUser(request):
  serializer = UserSerializer(data = request.data)

  if serializer.is_valid():
    serializer.save()

  return Response(serializer.data) # user 정보 모두 돌려줌

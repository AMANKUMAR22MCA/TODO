from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer

from .models import Task
# Create your views here.

@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'List':'/task-list/',
		'Detail View':'/task-detail/<str:pk>/',
		'Create':'/task-create/',
		'Update':'/task-update/<str:pk>/',
		'Delete':'/task-delete/<str:pk>/',
		}

	return Response(api_urls)

@api_view(['GET'])
def taskList(request):
	tasks = Task.objects.all().order_by('-id')
	serializer = TaskSerializer(tasks, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def taskDetail(request, pk):
	tasks = Task.objects.get(id=pk)
	serializer = TaskSerializer(tasks, many=False)
	return Response(serializer.data)


@api_view(['POST'])
def taskCreate(request):
	serializer = TaskSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['POST'])
def taskUpdate(request, pk):
	task = Task.objects.get(id=pk)
	serializer = TaskSerializer(instance=task, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def taskDelete(request, pk):
	task = Task.objects.get(id=pk)
	task.delete()

	return Response('Item succsesfully delete!')


from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserRegistrationSerializer

class UserRegistrationView(APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # This will call the create method of the serializer
            return Response({'message': 'User registered successfully!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




from django.contrib.auth import authenticate

class UserLoginView(APIView):
    def post(self, request):
		
        email = request.data.get('email')
        password = request.data.get('password')

        # Try to authenticate the user
        user = authenticate(request, email=email, password=password)
        
        if user is not None:
            # User is authenticated, return success response
            return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
        else:
            # User is not authenticated or user does not exist
            return Response({'error': 'Invalid credentials or user not registered'}, status=status.HTTP_400_BAD_REQUEST)

# from rest_framework.response import Response
# from rest_framework import viewsets,status
# from rest_framework import mixins
# from .models import Task
# from .serializers import TaskSerializer

# class TaskViewSet(mixins.CreateModelMixin,
                  
#                   mixins.RetrieveModelMixin,
#                   mixins.UpdateModelMixin,
#                   mixins.DestroyModelMixin,
#                   mixins.ListModelMixin,
#                   viewsets.GenericViewSet):
#     """
#     A viewset for viewing and editing Task instances.
#     """
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer
    
	
# 	 def create(self, request, *args, **kwargs):
# 		serializer = self.get_serializer(data=request.data)
# 		serializer.is_valid(raise_exception=True)
# 		self.perform_create(serializer)
# 		headers = self.get_success_headers(serializer.data)
# 		return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

# 	 def perform_create(self, serializer):
# 		serializer.save()



# from rest_framework.response import Response
# from rest_framework import viewsets, status
# from rest_framework import mixins
# from .models import Task
# from .serializers import TaskSerializer

# class TaskViewSet(mixins.CreateModelMixin,
#                   mixins.RetrieveModelMixin,
#                   mixins.UpdateModelMixin,
#                   mixins.DestroyModelMixin,
#                   mixins.ListModelMixin,
#                   viewsets.GenericViewSet):
#     """
#     A viewset for viewing and editing Task instances.
#     """
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer

    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #     headers = self.get_success_headers(serializer.data)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    # def perform_create(self, serializer):
    #     serializer.save()

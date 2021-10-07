from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView
from users.serializers import GroupsSerializer, UserSerializer
from users.models_users import Users
from users.models_groups import Groups

# Group views
class ListGroups(ListAPIView):
	"""This endpoint list all of the available groups"""
	queryset = Groups.objects.all()
	serializer_class = GroupsSerializer

class CreateGroup(CreateAPIView):
	"""This endpoint allows for creation of a group"""
	queryset = Groups.objects.all()
	serializer_class = GroupsSerializer

class UpdateGroup(UpdateAPIView):
	"""This endpoint allows for updating a specific group"""
	queryset = Groups.objects.all()
	serializer_class = GroupsSerializer

class DelelteGroup(DestroyAPIView):
	"""This endpoint allows for deletion a specific group"""
	queryset = Groups.objects.all()
	serializer_class = GroupsSerializer

# Users views
class ListUsers(ListAPIView):
	"""This endpoint list all of the available groups"""
	queryset = Users.objects.all()
	serializer_class = UserSerializer

class CreateUser(CreateAPIView):
	"""This endpoint allows for creation of a group"""
	queryset = Users.objects.all()
	serializer_class = UserSerializer

class UpdateUser(UpdateAPIView):
	"""This endpoint allows for updating a specific group"""
	queryset = Users.objects.all()
	serializer_class = UserSerializer

class DelelteUser(DestroyAPIView):
	"""This endpoint allows for deletion a specific group"""
	queryset = Users.objects.all()
	serializer_class = UserSerializer

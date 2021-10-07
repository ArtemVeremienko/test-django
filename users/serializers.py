from rest_framework import fields, serializers
from users.models_users import Users
from users.models_groups import Groups

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = Users
		fields = "__all__"

class GroupsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Groups
		fields = "__all__"

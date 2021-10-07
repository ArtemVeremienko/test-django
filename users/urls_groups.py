from django.urls import path
from users import views

urlpatterns = [
	path('', views.ListGroups.as_view(), name='groups_list'),
	path('create/', views.CreateGroup.as_view(), name='group_create'),
	path('update/<int:pk>', views.UpdateGroup.as_view(), name='group_update'),
	path('delete/<int:pk>', views.DelelteGroup.as_view(), name='group_delete'),
]

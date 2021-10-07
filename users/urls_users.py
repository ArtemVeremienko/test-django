from django.urls import path
from users import views

urlpatterns = [
	path('', views.ListUsers.as_view(), name='users_list'),
	path('create/', views.CreateUser.as_view(), name='user_create'),
	path('update/<int:pk>', views.UpdateUser.as_view(), name='user_update'),
	path('delete/<int:pk>', views.DelelteUser.as_view(), name='user_delete'),
]

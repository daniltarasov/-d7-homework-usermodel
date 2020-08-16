# from common.views import index, login, logout  
from common.views import RegisterView, CreateUserProfile, CreateSocUserProfile, ProfileUpdate, SocProfileUpdate  
# from common.views import index, RegisterView, CreateUserProfile  
from django.urls import path  
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy  
from allauth.account.views import login, logout, signup
from common import views


app_name = 'common'  
urlpatterns = [  
    # path('', index, name='index'),  
	# вариант с функциями
	# path('login/', login, name='login'),  
	# path('logout/', logout, name='logout'),
	# вариант с CBV
	# path('login/', LoginView.as_view(template_name='login.html'), name='login'),
	# path('logout/', LogoutView.as_view(), name='logout'),  
	# вариант с гитхабом
    path('profile/', views.profile, name='profile'),
	path('profile/user/<int:pk>/', ProfileUpdate.as_view()),
	path('profile/socuser/<int:pk>/', SocProfileUpdate.as_view()),

	path('login/', login, name='login'),  
	path('logout/', logout, name='logout'),
	# path('register/', RegisterView.as_view(  
    #     template_name='register.html',  
	# 	success_url=reverse_lazy('common:profile-create')
	# 	), name='register'),
	path('register/', signup, name='register'),
	path('profile-create/', 
		CreateUserProfile.as_view(), name='profile-create'),
    path('socprofile-create/', 
		CreateSocUserProfile.as_view(), name='socprofile-create'),    
  
]
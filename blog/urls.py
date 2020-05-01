    
from django.urls import path
from . import views
from .views import PostListView,UserPostListView


#we call funtions in the views file like views.home or views.about

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    
    path('about/', views.about, name='blog-about'),
    path('createpost/',views.CreatePost,name='create-post'),
   	path('user/<str:username>', UserPostListView.as_view(), name='user-post'),
    path('post/<int:pk>',views.PostDetailView.as_view(),name='post-detail'),
    path('post/<int:pk>/update',views.UpdatePost.as_view(),name='post-update'),
    path('post/<int:pk>/delete',views.DeletePostView.as_view(),name='post-delete'),
    

]
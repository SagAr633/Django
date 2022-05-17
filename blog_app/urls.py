from django.urls import path
from blog_app import views

urlpatterns=[

    path('',views.HomeView.as_view(),name='home'),
    path('signup',views.UserRegView.as_view(),name='signup'),
    path('login',views.UserLoginView.as_view(),name='u_login'),
    path('add',views.AddBlogView.as_view(),name='add_blog'),
    path('blog',views.ListBlogView.as_view(),name='user_blogs'),
    path('signout',views.signout,name='signout'),
    path('edit/<int:id>',views.EditView.as_view(),name='edit_blog'),
    path('remove/<int:id>',views.RemoveView.as_view(),name='delete'),
    path('all',views.ListAllBlogsView.as_view(),name='all_user_blogs'),
    path('politics',views.PoliticsView.as_view(),name='topic_politics'),
    path('entertainment',views.EntertainmentView.as_view(),name='topic_entertainment'),
    path('news',views.NewsView.as_view(),name='topic_news'),
    path('sports',views.SportsView.as_view(),name='topic_sports'),
    path('tech',views.TechView.as_view(),name='topic_tech'),
    path('profile',views.UserProfileCreateView.as_view(),name='u_pro'),
    path('pro_det/<int:id>',views.UserProfileView.as_view(),name='pro_detail'),
    path('pro_up/<int:id>',views.UserProfileUpdateView.as_view(),name='pro_update')



]

from django.shortcuts import render,redirect
from blog_app.models import Blogs,UserProfile
from blog_app.forms import UserRegForm,UserLoginForm,AddBlogForm,UserProfileForm
from django.views.generic import View,CreateView,ListView,UpdateView,DetailView
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from blog_app.decorators import sigin_required
# from blog_app.decorators import sigin_required
# from django.utils.decorators import method_decorator

class HomeView(ListView):
    model = Blogs
    template_name = 'Home.html'
    context_object_name = 'home'

class UserRegView(View):
    template_name = 'UserSignup.html'
    def get(self,request):
        form=UserRegForm()
        return render(request,self.template_name,{'form':form})
    def post(self,request):
        form=UserRegForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('u_login')
        else:
            return redirect('signup')

class UserLoginView(View):
    template_name='UserLogin.html'
    def get(self,request,*args,**kwargs):
        form=UserLoginForm()
        return render(request,self.template_name,{'form':form})
    def post(self,request,*args,**kwargs):
        form=UserLoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(request,username=username,password=password)
            if user:
                login(request,user)
                return redirect('all_user_blogs')
            else:
                return redirect('signup')


class AddBlogView(CreateView):
    model = Blogs
    form_class = AddBlogForm
    template_name = 'AddBlog.html'
    success_url = reverse_lazy('user_blogs')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ListBlogView(ListView):
    model = Blogs
    template_name = 'UserBlogs.html'
    context_object_name = 'u_blogs'
    def get_queryset(self):
        return Blogs.objects.filter(user=self.request.user)


class ListAllBlogsView(ListView):
    model = Blogs
    template_name = 'AllBlogs.html'
    context_object_name = 'all_blogs'

class EditView(UpdateView):
    model = Blogs
    form_class = AddBlogForm
    template_name = 'EditBlog.html'
    success_url = reverse_lazy('user_blogs')
    pk_url_kwarg = 'id'

class RemoveView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get('id')
        Blogs.objects.get(id=id).delete()
        return redirect('user_blogs')

# class PoliticsView(View):
#     def get(self,request,*args,**kwargs):
#         news=kwargs.get('topic')
#         topic=[]
#         return render(request,'Politics.html')

class PoliticsView(ListView):
    model = Blogs
    template_name = 'Politics.html'
    context_object_name = 'n_topic'

class EntertainmentView(ListView):
    model = Blogs
    template_name = 'Entertainment.html'
    context_object_name = 'n_topic'

class NewsView(ListView):
    model = Blogs
    template_name = 'News.html'
    context_object_name = 'n_topic'

class SportsView(ListView):
    model = Blogs
    template_name = 'Sports.html'
    context_object_name = 'n_topic'

class TechView(ListView):
    model = Blogs
    template_name = 'Tech.html'
    context_object_name = 'n_topic'

# @method_decorator(sigin_required,name='dispatch')
class UserProfileCreateView(CreateView):
    model = UserProfile
    form_class = UserProfileForm
    template_name = 'User_Profile_Create.html'
    success_url = reverse_lazy('pro_detail')

    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)


class UserProfileView(DetailView):
    model = UserProfile
    template_name = 'ProfileDetail.html'
    context_object_name = 'prof'
    pk_url_kwarg = 'id'

class UserProfileUpdateView(UpdateView):
    model = UserProfile
    form_class = UserProfileForm
    template_name = 'Profile_update.html'
    success_url = reverse_lazy('u_pro')
    pk_url_kwarg = 'id'


def signout(request):
    logout(request)
    return redirect('u_login')


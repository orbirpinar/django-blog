from django.shortcuts import render,redirect,get_object_or_404
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import UserPassesTestMixin,LoginRequiredMixin
from django.views import generic
from django.views.generic.edit import DeleteView,UpdateView
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.contrib.auth.models import User
#Buradaki fonksiyonlar HttpResponse gönderiyorlar


	
class PostListView(generic.ListView):
	paginate_by = 5
	model = Post
	template_name = 'blog/home.html'
	context_object_name = 'posts'
	ordering = ['-date_posted']

def about(request):
    return render(request, 'blog/about.html',{'title':'About'})
    #About a title oluşturduk şimdi bunu templatede çağıracağız

class PostDetailView(generic.DetailView):
	model = Post
	


class UserPostListView(generic.ListView):
	model = Post
	context_object_name = 'posts'
	template_name = 'blog/user_post.html'
	paginate_by = 5
	def get_queryset(self):
		user = get_object_or_404(User, username = self.kwargs.get('username'))
		return Post.objects.filter(author=user).order_by('-date_posted')


@login_required
def CreatePost(request):
	if request.method == 'POST':
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.save()
			return redirect('blog-home')
	else:
		form = PostForm()
	return render(request, 'blog/create_post.html',{'form':form})

class UpdatePost(UserPassesTestMixin,LoginRequiredMixin,UpdateView):

	model = Post
	template_name = 'blog/create_post.html'
	fields = ['title','content']

	#UsersPassesTestMixin eğer sadece kendi postunu update etmeye yarıyor
	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False
	

	

class DeletePostView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
	model = Post
	success_url = reverse_lazy('blog-home')
	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False	





#blog --> templates -->blog --> template.html

"""
Bu Bölümde Yapılanlar
1)Dummy data oluşturuldu
2)Bu dummy dictionaryi home page aktardık
3)home pagein templatein de for döngüsüyle bu post verilerini çağırdık
4)İf statemenlı title oluşturuldu eğer varsa yazdır yoksa default olanı yazdır.
5)base.html adında bir dosya oluşturduk
6)base.htmli bizim layoutumuz oldu buna göre diğer html dosyalarına ekstradan aynı şeyleri yazmayacağız.
7)Bunun için block endblock ve extends yapılarını gördük
8)navbar ve custom css oluşturduk
9)article html ve css contentlerini düzenledik
10)href içindeki url'i değiştirerek  django url tagini kullanıyoruz bunu yapmamızın sebebi çünkü sonradan eğer ordaki adresin yeri değişirse bizim kodumuz o adrese gidemeyecek
bu sebeple oraya django urli girerek bunu önlemiş oluyoruz
11)Yukarıdaki olay şöyle çalışıyor --> % % curly braces ve yüzde işaretleri arasına url giriyoruz yanına ise 'urls.py deki o adresin name'ini giriyoruz'





"""

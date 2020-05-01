from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm
from django.views import generic
from .models import Profile

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'{username} hesabı oluşturuldu.Şimdi giriş yapabilirsin')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})



@login_required
def profile(request):
    if request.method == 'POST':
        ##instance=request.user userformunu o anki login olan kişiyle dolduruyor,request.Post ise formun içindekileri Post ediyor
        u_form = UserUpdateForm(request.POST,instance=request.user)
        ##burada ise profil formunu o yani pictureı dolduruyor
        p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,f'Profiliniz güncellenmiştir')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
    'u_form':u_form,
    'p_form':p_form
    }
    return render(request,'users/profile.html',context)

class AuthorDetailView(generic.DetailView): 
    model = Profile
    fields = ['username','image','bio','birth_date']
    def author_detail_view(request,primary_key):
        profile = get_object_or_404(Profile,pk=primary_key)
        return render(request,'users/profile_detail.html',context={'profile':profile})


class AuthorListView(generic.ListView):
    model = Profile
    template_name  = 'users/profile_list.html'
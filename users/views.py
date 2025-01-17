
# Reemplazado por clase de SignupView
#from django.shortcuts import render, redirect
#from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

#Views

from django.contrib.auth import views as auth_views

from django.views.generic import DetailView , FormView , UpdateView
from django.urls import reverse,reverse_lazy

# Models

from django.contrib.auth.models import User
from posts.models import Post
from users.models import Profile

#Exception

from django.db.utils import IntegrityError

#Forms

# Reemplazado por clase view y se quito el import ProfileForm

from users.forms import SignupFrom

class UserDetailView(LoginRequiredMixin,DetailView):
    """User detail view."""

    template_name = 'users/detail.html'
    slug_field = 'username'
    slug_url_kwarg = 'username'
    queryset = User.objects.all()
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        """Add user's posts to context."""
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context['posts'] = Post.objects.filter(user=user).order_by('-created')
        return context


class SignupView(FormView):

    template_name = 'users/signup.html'
    form_class = SignupFrom
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class UpdateProfileView(LoginRequiredMixin, UpdateView):

    template_name = 'users/update_profile.html'
    model = Profile
    fields = ['website', 'biography', 'phone_number', 'picture']

    def get_object(self):
        #regresa el perfil del usuario
        return self.request.user.profile


    def get_success_url(self):
        username = self.object.user.username
        return reverse('users:detail', kwargs={'username': username})


#Reemplazado por clase view

'''

@login_required
def update_profile(request):
    """Update a user's profile view."""
    profile = request.user.profile

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data

            profile.website = data['website']
            profile.phone_number = data['phone_number']
            profile.biography = data['biography']
            profile.picture = data['picture']
            profile.save()

            url = reverse('users:detail', kwargs={'username': request.user.username})
            return redirect(url)

    else:
        form = ProfileForm()

    return render(
        request=request,
        template_name='users/update_profile.html',
        context={
            'profile': profile,
            'user': request.user,
            'form': form
        }
    )
'''
class LoginView(auth_views.LoginView):
    """Login view."""

    template_name = 'users/login.html'


class LogoutView(LoginRequiredMixin, auth_views.LogoutView):
    """Logout view."""

    template_name = 'users/logged_out.html'



'''
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
           login(request, user)
           return redirect ('posts:feed')
        else:
            return render(request,'users/login.html', {'error':'Invalid username and password'})

    return render(request, 'users/login.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('users:logout')


def signup_view(request):
    if request.method == 'POST':
        form = SignupFrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users:login')
    else:
            form = SignupFrom()
    return render(
            request=request,
            template_name='users/signup.html',
            context={'form':form}
        )
        '''
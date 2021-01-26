from django.views.generic.detail import DetailView
from accounts.models import Profile
from django.shortcuts import render, redirect
from .forms import ProfileEditForm, RegistrationForm, UserEditForm
# from django.contrib.auth.forms import UserCreationForm
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from .decorators import login_forbidden
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.urls import reverse
from django.contrib.auth.mixins import  LoginRequiredMixin
from django.contrib import messages

# Create your views here.

@method_decorator(login_forbidden, name='dispatch')
class RegistrationView(View):
    def get(self, request):
        return render(request, 'accounts/register.html', {'form': RegistrationForm})

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            # save an instance of the data
            new_user = form.save(commit=False)
            # hash the password
            new_user.set_password(cd['password'])

            new_user.save()

            # create a new profile for the new user
            Profile.objects.create(user=new_user)

            return redirect(reverse('index'))

class ProfileView(LoginRequiredMixin, UpdateView):
    login_url = '/auth/login'
    redirect_field_name = 'login'
    template_name = 'accounts/profile.html'
    context_object_name = 'profile'
    fields = ['address', 'phone', ]
    # form_class = RegistrationForm()

    # def get_object(self):
    #     user = get_object_or_404(Profile, user=self.request.user)
    #     print(user)
    #     return user

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['profile_form'] = ProfileEditForm(instance=self.request.user.profile) 
    #     context['user_form'] = UserEditForm(instance=self.request.user)
    #     return context

    # def get_success_url(self) -> str:
    #     url = '/auth/profile'
    #     return url

    def get(self, request):
        profile_form = ProfileEditForm(instance=request.user.profile)
        user_form = UserEditForm(instance=request.user)
        return render(request, 'accounts/profile.html', {'profile_form' : profile_form, 'user_form': user_form})

    def post(self, request):
        profile_form = ProfileEditForm(data=request.POST, instance=request.user.profile, files=request.FILES)
        user_form = UserEditForm(data=request.POST, instance=request.user)
        if profile_form.is_valid() and user_form.is_valid():
            profile_form.save()
            user_form.save()
            messages.success(request, 'Profile was successfully updated')
            print(messages.success(request, 'Profile was successfully updated'))
            return redirect(reverse('accounts:profile'))


# class UpdateProfileView():


        
    # queryset = get_object_or_404(Profile, user=self.request.user)
    # def get_queryset(self):
    #     self.profile = get_object_or_404(Profile, user=self.request.user)
    #     print(self.profile)
    #     return self.profile
    # def get_queryset(self):
    #     return super(ProfileView).get_queryset(self.request, )
    
    # def get(self, request):
        
    #     return render()

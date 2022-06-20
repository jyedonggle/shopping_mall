from django.shortcuts import render
from .form import RegisterForm

# Create your views here.

def register(request):
    if request.method =='POST':
        user_form = RegisterForm(request.POST)
        if user_form.is_vaild():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'registeration/register_done.html', {'new_user':new_user})
    else:
        user_form = RegisterForm()

        return render(request, 'registeration/register.html', {'form':user_form})

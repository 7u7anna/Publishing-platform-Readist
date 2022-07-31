from django.shortcuts import redirect, render
from .forms import UserAccountCreationForm, AccountUpdateForm, AccountPhotoUpdate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from base.models import Article

def register(request):
    form = UserAccountCreationForm()

    if request.method == 'POST':
        form = UserAccountCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f"Account have been created. Thank you for joining Readist.")
            return redirect('homepage')
    else:
        form = UserAccountCreationForm()

    context = {
        'form' : form,
    }

    return render(request, 'accounts/register.html', context)

def account(request):
    user_articles_list = Article.objects.all().filter(author=request.user)
    
    context = {
        'user_articles_list' : user_articles_list,
    }

    return render(request, 'accounts/account.html', context)

@login_required
def account_update(request):
    if request.method == 'POST':
        photo_form = AccountPhotoUpdate(request.POST, request.FILES, instance=request.user.account)
        data_form = AccountUpdateForm(request.POST, request.FILES, instance=request.user)
        if photo_form.is_valid() and data_form.is_valid():
            photo_form.save()
            data_form.save()
            messages.success(request, f"Changes have been saved.")
            return redirect('account')
    else:
        photo_form = AccountPhotoUpdate(instance=request.user.account)
        data_form = AccountUpdateForm(instance=request.user)

    context = {
        'photo_form' : photo_form,
        'data_form' : data_form,
    }

    return render(request, 'accounts/update_account.html', context)

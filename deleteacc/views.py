from django.shortcuts import render, redirect
from django.core.exceptions import PermissionDenied
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.models import User
from .forms import DeleteAccountForm

# Create your views here.

def DeleteAccount(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            delete_post = DeleteAccountForm(request.POST)
            if delete_post.is_valid():
                user = User.objects.get(email = request.user.email)
                user.delete()
                return redirect(DeleteAccountConfirm)
        form = DeleteAccountForm
        context = {"form" : form}
        return render(request, 'deleteacc/delete_account.html', context)
    else:
        #If the user accesses this page without being logged in
        #A 403 error will be raised
        raise PermissionDenied()
    
def DeleteAccountConfirm(request):
    return render(request, 'deleteacc/delete_account_confirm.html')

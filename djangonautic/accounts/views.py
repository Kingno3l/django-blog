from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # log the user in later...
            return redirect('articles:list')
    else:
        form = UserCreationForm()  # Initialize the form for a GET request or if form is invalid

    return render(request, 'accounts/signup.html', {'form': form})

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Demo
@login_required
def protected_view(request):
    return render(request, 'app/protected.html')

@login_required
def index(request):
    return render(request, 'app/index.html')
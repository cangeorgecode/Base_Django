# Django base template  

## Authentication usage  
Using django-allauth for authentication. Here's how to use it:  

### For Function-Based Views
```python
from django.contrib.auth.decorators import login_required

@login_required
def protected_view(request):
    # Your view logic
```

```python
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

class ProtectedView(LoginRequiredMixin, TemplateView):
    template_name = 'protected.html'
    # Optional customizations
    login_url = '/custom-login/'
    redirect_field_name = 'next'
```
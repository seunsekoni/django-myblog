from .models import Category

def categories(request):
    return Category.objects.all()
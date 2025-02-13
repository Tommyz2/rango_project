from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.models import User
from rango.models import Category, Page
from rango.forms import PageForm, UserForm, UserProfileForm, CategoryForm

def about(request):
    return render(request, 'rango/about.html')

def index(request):
    category_list = Category.objects.order_by('-likes')[:5]
    page_list = Page.objects.order_by('-views')[:5]  # 获取浏览次数最多的五个页面
    context_dict = {
        'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!',
        'categories': category_list,
        'pages': page_list,
    }
    return render(request, 'rango/index.html', context=context_dict)

def some_view(request):
    categories = Category.objects.all()  
    return render(request, 'rango/template.html', {'categories': categories})

def show_category(request, category_name_slug):
    category = get_object_or_404(Category, slug=category_name_slug)
    pages = Page.objects.filter(category=category)
    context_dict = {'pages': pages, 'category': category}
    return render(request, 'rango/category.html', context=context_dict)

def add_category(request):
    form = CategoryForm()
    
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('/rango/')
        else:
            print(form.errors)

    return render(request, 'rango/add_category.html', {'form': form})

def add_page(request, category_name_slug):
    try:
        category = Category.objects.get(slug=category_name_slug)
    except Category.DoesNotExist:
        category = None

    if category is None:
        return redirect('/rango/')

    form = PageForm()
    
    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            page = form.save(commit=False)
            page.category = category
            page.views = 0
            page.save()
            return redirect(reverse('rango:show_category', kwargs={'category_name_slug': category_name_slug}))
        else:
            print(form.errors)

    return render(request, 'rango/add_page.html', {'form': form, 'category': category})

def register(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()
            return redirect('rango:index')
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request, 'rango/register.html', {'user_form': user_form, 'profile_form': profile_form})
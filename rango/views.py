from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponse
from datetime import datetime
from rango.models import Category, Page, UserProfile
from rango.forms import CategoryForm, PageForm, UserForm, UserProfileForm


def index(request):
    """ Display the homepage """
    category_list = Category.objects.order_by('-likes')[:5]
    page_list = Page.objects.order_by('-views')[:5]
    return render(request, 'rango/index.html', {'categories': category_list, 'pages': page_list})


def about(request):
    """ Track visit count """
    visits = request.session.get('visits', 0)
    last_visit_time = request.session.get('last_visit', str(datetime.now()))

    try:
        last_visit = datetime.strptime(last_visit_time[:19], "%Y-%m-%d %H:%M:%S")
    except ValueError:
        last_visit = datetime.now()

    if (datetime.now() - last_visit).seconds > 86400:  
        visits += 1
        request.session['visits'] = visits
        request.session['last_visit'] = str(datetime.now())
        request.session.modified = True

    return render(request, 'rango/about.html', {'visits': visits})


def show_category(request, category_name_slug):
    """ Display category details """
    category = get_object_or_404(Category, slug=category_name_slug)
    pages = Page.objects.filter(category=category)
    return render(request, 'rango/category.html', {'category': category, 'pages': pages})


def add_category(request):
    """ Handle category creation """
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect(reverse('rango:index'))
    else:
        form = CategoryForm()
    return render(request, 'rango/add_category.html', {'form': form})


def add_page(request, category_name_slug):
    """ Allow users to add a new page to a specific category """
    category = get_object_or_404(Category, slug=category_name_slug)

    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            page = form.save(commit=False)
            page.category = category
            page.views = 0
            page.save()
            return redirect(reverse('rango:show_category', kwargs={'category_name_slug': category.slug}))
    else:
        form = PageForm()

    return render(request, 'rango/add_page.html', {'form': form, 'category': category})


def register(request):
    """ Handle user registration """
    registered = False

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST, request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request, 'rango/register.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        'registered': registered
    })


def user_login(request):
    """ Handle user login, supporting 'next' parameter """
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            next_url = request.GET.get('next', reverse('rango:index'))
            return redirect(next_url)
        else:
            return render(request, 'rango/login.html', {'error': 'Invalid credentials'})

    return render(request, 'rango/login.html')


@login_required
def user_logout(request):
    """ Handle user logout """
    logout(request)
    return redirect(reverse('rango:index'))
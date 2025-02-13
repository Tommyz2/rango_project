import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')

import django
django.setup()

from rango.models import Category

def populate():
    python_cat = Category.objects.get_or_create(name='Python')[0]
    python_cat.views = 128
    python_cat.likes = 64
    python_cat.save()

    django_cat = Category.objects.get_or_create(name='Django')[0]
    django_cat.views = 64
    django_cat.likes = 32
    django_cat.save()

    other_cat = Category.objects.get_or_create(name='Other Frameworks')[0]
    other_cat.views = 32
    other_cat.likes = 16
    other_cat.save()

if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()

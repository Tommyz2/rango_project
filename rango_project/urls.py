from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('rango.urls')),  # ✅ 确保 rango.urls 在根目录下被包含
    path('admin/', admin.site.urls),
]

# 让 Django 处理静态文件
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
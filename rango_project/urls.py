from django.contrib import admin
from django.urls import path, include
from rango import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),  # 根 URL 访问 index
    path('rango/', include('rango.urls')),  # rango 相关 URL 交由 rango/urls.py 处理
    path('admin/', admin.site.urls),  # Django 管理后台
]

# 确保静态文件和媒体文件能够被正确访问
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.schemas import get_schema_view
from rest_framework import permissions
from drf_yasg.views import get_schema_view as gsv
from drf_yasg import openapi


schema_view = gsv(
    openapi.Info(
        title='Doc title',
        default_version='v1',
        description='Doc description',
        terms_of_service='https://www.instagram.com/',
        contact=openapi.Contact(email='anvar@gmail.com'),
        license=openapi.License(name="Bez license")
    ),
    public=True, permission_classes=(permissions.AllowAny, ),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shop.urls', namespace='shop')),
    path('', include('others.urls', namespace='others')),
    path('', include('registrations.urls')),
    path('rest-auth/', include('rest_framework.urls')),
    path('cart/', include('cart.urls', namespace='cart')),
    path('api/v1/', include('api.urls')),
    path('openapi/', get_schema_view(
        title="Dm yomon title",
        description="Dm yomon description",
        version="1.0.0"
    ), name="openapi-schema"),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='redoc')
    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

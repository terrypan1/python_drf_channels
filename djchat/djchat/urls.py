from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
# from server.views import ServerListViewSet
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from server.views import ServerListAPIView, ServerDetailAPIView
# router = DefaultRouter()
# router.register("api/server/select", ServerListViewSet)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path('servers/', ServerListAPIView.as_view(), name='server-list'),
    path('servers/<int:pk>/', ServerDetailAPIView.as_view(), name='server-detail'),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    # Optional UI:
    path(
        "api/schema/swagger-ui/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/schema/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
]

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from evaluations.views import PlayerViewSet, EvaluationViewSet, WeightViewSet


# Create a router and register viewsets
router = DefaultRouter()
router.register('players', PlayerViewSet)
router.register('evaluations', EvaluationViewSet)
router.register('weights', WeightViewSet)

# Add the router's URLs to the urlpatterns
urlpatterns = [
    path('admin/', admin.site.urls),  # admin panel
    path('api/', include(router.urls)),  # Add API routes
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

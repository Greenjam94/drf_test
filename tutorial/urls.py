from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from tutorial.quickstart import views as q_views
from snippets import views as s_views

router = routers.DefaultRouter()
router.register(r'users', q_views.UserViewSet)
router.register(r'groups', q_views.GroupViewSet)
router.register(r'snippets', s_views.SnippetViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
    path('web/', include('domains.urls')),
    path('network/', include('servers.urls'))
]

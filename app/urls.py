from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),
    path('registration/', views.registration, name='registration'),
    path('account/', include('django.contrib.auth.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('profile/', views.profile, name='profile'),
    path('project/<post>', views.project, name='project'),
    path('search/', views.search_results, name='search_results'),
    url(r'^api/projects/$', views.ProjectList.as_view()),
    url(r'^api/profiles/$', views.ProfileList.as_view())
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
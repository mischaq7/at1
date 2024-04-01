from django.urls import path, include

app_name = 'eduprod'
urlpatterns = [
    path('users/', include('users.urls')),
    path('eduprod/', include('eduprod.urls')), 
]

from django.contrib import admin
from django.urls import path

from planes.views import login

from schema_graph.views import Schema

urlpatterns = [
    path('admin/', admin.site.urls),
    path("schema/", Schema.as_view()),
    path('login/', login, name='login_url'),
]

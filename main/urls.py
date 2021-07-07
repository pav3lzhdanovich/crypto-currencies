from django.urls import path
from . import views
from main import views

# Ссылки на странциы
urlpatterns = [
    path('', views.index)

    # path('', views.index)

]
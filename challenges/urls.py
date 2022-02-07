
from importlib.resources import path
from unicodedata import name
from . import views


from django.urls import path
# make sure to import views from the current directory always
from . import views
urlpatterns = [
    path("", views.index, name='home'),
    path('<int:month>', views.month_by_number),
    path('<str:month>', views.monthly_challenge, name='month-name')
]

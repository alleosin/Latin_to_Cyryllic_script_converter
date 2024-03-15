from django.urls import path
from .views import view_page

urlpatterns = [
    path("<str:username>/", view_page, name="view_page"),
]

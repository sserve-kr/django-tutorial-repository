from django.urls import path

from .views import post_view

app_name = 'post'

urlpatterns = [
    path('<int:post_id>', post_view, name="post_view")
]

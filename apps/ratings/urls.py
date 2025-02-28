from django.contrib import admin
from django.urls import path

from .views import PostRatingView

urlpatterns = [
    path("post/<int:post_id>/mark_add", PostRatingView.as_view(), name='post_rating'),

]
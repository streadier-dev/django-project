
from django.urls import path

#views
from posts import views

urlpatterns = [
    path(route='',
    view=views.PostFeedView.as_view(),
    name='feed'),

    path(route='',
    view=views.create_post,
    name='create'),

    path(
        route='posts/<int:post_id>/',
        view=views.PostDetailView.as_view(),
        name='post_detail'
    ),
]

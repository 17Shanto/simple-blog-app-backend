from . import views
from django.urls import path

urlpatterns = [
    path("homepage/", views.homepage, name= "post_home"),
    path("", views.PostListCreateView.as_view(), name="list_posts"),
    path("<int:pk>/", views.PostRetrieveUpdateDeleteView.as_view(), name="post_retrieve_delete_update")
    # path("<int:post_id>", views.post_detail, name= "post_details"),
    # path("update/<int:post_id>/", views.update_post),
    # path("delete/<int:post_id>/", views.delete_post, name="delete_post")
]
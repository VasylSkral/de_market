from django.urls import path
from product import views

urlpatterns = [
    path('<int:item_id>/comment/<int:comment_id>/delete/', views.comment_delete),
    path('<int:item_id>/comment/create', views.create_comment),
    path('<int:item_id>/comment/<int:comment_id>/update', views.update_comment)
    ]
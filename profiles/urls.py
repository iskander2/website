from django.urls import path
from .views import add_comment, signup, feedback


app_name="profiles"



urlpatterns = [
    path( 'signup/',signup, name ="signup"),
    path('comment/<int:pk>,',add_comment,name="add_comment"),
    path( 'feedback/',feedback, name ="feedback"),
]
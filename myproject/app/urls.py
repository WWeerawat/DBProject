from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("resCard/<str:pk>", views.resCard, name="resCard"),
    path("card3Col", views.card3Col, name="card3Col"),
    # path("categoryCard", views.categoryCard, name="categoryCard"),
    path("login", views.login, name="login"),
    path("signup", views.signup, name="signup"),
    path("review", views.review, name="review"),
    path("userprofile/<str:pk>", views.userprofile, name="userprofile"),
    path("manager", views.managerprofile, name="workerprofile"),
    path("queueManagement", views.queueManagement, name="queueManagement"),
    # path("foodList", views.foodList, name="foodList"),
    path("admin", views.admin, name="adminpage"),
    path("requestRegistration", views.requestRegistration, name="requestRegistration"),
    path("foodList/<str:pk>", views.foodList, name="foodList"),
    path("category/<str:pk>", views.category, name="category"),
    path("managerControl/<str:pk>", views.managerControl, name="managerControl"),
    path("staffList/<str:pk>", views.staffList, name="staffList"),
    path("profileDetail/", views.profileDetail, name="profileDetail"),

]

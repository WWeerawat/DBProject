from django import forms
from django.contrib import messages
from django.db.models.aggregates import Sum
from django.utils import timezone
from django.contrib.auth.models import Group
from django.shortcuts import redirect, render, get_object_or_404

from users.models import Member

from django.shortcuts import render
from django.contrib.auth.models import Group, User
from django.contrib.auth.decorators import login_required
from restaurants.models import Category, Restaurant, Menu, Company
from users.decorators import unauthenticated_user, allowed_users, admin_only
from users.models import Member
from queueSystem.models import Queue, Review

from app.forms import editRoleForm
from restaurants.forms import (
    editMenuForm,
    createMenuForm,
    editCompanyForm,
    editRestaurantForm,
)
from users.forms import editMemberForm
from queueSystem.forms import createQueueForm, createNowQueueForm, createReviewForm

from django.db.models import Avg
from django.views.generic import TemplateView

import sweetify

# Create your views here.


def index(request):
    categories = Category.objects.all()
    restaurants = Restaurant.objects.all()
    ratings = Review.objects.values("resID").annotate(average_rating=Avg("rating"))
    context = {"categories": categories, "restaurants": restaurants, "ratings": ratings}
    return render(request, "app/index.html", context)


@login_required(login_url="users/login")
@admin_only
def admin(request):
    companies = Company.objects.all()
    restaurants = Restaurant.objects.all()
    context = {
        "companies": companies,
        "restaurants": restaurants,
    }
    return render(request, "admin/admin.html", context)


@login_required(login_url="users/login")
@admin_only
def registerRequest(request):
    companies = Company.objects.all()
    restaurants = Restaurant.objects.all()
    context = {
        "companies": companies,
        "restaurants": restaurants,
    }
    return render(request, "admin/registerRequest.html", context)


@login_required(login_url="users/login")
@admin_only
def dashboard(request):
    allQueue = Queue.objects.all()
    memberPoint = allQueue.values("memberID").annotate(my_sum=Sum("point"))
    print(memberPoint)
    return render(request, "admin/dashboard.html")

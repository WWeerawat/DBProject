from django.shortcuts import render

# Create your views here.
def card3Col(request):
    return render(request, "card3Col.html")


def index(request):
    myContext = {
        "categoryTitles": ["A", "B", "C", "D", "E", "F"],
        "restaurant": {
            "resTitle": ["KFC", "MK"],
            "resDesc": ["Fast Food", "Sukki"],
        },
    }
    return render(request, "app/index.html", myContext)


def resCard(request):

    return render(request, "resCard.html")


def categoryCard(request):

    return render(request, "categoryCard.html")


def login(request):
    return render(request, "app/login.html")


def signup(request):
    return render(request, "app/signup.html")


def review(request):
    return render(request, "review.html")


def profile(request):
    return render(request, "profile.html")


def queueManagement(request):

    return render(request, "queueManagement.html")


def foodList(request):

    return render(request, "foodList.html")

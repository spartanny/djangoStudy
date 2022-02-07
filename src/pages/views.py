from django.shortcuts import render

# Create your views here
"""
    List of url paths used from this django-app

    path('home/', home_view),
    path('about/', about_view),
    path('contact/', contact_view),
    path('faq/', faq_view),

"""


def home_view(request):
    print(request.user)
    return render(request, "pages/home.html")


def about_view(request):
    return render(request, 'pages/about.html')


def contact_view(request):
    return render(request, 'pages/contact.html')


def faq_view(request):
    return render(request, 'pages/faq.html')

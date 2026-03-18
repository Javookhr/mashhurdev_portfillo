from django.shortcuts import render
from .models import Profile, Experience, SocialLink, ContactInfo


def index(request):
    profile = Profile.objects.first()
    experiences = Experience.objects.all()
    social_links = SocialLink.objects.all()
    contact = ContactInfo.objects.first()

    context = {
        'profile': profile,
        'experiences': experiences,
        'social_links': social_links,
        'contact': contact,
    }
    return render(request, 'main/index.html', context)

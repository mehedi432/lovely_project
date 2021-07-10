from django.shortcuts import render


def about_us(request):
    return render(request, 'main/about_us.html')


def contact_us(request):
    return render(request, 'main/contact_us.html')


def disclaimer(request):
    return render(request, 'main/disclaimer.html')


def privacy_policy(request):
    return render(request, 'main/privacy_policy.html')
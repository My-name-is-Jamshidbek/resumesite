from django.shortcuts import render, redirect
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from contact.models import Contact
from project.models import Project
from service.models import Service


def index(request):
    return render(request, 'user/pages/index.html')


def contact(request):
    errors = []
    success_message = None
    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Validation checks
        if not fullname or len(fullname) > 255:
            errors.append("Full name is required and should be less than 255 characters.")

        if not phone_number or len(phone_number) > 255:
            errors.append("Phone number is required and should be less than 255 characters.")

        if not email or len(email) > 255:
            errors.append("Email is required and should be less than 255 characters.")
        else:
            try:
                validate_email(email)
            except ValidationError:
                errors.append("Enter a valid email address.")

        if not message:
            errors.append("Message is required.")

        if not errors:
            # Save to database if no errors
            Contact.objects.create(
                fullname=fullname,
                phone_number=phone_number,
                email=email,
                message=message
            )
            success_message = "Your message has been sent successfully!"

    return render(request, 'user/pages/contact.html', {'errors': errors, 'success_message': success_message})


def portfolio(request):
    projects = Project.objects.all()
    return render(request, 'user/pages/portfolio.html', {"projects": projects})


def services(request):
    services = Service.objects.all()
    return render(request, 'user/pages/services.html', {"services": services})


def about(request):
    return render(request, 'user/pages/about.html')

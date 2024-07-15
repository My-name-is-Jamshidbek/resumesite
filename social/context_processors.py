from .models import SocialLink


def social_links(request):
    socials = SocialLink.objects.all()
    return {'social_links': socials}

from .models import Config


def site_config(request):
    config = Config.load()
    return {'site_config': config}

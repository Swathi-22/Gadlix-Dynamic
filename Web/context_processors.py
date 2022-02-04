
from .models import Client
def main_context(request):
    clients=Client.objects.all()
    return {
        'clients':clients,
        'domain' : request.META['HTTP_HOST'],
    }
from .models import District

def menu_links(request):
    links=District.objects.all()
    return dict(links=links)


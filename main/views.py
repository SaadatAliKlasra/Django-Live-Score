from django.db.models import Q
from django.shortcuts import render
from .models import Fixture

# Create your views here.


def home(request):
    return render(request, "index.html")


def fixtures(request):
    fixtures = Fixture.objects.all()
    search = request.GET.get("search")
    if search:
        fixtures = fixtures.filter(
            Q(home_team__name__icontains=search) | Q(away_team__name__icontains=search)
        )
    context = {"fixtures": fixtures}
    if request.htmx:
        return render(request, "partials/fixturelist.html", context)
    return render(request, "fixtures.html", context)

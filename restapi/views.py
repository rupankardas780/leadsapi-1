from django.http import HttpResponse
from restapi.serializers import LeadSerializer
from restapi.models import Lead
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend


# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at Leads API.")


class LeadsViewSet(viewsets.ModelViewSet):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('email','location_type',"location_string")
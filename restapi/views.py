from django.http import HttpResponse
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from restapi.serializers import LeadSerializer
from restapi.models import Lead
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework import status
from restapi.enums import LeadStatus


# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at Leads API.")


class LeadsViewSet(viewsets.ModelViewSet):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('email',"location_string")


@api_view(['PUT'])
@renderer_classes((JSONRenderer,))
def mark_communication(request, pk):
    lead = Lead.objects.filter(id=pk).all()
    if len(lead) == 0:
        return Response({"reason": "entity not found"}, status=status.HTTP_404_NOT_FOUND)
    lead = lead[0]
    lead.communication = request.data.get('communication')
    lead.status = LeadStatus.Contacted
    lead.save()
    return Response({"status": "Contacted"}, status=status.HTTP_202_ACCEPTED)

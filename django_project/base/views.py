from .models import *
from .serializers import *
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.pagination import PageNumberPagination
# Create your views here.

class SmallPagesPagination(PageNumberPagination):  
    page_size = 6
    
class ServiceListView(ListAPIView):
    serializer_class = ServiceListSerializer
    queryset = Service.objects.all()

class ServiceDetailView(RetrieveAPIView):
    serializer_class = ServiceSerializer
    queryset = Service.objects.all()
    lookup_field = "id"

class NewsListView(ListAPIView):
    serializer_class = NewsListSerializer
    queryset = News.objects.all()
    pagination_class = SmallPagesPagination

class NewsDetailView(ListAPIView):
    serializer_class = NewsSerializer
    queryset = News.objects.all()
    lookup_field = "id"

class ClientListView(ListAPIView):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()

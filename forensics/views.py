from rest_framework import generics

from forensics.models import ForensicsData
from forensics.serializers import ForensicsDataSerializer


class ForensicsDataList(generics.ListCreateAPIView):
    """
    List all illustration sets, or create a new illustration set.
    """

    queryset = ForensicsData.objects.all()
    serializer_class = ForensicsDataSerializer


class ForensicsDataDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete illustration set
    """

    queryset = ForensicsData.objects.all()
    serializer_class = ForensicsDataSerializer

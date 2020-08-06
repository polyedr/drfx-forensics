from rest_framework import generics

from color_augmenter.models import IllustrationSet
from color_augmenter.serializers import IllustrationSetSerializer


class IllustrationSetList(generics.ListCreateAPIView):
    """
    List all illustration sets, or create a new illustration set.
    """

    queryset = IllustrationSet.objects.all()
    serializer_class = IllustrationSetSerializer


class IllustrationSetDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete illustration set
    """

    queryset = IllustrationSet.objects.all()
    serializer_class = IllustrationSetSerializer

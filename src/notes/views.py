from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from . import permissions, serializers, models


class NotesListView(generics.ListCreateAPIView):
    queryset = models.Notes.objects.all()
    permission_classes = (IsAuthenticated,)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return serializers.NotesCreateSerializer
        return serializers.NotesListSerializer


class NotesDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Notes.objects.all()
    serializer_class = serializers.NotesDetailSerializer
    permission_classes = (permissions.IsOwnerOrReadOnly,)

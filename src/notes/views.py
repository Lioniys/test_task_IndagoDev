from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from . import permissions, serializers, models, services


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


class CreateUserView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = serializers.UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = services.create_user(validated_data=serializer.validated_data)
        return Response(data, status=status.HTTP_201_CREATED)

from rest_framework import viewsets, permissions

from . import models
from . import serializers


class NoteViewSet(viewsets.ModelViewSet):

    serializer_class = serializers.NoteSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        outer_user_id = self.request.query_params.get('outer_user_id')
        objects = models.Note.objects.filter(user=self.request.user)

        if outer_user_id:
            objects = objects.filter(outer_user_id=outer_user_id)

        return objects

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

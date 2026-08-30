from django.contrib.auth.models import User
from django.http import Http404

from rest_framework.decorators import api_view, action
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.reverse import reverse
from rest_framework import mixins, generics, status, permissions, renderers, viewsets

from snippets.models import Snippet
from snippets.permissions import IsOwnerOrReadOnly
from snippets.serializers import SnippetSerializer, UserSerializer

class SnippetViewSet(viewsets.ModelViewSet):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request: Request, *args, **kwargs) -> Response:
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer: SnippetSerializer) -> None:
        serializer.save(owner=self.request.owner)

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
from django.contrib.auth.models import User
from rest_framework import serializers

from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES

class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Snippet
        fields = ["url", "id", "highlight", "owner", "title", "code", "linenos", "language", "style"]

    owner = serializers.ReadOnlyField(source="owner.username")
    highlight = serializers.HyperlinkedIdentityField(
        view_name="snippet-highlight", format="html"
    )


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "id", "username", "snippets"]

    snippets = serializers.HyperlinkedRelatedField(
        many=True, view_name="snippet-detail", read_only=True
    )

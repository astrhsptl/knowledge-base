from rest_framework.serializers import ModelSerializer

from authsystem.models import User
from incommonpanel.models import Document, Catalog


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        read_only_fields = ("id", "is_admin", "is_superuser",)

class DocumentSerializer(ModelSerializer):
    class Meta:
        model = Document
        fields = "__all__"
        read_only_fields = ("id", "created_at",)


class CatalogSerializer(ModelSerializer):
    class Meta:
        model = Catalog
        fields = ("title",)
        read_only_fields = ("id",)
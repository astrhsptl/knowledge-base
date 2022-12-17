from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView

from .serializers import (
    UserSerializer, CatalogSerializer, DocumentSerializer
)

from authsystem.models import User
from incommonpanel.models import Document, Catalog

from buisneslogic.tasks import mail_sending_task



class UserAPIView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        ans = super().post(request, *args, **kwargs)
        try:
            mail_sending_task.delay(request.data['email'], request.data['password'])
        except:
            print('invalid recipier')
        return ans

class UserDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class DocumentAPIView(ListCreateAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

class DocumentDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer



class CatalogAPIView(ListCreateAPIView):
    queryset = Catalog.objects.all()
    serializer_class = CatalogSerializer

class CatalogDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Catalog.objects.all()
    serializer_class = CatalogSerializer
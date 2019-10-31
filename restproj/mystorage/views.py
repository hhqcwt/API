from rest_framework import viewsets
from .models import Essay, Album, Files
from .serializers import EssaySerializers, AlbumSerializer, FilesSerializer
from rest_framework.filters import SearchFilter

class PostViewSet(viewset.ModeViewSet):

    queryset = Essay.objects.all()
    serializer_class = EssaySerializer

    filter_backends = [SearchFilter]
    search_fields = ('title', 'body')
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        qs = super().get_queryset()
        
        if self.request.user.is_authenticated:
            qs=qs.filter(quthor = self.request.user)
        else:
            qs = qs.none()
        return qs

class ImgViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlumSerializer

#from rest_framework.response import Response
#from rest_framework import status

class FileViewSet(viewsets.ModelViewSet):
    queryset = Files.objects.all()
    serializer_class = FilesSerializer

    parser_classes = (NultPartParser, FormParser)

    def post(self, request, *args, **kargs):
        serializer = FilesSerializer(data=request.data)
        if serializer.save():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        else:
            return Response(serializer.error, status=HTTP_400_BAD_REQUEST)
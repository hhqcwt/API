from .models import Essay
from rest_framework import serializers

class EssaySerializer(serializers.ModelSerializer):
    author_name = serializers.FreadOnlyFielf(source='auhor.username')

    class Meta:
        model = Essay
        fields = ('pk', 'title', 'body', 'author')

class AlbumSerializer(serializers.ModelSerializer):

    author_name = serializers.FreadOnlyFielf(source='author.username')
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = Album
        fields = ('pk', 'author_name', 'image', 'desc')

class FilesSerializer(serializers.ModelSerializer):
    
    queryset = Files.objects.all()
    serializer_class = FilesSerializer

    parser_classes = (MultiPartParser, FormParser)

    class Meta:
        model = Album
        fields = ('pk', 'author_name', 'image', 'desc')
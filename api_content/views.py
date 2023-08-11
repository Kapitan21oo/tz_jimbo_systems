from rest_framework import generics
from rest_framework.response import Response

from .models import Page, Block
from .serializers import PageSerializer, BlockSerializer


class PageListView(generics.ListAPIView):
    queryset = Page.objects.all()
    serializer_class = PageSerializer


class PageDetailView(generics.RetrieveAPIView):
    queryset = Page.objects.all()
    serializer_class = PageSerializer
    lookup_field = 'slug'

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        blocks = Block.objects.filter(pages__slug=instance.slug)
        serializer = BlockSerializer(blocks, many=True)

        for block in blocks:
            block.increment_view_count()
            block.save()

        return Response(serializer.data)

from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class CustomPaginations(PageNumberPagination):
    def get_paginated_response(self, data):
        return Response({
            'links': {
                'keyinki': self.get_next_link(),
                'burunqi': self.get_previous_link()
            },
            'count': self.page.paginator.count,
            'results': data
        })
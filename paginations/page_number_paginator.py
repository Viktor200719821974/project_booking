import math

from rest_framework.pagination import PageNumberPagination as Paginator
from rest_framework.response import Response


class PageNumberPaginator(Paginator):
    page_size = 5
    page_size_query_param = 'size'
    max_page_size = 10

    def get_paginated_response(self, data):
        total_pages = math.ceil(self.page.paginator.count/self.get_page_size(self.request))
        return Response({
            "total_items": self.page.paginator.count,
            "total_pages": total_pages,
            "next": self.get_next_link(),
            "prev": self.get_previous_link(),
            "data": data
        })

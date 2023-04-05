from django.conf import settings
from django.core.paginator import Paginator


def get_page_obj(posts_list, page_number):
    paginator = Paginator(posts_list, settings.POST_COUNT_DISPLAY)
    page_obj = paginator.get_page(page_number)
    return page_obj

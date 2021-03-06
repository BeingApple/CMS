import math
import abc


class ServicePagination:
    _count = 0
    _page = 1
    _row_block = 20
    _max_page = 0
    _limit_start = 0
    _limit_end = 0
    _page_block = 10
    _page_start = 1
    _page_end = 10

    __metaclass__ = abc.ABCMeta

    def __init__(self):
        self._set_count()

    def set_row_block(self, row_block):
        self._row_block = row_block
        self._set_max_page()

    def get_row_block(self):
        return self._row_block

    @abc.abstractmethod
    def _set_count(self):
        pass

    def _set_max_page(self):
        self._max_page = math.ceil(self._count / float(self._row_block))

    def _set_limit(self, page=1):
        self._page = page

        if self._page > self._max_page:
            self._page = self._max_page

        if self._page <= 0:
            self._page = 1

        self._limit_start = ((self._page - 1) * self._row_block)
        self._limit_end = (self._page * self._row_block)

    def _set_page_start_end(self):
        self._set_max_page()

        self._page_start = \
            (int((self._page - 1) / self._page_block) * self._page_block) + 1
        self._page_end = self._page_start + (self._page_block - 1)

        if self._page_end >= self._max_page:
            self._page_end = self._max_page

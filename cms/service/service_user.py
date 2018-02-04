from cms.database import db
from cms.entities.user import User
from cms.service.service_pagination import ServicePagination
from flask import render_template
from flask import Markup
import urllib


class ServiceUser(ServicePagination):
    
    def _set_count(self):
        self._count = db.session.query(User).count()
        self._set_max_page()

    def get_count(self):
        return self._count

    def get_customer_list(self, page=1):
        self._set_limit(page)

        return db.session.query(User).order_by(User.name)[
               self._limit_start:self._limit_end]

    def get_pagination(self, url, page=1, search=None):
        self._set_limit(page)
        self._set_page_start_end()

        pages = range(self._page_start, self._page_end + 1)
        search_string = urllib.parse.urlencode(search)

        print(search_string)

        link = Markup(render_template("pagination.html", url=url, pages=pages,
                                      search_string=search_string, nowPage=self._page))
        pagination = {"link": link, "skip": self._limit_start}
        return pagination

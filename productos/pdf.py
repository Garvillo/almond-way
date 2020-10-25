import io
import os

from django.conf import settings
from django.contrib.staticfiles import finders
from django.template.loader import render_to_string
from django.views.static import safe_join
from weasyprint import HTML, default_url_fetcher


class PdfRenderer(object):

    def __init__(self, template, context={}):
        self.template = template
        self.context = context

    def _url_fetcher(self, url):
        if url.startswith('static://'):
            url = url[len('static://'):]
            url = "file://" + finders.find(url)
            #url = finders.find(url)
            #print(url)

        if url.startswith('media://'):
            url = url[len('media://'):]
            url = "file://" + os.path.join(settings.MEDIA_ROOT, url)

        if url.startswith('imgpdf://'):
            url = url[len('imgpdf://'):]
            url = os.path.join(settings.DOMINIO, url)
            print(url)

        return default_url_fetcher(url)

    def render_to_string(self):
        return render_to_string(self.template,
                                self.context)

    def render_to_pdf(self, html):
        return self.get_html(html).write_pdf()

    def get_html(self, html):

        html = HTML(string=html,
                    base_url=self.context.get("base_url"),
                    url_fetcher=self._url_fetcher)

        return html

    def render(self,):
        return io.BytesIO(self.render_to_pdf(self.render_to_string()))



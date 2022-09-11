from django.views.generic import TemplateView


class IndexView(TemplateView):
    """Simple index page view."""
    template_name = 'main/index.html'

from django.views import generic


class Index(generic.TemplateView):
    template_name = "{{cookiecutter.app_slug}}/index.html"

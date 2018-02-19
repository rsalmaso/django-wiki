from django.apps import AppConfig
from django.core.checks import register
from django.utils.translation import gettext_lazy as _
from wiki.core.plugins.loader import load_wiki_plugins

from . import checks
from .core.urls import reverse, reverse_lazy


class WikiConfig(AppConfig):
    default_site = 'wiki.sites.WikiSite'
    name = "wiki"
    verbose_name = _("Wiki")

    def ready(self):
        self.patch_urls()
        register(checks.check_for_required_installed_apps, checks.Tags.required_installed_apps)
        register(checks.check_for_obsolete_installed_apps, checks.Tags.obsolete_installed_apps)
        register(checks.check_for_context_processors, checks.Tags.context_processors)
        load_wiki_plugins()

    def patch_urls(self):
        from django.urls import base
        from django import urls
        from django import shortcuts
        base.reverse = reverse
        base.reverse_lazy = reverse_lazy
        urls.reverse = reverse
        urls.reverse_lazy = reverse_lazy
        shortcuts.reverse = reverse

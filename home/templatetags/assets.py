import json

from django import template
from django.templatetags.static import static
from django.utils.safestring import mark_safe
from django.conf import settings

register = template.Library()


def asset_tag(url):
    if url.endswith('css'):
        return '<link href="{0}" rel="stylesheet" />'.format(url)
    elif url.endswith('js'):
        return '<script src="{0}"></script>'.format(url)
    else:
        return ''


def manifest_assets():
    assets = json.load(open(settings.MANIFEST_PATH))
    return "\n".join(
        asset_tag(static(assets[v])) for v in settings.WEBPACK_ASSETS
    )


def webpack_dev_assets():
    return "\n".join(
        asset_tag("{0}/{1}".format(settings.WEBPACK_DEV_URL, a))
        for a in settings.WEBPACK_ASSETS
    )


@register.simple_tag
def webpack_assets():
    if settings.MANIFEST_PATH:
        return mark_safe(manifest_assets())
    elif settings.WEBPACK_DEV_URL:
        return mark_safe(webpack_dev_assets())
    else:
        return ''

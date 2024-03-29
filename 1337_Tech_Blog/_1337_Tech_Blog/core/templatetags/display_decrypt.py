"""
DBA 1337_TECH, AUSTIN TEXAS © MAY 2021
Proof of Concept code, No liabilities or warranties expressed or implied.
"""

from _1337_Tech_Blog.organizer.models import Gor_El
from django.template import (
    Library, TemplateSyntaxError)

# https://docs.djangoproject.com/en/1.8/howto/custom-template-tags/

register = Library()

@register.simple_tag(name='getSecureNote', takes_context=True)
def getSecureNote(context, secure_note):
    secure_note = context['object']
    request = context['request']
    gor_el = Gor_El()
    return gor_el._decrypt_text(secure_note, request)

@register.filter(name='decrypt_text', takes_context=True)
def decrypt_text(secure_note, context):
    gor_el = Gor_El()
    secure_text = context['secureddataatrestpost']
    return gor_el._decrypt_text(secure_text, context)

@register.inclusion_tag(
    'core/includes/downloads.html',
    takes_context=True)
def decrypt(context, *args, **kwargs):
    action = (args[0] if len(args) > 0
              else kwargs.get('action'))
    button = (args[1] if len(args) > 1
              else kwargs.get('button'))
    method = (args[2] if len(args) > 2
              else kwargs.get('method'))
    decrypt = context.get('decrypt')
    if action is None:
        raise TemplateSyntaxError(
            "form template tag requires "
            "at least one argument: action, "
            "which is a URL.")
    return {
        'action': action,
        'button': button,
        'decrypt': decrypt,
        'method': method}


@register.inclusion_tag(
    'core/includes/confirm_delete_form.html',
    takes_context=True)
def decrypt_form(context, *args, **kwargs):
    action = (args[0] if len(args) > 0
              else kwargs.get('action'))
    method = (args[1] if len(args) > 1
              else kwargs.get('method'))
    form = context.get('form')
    display_object = kwargs.get(
        'object', context.get('object'))
    if action is None:
        raise TemplateSyntaxError(
            "delete_form template tag "
            "requires at least one argument: "
            "action, which is a URL.")
    if display_object is None:
        raise TemplateSyntaxError(
            "display_form needs object "
            "manually specified in this case.")
    if hasattr(display_object, 'name'):
        obj_title = display_object.name
    elif hasattr(display_object, 'title'):
        obj_title = display_object.title.title()
    else:
        obj_title = str(display_object)
    obj_type = kwargs.get(
        'obj_type',
        display_object._meta.verbose_name.title())
    return {
        'action': action,
        'form': form,
        'method': method,
        'object': display_object.Gor_El.Decyrpt(),
        'obj_title': obj_title,
        'obj_type': obj_type}

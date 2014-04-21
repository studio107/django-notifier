# coding=utf-8

from .models import DbTemplate

def render_db_template(code, data):
    try:
        tpl = DbTemplate.objects.filter(code=code).get()
        return tpl.render(data)
    except:
        return None, None

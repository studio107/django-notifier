# coding=utf-8

from django.db import models
from django.template import Context, Template


class DbTemplate(models.Model):
    name = models.CharField(max_length=255, blank=False, null=True)
    code = models.CharField(max_length=8, blank=False, null=True)
    subject_template = models.TextField(default='', blank=False)
    body_template = models.TextField(default='', blank=False)

    def __unicode__(self):
        return "%s" % self.name

    def render(self, data):
        subject = Template(self.subject_template)
        body = Template(self.body_template)
        context = Context(data)
        return subject.render(context), body.render(context)

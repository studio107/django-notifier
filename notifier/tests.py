# coding=utf-8

from django.test import TestCase
from notifier.models import DbTemplate
from notifier.utils import render_db_template


class NotifierTest(TestCase):
    def setUp(self):
        self.tpl = DbTemplate()
        self.tpl.subject_template = 'hello {{ world }}'
        self.tpl.body_template = 'foo {{ bar }}'
        self.tpl.name = 'example'
        self.tpl.code = 'extra'
        self.tpl.save()

    def test_simple(self):
        subject, template = self.tpl.render({
            'world': 'hello',
            'bar': 'foo'
        })
        self.assertEqual('hello hello', subject)
        self.assertEqual('foo foo', template)

    def test_util(self):
        subject, template = render_db_template('extra', {
            'world': 'hello',
            'bar': 'foo'
        })
        self.assertEqual('hello hello', subject)
        self.assertEqual('foo foo', template)

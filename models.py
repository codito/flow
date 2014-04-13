# -*- coding: utf-8 -*-

from peewee import CharField, TextField, Model
from flow import db


class Flow(db.Model):
    name = CharField()
    data = TextField()


def setup():
    Flow.create_table(fail_silently=True)

from __future__ import unicode_literals
from importlib import import_module

from django.utils.encoding import python_2_unicode_compatible
from django.db import models


@python_2_unicode_compatible
class Condition(models.Model):
    """
    Stores the details of a Python function which will be used to determine this condition's
    truthiness.
    """
    name = models.CharField(max_length=64)
    module = models.CharField(
        max_length=128, help_text="Module in which the condition function resides")
    function = models.CharField(
        max_length=64,
        help_text=("The function which returns True or False to determine the result of this "
                   "condition"))

    def __str__(self):
        return self.name

    def __call__(self, *args, **kwargs):
        """
        Imports and calls the condition function with the provided arguments and returns its
        response.
        """
        return getattr(import_module(self.module), self.function)(*args, **kwargs)


class Chain(models.Model):
    name = models.CharField(max_length=128)

    def __call__(self, *args, **kwargs):
        """
        Runs each condition and evaluates whether the entire condition chain has succeeded. Passes
        through any arguments provided to each Condition.
        """
        pass


@python_2_unicode_compatible
class ChainElement(models.Model):
    links = (
        (u'AND', u'and'),
        (u'OR', u'or')
    )
    chain = models.ForeignKey(Chain)
    joiner = models.CharField(choices=links, max_length=3, blank=True)
    negated = models.BooleanField(default=False)
    condition = models.ForeignKey(Condition)

    def __str__(self):
        isnt = "NOT " if self.negated else ""
        joiner = self.joiner if self.joiner else "IF"
        return "%s %s%s" % (joiner, isnt, self.condition)

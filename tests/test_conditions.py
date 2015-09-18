try:
    import unittest
except ImportError:
    import django.utils.unittest as unittest

from django_dynamic_fixture import G
from django.db import IntegrityError

from django_condition_chain.models import Condition, Chain, ChainElement


return_arg = lambda x: x


class ConditionTestCase(unittest.TestCase):

    def test_str(self):
        """
        Should return the Condition.name as the unicode value.
        """
        name = "Test Condition"
        condition = G(Condition, name=name)
        self.assertEqual(condition.__str__(), name)

    def test_call(self):
        """
        Should call the function configured and return its result.
        """
        return_value = "test_call response"
        condition = G(
            Condition,
            module="tests.test_conditions",
            function="return_arg")
        self.assertEqual(condition(return_value), return_value)


class ChainElementTestCase(unittest.TestCase):

    def test_str(self):
        """
        Should return a string containing a description of the model.
        """
        cond_name = "Test Condition"
        condition = Condition.objects.create(
            name=cond_name,
            module="tests.test_conditions",
            function="return_arg"
        )
        chain = Chain.objects.create(name="Test Chain")
        for joiner in ("AND", "OR"):
            element = ChainElement.objects.create(
                condition=condition,
                joiner=joiner,
                chain=chain)
            self.assertEqual(element.__str__(), "%s Test Condition" % joiner)

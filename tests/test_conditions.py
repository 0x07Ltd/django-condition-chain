try:
    import unittest
except ImportError:
    import django.utils.unittest as unittest

from django_dynamic_fixture import G

from django_condition_chain.models import Condition, Chain, ChainElement


return_arg = lambda x: x
return_true = lambda: True
return_false = lambda: False


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
        self.assertEqual(condition.call(return_value), return_value)


class ChainTestCase(unittest.TestCase):

    def test_call_one_condition(self):
        """
        Should evaluate whether all of the conditions passed based on their configurations.
        """
        ret_true = G(Condition, module="tests.test_conditions", function="return_true")
        chain = G(Chain)
        G(ChainElement, chain=chain, condition=ret_true)
        self.assertTrue(chain.call())

    def test_call_two_conditions_true(self):
        """
        Should return True when two conditions both return True.
        """
        ret_true = G(Condition, module="tests.test_conditions", function="return_true")
        chain = G(Chain)
        G(ChainElement, chain=chain, condition=ret_true)
        G(ChainElement, chain=chain, condition=ret_true)
        self.assertTrue(chain.call())

    def test_call_two_conditions_true_and(self):
        """
        Should return True when two conditions both return True and they're linked with AND.
        """
        ret_true = G(Condition, module="tests.test_conditions", function="return_true")
        chain = G(Chain)
        G(ChainElement, chain=chain, condition=ret_true, order=0)
        G(ChainElement, chain=chain, condition=ret_true, order=1, joiner="and")
        self.assertTrue(chain.call())

    def test_call_two_conditions_true_or(self):
        """
        Should return True when two conditions both return True and they're linked with OR.
        """
        ret_true = G(Condition, module="tests.test_conditions", function="return_true")
        chain = G(Chain)
        G(ChainElement, chain=chain, condition=ret_true, order=0)
        G(ChainElement, chain=chain, condition=ret_true, order=1, joiner="or")
        self.assertTrue(chain.call())

    def test_call_one_condition_false(self):
        """
        Should return False when one condition is False.
        """
        ret_false = G(Condition, module="tests.test_conditions", function="return_false")
        chain = G(Chain)
        G(ChainElement, chain=chain, condition=ret_false)
        self.assertFalse(chain.call())

    def test_call_two_conditions_one_false(self):
        """
        Should return False when one of two conditions are False.
        """
        ret_true = G(Condition, module="tests.test_conditions", function="return_true")
        ret_false = G(Condition, module="tests.test_conditions", function="return_false")
        chain = G(Chain)
        G(ChainElement, chain=chain, condition=ret_true)
        G(ChainElement, chain=chain, condition=ret_false)
        self.assertFalse(chain.call())

    def test_call_two_conditions_one_false_and(self):
        """
        Should return False when one of two conditions are False and they're linked with AND.
        """
        ret_true = G(Condition, module="tests.test_conditions", function="return_true")
        ret_false = G(Condition, module="tests.test_conditions", function="return_false")
        chain = G(Chain)
        G(ChainElement, chain=chain, condition=ret_true, order=0)
        G(ChainElement, chain=chain, condition=ret_false, order=1, joiner="and")
        self.assertFalse(chain.call())

    def test_call_two_conditions_one_false_or(self):
        """
        Should return True when one of two conditions are True and they're linked with OR.
        """
        ret_true = G(Condition, module="tests.test_conditions", function="return_true")
        ret_false = G(Condition, module="tests.test_conditions", function="return_false")
        chain = G(Chain)
        G(ChainElement, chain=chain, condition=ret_true, order=0)
        G(ChainElement, chain=chain, condition=ret_false, order=1, joiner="or")
        self.assertTrue(chain.call())

    def test_call_three_conditions_one_true_or(self):
        """
        Should return True when one of three conditions are True and they're linked with OR.
        """
        ret_true = G(Condition, module="tests.test_conditions", function="return_true")
        ret_false = G(Condition, module="tests.test_conditions", function="return_false")
        chain = G(Chain)
        G(ChainElement, chain=chain, condition=ret_false, order=0)
        G(ChainElement, chain=chain, condition=ret_false, order=1, joiner="or")
        G(ChainElement, chain=chain, condition=ret_true, order=2, joiner="or")
        self.assertTrue(chain.call())

    def test_iter(self):
        """
        Should return an iterator containing the ChainElements.
        """
        chain = G(Chain)
        ces = (
            G(ChainElement, chain=chain),
            G(ChainElement, chain=chain),
            G(ChainElement, chain=chain)
        )
        iterator = iter(chain)
        for ce in ces:
            self.assertEqual(next(iterator), ce)

    def test_len(self):
        """
        Should return the amount of ChainElements in the chain.
        """
        amt = 10
        chain = G(Chain)
        for _ in range(amt):
            G(ChainElement, chain=chain)
        self.assertEqual(len(chain), amt)

    def test_getitem(self):
        """
        Should return a specific ChainElement based on its order.
        """
        chain = G(Chain)
        ces = (
            G(ChainElement, chain=chain, order=0),
            G(ChainElement, chain=chain, order=1),
            G(ChainElement, chain=chain, order=2)
        )
        for i in range(len(ces)):
            self.assertEqual(chain[i], ces[i])

    def test_reversed(self):
        """
        Should return the ChainElements in reverse order.
        """
        chain = G(Chain)
        ces = (
            G(ChainElement, chain=chain, order=2),
            G(ChainElement, chain=chain, order=1),
            G(ChainElement, chain=chain, order=0)
        )
        for i, ce in enumerate(reversed(chain)):
            self.assertEqual(ce, ces[i])

    def test_elements_queryset(self):
        """
        Should return a queryset with only the Chain's ChainElements in order.
        """
        chain = G(Chain)
        other_chain = G(Chain)
        ces = (
            G(ChainElement, chain=chain, order=1),
            G(ChainElement, chain=chain, order=2),
            G(ChainElement, chain=chain, order=3)
        )
        other_ces = (
            G(ChainElement, chain=other_chain),
            G(ChainElement, chain=other_chain),
            G(ChainElement, chain=other_chain)
        )
        ret = list(chain.elements_queryset)
        for i, ce in enumerate(ces):
            self.assertEqual(ce, ret[i])
        for ce in other_ces:
            self.assertTrue(ce not in ret)


class ChainElementTestCase(unittest.TestCase):

    def test_str(self):
        """
        Should return a string containing a description of the model.
        """
        cond_name = "Test Condition"
        condition = G(Condition, name=cond_name)
        for joiner in ("AND", "OR"):
            element = G(
                ChainElement,
                condition=condition,
                joiner=joiner)
            self.assertEqual(element.__str__(), "%s Test Condition" % joiner)

[![Build Status](https://travis-ci.org/0x07Ltd/django-condition-chain.svg?branch=master)](https://travis-ci.org/0x07Ltd/django-condition-chain) [![Coverage Status](https://coveralls.io/repos/0x07Ltd/django-condition-chain/badge.svg?branch=master&service=github)](https://coveralls.io/github/0x07Ltd/django-condition-chain?branch=master)
django-condition-chain
======================

This small Django app provides a set of models and methods which can be used to set up an arbitrary
list of conditions from the admin interface. For example, in a home automation system, based on an
input you may want to change status of an output as long as a chain of conditions are met:

Input:
Front door opens

Conditions:
IF hallway movement sensor has not been triggered in the last ten seconds (somebody is coming *into* the house)
AND outside light sensor is less than 20 (it's dark outside)

Output:
Turn hallway lights on

The app provides the models in which to store the defined conditions and the admin interface
required to create them.

Usage
-----

Include `django_condition_chain` in your `INSTALLED_APPS`, then use the ConditionChain like so:

```python
# @TODO: Write an example
```

Usage with South
----------------

The migrations for this project in the `migrations` directory have been made using Django 1.8. This
means that if you're using South you must tell it to look in the `south_migrations` directory for
its migrations by putting the following in your settings file:

```python
SOUTH_MIGRATION_MODULES = {
    'django_condition_chain': 'django_condition_chain.south_migrations'
}
```

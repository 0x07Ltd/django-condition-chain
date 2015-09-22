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

Include `django_condition_chain` in your `INSTALLED_APPS`, then set up and use the conditions like so:

Write your own conditions into your project, optionally taking extra arguments which you can either pass in during run-time (eg. `house`) or specify in the configuration stage (eg. `seconds`).
`yourproject/conditions.py`
```python
def is_dark_outside(house):
    return house.ext_light_sensor < 20

def hallway_movement_in_last_x_secs(house, seconds):
    return (datetime.now() - house.hallway.last_movement) < timedelta(seconds=seconds)
```

Set up the conditions and chain. This could also be done using the admin interface.
```python
from django_condition_chain.models import Condition, Chain, ChainElement
is_dark = Condition.objects.create(
    name="is dark outside",
    module="yourproject.conditions",
    function="is_dark_outside")
hallway_movement = Condition.objects.create(
    name="hallway movement in last 10 secs",
    module="yourproject.conditions",
    function="hallway_movement_in_last_x_secs",
    custom_kwargs='{"seconds": 10}')
chain = Chain.objects.create(name="Is dark and person coming in front door")
ChainElement.objects.create(
    chain=chain,
    condition=is_dark,
    order=0)
ChainElement.objects.create(
    chain=chain,
    condition=hallway_movement,
    joiner="and",
    order=1)
```

When the front door opens, use the condition chain to see if you should turn the lights on.
```python
from django_condition_chain.models import Chain
def on_front_door_open(house)
    condition_chain = Chain.objects.get(name="Is dark and person coming in front door")
    if condition_chain.run(house):
        house.hallway.lights.on()
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

============
FormLayout
============

Layout manager designed for creating forms or input layouts in a user interface. It arranges widgets in a two-column format: one column for labels and another for input fields or other widgets. This layout is commonly used when you have a series of labels and corresponding input fields, such as in a settings page or a data entry form.

.. code-block:: lua

  local layout = FormLayout()

.. note::

  Additonal properties shall be provided on our next release.

Properties
***************

.. function:: addChild(label, widget)

  Adds a widget to a layout with a given label

.. function:: addLayout(label, layout):

  Adds a layout to the widget with a given label


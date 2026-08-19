Container
############

A blank panel that holds a layout. Containers are the building block for
grouping part of an interface so it can be shown, hidden, styled or swapped as
a unit.

.. code-block:: lua
  :linenos:

  local ui = require("limekit.ui")

  local panel  = ui.Container()
  local inner  = ui.VLayout()
  inner:addChild(ui.Label("Settings"))
  inner:addChild(ui.CheckBox("Enable notifications"))

  panel:setLayout(inner)

Because a Container is a single widget, you can hide the whole group at once:

.. code-block:: lua

  panel:hide()

Containers are also what you put into a
:doc:`Tab </widgets/tab>`, an :doc:`Accordion </widgets/accordion>` or a
:doc:`SlidingStackedWidget </widgets/sliding-stacked-widget>` when a page needs
more than one widget.

Properties
***************

.. function:: setLayout(layout) / getLayout()
  :no-index:

  The layout held inside the container.

.. function:: setOnKeyPress(callback)
  :no-index:

  Runs when a key is pressed while the container has focus. The handler
  receives the container, the key's name -- ``"A"``, ``"Return"``, ``"F1"`` --
  and the character it typed, which is an empty string for keys that produce
  none.

  .. code-block:: lua

     panel:setOnKeyPress(function(sender, key, text)
         print(key, text)
     end)

  .. note::

     Observing a key is not the same as consuming it: the handler runs and Qt
     still processes the key as usual, so text boxes inside the container keep
     working. In 1.x attaching this handler silently switched off default key
     handling for everything inside.

ButtonGroup
##############

Groups buttons together so they behave as one set of choices, and gives you a
single handler for all of them.

A ButtonGroup is not a visible widget -- it has no appearance of its own and is
not added to a layout. It manages buttons that are laid out normally.

.. code-block:: lua
  :linenos:

  local ui = require("limekit.ui")

  local small  = ui.RadioButton("Small")
  local medium = ui.RadioButton("Medium")
  local large  = ui.RadioButton("Large")

  local sizes = ui.ButtonGroup()
  sizes:addButton(small)
  sizes:addButton(medium)
  sizes:addButton(large)

  sizes:setOnClick(function(button)
      print("chose " .. button:getText())
  end)

  -- the buttons still go in a layout as usual
  local layout = ui.HLayout()
  layout:addChild(small)
  layout:addChild(medium)
  layout:addChild(large)

Properties
***************

.. function:: addButton(button)
  :no-index:

  Adds a button to the group.

.. function:: removeButton(button)
  :no-index:

  Removes a button from the group.

.. function:: setExclusive(exclusive) / isExclusive()
  :no-index:

  Whether only one button in the group may be selected at a time. On by
  default -- turn it off to let the group act as a set of independent toggles
  that still share one handler.

.. function:: setOnClick(callback)
  :no-index:

  Runs when any button in the group is clicked. The handler receives the button
  that was clicked, not the group.

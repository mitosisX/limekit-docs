CommandButton
################

A large button with a heading and a line of explanation underneath. Use it when
a choice needs more than a couple of words -- setup wizards and "what do you
want to do?" screens are the usual places.

.. code-block:: lua

  local ui = require("limekit.ui")

  local newProject = ui.CommandButton("Create a new project")
  newProject:setDescription("Start from an empty folder")
  newProject:setOnClick(function()
      createProject()
  end)

Properties
***************

.. function:: setText(text) / getText()
  :no-index:

  The heading.

.. function:: setDescription(text) / getDescription()
  :no-index:

  The smaller explanatory line beneath the heading.

.. function:: setIcon(path) / getIcon()
  :no-index:

  An icon shown to the left.

.. function:: setIconSize(width, height)
  :no-index:

  Resizes the icon.

.. function:: setOnClick(callback)
  :no-index:

  Runs when the button is clicked.

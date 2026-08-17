Modal
###########

A secondary window for a focused task -- preferences, a login form, a
confirmation with more to it than a plain
:doc:`dialog </services>` can express.

.. code-block:: lua
  :linenos:

  local ui = require("limekit.ui")

  local prefs = ui.Modal("Preferences")

  local inner = ui.VLayout()
  inner:addChild(ui.CheckBox("Start on login"))

  local close = ui.Button("Done")
  close:setOnClick(function()
      prefs:dismiss()
  end)
  inner:addChild(close)

  prefs:setLayout(inner)
  prefs:show()

Showing and closing
**********************

.. function:: show()
  :no-index:

  Shows the modal without blocking. Your code carries on running.

.. function:: open()
  :no-index:

  Shows the modal and **waits** until it is closed before returning. Use this
  when the next line of your code depends on the user's answer.

  .. code-block:: lua

     prefs:open()
     print("the user has finished with the dialog")

  .. important::

     In 1.x, ``show()`` blocked -- it did what ``open()`` does now. If you are
     porting an app that relied on that, change ``show()`` to ``open()``.
     Everywhere else in Limekit, ``show()`` does not block, and now this widget
     agrees.

.. function:: dismiss()
  :no-index:

  Closes the modal.

Properties
***************

.. function:: setLayout(layout) / getLayout()
  :no-index:

  The layout held inside.

.. function:: setTitle(text) / getTitle()
  :no-index:

  The text in the title bar.

.. function:: setIcon(path) / getIcon()
  :no-index:

  The window icon.

.. function:: setModal(modal) / isModal()
  :no-index:

  Whether the rest of the app is blocked while this window is open. On by
  default.

Events
***************

.. function:: setOnShown(callback)
  :no-index:

  Runs when the modal is shown.

.. function:: setOnClose(callback)
  :no-index:

  Runs when the modal is closed.

.. function:: setOnResize(callback)
  :no-index:

  Runs when the modal is resized.

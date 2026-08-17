StatusBar
############

The strip along the bottom of a window, for brief messages and small permanent
indicators.

.. code-block:: lua
  :linenos:

  local ui = require("limekit.ui")

  local status = ui.StatusBar()
  status:setText("Ready")

  window:setMainChild(status)

Messages
***************

.. function:: setText(text, timeout)
  :no-index:

  Shows a message. With a ``timeout`` in milliseconds the message clears itself
  afterwards; without one it stays until replaced.

  .. code-block:: lua

     status:setText("Saved", 3000)   -- disappears after three seconds

.. function:: clear()
  :no-index:

  Clears the current message.

Permanent widgets
********************

.. function:: addChild(child, stretch)
  :no-index:

  Adds a widget on the left, alongside messages.

.. function:: addPermanentChild(child, stretch)
  :no-index:

  Adds a widget on the right that messages never cover. Use it for things that
  should always be readable -- a line number, a connection indicator.

  .. code-block:: lua

     local position = ui.Label("Ln 1, Col 1")
     status:addPermanentChild(position)

Appearance
***************

.. function:: setSizeGripEnabled(enabled) / isSizeGripEnabled()
  :no-index:

  Whether the resize handle is shown in the corner.

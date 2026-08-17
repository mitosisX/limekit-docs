Button
###########

One of the most used widgets in any interface. Label it with text, an icon, or
both, and give it something to do when it is clicked.

.. code-block:: lua

  local ui = require("limekit.ui")

  local button = ui.Button("Save")

You react to a click with ``setOnClick``:

.. code-block:: lua
  :linenos:

  button:setOnClick(function(sender)
      print("clicked")
  end)

The handler receives the button itself as ``sender``, which is handy when
several buttons share one function.

.. note::

  If your handler raises an error, Limekit reports it naming ``Button.onClick``
  and the app keeps running. See :doc:`Core concepts </concepts>`.

Properties
***************

.. function:: setOnClick(callback)
  :no-index:

  The function executed when the button is clicked.

.. function:: setText(text) / getText()
  :no-index:

  The button's label.

.. function:: setIcon(path) / getIcon()
  :no-index:

  Sets an icon on the button.

  .. code-block:: lua

     local res = require("limekit.res")
     button:setIcon(res.Resources.images("save.png"))

  See :doc:`Services </services>` for resolving resource paths.

.. function:: setIconSize(size)
  :no-index:

  Resizes the icon, from a ``{width, height}`` pair.

  .. code-block:: lua

     button:setIconSize({ 24, 24 })

.. function:: setFlat(flat) / isFlat()
  :no-index:

  Draws the button without its raised border.

.. function:: setCheckable(checkable) / isCheckable()
  :no-index:

  Whether the button can be toggled on and off rather than just pressed.

.. function:: setChecked(checked) / isChecked()
  :no-index:

  The toggle state. Only meaningful on a checkable button.

  .. code-block:: lua

     local mute = ui.Button("Mute")
     mute:setCheckable(true)
     mute:setOnClick(function(sender)
         if sender:isChecked() then
             print("muted")
         else
             print("unmuted")
         end
     end)

.. function:: toggle()
  :no-index:

  Flips the checked state.

.. function:: click()
  :no-index:

  Clicks the button from code, running its ``onClick`` handler.

.. function:: setMenu(menu)
  :no-index:

  Attaches a menu that drops down when the button is pressed.

  See :doc:`working with menus </widgets/menu>`.

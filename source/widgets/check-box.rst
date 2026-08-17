CheckBox
###########

A box the user can tick. Use it for settings that are independently on or off --
when the options are mutually exclusive, use a
:doc:`RadioButton </widgets/radio-button>` instead.

.. code-block:: lua

  local ui = require("limekit.ui")

  local remember = ui.CheckBox("Remember me")
  remember:setChecked(true)

Properties
***************

.. function:: setText(text) / getText()
  :no-index:

  The label beside the box.

.. function:: setChecked(checked) / isChecked()
  :no-index:

  Whether the box is ticked.

.. function:: setOnCheck(callback)
  :no-index:

  Runs when the box is ticked or unticked. The handler receives the checkbox,
  so you can read its new state straight away.

  .. code-block:: lua

     remember:setOnCheck(function(sender)
         if sender:isChecked() then
             print("will remember")
         else
             print("will forget")
         end
     end)

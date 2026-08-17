Accordion
############

A stack of collapsible sections, one open at a time. It suits long forms and
settings screens where showing everything at once would overwhelm.

.. code-block:: lua
  :linenos:

  local ui = require("limekit.ui")

  local accordion = ui.Accordion()

  local accountLayout = ui.VLayout()
  accountLayout:addChild(ui.Label("Email"))
  accountLayout:addChild(ui.LineEdit())

  accordion:addLayout(accountLayout, "Account")

  local privacyLayout = ui.VLayout()
  privacyLayout:addChild(ui.CheckBox("Share usage data"))

  accordion:addLayout(privacyLayout, "Privacy")

Sections
***************

.. function:: addChild(child, label, icon)
  :no-index:

  Adds a section holding a single widget. ``icon`` is optional.

.. function:: addLayout(layout, label, icon)
  :no-index:

  Adds a section holding a whole layout. This is the usual one.

.. function:: getCount()
  :no-index:

  How many sections there are.

.. function:: setCurrentIndex(index) / getCurrentIndex()
  :no-index:

  Which section is open. **Positions start at 1.**

.. function:: setOnCurrentChange(callback)
  :no-index:

  Runs when a different section is opened.

  .. code-block:: lua

     accordion:setOnCurrentChange(function(sender)
         print("opened section " .. sender:getCurrentIndex())
     end)

TabItem
###########

A page inside a :doc:`Tab </widgets/tab>`. It is a blank panel that holds a
layout -- the same idea as a :doc:`Container </widgets/container>`, named for
where it is used.

.. code-block:: lua
  :linenos:

  local ui = require("limekit.ui")

  local tabs = ui.Tab()

  local general = ui.TabItem()
  local inner = ui.VLayout()
  inner:addChild(ui.Label("Language"))
  inner:addChild(ui.ComboBox({ "English", "Chichewa", "Swahili" }))
  general:setLayout(inner)

  tabs:addTab(general, "General")

Properties
***************

.. function:: setLayout(layout) / getLayout()
  :no-index:

  The layout held on the page.

Everything in :doc:`common to every widget </widgets>` applies here too, so a
page can be hidden, styled or disabled like anything else.

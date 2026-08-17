StackedLayout
################

Several pages occupying the same space, with one visible at a time. Use it for
wizards, or for a sidebar where each entry swaps the main panel.

.. code-block:: lua
  :linenos:

  local ui = require("limekit.ui")

  local pages = ui.StackedLayout()
  pages:addLayout(welcomePage)
  pages:addLayout(detailsPage)
  pages:addLayout(finishPage)

  pages:setCurrentIndex(1)

  nextButton:setOnClick(function()
      pages:setCurrentIndex(pages:getCurrentIndex() + 1)
  end)

Properties
***************

.. function:: addChild(child)
  :no-index:

  Adds a widget as a page.

.. function:: addLayout(layout)
  :no-index:

  Adds a whole layout as a page.

  .. note::

     This did not work in 1.x -- it called a method that does not exist, so the
     branch was unreachable. It works now.

.. function:: setCurrentIndex(index) / getCurrentIndex()
  :no-index:

  Which page is visible. **Positions start at 1.**

.. function:: getCount()
  :no-index:

  How many pages there are.

.. seealso::

  :doc:`SlidingStackedWidget </widgets/sliding-stacked-widget>` does the same
  job with an animated transition between pages.

  :doc:`Layout Managers </layouts>` for the methods every layout shares.

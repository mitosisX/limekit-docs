Layout Managers
==================

Layouts arrange widgets. Rather than positioning things at fixed coordinates,
you describe how they relate -- side by side, stacked, in a grid -- and the
layout works out the positions, adjusting as the window is resized.

Every layout lives in ``limekit.ui``:

.. code-block:: lua

   local ui = require("limekit.ui")

   local layout = ui.VLayout()
   layout:addChild(ui.Label("Name"))
   layout:addChild(ui.LineEdit())

   window:setLayout(layout)

.. important::

   A widget appears on screen only once it is inside a layout, and that layout
   is given to a window with ``setLayout``. This is the single most common
   reason a widget does not show up.

Choosing one
--------------

.. list-table::
   :header-rows: 1
   :widths: 26 74

   * - Layout
     - Use it when
   * - :doc:`HLayout </layouts/hlayout>`
     - Widgets sit in a row
   * - :doc:`VLayout </layouts/vlayout>`
     - Widgets stack in a column
   * - :doc:`GridLayout </layouts/grid-layout>`
     - Widgets line up in rows *and* columns
   * - :doc:`FormLayout </layouts/form-layout>`
     - Labelled fields, each label beside its input
   * - :doc:`StackedLayout </layouts/stacked-layout>`
     - Several pages share one space, one visible at a time

Layouts nest, which is how real interfaces get built -- a row inside a column,
a grid inside a page:

.. code-block:: lua
   :linenos:

   local buttons = ui.HLayout()
   buttons:addChild(ui.Button("Cancel"))
   buttons:addChild(ui.Button("Save"))

   local page = ui.VLayout()
   page:addChild(ui.Label("Settings"))
   page:addChild(settingsGrid)
   page:addStretch(1)
   page:addLayout(buttons)

Common to every layout
------------------------

.. function:: addChild(child)
  :no-index:

   Adds a widget. Some layouts take extra arguments -- see their pages.

.. function:: addLayout(layout)
  :no-index:

   Adds another layout inside this one.

.. function:: getChildAt(index)
  :no-index:

   The widget at a position. **Positions start at 1.**

.. function:: getLayoutAt(index)
  :no-index:

   The nested layout at a position.

.. function:: getCount()
  :no-index:

   How many items the layout holds.

.. function:: clear()
  :no-index:

   Removes everything.

.. function:: setSpacing(pixels) / getSpacing()
  :no-index:

   The gap between items.

.. function:: setMargins(left, top, right, bottom)
  :no-index:

   The space between the layout's edge and its contents.

   .. code-block:: lua

      layout:setSpacing(10)
      layout:setMargins(20, 20, 20, 20)

.. function:: setContentAlignment(...)
  :no-index:

   Where the contents sit within the space available. Takes one or more of
   ``left``, ``right``, ``center``, ``top``, ``bottom``, ``hcenter``,
   ``vcenter``, ``justify``.

.. toctree::
   :maxdepth: 1

   layouts/hlayout
   layouts/vlayout
   layouts/grid-layout
   layouts/form-layout
   layouts/stacked-layout

Widget Items
=================

Some widgets are containers for smaller pieces rather than things you configure
directly. A :doc:`Menu </widgets/menu>` holds menu items, a
:doc:`Table </widgets/table>` holds cells, a :doc:`TreeView </widgets/tree-view>`
holds branches. Those pieces are classes of their own, and this section covers
them.

Like everything else, they come from ``limekit.ui``:

.. code-block:: lua

   local ui = require("limekit.ui")

   local item = ui.MenuItem("Open")

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Item
     - Belongs to
   * - :doc:`MenuItem </widget-items/menu-item>`
     - :doc:`Menu </widgets/menu>`, :doc:`Menubar </widgets/menu-bar>`
   * - :doc:`ToolbarButton </widget-items/toolbar-item>`
     - :doc:`Toolbar </widgets/tool-bar>`
   * - :doc:`TabItem </widget-items/tab-item>`
     - :doc:`Tab </widgets/tab>`
   * - :doc:`TableItem </widget-items/table-item>`
     - :doc:`Table </widgets/table>`
   * - :doc:`TreeViewItem </widget-items/tree-view-item>`
     - :doc:`TreeView </widgets/tree-view>`

.. toctree::
   :maxdepth: 2
   :titlesonly:

   widget-items/menu-item
   widget-items/toolbar-item
   widget-items/tab-item
   widget-items/table-item
   widget-items/tree-view-item

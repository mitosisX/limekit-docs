===========
VLayout
===========

A layout that helps organize widgets in a vertical arrangement within a window or interface. It stacks elements on top of each other from top to bottom, making it easy to place widgets vertically one after another. This layout ensures that when you add widgets, they align vertically and adjust their positions automatically if the window is resized. It's useful for creating interfaces where elements are stacked vertically, like a list of items or a column of buttons.

.. code-block:: lua

  local layout = VLayout()

Properties
***************

.. function:: addChild(widget, stretch: optional)

  The **optional** stretch parameter in the ``addChild`` method determines how much space a widget occupies relative to other widgets in the layout.

  For instance, if you add three widgets to a vertical layout and set the stretch factor to 0 for the first widget, 1 for the second widget, and 2 for the third widget, the third widget will take up more vertical space compared to the first and second widgets. The space distribution is proportional to the stretch factors assigned to each widget.

  .. code-block:: lua
    
    local layout = VLayout()

    local button1 = Button("Button 1")
    local button2 = Button("Button 2")
    local button3 = Button("Button 3")

    layout:addChild(button1)     -- default stretch factor is 0 anyway
    layout:addChild(button2, 1)  -- stretch factor 1
    layout:addChild(button3, 2)  -- stretch factor 2

.. note::

  You don't have to specify a stretch value unless needed. By default, it's always set to ``0``. Feel free to omit it if you don't require a specific stretch for your layout.

.. function:: setContentAlignment(alignment)
  
  This property allows you to specify the alignment of the widgets within a layout. This method sets the alignment of the entire layout's content within its allocated space. Available alignment flags: ``leading``, ``left``, ``tight``, ``trailing``, ``hcenter``, ``justify``, ``absolute``, ``horizontal_mask``, ``top``, ``bottom``, ``vcenter``, ``center``, ``baseline`` and ``vertical_mask``

.. function:: addLayout(layout)

  This allows you to add an entire layout as a single element within another layout. This is helpful when you want to nest layouts to create more complex UI structures.

.. function:: addStretch(stretch)
  
  This property is used to add stretchable space within a layout. This stretchable space pushes the widgets towards the beginning or end of the layout, depending on where the stretch is added.

  For instance, if you have a horizontal layout and you add addStretch before and after adding widgets, it will push the widgets to the center, creating space before and after them that expands or contracts based on the available space.

  .. code-block:: lua

    local layout = HLayout()

    local button1 = Button("Button 1")
    local button2 = Button("Button 2")
    local button3 = Button("Button 3")

    layout:addStretch(1)  -- Adds stretchable space before buttons
    layout:addChild(button1)
    layout:addChild(button2)
    layout:addChild(button3)
    layout:addStretch(1)  -- Adds stretchable space after buttons

.. function:: setMargins(left, top,right,bottom)

  Sets the margins of the layout
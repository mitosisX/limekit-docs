Widgets
========

Widgets are graphical elements or components that make up the user interface of an application. They can be buttons, text boxes, labels, windows, checkboxes, sliders, and more. These widgets allow users to interact with the program by providing input, displaying information, or triggering specific actions. This framework provides a wide range of widgets that can be arranged to create a functional and visually appealing user interface.

Presently, there are :mod:`35` widgets at your disposal within the framework. Considering the framework is new, the count is subject to change. Anticipate additional widgets as the framework evolves.

.. important::

   Every app requires a Window to function properly. In your :mod:`main.lua` file, create a window object like shown below.

   .. code-block:: lua
      :linenos:

      local window = Window{title = 'Limekit', icon = images('app.png'), size={200,200}}
      window:show()

   This creates an interactive window that serves your layouts holding all of your widgets.

   checkout using :doc:`Window </widgets/window>`


.. important::

   All widgets can be added to a layout using the :mod:`addChild` function

.. admonition:: Hey, heads up!

   Before you start, you might want to take a look at how to access your resources. Just head over :doc:`here </user-resources>`


For a comprehensive understanding of their usage, explore the available widgets in-depth:

.. toctree::
   :maxdepth: 2
   :titlesonly:
   
   widgets/accordion
   widgets/button
   widgets/button-group
   widgets/calendar
   widgets/check-box
   widgets/combo-box
   widgets/command-button
   widgets/date-picker
   widgets/dock
   widgets/double-spinner
   widgets/gif-player
   widgets/group-box
   widgets/hline
   widgets/image
   widgets/knob
   widgets/label
   widgets/line-edit
   widgets/list-box
   widgets/menu
   widgets/menu-bar
   widgets/modal
   widgets/progress-bar
   widgets/radio-button
   widgets/scroller
   widgets/slider
   widgets/sliding-stacked-widget
   widgets/splitter
   widgets/spinner
   widgets/tab
   widgets/table
   widgets/text-field
   widgets/time-picker
   widgets/tool-bar
   widgets/vline
   widgets/window
Charts
========

.. contents:: Content
    :depth: 2
    :local:
    :backlinks: top

Charts are built from three pieces:

1. A **series** holds your data -- :ref:`LineChart <linechart>`, one of the
   four :ref:`bar arrangements <barchart>`, or :ref:`AreaChart <areachart>`.
2. A **Chart** collects one or more series, along with the title, legend and axes.
3. A **ChartView** is the widget that displays it. This is the part you add to a layout.

.. code-block:: lua
   :linenos:

   local ui    = require("limekit.ui")
   local chart = require("limekit.chart")

   local window = ui.Window { title = "Sales", size = { 640, 420 } }

   -- 1. the data
   local line = chart.LineChart()
   line:setName("2026")
   line:setData({ {1, 40}, {2, 65}, {3, 55}, {4, 90} })

   -- 2. the chart
   local graph = chart.Chart { title = "Quarterly sales" }
   graph:addSeries(line)
   graph:setAnimation("all")
   graph:setLegendAlignment("bottom")

   -- 3. the widget
   local view = chart.ChartView(graph)

   local layout = ui.VLayout()
   layout:addChild(view)
   window:setLayout(layout)
   window:show()

.. note::

   Charts need Qt's charting add-on, which ships with PySide6 by default. If it
   is missing from your Python installation, creating a chart raises an error
   telling you so -- the rest of the framework is unaffected.

The chart
-----------

.. function:: chart.Chart(options)
  :no-index:

   Creates a chart. ``options`` accepts ``title`` and ``animation``.

   .. code-block:: lua

      local graph = chart.Chart { title = "Revenue", animation = "all" }

.. function:: setTitle(text) / getTitle()
  :no-index:

   The heading shown above the chart.

.. function:: addSeries(series)
  :no-index:

   Adds a series. A chart can hold several, and they are drawn together.

.. function:: addAxis(axis, position)
  :no-index:

   Attaches an axis. ``position`` is ``left``, ``right``, ``top`` or ``bottom``
   and defaults to ``top``.

.. function:: setAnimation(animation)
  :no-index:

   How the chart animates as it draws. One of ``none``, ``series``, ``grid`` or
   ``all``.

.. function:: setLegendVisibility(visible)
  :no-index:

   Shows or hides the legend.

.. function:: setLegendAlignment(position)
  :no-index:

   Where the legend sits: ``left``, ``right``, ``top`` or ``bottom``. Defaults
   to ``bottom``.

The chart widget
------------------

.. function:: chart.ChartView(chart)
  :no-index:

   The widget that draws a chart. Add it to a layout like any other widget.

.. function:: setChart(chart) / getChart()
  :no-index:

   The chart being displayed. Set a different one to swap the whole graph.

.. function:: setTheme(theme)
  :no-index:

   Applies one of the built-in chart colour themes.

.. function:: getThemes()
  :no-index:

   A table of the available theme names.

``ChartView`` is a widget, so everything on :doc:`every widget </widgets>` --
``setSize``, ``setToolTip``, ``show``, ``hide`` -- works here too.

.. _linechart:

Line charts
-------------

.. function:: chart.LineChart()
  :no-index:

   A series drawn as a line.

.. function:: setName(name) / getName()
  :no-index:

   The label shown for this series in the legend.

.. function:: append(x, y)
  :no-index:

   Adds a single point.

.. function:: setData(points)
  :no-index:

   Adds many points at once, from a table of ``{x, y}`` pairs.

   .. code-block:: lua

      line:setData({ {1, 10}, {2, 24}, {3, 18} })

.. function:: attachAxis(axis)
  :no-index:

   Binds the series to an axis you added to the chart.

   .. important::

      Adding an axis to the chart is only half the job -- without this call
      the series is drawn against Qt's own default axis, so the range and
      title you set are quietly ignored. Every series needs it, once per axis.

      .. code-block:: lua

         graph:addAxis(x, "bottom")
         graph:addAxis(y, "left")
         line:attachAxis(x)
         line:attachAxis(y)

.. _barchart:

Bar charts
------------

A bar chart holds one or more **bar sets**. Each set is a named group of
values -- one set per thing you want to compare.

There are four bar series, and which one you pick decides what a reader can
easily compare. They share exactly the same methods, so swapping one for
another is a one-word change.

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Series
     - Draws
   * - ``chart.BarChart``
     - Each set side by side within a category. Best for comparing sets against
       each other.
   * - ``chart.StackedBarChart``
     - Each set piled on the one below, so a bar's height is the total. Best
       when the total matters as much as the parts.
   * - ``chart.PercentBarChart``
     - Stacked, then scaled so every bar is full height. Sizes disappear and
       what is left is each set's **share**.
   * - ``chart.HorizontalBarChart``
     - Side by side, running left to right. Worth reaching for when the
       category labels are long enough to collide under a vertical axis.

.. important::

   ``HorizontalBarChart`` swaps the axes round with the bars: the
   ``CategoryAxis`` goes on the ``left`` and the ``ValueAxis`` along the
   ``bottom``.

.. code-block:: lua

   local sales = chart.BarSet("Sales")
   sales:append({ 40, 65, 55, 90 })

   local costs = chart.BarSet("Costs")
   costs:append({ 25, 30, 40, 50 })

   local bars = chart.BarChart()
   bars:append(sales)
   bars:append(costs)

   local axis = chart.CategoryAxis({ "Q1", "Q2", "Q3", "Q4" })

   local graph = chart.Chart { title = "Sales vs costs" }
   graph:addSeries(bars)
   graph:addAxis(axis, "bottom")
   bars:attachAxis(axis)

Swapping the arrangement is one word:

.. code-block:: lua

   local bars = chart.StackedBarChart()     -- was chart.BarChart()

.. function:: chart.BarChart() / chart.StackedBarChart() / chart.PercentBarChart() / chart.HorizontalBarChart()
  :no-index:

   A series drawn as bars, in one of the four arrangements above. Every method
   below is shared by all four.

.. function:: append(barset)
  :no-index:

   Adds a bar set.

.. function:: attachAxis(axis)
  :no-index:

   Binds the series to an axis you added to the chart. See the note under
   :ref:`LineChart <linechart>` -- skipping it means your axes are ignored.

.. function:: setBarWidth(width)
  :no-index:

   How much of each category slot the bars fill, from ``0`` to ``1``.

.. function:: setLabelsVisible(visible)
  :no-index:

   Draws each bar's value on the bar itself. This is what makes a
   ``PercentBarChart`` readable -- without labels you are eyeballing
   proportions.

.. function:: setLabelsFormat(text)
  :no-index:

   A format string for those labels, where ``@value`` stands for the number.

   .. code-block:: lua

      bars:setLabelsVisible(true)
      bars:setLabelsFormat("@value%")

.. function:: setLabelsPosition(position)
  :no-index:

   Where on the bar the label sits: ``center``, ``insideend``, ``insidebase``
   or ``outsideend``. An unrecognised name raises and lists the valid ones.

.. function:: chart.BarSet(title)
  :no-index:

   A named group of bar values.

.. function:: setLabel(text) / getLabel()
  :no-index:

   The name shown in the legend.

.. function:: append(values)
  :no-index:

   Adds values, from a table of numbers.

.. _areachart:

Area charts
-------------

An area chart fills the space between two line series. Pass the upper series,
and optionally a lower one -- with only an upper series, the area is filled down
to the axis.

.. code-block:: lua

   local upper = chart.LineChart()
   upper:setData({ {1, 30}, {2, 45}, {3, 40} })

   local lower = chart.LineChart()
   lower:setData({ {1, 10}, {2, 20}, {3, 15} })

   local band = chart.AreaChart(upper, lower)
   band:setName("Range")

.. function:: chart.AreaChart(upper, lower)
  :no-index:

   A filled area between two line series.

.. function:: setName(name) / getName()
  :no-index:

   The label shown in the legend.

Axes
------

.. function:: chart.ValueAxis()
  :no-index:

   A numeric axis.

.. function:: setTitleText(text) / getTitleText()
  :no-index:

   The axis label.

.. function:: setRange(start, end_)
  :no-index:

   The range of values the axis covers.

.. function:: chart.CategoryAxis(categories)
  :no-index:

   An axis of named categories rather than numbers -- month names, product
   names, and so on.

.. function:: append(categories)
  :no-index:

   Adds categories, from a table of strings.

.. code-block:: lua

   local y = chart.ValueAxis()
   y:setTitleText("Units sold")
   y:setRange(0, 100)

   graph:addAxis(y, "left")

Batteries included
====================

.. highlight:: console

.. contents:: Content
    :depth: 1
    :local:
    :backlinks: top

This comprehensive tutorial covers the rest of the available functionalities in the framework. These include accessing SQLite3 databases, sending system notifications, utilizing the system tray, theming, multitasking, handling signals, and much more.

Let's go through them in detail

1. Theming
-------------

Themes are what make modern design in Limekit possible.

There are currently 3 categories of themes in Limekit; :mod:`darklight`, :mod:`material` and :mod:`misc`. Use ``getThemes()`` to get themes for a particular theme category, and ``setTheme(theme)`` to set the theme.

.. code-block:: lua

  local theme = Theme('darklight')
  local allThemes = theme:getThemes()

  theme:setTheme(allThemes[1])

2. Dialogs
------------

- Limekit offers various dialogs for tasks such as opening files, saving files, receiving input, and more, all of which will be discussed.

File and Folder dialogs
^^^^^^^^^^^^^^^^^^^^^^^^^

.. note::
  :mod:`filters` allows you to specify the type of files that will be displayed in the dialog's file type dropdown filter.
  
  example: ``{['Image Files'] = {'.jpg', '.png'}, Audio = {'.mp3', '.flac'}, Archieves = {'.zip', '.tar', '.rar'}}``

  :mod:`dir` is used to specify the initial directory that the file dialog will open when it's launched. Pass an empty string to ignore

.. code-block:: lua

  -- allows opening of files
  app.openFileDialog(window, title, dir, filters)

.. code-block:: lua

  app.saveFileDialog(window, title, dir, filters)

.. code-block:: lua

  app.folderPickerDialog(window, title, dir)

Input Dialogs
^^^^^^^^^^^^^^^

.. code-block:: lua

  app.textInputDialog(window, title, label)


.. code-block:: lua

  -- can ignore content
  app.multilineInputDialog(window, title, label, content)


.. code-block:: lua

  -- items: table
  -- can ignore startIndex
  app.comboBoxInputDialog(window, title, label, items, startIndex)


.. code-block:: lua

  -- step: increment by
  -- can ignore step
  app.integerInputDialog(window, title, label, startValue, minValue, maxValu, step)


.. code-block:: lua

  -- can ignore step
  app.doubleInputDialog(window, title, label, value, minValue, maxValue, step)

Alerts
^^^^^^^^^

.. code-block:: lua

  -- returns true or false
  -- for an alert like this, you don't really need the result
  local result = app.alert(window, title, message)

.. code-block:: lua

  -- Contains the 'do not show this message again' button
  app.infoMessageDialog(window, title, message)

.. code-block:: lua

  app.aboutAlertDialog(window, title, message)

.. code-block:: lua

  app.criticalAlertDialog(window, title, message)

.. code-block:: lua

  app.infoAlertDialog(window, title, message)

.. code-block:: lua

  -- returns true or false
  local result = app.questionAlertDialog(window, title, message)

.. code-block:: lua

  app.warningAlertDialog(window, title, message)

Other
^^^^^^^

.. code-block:: lua

  -- type: hex or RGB
  app.colorPickerDialog(window, type)

3. System Tray and System Notification
----------------------------------------

Learn how to create a system tray icon or send system notifications

System Tray
^^^^^^^^^^^^

.. code-block:: lua

  local tray = SysTray(icon)

Properties
^^^^^^^^^^^

.. function:: setIcon(icon)

  Sets the icon

.. function:: setToolTip(text)

  Sets the icon

.. function:: setMenu(menu)

  Sets menu

checkout :doc:`Menus </widgets/menu>`

.. function:: setVisibility(text)

  Sets the visibility

System Notifications
^^^^^^^^^^^^^^^^^^^^^

Allows you to send notification from your app.

.. code-block:: lua

  local tray = SysNotification(icon)

Properties
^^^^^^^^^^^


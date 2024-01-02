===========
MenuBar
===========

This widget provides a horizontal bar typically placed at the top of the application window, containing various menus. Each menu can hold menu items, which when clicked, can trigger specific actions or open sub-menus. The MenuBar widget is an essential component for organizing and providing access to different functionalities or commands within an application.

.. code-block:: lua

  local menubar = MenuBar()

checkout :doc:`MenuItems </widgets-items/menu-item>`

.. note::

  It is highly recommended to use the ``buildFromTemplate(template)`` as this saves you a lot of time from individualy creating ``MenuItem`` objects. This powerful features uses tables


Properties
***************

.. function:: buildFromTemplate(template: table)

  A powerful features that allows developing complex menus using tables. 

  .. code-block:: lua

    local menubar = MenuBar();
    menubar:buildFromTemplate({{
          label = '&File',
          submenu = {{
              label = 'New File',
              name = 'new_file',
              shortcut = "Ctrl+N",
              icon = images('newfile.png'),
              click = createFileFunc}}
        },
        {
          label = 'Help',
          submenu = {{
            label = 'About'}}
        }})

- The preceding code example illustrates the capabilities of the ``buildFromTemplate`` function, showcasing its power in creating a sample menubar using tables

.. function:: getChild(name)

  Returns the ``MenuItem`` widget assigned with the name. This only applies when ``name`` was used on a ``submenu`` inside ``buildFromTemplate``.


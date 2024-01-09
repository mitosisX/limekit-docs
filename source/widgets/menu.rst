Menu
===========

A customizable pop-up menu that appears in response to user actions, such as clicking a button. It provides a list of options or actions for users to choose from, typically displayed as a drop-down menu. Developers can populate a menu with various menu items, submenus and separators to create a hierarchy of actions or choices. :mod:`Menu` is commonly used with other widgets, like buttons or toolbars or the system tray, to offer users a set of actions or options in a neatly organized menu format, improving the usability and functionality of the application.

.. code-block:: lua

  local menu = Menu()

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
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MyMenu(Gtk.MenuBar):

	def __init__(self, parent):
		super(MyMenu, self).__init__()

		file_menu_content = Gtk.Menu()
		file_menu = Gtk.MenuItem(label="File")
		file_menu.set_submenu(file_menu_content)
		file_menu_exit = Gtk.MenuItem(label="Exit")
		file_menu_exit.connect("activate", Gtk.main_quit)
		file_menu_content.append(file_menu_exit)
		self.append(file_menu)

		edit_menu_content = Gtk.Menu()
		edit_menu = Gtk.MenuItem(label="Edit")
		edit_menu.set_submenu(edit_menu_content)
		edit_menu_content.append(Gtk.MenuItem(label="Settings"))
		self.append(edit_menu)

		view_menu_content = Gtk.Menu()
		view_menu = Gtk.MenuItem(label="View")
		view_menu.set_submenu(view_menu_content)
		view_menu_hidden = Gtk.MenuItem(label="Show hidden files")
		view_menu_hidden.connect("activate", parent.toggle_hidden)
		view_menu_content.append(view_menu_hidden)
		self.append(view_menu)

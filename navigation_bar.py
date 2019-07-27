import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

def create_navigation_bar(parent):
	bar = Gtk.Grid()
	back_icon = Gtk.Image(stock=Gtk.STOCK_GO_BACK)
	back_button = Gtk.Button(image=back_icon)
	forward_icon = Gtk.Image(stock=Gtk.STOCK_GO_FORWARD)
	forward_button = Gtk.Button(image=forward_icon)
	up_icon = Gtk.Image(stock=Gtk.STOCK_GO_UP)
	up_button = Gtk.Button(image=up_icon)
	up_button.connect("clicked", parent.move_up)
	refresh_icon = Gtk.Image(stock=Gtk.STOCK_REFRESH)
	refresh_button = Gtk.Button(image=refresh_icon)
	refresh_button.connect("clicked", parent.refresh)
	home_icon = Gtk.Image(stock=Gtk.STOCK_HOME)
	home_button = Gtk.Button(image=home_icon)
	home_button.connect("clicked", parent.move_home)

	parent.search_bar = Gtk.Entry()

	parent.search_bar.set_hexpand(True)
	back_button.set_hexpand(False)
	forward_button.set_hexpand(False)
	up_button.set_hexpand(False)
	refresh_button.set_hexpand(False)
	home_button.set_hexpand(False)

	bar.attach(back_button, 0, 1, 1, 1)
	bar.attach(forward_button, 1, 1, 1, 1)
	bar.attach(up_button, 2, 1, 1, 1)
	bar.attach(home_button, 3, 1, 1, 1)
	bar.attach(parent.search_bar, 4, 1, 9, 1)
	bar.attach(refresh_button, 13, 1, 1, 1)
	parent.grid.attach(bar, 0, 1, 1, 1)

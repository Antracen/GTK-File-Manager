import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GdkPixbuf

class Panel(Gtk.TreeView):

	def __init__(self, parent):
		super(Panel, self).__init__()

		folder_icon = Gtk.Image(stock=Gtk.STOCK_DIRECTORY)
		favorites_list = ["/home/wass", "/home/wass/Skrivbord", "/media/wass/My Passport"]
		self.file_list = Gtk.ListStore(str, str)
		for item in favorites_list:
			self.file_list.append(["folder", item])
		self.set_model(self.file_list)

		favorite_column = Gtk.TreeViewColumn("Favorites")
		pixbuf_renderer = Gtk.CellRendererPixbuf()
		text_renderer = Gtk.CellRendererText()
		favorite_column.pack_start(pixbuf_renderer, expand=False)
		favorite_column.pack_start(text_renderer, expand=True)
		favorite_column.add_attribute(pixbuf_renderer, "icon_name", 0)
		favorite_column.add_attribute(text_renderer, "text", 1)
		self.append_column(favorite_column)

		self.set_vexpand(True)
		self.set_property("activate-on-single-click", True)
		self.connect("row-activated", parent.handle_click)

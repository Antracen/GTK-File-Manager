import gi, os, subprocess
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GdkPixbuf
from menu import MyMenu
import navigation_bar as navbar
import favorite_panel as favorite

def size_str(size):
	sizes = [" b", " kB", " MB", " GB", " TB", " PB", " EB"]
	for unit in sizes:
		if size < 1000: return str(round(size, 1)) + unit
		size = size / 1000

class FileManager(Gtk.Window):

	def __init__(self):

		self.show_hidden_files = False

		Gtk.Window.__init__(self, title="FileManager")

		self.grid = Gtk.Grid()
		self.add(self.grid)
		
		self.menu_bar = MyMenu(parent=self)
		self.grid.attach(self.menu_bar, 0, 0, 1, 1)

		navbar.create_navigation_bar(self)

		main_window = Gtk.Paned()

		self.favorite_panel = favorite.Panel(self)

		pixbuf_renderer = Gtk.CellRendererPixbuf()
		text_renderer = Gtk.CellRendererText()

		self.file_list = Gtk.ListStore(str, str, str)
		self.file_window = Gtk.TreeView(model=self.file_list)
		self.refresh()
		filename_col = Gtk.TreeViewColumn("Filename")
		filename_col.pack_start(pixbuf_renderer, expand=False)
		filename_col.pack_start(text_renderer, expand=True)
		filename_col.set_resizable(True)
		filename_col.set_sort_column_id(1)
		filename_col.add_attribute(pixbuf_renderer, "icon_name", 0)
		filename_col.add_attribute(text_renderer, "text", 1)
		self.file_window.append_column(filename_col)
		filesize_col = Gtk.TreeViewColumn("Filesize", Gtk.CellRendererText(), text=2)
		filesize_col.set_resizable(True)
		filesize_col.set_sort_column_id(1)
		self.file_window.append_column(filesize_col)
		self.file_window.set_vexpand(True)
		self.file_window.connect("row-activated", self.handle_click)

		main_window.add1(self.favorite_panel)
		main_window.add2(self.file_window)
		self.grid.attach(main_window, 0, 2, 1, 1)
		self.refresh()

	def handle_click(self, widget, row, col):
		self.change_folder(widget.get_model()[row][1])

	def move_up(self, button):
		self.change_folder("..")

	def move_home(self, button):
		self.change_folder(os.path.expanduser("~"))

	def change_folder(self, folder):
		if(os.path.isdir(folder)):
			os.chdir(folder)
			self.refresh()
		else:
			subprocess.Popen(["xdg-open", folder])

	def toggle_hidden(self, button=None):
		self.show_hidden_files = not self.show_hidden_files
		self.refresh()

	def refresh(self, button=None):
		self.file_list.clear()
		new_model = Gtk.ListStore(str, str)
		for file in os.listdir(os.getcwd()):
			if self.show_hidden_files or not file.startswith('.'):
				file_info = os.stat(file)
				icon = "text-x-generic"
				if os.path.isdir(file):
					icon = "folder"
				else:
					extension = file.split(".")[-1]
					switcher = {
						"png": "image-x-generic",
						"mkv": "video-x-generic",
						"mp3": "audio-x-generic",
						"jpg": "image-x-generic",
						"zip": "package-x-generic",
						"zip": "package-x-generic",
						"cpp": "text-x-script",
					}
					icon = switcher.get(extension, "text-x-generic")
				self.file_list.append([icon, file, size_str(file_info.st_size)])
		self.file_window.set_model(self.file_list)
		self.search_bar.set_text(os.getcwd())

window = FileManager()
window.connect("destroy", Gtk.main_quit)
window.show_all()
Gtk.main()

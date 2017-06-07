from tkinter import Tk, Label, Button, Entry, filedialog
from smurf import Smurf

def buttonWithLabel(master, label, command):
    """
    Creates input field with label and returns the input field
    """
    label = Label(master, text=label)
    label.pack()
    button = Button(master, text="Choose File", command=command)
    button.pack()

    return button

class App:
    def __init__(self, master):
        self.master = master
        # self.master.geometry('{}x{}'.format(800, 600))
        master.title("Photo Smurf")

        self._config = {
          "src": None,
          "dest": None,
          "album_config": None
        }
        self._src_folder = None
        self._dest_folder = None
        self._album_file = None

        self._smurf = None

        self.label = Label(master, text="Photosmurf")
        self.label.pack()

        buttonWithLabel(master, "Source Folder", lambda: self.load_directory("src", "Open Source Folder"))
        buttonWithLabel(master, "Destination Folder", lambda: self.load_directory("dest", "Open Dest Folder"))
        buttonWithLabel(master, "Albums file", lambda: self.load_file("album_config", "Open Album Config file (*.txt)"))

        self.button_go = Button(master, text="Go!", command=self.run)
        self.button_go.pack()


    def load_directory(self, item, title):
        self._config[item] = filedialog.askdirectory(title=title)

    def load_file(self, item, title):
        self._config[item] = filedialog.askopenfilename(title=title)

    def run(self):
        if self._smurf is None:
            self._smurf = Smurf(self._config["src"],
                                self._config["dest"],
                                self._config["album_config"]
                              )

        self._smurf.run()

root = Tk()
my_gui = App(root)
root.mainloop()
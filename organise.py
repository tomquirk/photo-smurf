import os, sys, datetime, time, ttk
import Tkinter as tk

class Organise(object):

    def __init__(self, src, dest):
        """Initialises data. Specify prospective folder names, with date intervals (tuples), in self._categories
        """
        self._src = src
        self._dest = dest
        self._categories = [
                            {'dir_name': 'c_wedding_renee', 'date_range': [(2015, 4, 18), (2015, 4, 18)]},
                            {'dir_name': 'c_stylemag_chanel7', 'date_range': [(2014, 1, 24), (2014, 1, 24)]}
                            ]

    def create_dir(self):
        """Creates directory within destination directory, based on category dir_name
        :return: None
        """
        for cat in self._categories:
            dir_name = cat['dir_name']
            os.chdir(self._dest)
            os.makedirs(dir_name)

        return None

    def seek(self, cwd):
        """
        Crawls through directory and places files within a specified date range in their specified category
        :param cwd: str
        :return: None
        """
        cwd += '/'
        os.chdir(cwd)   # change current working dir to 'cwd' arg
        src_files = os.listdir(cwd)
        src_files.remove('.DS_Store')
        src_folders = []

        for item in src_files:
            item_path = cwd + item

            if os.path.isfile(item_path):
                self.move(item_path)
            else:
                src_folders.append(item_path)

        for folder_path in src_folders:
            self.seek(folder_path)

        return None



    def move(self, file):

        """
        Moves given file to new directory, as determined by its created date and the date range of a particular category
        :param file: str
        :return: None
        """
        print(file)
        if file.endswith('.jpg') or file.endswith('.JPG'):
            date_arr = str(datetime.datetime.fromtimestamp(os.path.getmtime(file)))[:-9].split('-')
            date_path = date_arr[0] + '-' + date_arr[1] + '-' + date_arr[2] + '/'
            date_created = (int(date_arr[0]), int(date_arr[1]), int(date_arr[2]))

            for cat in self._categories:
                date_range = cat['date_range']
                dir_name = cat['dir_name']
                if date_range[0] <= date_created <= date_range[1]:
                    new_path = self._dest + '/' + dir_name + '/' + file.split('/')[-1]
                    os.rename(file, new_path)

        return None

    def run(self):
        """
        Runs script
        :return:
        """
        self.create_dir()
        self.seek(self._src)

class App(object):
    """The Top-level class for the GUI."""
    
    def __init__(self, root):
        """Initialises Gui params
        """
        self._root = root
        title = tk.Label(self._root, text="Photo Smurf")
        
        self._input_count = 0
        
        add_input = tk.Button(self._root, text="Add Album", command=self.create_input)
        
        title.pack()
        add_input.pack()
        
    def create_input (self):
        print('input created! ID: %d' % self._input_count)
        entryId = self._input_count
        entryId = tk.Entry(self._root, width=60)
        entryId.pack()
        
        self._input_count += 1
        
    def exit(self):
        """Close the application.
        TemperaturePlotApp.exit() -> None
        """
        self._master.destroy()
        
def main():
    root = tk.Tk()
    app = App(root)
    app.create_input()
    root.geometry("800x400")
    root.mainloop()

if __name__ == '__main__':
    main()
    
#src = '/Users/tomquirk/Documents/collection'
#dest = '/Users/tomquirk/Documents/photos'
#
#organise = Organise(src, dest)
#
#organise.run()

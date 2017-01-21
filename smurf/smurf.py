import os, sys, datetime, time, shutil

class Colour:
    """Class for holding ANSI print colours"""
    def __init__(self):
        return None

    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Smurf(object):

    def __init__(self, src, dest, f):
        """Initialises data. Specify prospective folder names, with date intervals (tuples), in self._categories
        """
        self._src = src
        self._dest = dest
        self._albums = open(f)

        self._file_types = ['.jpg', '.cr2']
        self._categories = []

    def get_albums(self, txt_file):
        """
        Populates self._categories object based on text file (see documentation for naming convention)
        :param txt_file: str
        :return: list
        """
        albums = txt_file.read().split('\n')

        # converts 1-digit int with '0' char to int, and changes str to int
        def clean(dates):
            index = 0
            for date in dates:
                if date[0] == '0':
                    dates[index] = int(date[1])
                else:
                    dates[index] = int(date)
                index += 1

            return dates

        for album in albums:
            album = album.split(' ')

            if len(album) < 2:
                break

            dir_name = album[0]

            date_1 = clean(album[1].split('/'))
            if len(album) == 3:
                date_2 = clean(album[2].split('/'))
                date_range = [(date_1[2], date_1[1], date_1[0]), (date_2[2], date_2[1], date_2[0])]
            else:
                date_range = [(date_1[2], date_1[1], date_1[0]), (date_1[2], date_1[1], date_1[0])]

            self._categories.append({'dir_name': dir_name, 'date_range': date_range, 'fcount': 0})

        return self._categories

    def test(self):
        """Unit tests on src, dest paths
        :return: Boolean"""
        if not os.path.exists(self._src):
            print(Colour.WARNING + 'The source directory you entered does not exist!\n' + Colour.ENDC)
            return False
        if not os.path.exists(self._dest):
            print(Colour.WARNING + 'The destination directory you entered does not exist!\n' + Colour.ENDC)
            return False

        return True

    def seek(self, cwd):
        """
        Crawls through directory and places files within a specified date range in their specified category
        :param cwd: str
        :return: None
        """
        cwd += '/'
        os.chdir(cwd)   # change current working dir to 'cwd' arg
        src_files = os.listdir(cwd)
        if 'DS_Store' in src_files:
            src_files.remove('.DS_Store')
        src_folders = []

        for item in src_files:
            item_path = cwd + item

            if os.path.isfile(item_path):
                self.move(item_path)
            else:
                src_folders.append(item_path)

        for folder_path in src_folders:
            print(folder_path.split('/')[-1])
            self.seek(folder_path)

        return None

    def move(self, file):
        """
        Moves given file to new directory, as determined by its created date and the date range of a particular category
        :param file: str
        :return: None
        """
        file_ext = os.path.splitext(file)[1]
        if file_ext.lower() in self._file_types:
            date_arr = str(datetime.datetime.fromtimestamp(os.path.getmtime(file)))[:-9]
            if len(date_arr) > len('2014-02-10'):
                date_arr = date_arr[:-7]
            date_arr = date_arr.split('-')
            date_created = (int(date_arr[0]), int(date_arr[1]), int(date_arr[2]))

            for i, cat in enumerate(self._categories):
                date_range = cat['date_range']
                fcount = cat['fcount']
                dir_name = cat['dir_name']

                if date_range[0] <= date_created <= date_range[1]:

                    # make album dir
                    os.chdir(self._dest)
                    try:
                        os.makedirs(dir_name)
                    except OSError:
                        pass

                    new_fname = dir_name[2:] + '_%d%s' % (fcount, file_ext)

                    new_path = self._dest + '/' + dir_name + '/' + new_fname
                    if not os.path.isfile(new_path):
                        shutil.copy2(file, new_path)
                        print(str('\tCopied file ' + Colour.OKGREEN + '%s' + Colour.ENDC + ' to album ' + Colour.OKGREEN + '%s' + Colour.ENDC) % (new_fname, os.path.basename(dir_name)))

                        self._categories[i]['fcount'] += 1

        return None

    def run(self):
        """
        Runs script
        :return:
        """
        print(Colour.OKBLUE + '\nSMURFS HAVE BEGUN WORK ON YOUR PHOTOS!\n' + Colour.ENDC)

        if not self.test():
            return None

        self.get_albums(self._albums)
        self.seek(self._src)
        print(Colour.OKBLUE + '\nSMURFS ARE FINISHED!\n' + Colour.ENDC)
        return None

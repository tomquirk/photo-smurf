import os
import sys
import datetime

class Organise(object):
    def __init__(self):
        """Initialises data. Stores names for date intervals (tuples) in self._names
        """
        
        self._current_dir = ''
        self._dest_dir = ''
        self._names = {'c_wedding_renee':[(2015,10,27),(2015,10,27)],
                       'mum_peru':[(2014,8,1),(2014,9,3)]
                 }
    
    def move(self, src, dest):
        """Takes source folder, iterates through each nested object
           (folder or file) and moves each file to destination dir (created)
           
           move('path/to/src','path/to/dest') -> None
        """
        #havent incorporated dest yet
        str_src = src +'/'
        os.chdir(str(src))
        src = os.listdir(src)

        for i in src:
            if i.endswith('.jpg') or i.endswith('.JPG'):
                created = str(datetime.datetime.fromtimestamp(os.path.getctime(i)))[:-9].split('-')
                print(created)
                newdir =  created[0] + '-' + created[1] + '-' + created[2] +'/'
                date = (int(created[0]), int(created[1]), int(created[2]))
                print(i)
                for name in self._names:

                    if self._names[name][0] <= date <= self._names[name][1]:
                        if os.path.exists(name):
                            name += '/'
                            os.rename(str_src + str(i), str_src + name + str(i))
                        else:
                            os.makedirs(name)
                            name += '/'
                            os.rename(str_src + str(i), str_src + name + str(i))

                    elif os.path.exists(newdir):
                        os.rename(str_src + str(i), str_src + newdir + str(i))
                        
                    else:
                        os.makedirs(newdir)
                        os.rename(str_src + str(i), str_src + newdir + str(i)) 

x = Organise()

src = '/Users/Quirky/Pictures/test'
dest= '/Users/Quirky/Desktop'

x.move(src, dest)
    

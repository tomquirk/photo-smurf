from smurf import Smurf
import sys

if len(sys.argv) != 4:
    print('USAGE:\n\tpython smurf.py [src dir] [dest dir] [album filepath]')
else:
    pics = Smurf(sys.argv[1], sys.argv[2], sys.argv[3])
    pics.run()
# Photo Smurf

### A Date-based File Crawler that Beautifies your Photo Library
<img src="http://vignette1.wikia.nocookie.net/smurfs/images/9/92/Handy_Comic_Book.jpg/revision/latest?cb=20120920121205">

## Why?

> All my photos are unorganised, scattered across my computer/harddrive - help!

Sound familiar?

Simply tell these smurfs when you went on holidays i.e New Zealand between 27/01/2016 and 15/02/2016. Photo smurf will search your computer for any photo taken between specified dates and put them in folders representing albums!

## Usage

Create an _albums_ config file as described below

### CLI
```
python smurf.py [src_dir] [dest_dir] [album_config]
```

### GUI
Load everything and click `Go!`

### Standalone Module

1. `from smurf import Smurf`.
2. `my_smurf = Smurf(<src>, <dest>, <album_config>)`
3. `my_smurf.run()`

## The Album Config File

Start by creating a file i.e. 'albums.txt' within this directory. To specifiy an album within this file:

`[ALBUM_NAME] [FROM_DATE] [TO_DATE]`

- Separate each album with newline.
- Date formatting: DD/MM/YYYY
- Make sure your album name contains NO SPACES (because that's silly)!
- If your album only spans 1 day, you only need `FROM_DATE`

#### Example
> albums.txt

```
family_holiday 11/01/2015 28/01/2015
work_trip 08/02/2015 09/02/2015
```

# Todo
-   multi-threading
-   GUI

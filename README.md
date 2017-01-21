# Photo Smurf (alpha)

### A Date-based File Crawler that Beautifies your Photo Library
<img src="http://vignette1.wikia.nocookie.net/smurfs/images/9/92/Handy_Comic_Book.jpg/revision/latest?cb=20120920121205">

## Why?
You have a bunch of unorganised photos somewhere. You want to move these photos into folders that are grouped by date. 
For example, you went on a holiday to New Zealand between 27/01/2016 and 15/02/2016 - Photo smurf will find all the photos between that date and put them in a folder!

## Usage

1. Complete 'albums.txt' as described below
2. 

  ```
  python smurf.py [src_dir] [dest_dir] [album_config]
  ```
3. ...
4. Profit

Have a look at `smurf.py` if you want to use it within your own Python project.

### Creating an "Album"

Start by creating 'albums.txt' within this directory. Within this file:

`[ALBUM_NAME] [FROM_DATE] [TO_DATE]`

- Separate each album with newline.
- Date formatting: DD/MM/YYYY
- Make sure your album name contains NO SPACES (because thats silly)!
- If your album only spans 1 day, you only need `FROM_DATE`

#### Example
> albums.txt

`family_holiday 11/01/2015 28/01/2015`
`work_trip 08/02/2015 09/02/2015`

## Progression from Alpha
### Aim

To create a standalone Mac app with GUI 

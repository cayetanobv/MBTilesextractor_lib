Description
============
A little python library to take an mbtiles file and split it apart into a folder hierarchy of individual image tile files.

This project is the conversion in a little class library of the command line utility developed by Patrick Barry:
https://github.com/pbarry/MBTiles-extractor


Requirements
=============
- No external dependencies. This library only uses PSL (The Python Standard Library).

Usage
=======
Basic usage (*):


```
from mbtilesextractor import MBTilesExtractor

input_file = '/my_datafolder/my_file.mbtiles'

ex_mbt = MBTilesExtractor(input_file, overwrite=True)

ex_mbt.extractTiles()

```

(*) See lib/bootstrap.py

License
========
This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.  

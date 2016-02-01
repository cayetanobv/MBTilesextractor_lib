# MBTilesextractor library
## Description
A little python library to take an mbtiles file and split it apart into a folder hierarchy of individual image tile files (or pbf files for vector tiles).

This project is a improved class library version of the command line utility developed by Patrick Barry:
https://github.com/pbarry/MBTiles-extractor


## Requirements
- No external dependencies. This library only uses PSL (The Python Standard Library).

## Usage
Basic usage (*):


```python
from mbtilesextractor import MBTilesExtractor

input_file = '/source_folder/my_file.mbtiles'

# optional: if not dirname, same folder as input_file
dest_folder = '/dest_folder'

ex_mbt = MBTilesExtractor(input_file, dirname=dest_folder, overwrite=False)

result = ex_mbt.extractTiles()

print(result)

```

(*) See lib/bootstrap.py

## License
This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.  

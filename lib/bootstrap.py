# -*- coding: utf-8 -*-

from mbtilesextractor import MBTilesExtractor

input_file = '/source_folder/my_file.mbtiles'

# optional: if not dirname, same folder as input_file
dest_folder = '/dest_folder'

ex_mbt = MBTilesExtractor(input_file, dirname=dest_folder, overwrite=False)

result = ex_mbt.extractTiles()

print result

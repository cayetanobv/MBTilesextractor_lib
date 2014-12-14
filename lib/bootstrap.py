# -*- coding: utf-8 -*-

from mbtilesextractor import MBTilesExtractor

input_file = '/source_folder/example.mbtiles'

dest_folder = '/dest_folder'

ex_mbt = MBTilesExtractor(input_file, dirname=dest_folder, overwrite=True)

ex_mbt.extractTiles()
# -*- coding: utf-8 -*-

from mbtilesextractor import MBTilesExtractor

input_file = '/my_datafolder/my_file.mbtiles'

ex_mbt = MBTilesExtractor(input_file, overwrite=True)

ex_mbt.extractTiles()

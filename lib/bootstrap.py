# -*- coding: utf-8 -*-
#
#  Author: Cayetano Benavent, 2014.
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
# 

from mbtilesextractor import MBTilesExtractor

input_file = '/source_folder/my_file.mbtiles'

# optional: if not dirname, same folder as input_file
dest_folder = '/dest_folder'

ex_mbt = MBTilesExtractor(input_file, dirname=dest_folder, overwrite=False)

result = ex_mbt.extractTiles()

print result

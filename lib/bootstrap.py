# -*- coding: utf-8 -*-
#
#  Author: Cayetano Benavent, 2014-2016.
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
dest_folder = '/tmp'

ex_mbt = MBTilesExtractor(input_file, dirname=dest_folder, overwrite=True)

ex_mbt.extractTiles()

# get total nmber of tiles
nt = ex_mbt.ntiles

print('Done! Extracted %d tiles from file "%s" in local directory "%s"\n' % (nt, input_file, dest_folder))

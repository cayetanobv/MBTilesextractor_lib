# -*- coding: utf-8 -*-


import os
import sys
import sqlite3
import shutil


class MBTilesExtractor(object):
    
    def __init__(self, input_filename, dirname=None, overwrite=False):
        self.input_filename = input_filename
        
        if dirname:
            if not os.path.exists(dirname):
                print 'Destination folder does not exist...\n'
                exit()
            filename = os.path.basename(self.input_filename[0:self.input_filename.index('.')])
            self.dirname =  os.path.join(dirname,filename)

        else:
            self.dirname = self.input_filename[0:self.input_filename.index('.')]
            
        self.overwrite = overwrite
    
    def extractTiles(self):
        if not os.path.exists(self.input_filename):
            print 'MBTiles file does not exist...\n'
            exit()
        
        if os.path.exists(self.dirname):
            if self.overwrite == False:
                print 'Data directory exists...\n'
                exit()
            elif self.overwrite == True:
                shutil.rmtree(self.dirname)
                os.makedirs(self.dirname)
        else:
            os.makedirs(self.dirname)
        
        try:
            # Database connection boilerplate
            connection = sqlite3.connect(self.input_filename)
            cursor = connection.cursor()
            
            cursor.execute("SELECT value FROM metadata WHERE name='format'")
            img_format = cursor.fetchone()
            
            if img_format[0] == 'png':
                out_format = '.png'
            elif img_format[0] == 'jpg':
                out_format = '.jpg'
            
            # The mbtiles format helpfully provides a table that aggregates all necessary info
            cursor.execute("SELECT * FROM tiles")
            
            os.chdir(self.dirname)
            for row in cursor:
                self.__setDir(str(row[0]))
                self.__setDir(str(row[1]))
                output_file = open(str(row[2]) + out_format, 'wb')
                output_file.write(row[3])
                output_file.close()
                os.chdir('..')
                os.chdir('..')
            
            result = 'Extracted tiles from file "%s" in local directory "%s"\n' % (self.input_filename, self.dirname)
            
            print 'Done!\n', result
            return result
        
        except Exception as e:
            if os.path.exists(self.dirname):
                shutil.rmtree(self.dirname)
            result = 'Error: %s - %s' % (e.message, e.args)
            print result
            return result
    
    def __safeMakeDir(self, dir_path):
        if os.path.exists(dir_path):
            return
        os.makedirs(dir_path)
    
    def __setDir(self, dir_path):
        self.__safeMakeDir(dir_path)
        os.chdir(dir_path)
    

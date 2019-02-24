#!/usr/bin/env python3

import os.path
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), ''))

import os, errno
import txt
import click

subfolders = ['docs', 'tests',] 
@click.command()
@click.option('--name', '-n')
def runApp(name):
    print(os.getcwd())
    if name == None:
        projektName = input('Projekt Name:')
    else:
        projektName = name
    folderCreator(projektName, subfolders)
    fileCreate(projektName)
    

def fileCreate(projektName):
    fileWriter( projektName + '/README.rst', txt=txt.readme_rst() )
    fileWriter (projektName + '/setup.py', txt=txt.setup_py() )
    fileWriter (projektName + '/.gitignore', txt=txt.gitignore_() )
    fileWriter (projektName + '/MANIFEST.in', txt=txt.manifest_in() )
    fileWriter (projektName + '/setup.cfg', txt=txt.setup_cfg() )
    fileWriter (projektName + '/' + projektName + '/__init__.py', txt= txt.init___py() )
    print('Files Createt')

def fileWriter(fname, txt=''):
   
    with open(fname, 'x') as f:
        f.write(txt)
        f.close

def folderCreator(name, subf):
    try:
        if os.path.isdir(name):
            i = input('folder alredy exists ...[Y] or [N] ') #need better text
            print(i)
            if not i == 'Y' or not i == 'y':
                print('Bye!!!')
                return
        else:
            os.makedirs(name)
            print('Main Folder Createt')

    except OSError as e:
        if e.errno !=errno.EEXIST:
            raise

    subf.append(name)
    for f in subf:
        os.makedirs(name + '/' + f + '/')
    print('Sub Folders Createt')

if __name__ == "__main__":
    runApp()
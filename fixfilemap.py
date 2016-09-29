#!/bin/python

from bs4 import BeautifulSoup
<<<<<<< HEAD
from lxml import etree
=======
>>>>>>> 56b9d9cdd233a7d0f1547e599431de1256286c8d
from os import path, chdir
from sys import version_info

homedir = path.expanduser('~')
importdir = path.join(homedir, 'Desktop/import')

if version_info.major > 2:
<<<<<<< HEAD
    raise SystemExit('Use Python 2.')

# tests
try:
    chdir(importdir)
=======
	raise SystemExit('Use Python 2.')

# tests
try:
	chdir(importdir)
>>>>>>> 56b9d9cdd233a7d0f1547e599431de1256286c8d
except:
    raise SystemExit('Create /Desktop/import')

try:
    with open('filemap.xml','r') as f:
		filemap = f.read()
except:
    raise SystemExit('Cannot open filemap.xml')

# functions to create/add ishfield
def ishmaker(name,level,string):
    ishfield = soup.new_tag('ishfield')
    ishfield['name'] = name
    ishfield['level'] = level
    ishfield['xml:space'] = 'preserve' # new to Trisoft 11
    ishfield.string = string
    return ishfield

def addishfield(soup,ish,ishfield):
    last = ish('ishfield')[2]
    last.insert_after('\n')
    last.next_sibling.insert_after(ishfield)
    return soup

def getrootelement(filepath):
    with open(filepath,'r') as f:
        doc = f.read()
    root = etree.fromstring(doc).tag
    if root[:5] == 'gloss':
        root = root[:5] + ' ' + root[5:]
    return root.title()

# main
soup = BeautifulSoup(filemap,'html.parser')
ishes = soup('ishfields')

for ish in ishes:
    
    #ish.parent.parent['folderhasmixedcontent'] = 'False'

    # if we have less than 4 ishfield elements, the SDL conversion failed
    if len(ish('ishfield')) < 4:
	
<<<<<<< HEAD
        # if parent element's ishtype value is 'ISHIllustration' then we
        # need to add the ishfield for images, using Default as the string
        if ish.parent['ishtype'] == 'ISHIllustration':
            ish.parent.parent['targetfolder'] = "Import\\images"
            ishfield = ishmaker('FRESOLUTION','lng','Default')
            soup = addishfield(soup,ish,ishfield)

        # if parent element's ishtype value is 'ISHMasterDoc' then we have
        # a map, so use Map as the string
        elif ish.parent['ishtype'] == 'ISHMasterDoc':
            ish.parent.parent['targetfolder'] = "Import\\maps"
            root = getrootelement(ish.parent.parent['filepath'])
            ishfield = ishmaker('FMASTERTYPE','logical',root)
            soup = addishfield(soup,ish,ishfield)
		
        # if parent element's ishtype value is 'ISHModule' then we have a
        # normal topic. Open the file referenced via 'filepath' attribute
        # and determine it's topic type
        elif ish.parent['ishtype'] == 'ISHModule':
            ish.parent.parent['targetfolder'] = "Import\\topics"
            root = getrootelement(ish.parent.parent['filepath'])
            ishfield = ishmaker('FMODULETYPE','logical',root)
            soup = addishfield(soup,ish,ishfield)
		
# Use Default as FRESOLUTION value
for ish in soup('ishfield',{'name':'FRESOLUTION'}):
    ish.string = "Default"
=======
		# if parent element's ishtype value is 'ISHIllustration' then we
		# need to add the ishfield for images, using Default as the string
		if ish.parent['ishtype'] == 'ISHIllustration':
			ish.parent.parent['targetfolder'] = "Import\\images"
			ishfield = ishmaker('FRESOLUTION','lng','Default')
			soup = addishfield(soup,ish,ishfield)

		# if parent element's ishtype value is 'ISHMasterDoc' then we have
		# a map, so use Map as the string
		elif ish.parent['ishtype'] == 'ISHMasterDoc':
			ish.parent.parent['targetfolder'] = "Import\\maps"
			ishfield = ishmaker('FMASTERTYPE','logical','Map')
			soup = addishfield(soup,ish,ishfield)
		
		# if parent element's ishtype value is 'ISHUnknown' then we have a
		# topic.xml file, requiring no action
		elif ish.parent['ishtype'] == 'ISHUnknown':
			print "Ignoring %s" % ish.parent.parent['filepath']
			pass

		# if parent element's ishtype value is 'ISHModule' then we have a
		# normal topic. Open the file referenced via 'filepath' attribute
		# and determine it's topic type
		elif ish.parent['ishtype'] == 'ISHModule':
			ish.parent.parent['targetfolder'] = "Import\\topics"
			filename = ish.parent.parent['filepath']

			with open(filename,'r') as f:
				doc = f.read()
			doc = doc.decode("utf-16")
			docsoup = BeautifulSoup(doc,'html.parser')
			ttype = gettype(docsoup)
			ishfield = ishmaker('FMODULETYPE','logical',ttype)
			soup = addishfield(soup,ish,ishfield)
>>>>>>> 56b9d9cdd233a7d0f1547e599431de1256286c8d

# Use Default as FRESOLUTION value
for ish in soup('ishfield',{'name':'FRESOLUTION'}):
	ish.string = "Default"

# write changes to file
content = str(soup)
with open('filemap.xml','w') as out:
    out.write(content)

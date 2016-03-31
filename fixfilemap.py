#!/bin/python

from bs4 import BeautifulSoup
from os import path, chdir
from sys import version_info

homedir = path.expanduser('~')
importdir = path.join(homedir, 'Desktop/import')

if version_info.major > 2:
	raise SystemExit('Use Python 2.')

# tests
try:
	chdir(importdir)
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
	ishfield.string = string
	return ishfield

def addishfield(soup,ish,ishfield):
	last = ish('ishfield')[2]
	last.insert_after('\n')
	last.next_sibling.insert_after(ishfield)
	return soup

def gettype(soup):
	if soup.title.parent.name == 'concept':
		string = 'Concept'
	elif soup.title.parent.name == 'task':
		string = 'Task'
	elif soup.title.parent.name == 'reference':
		string = 'Reference'
	else:
		raise SystemExit('Topic type error: %s' % str(soup.title.string))
	return string
	
# main
soup = BeautifulSoup(filemap,'html.parser')
ishes = soup('ishfields')

for ish in ishes:
	# if we have less than 4 ishfield elements, the SDL conversion failed
	if len(ish('ishfield')) < 4:
	
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

# Use Default as FRESOLUTION value
for ish in soup('ishfield',{'name':'FRESOLUTION'}):
	ish.string = "Default"

# write changes to file
content = str(soup)
with open('filemap.xml','w') as out:
	out.write(content)

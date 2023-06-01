#!/usr/bin/python3

import sys
import os
import xml.etree.ElementTree as ET
from dateutil import parser
import datetime

dir = str(sys.argv[1])
metadataExtension = '.xmp'
mediaExtensions = ['jpg', 'jpeg', 'mpg', 'mpeg', 'mp4', 'mov', '3gp', 'm4v', 'dng', 'png']
tagSelector = 'DateCreated'
debug = True
modifiedCount = 0
noCandidatesCount = 0

if debug:
	print ('operating on directory:', dir)

for fname in os.listdir(dir):
	f = os.path.join(dir, fname)
	osFile = os.path.splitext(fname)
	if os.path.isfile(f) and str(osFile[1]).lower() == metadataExtension.lower():
		
		tree = ET.parse(f)
		xmlTree = tree.getroot().iter()
		dateText = [item.text for item in xmlTree if tagSelector in item.tag ]
		try:
			dateTime = parser.parse(dateText[0])
			if debug:
				print('xmp found:', osFile[0], 'extracted date:', dateTime)
			candidates = [os.path.join(dir, osFile[0]+'.'+ext) for ext in mediaExtensions]
			mediaFileName = [fName for fName in candidates if os.path.isfile(fName.lower())]
			if mediaFileName:
				if debug:
					print('found matching media: ', mediaFileName[0])
				os.utime(mediaFileName[0], (dateTime.timestamp(), dateTime.timestamp()))
				modifiedCount += 1
			else:
				noCandidatesCount += 1
				
		except Exception as e:
			print("An exception occurred on", osFile, e)
print('Operation completed on', modifiedCount, 'file(s).')
print(noCandidatesCount, 'file(s) had no matching media')
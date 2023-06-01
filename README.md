# date_corrector.py

## A quick and dirty python script to modify the creation/modifed date for files exported from Apple Photos alongside XMP metadata.

When exporting images from Apple photos to be used in another photo manager (Synology photos in my case), some files were indexed with the wrong date. This is because Synology photos uses the modified date (mtime) of the files to build the library.

When exporting, Apple Photos updates the mtime to the current date. This is especially problematic for videos which usually do not contain metadata information.

This is a quick fix that changes the mtime/ctime based on the XMP metadata exported with the files, which should fix dates in Synology Photos, or maybe other photo managers.

## Prerequisites:
- Images/video etc. are exported from Apple Photos into a single directory with 'Export IPTC as XMP' selected

- dateutil installed using pip

## Usage:
date_corrector.py [photo directory]
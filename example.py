#!/usr/bin/python
Usage = """Default python script layout."""

from backuptools.classbackup import BackUpFolder
import os

__author__ = "Jonny Elliott"
__copyright__ = "Copyright 2011"
__credits__ =  ""
__license__ = "GPL"
__version__ = "0.0"
__maintainer__ = "Jonny Elliott"
__email__ = "jonnyelliott@mpe.mpg.de"
__status__ = "Prototype"

def main():

	# Define first:
	#	A. The master folder, todays date and make the directory
	#
	#		B. The folders I want to copy:
	#		
	#		1. ~/workspace
	#		2. ~/software
	#		3. ~/bin
	#
	#	C. Send it all to be backed up, either at gate or Bilbo

	# A.
	MasterFolder = BackUpFolder()
	MasterPath = "~/backups/%s" % (MasterFolder.getDate())
	MasterPath = os.path.expanduser(MasterPath)
	MasterFolder.setName(MasterPath)
	MasterFolder.makeMyself()

	# B.
	WorkSpace = BackUpFolder()
	WorkSpace.setName("%s" % os.path.expanduser("~/workspace"))
	WorkSpace.setBackUpPath("%s/%s" % (MasterPath,"workspace"))
	WorkSpace.makeReplica()

	Software = BackUpFolder()
	Software.setName("%s" % os.path.expanduser("~/software"))
        Software.setBackUpPath("%s/%s" % (MasterPath,"software"))
        Software.makeReplica()

	Bin = BackUpFolder()
	Bin.setName("%s" % os.path.expanduser("~/bin"))
        Bin.setBackUpPath("%s/%s" % (MasterPath,"bin"))
        Bin.makeReplica()

	# C.
	MasterFolder.sendMyself("jonny@ga-ws04:~/backups/merry/.")	


if __name__ == "__main__":
	main()
# Fri Dec 2 16:50:43 CET 2011

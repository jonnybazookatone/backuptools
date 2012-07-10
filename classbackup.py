#!/usr/bin/python
"""Folder class which is built specifically for copying themselves with a date appended.
use:
from backuptools.classbackup import BackUpFolder"""

import datetime, os, shutil, subprocess, sys

__author__ = "Jonny Elliott"
__copyright__ = "Copyright 2011"
__credits__ =  ""
__license__ = "GPL"
__version__ = "0.0"
__maintainer__ = "Jonny Elliott"
__email__ = "jonnyelliott@mpe.mpg.de"
__status__ = "Prototype"

def main():
	print __doc__

	#Test = BackUpFolder()
	#Test.setName(os.getcwd())
	#Test.setBackUpPath(os.getcwd())
	#Test.makeReplica()

# First define the backup folder class

class BackUpFolder(object):

	# Initialise the values it will have once created
	def __init__(self):
		self._Name = None
		self._Date = datetime.datetime.today().date()
		self._BackUpPath = "~/backups/"
		
	# Follow convention of C++
	def getDate(self):
		return self._Date

	def setName(self, name):
		self._Name = name

	def getName(self):
		return self._Name

	def setBackUpPath(self, bkuppath):
		self._BackUpPath = bkuppath

	def getBackUpPath(self):
		return self._BackUpPath

	def checkBackUps(self, numdel=4):

		backup_path = os.path.expanduser(self._BackUpPath)
		print "Backup path: %s" % backup_path
		backup_glob = os.listdir("%s" % backup_path)
		print "Found folders: %s" %  backup_glob
		if len(backup_glob) > numdel:
			print "Too many backups, deleting current selection"
			for bkdir in backup_glob:
				print "Deleting: %s/%s" % (backup_path, bkdir)
				shutil.rmtree("%s/%s" % (backup_path, bkdir))
		else:
			print "You have less than %d backups, no deletions" % numdel

	# Make itself if it does not exist
	def makeMyself(self):
		
		# Check the folder doesn't exist
		if not os.path.isdir(self._Name):
			print "I do not exist, making myself: %s" % (self._Name)
			os.mkdir(self._Name)
		else:
			print "I already exist, you cannot create me: %s" % (self._Name)
	
	# Make a copy of the folder, with a given name
	def makeReplica(self):
	
		# New backups will follow a dating convention

		destinationDIR = "%s" % (self._BackUpPath)
		print "Destination directory: %s" % destinationDIR

		# Check the output folder does not exist
		if not os.path.isdir(destinationDIR):
			print "Backing up directory."
			try:
				# try to copy, if it doesn't work give an error
				shutil.copytree(self._Name, destinationDIR)
				print "Folder backed up successfully."
			except IOError as (errno, strerror):
				print "###########################"
				print "Error, folder not backed up"
				print "###########################"
    				print "I/O error({0}): {1}".format(errno, strerror)
			except:
                                print "###########################"
                                print "Error, folder not backed up"
                                print "###########################"	
			   	print "Unexpected error:", sys.exc_info()[0]
				raise
	
		else:
			# print to the user if the folder already exists
			print "Folder already exists, you may have already backed up today."

	def sendMyself(self, recipient):

		# SCP protocol as it is easiest
		cmd = ["scp", "-r", self._Name, recipient]
		scp = subprocess.Popen(cmd).wait()
		
	def copyBackup(self, dest):
	  
		# Copy to another location
		backupdir = "%s_%s" % (self._BackUpPath,self._Date)
		dest = "%s/%s_%s" % (dest, self._Name)
	
		# Check the output folder does not exist
		if not os.path.isdir(destinationDIR):
			print "Backing up directory."
			try:
				# try to copy, if it doesn't work give an error
				shutil.copytree(self._Name, destinationDIR)
				print "Folder backed up successfully."
			except IOError as (errno, strerror):
				print "###########################"
				print "Error, folder not backed up"
				print "###########################"
    				print "I/O error({0}): {1}".format(errno, strerror)
			except:
                                print "###########################"
                                print "Error, folder not backed up"
                                print "###########################"	
			   	print "Unexpected error:", sys.exc_info()[0]
				raise
	
		else:
			# print to the user if the folder already exists
			print "Folder already exists, you may have already backed up today."
		
		
		shutil.copytree(self._Name, dest)

if __name__ == "__main__":
  
	# Test bed
  
	main()
# Fri Dec 2 15:21:08 CET 2011

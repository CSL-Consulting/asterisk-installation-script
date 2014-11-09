#!/usr/bin/env python
# -*- coding: utf-8 -*- 
#####################################################################
# Author: Cristian Segura L.                                        #
# Email: cristian+dot+segura+dot+lepe+arroba+dot+gmail+dot+com      #
# Creation Date: Sat nov 8 20:11:38 CLST 2014                       #
# Version: 0.1                                                      #
# License: GPL v2.0 (check LICENSE file)                            #
# Usage: Installation of Asterisk IP PBX                            #
# Dependencies:                                                     #
#  + Python 2.7                                                     #
#  + wget                                                           #
# Tested on :                                                       #
#  + Ubuntu Desktop 13.10 amd64                                     #
#####################################################################

import subprocess
import time
import datetime
import os


# Create working directory to download source code

nowDateTime = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
wrkDir = "%s-asterisk11-sources" % ( nowDateTime )

if not os.path.exists( wrkDir ):
	os.makedirs( wrkDir )
else:
	print "[+] ERROR: Cannot create directory %s" % (wrkDir)
	exit -1

#print str(os.path) + wrkDir
# print str(os.getcwd()) + '/' + wrkDir
print "[+] Changing to directory %s" % (wrkDir)
os.chdir( os.getcwd() + '/' + wrkDir )


# Downloading Files

baseURL = "http://downloads.asterisk.org/pub/telephony"

lAstDir = "asterisk"
lAstTgzFile = "asterisk-11-current.tar.gz"
lAstDownPath = baseURL + '/' + lAstDir + '/' + lAstTgzFile

lPriDir = "libpri"
lPriTgzFile = "libpri-1.4-current.tar.gz"
lPriDownPath = baseURL + '/' + lPriDir + '/' + lPriTgzFile



print ""
print "*****************************************************"
print "*                                                   *"
print "*   Downloading LIBPRI                              *"
print "*                                                   *"
print "*****************************************************"
print "[+]downloading file: %s using wget" % ( lPriTgzFile )
print ""
subprocess.call( ["wget", lPriDownPath] )

print ""
print "*****************************************************"
print "*                                                   *"
print "*   Downloading ASTERISK                            *"
print "*                                                   *"
print "*****************************************************"
print "[+]downloading file: %s using wget" % ( lAstTgzFile )
print ""
subprocess.call( ["wget", lAstDownPath] )



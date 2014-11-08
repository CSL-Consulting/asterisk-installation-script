#!/usr/bin/env python
# -*- coding: utf-8 -*- 
#####################################################################
# Author: Cristian Segura L.                                        #
# Email: cristian+dot+segura+dot+lepe+arroba+dot+gmail+dot+com      #
# Creation Date: Sat nov 8 20:11:38 CLST 2014                       #
# Version: 0.1                                                      #
# License: GPL v2.0 (check LICENSE file)                            #
# Usage: Installation of Asterisk IP PBX                            #
#####################################################################


import subprocess

#lstArch = [
#	"amd64", "x86_64", "i386", "i686"
#]
#
#lstPkgs = {
#	'amd64': 'mv nmap tcpdump gcc gcc-g++ ',
#	'x86_64': 'mv nmap tcpdump gcc gcc-g++ ',
#	'i386': 'mv nmap tcpdump gcc gcc-g++ ',
#	'i686': 'mv nmap tcpdump gcc gcc-g++ '
#}


#subprocess.call(
#	args,
#	*, 
#	stdin=None, 
#	stdout=None,
#	stderr=None,
#	shell=False
#)



fname = ""
baseURL = "http://downloads.asterisk.org/pub/telephony"

lPriDir = "libpri"
lPriTgzFile = "libpri-1.4-current.tar.gz"
lPriDownPath = baseURL + '/' + lPriDir + '/' + lPriTgzFile

lPriDir = "libpri"
lPriTgzFile = "libpri-1.4-current.tar.gz"
lPriDownPath = baseURL + '/' + lPriDir + '/' + lPriTgzFile

print "==================================================="
print "                                                   "
print "   Downloading LIBPRI                              "
print "                                                   "
print "==================================================="
print "[+]downloading file: %s using wget" % ( lPriDownPath )
subprocess.call( ["wget", lPriDownPath] )




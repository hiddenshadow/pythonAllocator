#!/usr/bin/python

import ConfigParser


def getValue(section, property):
	configParser = ConfigParser.RawConfigParser()
	configFilePath = r'config.cfg'
	configParser.read(configFilePath)
	value = configParser.get(section, property)
	# print 'section: '+section+', property: '+property+', value: '+value
	return value

def getIntValue(section, property):	
	value = int( getValue(section, property) )
	# print value
	return value

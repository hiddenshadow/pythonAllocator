#!/usr/bin/python

import ConfigParser


def getValue(section, property):
	configParser = ConfigParser.RawConfigParser()
	configFilePath = r'config.cfg'
	configParser.read(configFilePath)
	value = configParser.get(section, property)
	# print value
	return value

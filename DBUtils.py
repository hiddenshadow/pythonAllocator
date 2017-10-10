#!/usr/bin/python

import mysql.connector
import ConfigReader

def getConnection():
	host = ConfigReader.getValue('db', 'host')
	user = ConfigReader.getValue('db', 'user')
	password = ConfigReader.getValue('db', 'password')
	database = ConfigReader.getValue('db', 'database')
	port = ConfigReader.getValue('db', 'port')

	# print 'Getting DB Connection:'
	# print  'host = '+host
	# print  'user = '+user
	# print  'password = '+password
	# print  'database = '+database	

	conn = mysql.connector.connect(user=user, password=password, host=host, database=database, port=port)

	return conn;

def executeSelectQuery(query):
	try:
		conn = getConnection()
		cursor = conn.cursor()
		cursor.execute(query)
		res = cursor.fetchall()
		cursor.close()
		conn.close()
	except Exception, e:
		print ''+e
	finally:
		cursor.close()
		conn.close()
				
	
	return res

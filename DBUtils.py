#!/usr/bin/python

import mysql.connector
import ConfigReader

def getConnection():
	try:
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

		if conn is None:
			raise Exception("Unable to connect to db.")

	except Exception as e:
		raise e

	return conn


def executeSelectQuery(query):
	try:
		conn = getConnection()
		cursor = conn.cursor()		
		cursor.execute(query)
		res = cursor.fetchall()
	except Exception, e:
		print 'Exception while executing Select Query: '+str(query)
	finally:
		cursor.close()
		conn.close()
					
	return res


def executeUpdateQuery(query):
	try:
		conn = getConnection()
		cursor = conn.cursor(buffered=True)
		cursor.execute(query)
		conn.commit()
		print 'Rows affected: '+str(cursor.rowcount)
	except Exception, e:
		print 'Exception while executing Update Query: '+query
	finally:
		cursor.close()
		conn.close()				
	
	return
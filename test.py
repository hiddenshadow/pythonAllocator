#!/usr/bin/python

import DBUtils
import ConfigReader
import main

def insertWelcomeCalls(count):
	
	return


def testSelectQuery():
	role = ConfigReader.getValue('db', 'role')
	filterAgentsQuery = 'SELECT user_id, role_id FROM bima_user_role_permission WHERE user_id < 0 and role_id = '+role+' limit 10'

	res = DBUtils.executeSelectQuery(filterAgentsQuery)

	if res is None:
		print 'Result is None for '+filterAgentsQuery

	if ( len(res) == 0):
		print 'Zero results found for '+filterAgentsQuery

	print 'res: '
	for row in res:
		print 'user_id - '+ str(row[0]) +', role_id - '+ str(row[1])

def testGetRemCountForAgent():
	res = main.getRemCountForAgent(1, 20, 123)
	for row in res:
		print row

def testSetRemWelCalToAgent():
	agentId=1
	rem=1
	allocatingStatus=3
	main.setRemWelCalToAgent(agentId, rem, allocatingStatus)


# testSetRemWelCalToAgent()

# testSelectQuery()

# main.makeValidWelCalQry()

# testGetRemCountForAgent()
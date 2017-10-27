#!/usr/bin/python

import ConfigReader
import DBUtils

def getMultipleStatusQryStr():
	mulStatus = ConfigReader.getValue('allocation', 'welCalStatusToPick').split(',')
	qry = ''
	for status in mulStatus:
		qry = qry+' status='+status+' or'
	qry = qry[:-3]
	return qry

def makeValidWelCalQry(max):	
	qry = 'SELECT id FROM welcome_calls WHERE '
	qry = qry + getMultipleStatusQryStr()
	qry = qry + ' limit '+str(max)
	# print qry
	return qry

def getMaxValWelCal(max):
	# Get valid welcome_calls, where status=0 or status=4. [NEW, INCOMPLETE]
	validWelcomeCallsQuery = makeValidWelCalQry(max)
	valWelCal = DBUtils.executeSelectQuery(validWelcomeCallsQuery)
	return valWelCal

def getRemCountForAgent(agentId, limit, pendStatus):
	qry = 'SELECT COUNT(*) FROM welcome_calls WHERE agent_id='+str(agentId)+' AND '+' status='+str(pendStatus)
	rem = DBUtils.executeSelectQuery(qry)
	# print 'rem='+str(rem)
	return (limit - int(rem[0][0]))

def setRemWelCalToAgent(agentId, rem, allocatingStatus):	
	qry = 'UPDATE welcome_calls SET agent_id='+str(agentId)+',status='+str(allocatingStatus)+' WHERE '	
	qry = qry + getMultipleStatusQryStr()
	qry = qry + ' limit '+str(rem)
	print qry
	DBUtils.executeUpdateQuery(qry)
	return


def getAgents():
	role = ConfigReader.getValue('db', 'role')

	# bima_customer, bima_user_role_permission.
	filterAgentsQuery = 'SELECT user_id, role_id FROM bima_user_role_permission WHERE user_id > 0 and role_id = '+role
	# print filterAgentsQuery

	validAgents = DBUtils.executeSelectQuery(filterAgentsQuery)
	return validAgents


def allocate():
	try:
		allocatingStatus=ConfigReader.getValue('allocation', 'allocatingStatus')
		assignlimit = ConfigReader.getIntValue( 'db', 'assignCount')

		agents = getAgents()

		if ( len(agents) == 0):
			print 'No valid Agents found: '+filterAgentsQuery
			return

		for agent in agents:
			print ''
			print 'agent - '+str(agent)
			agentId = agent[0]
			rem = (getRemCountForAgent(agentId,assignlimit,allocatingStatus))
			if (rem > 0) :
				print 'rem - '+str(rem)
				# In case no rows affected, we can check if there are any welcome calls remaining, else stop.
				setRemWelCalToAgent(agentId, rem, allocatingStatus)
			else:
				print 'No more assignment required for agent:'+str(agent)
			
	except Exception as e:
		print 'Exception while allocating'
		raise e
	finally:
		pass
	return


# allocate()
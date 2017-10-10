#!/usr/bin/python

import ConfigReader
import DBUtils

def getMultipleStatusQryStr():
	mulStatus = ConfigReader.getValue('allocation', 'welCalStatusToPick').split(',')
	qry = ''
	for status in mulStatus:
		qry = qry+' status='+status+' or'
	qry = qry[:-3]
	qry = qry
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


def allocate():
	try:
		role = ConfigReader.getValue('db', 'role')
		print  'role = '+role
		allocatingStatus=ConfigReader.getValue('allocation', 'allocatingStatus')
		assignlimit = int(ConfigReader.getValue( 'db', 'assignCount'))

		# bima_customer, bima_user_role_permission, No null values for user_id in bima_customer?
		filterAgentsQuery = 'SELECT user_id, role_id FROM bima_user_role_permission WHERE user_id > 0 and role_id = '+role
		# print filterAgentsQuery

		validAgents = DBUtils.executeSelectQuery(filterAgentsQuery)

		if ( len(validAgents) == 0):
			print 'No valid Agents found: '+filterAgentsQuery
			return

		for agent in validAgents:
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

def testSetup():
	updateQuery = 'UPDATE welcome_calls SET status=4,agent_id=100 where id=2'
	DBUtils.executeUpdateQuery(updateQuery)

# testSetup()

allocate()
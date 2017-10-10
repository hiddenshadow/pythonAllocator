#!/usr/bin/python

import ConfigReader
import DBUtils


role = ConfigReader.getValue('db', 'role')

print  'role = '+role

conn = DBUtils.getConnection()
conn2 = DBUtils.getConnection()
conn3 = DBUtils.getConnection()

# bima_customer, bima_user_role_permission
# No null values for user_id in bima_customer?
filterAgentsQuery = 'SELECT user_id, role_id FROM bima_user_role_permission WHERE user_id > 0 and role_id = '+role+' limit 10'

print filterAgentsQuery

agentsCursor = conn.cursor()

agentsCursor.execute(filterAgentsQuery)

# print 'agentsCursor: '
# for row in agentsCursor:
# 	print 'user_id - '+ str(row[0]) +', role_id - '+ str(row[1])	
		

# welcome_calls
# status=1 or status=4
# Get calls without agentId only.
validWelcomeCallsQuery = 'SELECT id FROM welcome_calls WHERE status = 1 or status = 4 '+' limit 10'

wcCursor = conn2.cursor()

wcCursor.execute(validWelcomeCallsQuery)


updateCursor = conn3.cursor()

count = 0
limit = ConfigReader.getValue( 'db', 'assignCount')
curAgent = agentsCursor.fetchone()
newStatus = 123

print 'Welcome Calls:'

for row in wcCursor:
	curCall = row
	curCallId = curCall[0]
	curAgentId = curAgent[0]
	newStatus = 123
	if (count < limit):
		print 'sss'
		updateQuery = 'UPDATE welcome_calls SET status=123, agent_id='+str(curAgentId)+' where id='+str(curCallId)
		print 'updateQuery - '+updateQuery
		updateCursor.execute(updateQuery)
		count=count+1
	else :
		curAgent = agentsCursor.fetchone()
		count = 0
		print curAgent

updateCursor = conn3.cursor()
updateQuery = 'UPDATE welcome_calls SET status=123,agent_id=1 where id=2'
updateCursor.execute(updateQuery)
conn3.commit();


wcCursor.close()
agentsCursor.close()
updateCursor.close()

conn.close()
conn2.close()
conn3.close()
filterAgentsQuery='SELECT '+customerTable+' FROM '+customerTable+' INNER JOIN '+roleTable + ' ON '+customerTable+''


SELECT Orders.OrderID, Customers.CustomerName, Orders.OrderDate
FROM Orders
INNER JOIN Customers ON Orders.CustomerID=Customers.CustomerID;

conn = mysql.connector.connect(user=user, password=password, host=host, database=database)

cur = conn.cursor()

res = cursor.execute()

	# print 'agentsCursor: '
	# for row in agentsCursor:
	# 	print 'user_id - '+ str(row[0]) +', role_id - '+ str(row[1])	

# +' limit 10'

# qry = 'SELECT id,agent_id,status FROM welcome_calls WHERE agent_id='+str(agentId)+' ORDER BY id DESC LIMIT '+str(limit)

# --------

		# # Get valid welcome_calls, where status=0 or status=4. [NEW, INCOMPLETE]
		# validWelcomeCallsQuery = makeValidWelCalQry(10)

		# valWelCal = DBUtils.executeSelectQuery(validWelcomeCallsQuery)

		# if ( len(valWelCal) == 0):
		# 	print 'No valid welcome calls found: '+validWelcomeCallsQuery
		# 	return

		# curAgentSeq = 0
		# agentCount = len(validAgents)
		# count = 0
		# limit = ConfigReader.getValue( 'db', 'assignCount')
		# curAgent = validAgents[curAgentSeq]
		# newStatus = ConfigReader.getValue( 'db', 'newStatus')

		# print 'Welcome Calls:'
		# for row in valWelCal:
		# 	curCall = row
		# 	curCallId = curCall[0]
		# 	curAgentId = curAgent[0]			
		# 	if (count < limit):	
		# 		updateQuery = 'UPDATE welcome_calls SET status='+newStatus+', agent_id='+str(curAgentId)+' where id='+str(curCallId)
		# 		print 'updateQuery - '+updateQuery
		# 		DBUtils.executeUpdateQuery(updateQuery)
		# 		count=count+1
		# 	else :
		# 		curAgentSeq = curAgentSeq + 1
		# 		curAgent = validAgents[curAgentSeq]
		# 		count = 0
		# 		print curAgent
filterAgentsQuery='SELECT '+customerTable+' FROM '+customerTable+' INNER JOIN '+roleTable + ' ON '+customerTable+''


SELECT Orders.OrderID, Customers.CustomerName, Orders.OrderDate
FROM Orders
INNER JOIN Customers ON Orders.CustomerID=Customers.CustomerID;

conn = mysql.connector.connect(user=user, password=password, host=host, database=database)

cur = conn.cursor()

res = cursor.execute()
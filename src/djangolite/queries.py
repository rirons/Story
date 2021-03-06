def getQuery(cname):

	query = f"""SELECT DISTINCT Name,CustomerRef_FullName, SUM(CAST(Cases AS FLOAT)) as TotalCases,Lbs,TxnDate,customfield5,customfield4,customfield6 from (
	SELECT DISTINCT
		quickbooks15_opensync2ff.dbo.ItemNonInventory.Name
		,quickbooks15_opensync2ff.dbo.ItemNonInventory.ListID
		,sum(quickbooks15_opensync2ff.dbo.SalesOrderLineDetail.Quantity) as Cases
		,SUM(CAST (quickbooks15_opensync2ff.dbo.SalesOrderLineDetail.Quantity AS float) * CAST (quickbooks15_opensync2ff.dbo.ItemNonInventory.CustomField12 AS float)) AS Lbs
		,quickbooks15_opensync2ff.dbo.ItemNonInventory.customfield4
		,quickbooks15_opensync2ff.dbo.ItemNonInventory.customfield5
		,quickbooks15_opensync2ff.dbo.ItemNonInventory.customfield6
		,CustomerRef_FullName
		
		,quickbooks15_opensync2ff.dbo.SalesOrder.TxnDate
	FROM (
		quickbooks15_opensync2ff.dbo.SalesOrder INNER JOIN quickbooks15_opensync2ff.dbo.SalesOrderLineDetail ON quickbooks15_opensync2ff.dbo.SalesOrder.TxnID = quickbooks15_opensync2ff.dbo.SalesOrderLineDetail.IDKey
		)
	INNER JOIN quickbooks15_opensync2ff.dbo.ItemNonInventory ON quickbooks15_opensync2ff.dbo.SalesOrderLineDetail.ItemRef_ListID = quickbooks15_opensync2ff.dbo.ItemNonInventory.ListID
	WHERE (
			CustomerRef_FullName = '{cname}' and
			(quickbooks15_opensync2ff.dbo.SalesOrder.TxnDate) >= '2/10/2020'
			AND (quickbooks15_opensync2ff.dbo.SalesOrder.TxnDate) <= '2/10/2020'
			)
			AND
			quickbooks15_opensync2ff.dbo.SalesOrderLineDetail.Quantity > 0
		AND LEFT(quickbooks15_opensync2ff.dbo.ItemNonInventory.Name, 3) NOT IN ('000')
	GROUP BY
	CustomerRef_FullName,
		Name
		,TxnDate
		,ListID
		,quickbooks15_opensync2ff.dbo.SalesOrderLineDetail.Quantity
		,quickbooks15_opensync2ff.dbo.ItemNonInventory.customfield4
		,quickbooks15_opensync2ff.dbo.ItemNonInventory.customfield5
		,quickbooks15_opensync2ff.dbo.ItemNonInventory.customfield6

	) as TotalCz
	Group by CustomerRef_FullName,Name,TxnDate,customfield4,customfield5,customfield6,Lbs
		"""
	return query


query2 = """
select itemtype,itemsize,itemprocess, sum(totalcases) as totalcasez from vproductinventory where invdate >= getdate()-1 and pickdate != '' group by itemsize,itemtype,itemprocess """

query3 = """ 
Select txndate, sum(totalcases) as totalcasez, sum(lbs) as totallbs, customfield4 as process,customfield5 as size,customfield6 as type from (

SELECT Name, SUM(CAST(Cases AS FLOAT)) as TotalCases,TxnDate,Lbs,customerref_fullname,customfield5,customfield4,customfield6 from (SELECT DISTINCT 
quickbooks15_opensync2ff.dbo.ItemNonInventory.Name,quickbooks15_opensync2ff.dbo.ItemNonInventory.ListID,quickbooks15_opensync2ff.dbo.SalesOrder.customerref_fullname,
sum(quickbooks15_opensync2ff.dbo.SalesOrderLineDetail.Quantity) as Cases,SUM(CAST (quickbooks15_opensync2ff.dbo.SalesOrderLineDetail.Quantity AS float) *
CAST (quickbooks15_opensync2ff.dbo.ItemNonInventory.CustomField12 AS float)) AS Lbs,quickbooks15_opensync2ff.dbo.ItemNonInventory.customfield4,quickbooks15_opensync2ff.dbo.ItemNonInventory.customfield5
,quickbooks15_opensync2ff.dbo.ItemNonInventory.customfield6,quickbooks15_opensync2ff.dbo.SalesOrder.TxnDate FROM (quickbooks15_opensync2ff.dbo.SalesOrder INNER JOIN quickbooks15_opensync2ff.dbo.SalesOrderLineDetail
ON quickbooks15_opensync2ff.dbo.SalesOrder.TxnID = quickbooks15_opensync2ff.dbo.SalesOrderLineDetail.IDKey)INNER JOIN quickbooks15_opensync2ff.dbo.ItemNonInventory ON
quickbooks15_opensync2ff.dbo.SalesOrderLineDetail.ItemRef_ListID = quickbooks15_opensync2ff.dbo.ItemNonInventory.ListID WHERE (quickbooks15_opensync2ff.dbo.SalesOrder.TxnDate) >= getdate() -1
 AND (quickbooks15_opensync2ff.dbo.SalesOrder.TxnDate) <= getdate() + 4 AND quickbooks15_opensync2ff.dbo.SalesOrderLineDetail.Quantity > 0
 AND LEFT(quickbooks15_opensync2ff.dbo.ItemNonInventory.Name, 3) NOT IN ('000') and quickbooks15_opensync2ff.dbo.itemnoninventory.name not like ('0%') GROUP BY Name,TxnDate,ListID,
 quickbooks15_opensync2ff.dbo.SalesOrderLineDetail.Quantity,quickbooks15_opensync2ff.dbo.SalesOrder.customerref_fullname,quickbooks15_opensync2ff.dbo.ItemNonInventory.customfield4
 ,quickbooks15_opensync2ff.dbo.ItemNonInventory.customfield5,quickbooks15_opensync2ff.dbo.ItemNonInventory.customfield6) as TotalCz Group by Name,TxnDate,customfield4,customfield5,customfield6,Lbs,customerref_fullname) as g
 group by txndate,customfield4,customfield5,customfield6"""
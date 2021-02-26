# 改

```sql
UPDATE metric_policy 
SET spl_statement = "* | stats count(Description) by _application,_host,_category,_service" 
WHERE
	id > 99 
```

# 删除
删除一行
DELETE FROM table WHERE id=1;
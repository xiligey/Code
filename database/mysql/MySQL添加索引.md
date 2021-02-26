- [1.添加PRIMARY KEY（主键索引）](#1添加primary-key主键索引)
- [2.添加UNIQUE(唯一索引)](#2添加unique唯一索引)
- [3.添加INDEX(普通索引)](#3添加index普通索引)
- [4.添加FULLTEXT(全文索引)](#4添加fulltext全文索引)
- [5.添加多列索引](#5添加多列索引)


### 1.添加PRIMARY KEY（主键索引） 
```sql
ALTER TABLE `table_name` ADD PRIMARY KEY ( `column` ) 
```

### 2.添加UNIQUE(唯一索引) 
```sql
ALTER TABLE `table_name` ADD UNIQUE ( 
`column` 
) 
```

### 3.添加INDEX(普通索引) 
```sql
ALTER TABLE `table_name` ADD INDEX index_name ( `column` ) 
```

### 4.添加FULLTEXT(全文索引) 
```sql
ALTER TABLE `table_name` ADD FULLTEXT ( `column`)
```

### 5.添加多列索引 

```sql
ALTER TABLE `table_name` ADD INDEX index_name ( `column1`, `column2`, `column3` )
```
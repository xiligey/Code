官网文档 [https://docs.influxdata.com/influxdb/v1.8/](https://docs.influxdata.com/influxdb/v1.8/)

## **使用help查看常用命令**

```sql
 > help
 Usage:
         connect <host:port>   connects to another node specified by host:port
         auth                  prompts for username and password
         pretty                toggles pretty print for the json format
         chunked               turns on chunked responses from server
         chunk size <size>     sets the size of the chunked responses.  Set to 0 to reset to the default chunked size
         use <db_name>         sets current database
         format <format>       specifies the format of the server responses: json, csv, or column
         precision <format>    specifies the format of the timestamp: rfc3339, h, m, s, ms, u or ns
         consistency <level>   sets write consistency level: any, one, quorum, or all
         history               displays command history
         settings              outputs the current settings for the shell
         clear                 clears settings such as database or retention policy.  run 'clear' for help
         exit/quit/ctrl+d      quits the influx shell
 
         show databases        show database names
         show series           show series information
         show measurements     show measurement information
         show tag keys         show tag key information
         show field keys       show field key information
 
         A full list of influxql commands can be found at:
         https://docs.influxdata.com/influxdb/latest/query_language/spec/
 > 
```

## **查看数据库**

```sql
 > show databases
 name: databases
 name
 ----
 _internal
 nmon_reports
 nmon2influxdb_log
 > 
```

## **删除数据库**

```sql
 > drop database nmon_reports
 > drop database nmon2influxdb_log
```

## **使用 or 切换数据库**

```sql
 > use nmon_reports
 Using database nmon_reports
```

## **查看所有表数据**

```sql
 > show measurements
 name: measurements
 name
 ----
 CPU_ALL
 ...
 > 
```

## **删除单表数据**

```sql
 > drop measurement CPU_ALL
```

## **查看所有表中的索引tag**

```sql
 > show tag keys;
 name: cpu
 tagKey
 ------
 cpu
 host
 
 name: disk
 tagKey
 ------
 device
 fstype
 host
 mode
 path
 
 name: diskio
 tagKey
 ------
 host
 name
```

## **查看表中有哪些字段是tag**

```sql
 > show tag keys from cpu;
 name: cpu
 tagKey
 ------
 cpu
 host
 > 
```

## **查看表中有哪些field字段**

```sql
 > show field keys from cpu;
 name: cpu
 fieldKey         fieldType
 --------         ---------
 usage_guest      float
 usage_guest_nice float
 usage_idle       float
 usage_iowait     float
 usage_irq        float
 usage_nice       float
 usage_softirq    float
 usage_steal      float
 usage_system     float
 usage_user       float
 > 
```

## **查询表中的点series**

```sql
 > show series from cpu;
 key
 ---
 cpu,cpu=cpu-total,host=QC_PREDEPL_API_02
 cpu,cpu=cpu-total,host=QC_PREDEPL_CMS-NGX-02
 cpu,cpu=cpu-total,host=QC_PREDEPL_Mongo_Mysql_02
 cpu,cpu=cpu-total,host=QC_PREDEPL_Redis_Memcache_02
 cpu,cpu=cpu-total,host=locust01
 cpu,cpu=cpu-total,host=locust02
```

## **查询单表10条数据**

```sql
 > select * from CPU_ALL limit 10
 name: CPU_ALL
 time                host                  name   value
 ----                ----                  ----   -----
 1551694907000000000 qc_predepl_cms-ngx-02 CPUs   4
 1551694907000000000 qc_predepl_cms-ngx-02 Idle%  96.9
 1551694907000000000 qc_predepl_cms-ngx-02 Steal% 0
 1551694907000000000 qc_predepl_cms-ngx-02 Sys%   0.9
 1551694907000000000 qc_predepl_cms-ngx-02 User%  0.7
 1551694907000000000 qc_predepl_cms-ngx-02 Wait%  1.5
 1551694910000000000 qc_predepl_cms-ngx-02 CPUs   4
 1551694910000000000 qc_predepl_cms-ngx-02 Idle%  99.7
 1551694910000000000 qc_predepl_cms-ngx-02 Steal% 0
 1551694910000000000 qc_predepl_cms-ngx-02 Sys%   0.1
 > 
```

## **查询表中最大的值**

```sql
 > select max(*) from CPU_ALL
 name: CPU_ALL
 time                max_value
 ----                ---------
 1551695447000000000 100
 > 
```

## **设置时间显示格式**

在influxDB的CLI界面执行`precision rfc3339`即可，但是显示是UTC的时区，与中国时区差了8个小时，需要在查询语句的最后加上`tz('Asia/Shanghai')`，这样查询的时间才是纠正为中国时区显示。

```sql
 > precision rfc3339
 
 > select * from CPU_ALL where time >= '2018-11-23 14:30:39' and time <= '2019-11-23 14:32:32' limit 10
 
 name: CPU_ALL
 time                 host                  name   value
 ----                 ----                  ----   -----
 2019-03-04T10:21:47Z qc_predepl_cms-ngx-02 CPUs   4
 2019-03-04T10:21:47Z qc_predepl_cms-ngx-02 Idle%  96.9
 2019-03-04T10:21:47Z qc_predepl_cms-ngx-02 Steal% 0
 2019-03-04T10:21:47Z qc_predepl_cms-ngx-02 Sys%   0.9
 2019-03-04T10:21:47Z qc_predepl_cms-ngx-02 User%  0.7
 2019-03-04T10:21:47Z qc_predepl_cms-ngx-02 Wait%  1.5
 2019-03-04T10:21:50Z qc_predepl_cms-ngx-02 CPUs   4
 2019-03-04T10:21:50Z qc_predepl_cms-ngx-02 Idle%  99.7
 2019-03-04T10:21:50Z qc_predepl_cms-ngx-02 Steal% 0
 2019-03-04T10:21:50Z qc_predepl_cms-ngx-02 Sys%   0.1
 > 
 
 > select * from CPU_ALL where time >= '2018-11-23 14:30:39' and time <= '2019-11-23 14:32:32' limit 10 tz('Asia/Shanghai')
 name: CPU_ALL
 time                      host                  name   value
 ----                      ----                  ----   -----
 2019-03-04T18:21:47+08:00 qc_predepl_cms-ngx-02 CPUs   4
 2019-03-04T18:21:47+08:00 qc_predepl_cms-ngx-02 Idle%  96.9
 2019-03-04T18:21:47+08:00 qc_predepl_cms-ngx-02 Steal% 0
 2019-03-04T18:21:47+08:00 qc_predepl_cms-ngx-02 Sys%   0.9
 2019-03-04T18:21:47+08:00 qc_predepl_cms-ngx-02 User%  0.7
 2019-03-04T18:21:47+08:00 qc_predepl_cms-ngx-02 Wait%  1.5
 2019-03-04T18:21:50+08:00 qc_predepl_cms-ngx-02 CPUs   4
 2019-03-04T18:21:50+08:00 qc_predepl_cms-ngx-02 Idle%  99.7
 2019-03-04T18:21:50+08:00 qc_predepl_cms-ngx-02 Steal% 0
 2019-03-04T18:21:50+08:00 qc_predepl_cms-ngx-02 Sys%   0.1
 > 
```

## **条件查询**

- 查询某时间下的数据

```sql
 > select * from CPU_ALL where "time" = 1551694910000000000
 name: CPU_ALL
 time                host                  name   value
 ----                ----                  ----   -----
 1551694910000000000 qc_predepl_cms-ngx-02 CPUs   4
 1551694910000000000 qc_predepl_cms-ngx-02 Idle%  99.7
 1551694910000000000 qc_predepl_cms-ngx-02 Steal% 0
 1551694910000000000 qc_predepl_cms-ngx-02 Sys%   0.1
 1551694910000000000 qc_predepl_cms-ngx-02 User%  0.2
 1551694910000000000 qc_predepl_cms-ngx-02 Wait%  0
 > 
```

- 查询某个时间返回的数据，设置时区为上海时区

```sql
 > select * from CPU_ALL where time >= '2018-11-23 14:30:39' and time <= '2019-11-23 14:32:32' tz('Asia/Shanghai')
```

- 查询特定字段数据

```sql
 select * from table_name where "字段1" =~ /匹配值/
```

```sql
 > select * from CPU_All3 limit 10
 name: CPU_All3
 time                Cpus Idle% Steal% Sys% User% Wait% host
 ----                ---- ----- ------ ---- ----- ----- ----
 1551689409000000000 4    94.5  0      0.9  0.7   3.9   qc_predepl_cms-ngx-02
 1551689412000000000 4    99.8  0      0.2  0.1   0     qc_predepl_cms-ngx-02
 1551689415000000000 4    99.5  0      0    0.1   0.4   qc_predepl_cms-ngx-02
 1551689418000000000 4    99.4  0      0.1  0.1   0.4   qc_predepl_cms-ngx-02
 1551689421000000000 4    99.7  0      0.2  0.2   0     qc_predepl_cms-ngx-02
 1551689424000000000 4    99.7  0      0.1  0.1   0.2   qc_predepl_cms-ngx-02
 1551689427000000000 4    99.5  0      0.2  0.2   0.2   qc_predepl_cms-ngx-02
 1551689430000000000 4    99.7  0      0.2  0.2   0     qc_predepl_cms-ngx-02
 1551689433000000000 4    99.7  0      0.1  0.2   0.1   qc_predepl_cms-ngx-02
 1551689436000000000 4    99.8  0      0.1  0.1   0     qc_predepl_cms-ngx-02
 > 
 > 
 > SELECT * FROM "CPU_All3" WHERE time < now() - 5m and "Idle%" =~ /94/
 name: CPU_All3
 time                Cpus Idle% Steal% Sys% User% Wait% host
 ----                ---- ----- ------ ---- ----- ----- ----
 1551689409000000000 4    94.5  0      0.9  0.7   3.9   qc_predepl_cms-ngx-02
 1551694925000000000 4    94.8  0      3.5  1.3   0.4   qc_predepl_cms-ngx-02
 1551694937000000000 4    94.2  0      4.3  1.3   0.3   qc_predepl_cms-ngx-02
 > 
 > SELECT * FROM "CPU_All3" WHERE time < now() - 5m and "Idle%" =~ /94.5/
 name: CPU_All3
 time                Cpus Idle% Steal% Sys% User% Wait% host
 ----                ---- ----- ------ ---- ----- ----- ----
 1551689409000000000 4    94.5  0      0.9  0.7   3.9   qc_predepl_cms-ngx-02
 > 
 > 
 > SELECT * FROM "CPU_All3" WHERE time < now() - 5m and "Idle%" =~ /94.5/ and host =~ /qc_predepl_cms/
 name: CPU_All3
 time                Cpus Idle% Steal% Sys% User% Wait% host
 ----                ---- ----- ------ ---- ----- ----- ----
 1551689409000000000 4    94.5  0      0.9  0.7   3.9   qc_predepl_cms-ngx-02
 > 
```

## **倒序查询**

```sql
 > select * from CPU_ALL order by time desc limit 10 tz('Asia/Shanghai')
 name: CPU_ALL
 time                      host                  name   value
 ----                      ----                  ----   -----
 2019-03-04T18:31:44+08:00 qc_predepl_cms-ngx-02 Wait%  0.3
 2019-03-04T18:31:44+08:00 qc_predepl_cms-ngx-02 User%  0.1
 2019-03-04T18:31:44+08:00 qc_predepl_cms-ngx-02 Sys%   0.1
 2019-03-04T18:31:44+08:00 qc_predepl_cms-ngx-02 Steal% 0
 2019-03-04T18:31:44+08:00 qc_predepl_cms-ngx-02 Idle%  99.5
 2019-03-04T18:31:44+08:00 qc_predepl_cms-ngx-02 CPUs   4
 2019-03-04T18:31:41+08:00 qc_predepl_cms-ngx-02 Wait%  0
 2019-03-04T18:31:41+08:00 qc_predepl_cms-ngx-02 User%  0.1
 2019-03-04T18:31:41+08:00 qc_predepl_cms-ngx-02 Sys%   0.2
 2019-03-04T18:31:41+08:00 qc_predepl_cms-ngx-02 Steal% 0
```

## **Distinct去重查询**

```sql
 > SELECT COUNT(DISTINCT("level description")) FROM "h2o_feet"
 
 name: h2o_feet
 time                   count
 ----                   -----
 1970-01-01T00:00:00Z   4
```

## **Max()最大值、Min() 最小值**

```sql
 > select min(*) from CPU_ALL tz('Asia/Shanghai')
 name: CPU_ALL
 time                      min_value
 ----                      ---------
 2019-03-04T18:21:47+08:00 0
 > 
 > select max(*) from CPU_ALL tz('Asia/Shanghai')
 name: CPU_ALL
 time                      max_value
 ----                      ---------
 2019-03-04T18:30:47+08:00 100
 > 
```

## **Mean()查询平均值**

```sql
 > select mean(*) from CPU_ALL tz('Asia/Shanghai')
 name: CPU_ALL
 time                      mean_value
 ----                      ----------
 1970-01-01T08:00:00+08:00 17.336166666666678
 > 
```

## MEDIAN() 中位数

```sql
> select median(*) from CPU_ALL tz('Asia/Shanghai')
name: CPU_ALL
time                      median_value
----                      ------------
1970-01-01T08:00:00+08:00 0.4
>
```

## SPREAD() 最小值与最大值之间的数值差距

```sql
> select spread(*) from CPU_ALL tz('Asia/Shanghai')
name: CPU_ALL
time                      spread_value
----                      ------------
1970-01-01T08:00:00+08:00 100
>
```
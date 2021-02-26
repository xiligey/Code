# 交付须知

平台版restapi相关配置需要根据最佳实践进行详细调整，默认配置文件的位置在aiops-restapi.jar 所在目录下的conf文件下application-prod.properties配置文件

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/e3bf3c28-8d84-4efc-a9f7-6f1515f1f958/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/e3bf3c28-8d84-4efc-a9f7-6f1515f1f958/Untitled.png)

如果是机械盘需要添加如下配置

index.merge.scheduler.max_thread_count=1

# ES 最佳部署配置说明-20191017

### **1.总览**

- 本文档用于介绍如何部署、配置 Elasticsearch，使得在大规模日志存储、处理场景下，尽可能地提升 ES 的写入、存储性能。

- 本文档主要分为以下几个部分，读者可以根据需求自行选取某些章节阅读：# 总览

- ES 介绍。简单介绍 ES 本身的功能、硬件资源的使用、以及运行时的部分行为特征。

- ES 部署硬件需求。介绍给定场景下最适合于 ES 的硬件需求和方案，包括不同的硬件可能造成何种不同的影响。

- ES 部署实例配置。主要介绍 ES 实例部署方案、配置，以及不同方案的影响。

- ES 日志索引配置。主要介绍 ES 索引 mapping 创建时的配置。

- 写入应用建议。主要介绍写入数据的应用程序应当如何调整，以实现最大的写入性能。

- 总结

- 上述的说明中的 第 3,4,5 节 是具体的 ES 配置说明。其中，通常*第5项*是可以完全由我们的产品应用来进行控制的，而*第3、4项*可能为由于客户环境约束而无法进行优化（比如使用的是客户的ES，则部署方面的配置优化将无法进行）。但是它们互不冲突、依赖，视情况优化即可。

- 本文档主要说明的是针对大规模日志写入场景的优化。

- 具体性能测试数据，请参考性能测试报告。

## 集群整体规划

- 实验环境不做要求
- 生产环境
    - master节点可根据实现情况申请，推荐8c16g, data节点至少16c64g, 硬盘最好SSD，单盘至少500g , negotiation node最好16c64g,硬盘不做要求
    - 最优：master(3个)+ negotiation node(N个)+data node(N个)
    - 中配：master(3个)+data node(N个)
    - 低配：master&data node(3个) 备注：master/data混部

### **[2.ES](http://2.ES) 运行特点介绍**

**ES 最初是作为一个线上通用搜索引擎来设计的，而后添加了一些实时计算的功能，总体上是为线上实时查询来服务的，其本身的设计初衷并不专注于数据存储。**

但是在我们的场景下，ES 单纯地被作为一个日志存储设施使用，未使用到其搜索功能，较少地使用了其查询功能。因此配置时主要针对写入性能，优化其吞吐量，降低对数据可用延迟的要求和查询性能的要求。

ES 的硬件资源使用方面，主要包含如下一些特征：

- 硬盘方面，主要以随机访问为主，批量读写较少。
- 内存方面，除需要一定基础的内存用于实例运行以外，总体内存占用取决于存储的索引数目、索引规模，一个实例的内存利用上界为 32G，更多内存配置没有意义（不会被用到）。
- CPU 方面，写入时的 cpu 占用相对较少，主要相关线程大都用于 IO；查询时的 cpu 占用相对写入而言更高一些。

数据特征对于 ES 的影响，目前发现的有以下几个方面：

- 索引规模。单个索引本身的规模会较大影响该索引的写入性能，因此分多个索引分别同时写入会有较好的性能。在索引中的数据达到一定规模以后，切换下一个索引进行写入（按天、按小时分割）。
- 数据相似度。在数据高度相似时，由于 ES 本身的压缩算法，会使得存储的数据量、索引的规模的增长速度大幅低于数据本身增长速度，因此写入较快；数据本身较为随机时，则使得存储、索引的量相对偏多，因而性能相对差一些。

### **[3.ES](http://3.ES) 硬件需求、配置**

**针对数据写入场景，硬盘的性能是主要瓶颈。**

**cpu、内存方面**：

- ES 实例建议部署在配置为 4核16G 以上的服务器上，cpu 核数与内存大小(GB) 的比例建议在 1:4 以上。
- 建议单个服务器配置不低于 8核32G。（测试环境）
- 建议单个服务器配置不低于 16核64G。（生产环境）

针对*硬盘*：

- 考虑到 ES 的硬盘访问主要以随机访问为主，因此 SSD 盘的性能将显著优于普通 HDD 硬盘。（测试时，普通 HDD 硬盘的性能显著优于 吞吐优化的 HDD 硬盘）
- 同等cpu、内存条件下，单机多硬盘的性能优于单个硬盘（比如两块 500G 的硬盘性能 会比 1块 1T 的硬盘性能好）

操作系统 IO 调度策略配置：

- 将操作系统的文件 IO 策略配置为 deadline 将优于默认值
- 配置方式：
- 执行以下命令，可查看操作系统当前某块设备的 IO 调度策略:
- 12345`>> cat` `/sys/block/<设备名>/queue/scheduler# [none] mq-deadline kyber# 表示当前系统策略为 none，此外还支持 mq-deadline、kyber 两种策略# 这个是 aws 上 centos 的调度策略列表，实际其它机器上可能会略有不同。但是 deadline 一类的策略应该是都有的。一般名叫 deadline`
- 以 root 权限执行以下命令（必须是 root 用户，不能是 sudo)，可以设置操作系统对某块设备的IO调度策略：
- 12345`>> echo` `mq-deadline > /sys/block/<硬盘设备名>/queue/scheduler# 上述命令中的策略名 mq-deadline 为 aws 上特有# 对于普通机器上，通常策略名是 deadline。# 运行 echo deadline > /sys/block/<硬盘设备名>/queue/scheduler 即可`
- 设置完成后可以再次查看确认。
- 不需要重启系统，但是可能需要重新登录、重启实例。
- 修改系统最大打开文件数
- `#并发连接数#echo "root soft nofile 65536"` `>> /etc/security/limits.conf#echo "root hard nofile 65536"` `>> /etc/security/limits.conf#echo "* soft nofile 65536"` `>> /etc/security/limits.conf#echo "* hard nofile 65536"` `>> /etc/security/limits.confecho -e "root soft nofile 65536\\nroot hard nofile 65536\\n* soft nofile 65536\\n* hard nofile 65536\\n* soft memlock unlimited\\n* hard memlock unlimited"` `>> /etc/security/limits.confsed -i 's#4096#65536#g'` `/etc/security/limits.d/20nproc.conf` `#临时设置方式 ulimit -n 65536ulimit -u 4096ulimit -l unlimited`
- 设置虚拟内存
- `sysctl -w vm.max_map_count=262144#验证sysctl vm.max_map_count`

### **[4.ES](http://4.ES) 实例部署配置**

总体原则：每个实例的内存最好在 8G 以上。在内存足够的前提下，尽可能地为每一块硬盘单独配置一个 ES data-node 实例。

同时将 master 节点与 data-node 节点分离。

config/elasticsearch.yml 主要需要设置的参数如下：

```
cluster.name: <cluster_name>
node.name: data-node-1
node.master: <true for master>
node.data: <true for data>
node.ingest: <false for data>
# 下面的目录应当配置到实例对应的硬盘上
path.data: /data2/elasticsearch-data/data
path.logs: /data2/elasticsearch-data/log
# 关闭内存 swap
bootstrap.memory_lock: true
# 单节点多实例参数需要启用如下参数,2或3取决于你单节点实例个数。如果只是单节点单实例，不需要设置下列参数
#node.max_local_storage_nodes: 2
# 同一机器上需配置不同的以下端口
http.port: 9201
transport.tcp.port: 9301
# 这里填写的是各个节点的 transport 地址、端口，可以全部写上，也可以只写master。尽可能写完整。
discovery.zen.ping.unicast.hosts: ["172.31.2.13:9300","172.31.2.4", "172.31.2.5", "172.31.2.6"]
# (master_eligible_nodes / 2) + 1
discovery.zen.minimum_master_nodes:2
http.cors.enabled: "true"
http.cors.allow-origin: "*"
# ES 6.X 版本
thread_pool:
write:
size: 16//cpu核数+1
queue_size: 15000
index:
size: 16//cpu核数+1
queue_size: 1000
```

**注：bootstrap.memory_lock 配置完成后可能需要调整操作系统的 ulimit 参数，方式是编辑 /etc/security/limits.conf，将 es 运行用户的 memlock 属性 (包括 hard 和 soft) 设置为 ulimited 或者 足够大。这个设置不需要重启系统，但是需要重新登录。**

config/jvm.options 中，主要调整 JVM 内存，根据实际情况填写就好。建议不低于 4G, 最佳配置是机器内存的一半。（不超过32G）

- `Xms32g`
- `Xmx32g`

```
## G1GC Configuration
# NOTE: G1GC is only supported on JDK version 10 or later.
# To use G1GC uncomment the lines below.
```

- `XX:+UseG1GC`
- `XX:MaxGCPauseMillis=50 //default:200ms`

### **注：启用es用户名密码认证参考链接**

https://blog.csdn.net/qq_27639777/article/details/98470844

### **5. 日志索引配置**

主要是关闭 norm 等解析操作，仅以 keyword 的形式存储文本数据，并且延长数据刷新、trans log 刷新时间，从而提高硬盘吞吐量。

**shard** 的数目需要根据实际情况而定，通常是和实例数目一致。若考虑横向扩展性，则应当比实例数目多 50%-100% 左右。

**replica** 的数目根据实际需求而定，默认是1

其余参数参考下面的配置即可。

除去业务相关的 mapping 配置外（比如时间格式等），建议创建 index 的 mapping 配置如下（curl 形式)：

```
curl -X PUT "localhost:9200/_template/<索引模板名>"` `-H 'Content-Type: application/json'` `-d'
{
"index_patterns": ["<索引名通配符，比如 log_index* >"],
"mappings": {
"doc": {
"dynamic_templates": [
{
"strings": {
"match_mapping_type": "string",
"mapping": {
"type": "keyword",
"norms": false
}
}
}
]
}
},
"settings"` `: {
"index.number_of_shards"` `: 12,//根据节点个数来分配主分片个数
"index.number_of_replicas": 1,
"index.refresh_interval": "30s",
//以下这些配置，不要初始化进去，根据实际情况调整
"index.translog.durability": "async",//default:request
"index.translog.flush_threshold_size": "512mb",//default:512mb
"index.translog.sync_interval": "60s",//default:5s
//下面这个配置项一般不要使用，如果node频繁离群，要优先解集群不稳定的问题：例如：网络，探活之类的
"index.unassigned.node_left.delayed_timeout":"1m"//default:1m
//如果是机械盘设置下面配置
"index.merge.scheduler.max_thread_count":1
}
}
'
```

### **6.写入应用建议**

总体上，对于应用方而言，影响写入性能较大的是索引的数目和规模，建议如下：

- 索引规模最好为当前索引下一个shard不超过40G，因此大规模写入一段时间后建议更换索引进行写入。
- 并行往多个索引写入性能比写入单个索引要好，因此建议同时往多个索引进行写入。单索引日增 T 级时，建议拆分成 3-5 个并行写入。
- 上述两条优化会使得索引数目大幅增加，主要影响的是 meta 数据的规模，占用内存较多。因此需要定期清理索引（合并、删除等等）。

由于 ES 查询支持索引通配符，因此上述两条优化对于查询使用的影响总体较小。

Meta 数据规模的问题，在我们的应用场景下，通常数据保存时间不会太长（3天/7天），因此 meta 数据的规模总体上是可控的。

### **7常规操作**

[Untitled](https://www.notion.so/e717a3593f93425fbdbc343f63535200)

### **8.插件**

- bigdesk 参考：https://blog.csdn.net/yelllowcong/article/details/78791975
- cerebro 参考：https://www.jianshu.com/p/433d821f9667
- esrally 基准测试： https://cloud.tencent.com/developer/article/1595636

### **9.总结**

ES 总体上是一个用于线上查询、分析、搜索业务的系统，作为存储设施而言其性能并不特别稳定可靠，其硬盘访问多以随机访问为主也验证了这一点，它并没有很好地利用到硬盘的吞吐效率。

因此在数据方面，我们一方面仅以 keyword 存储字符数据，减少分析时的cpu占用和最终存储的数据规模，另一方面是延长数据、log 刷新间隔，从而提高硬盘吞吐。

在实例配置方面，尽可能地以单机多磁盘、多实例的方式部署，并调整操作系统的相关调度策略，从而提高硬盘IO，并提高 cpu 和内存的利用率。
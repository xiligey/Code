import os

sdates = [
    "2019-05-11", "2019-05-12", "2019-05-13", "2019-05-14", "2019-05-15",
    "2019-05-16", "2019-05-17", "2019-05-18", "2019-05-19", "2019-05-20",
    "2019-05-21", "2019-05-22", "2019-05-23", "2019-05-24", "2019-05-25",
    "2019-05-26", "2019-05-27", "2019-05-28", "2019-05-29", "2019-05-30"
]


for sdate in sdates:
    print("sdate")
    print("start")
    command = """/usr/bin/spark-submit \
--master yarn \
--deploy-mode cluster \
--driver-memory 12g \
--executor-memory 10g \
--num-executors 16 \
--executor-cores 8 \
--class com.joomob.dmp.statistic.SlotDayData \
--conf spark.yarn.executor.memoryOverhead=4096 \
--conf spark.default.parallelism=200 \
--conf spark.speculation=false \
--conf spark.sql.shuffle.partitions=200 \
--conf spark.task.maxFailures=1 \
--conf spark.storage.blockManagerTimeoutIntervalMs=100000 \
--jars /home/www/dmp/chenxilin/mysql-connector-java.jar /home/www/dmp/chenxilin/batch-1.0-SNAPSHOT.jar %s""" % sdate
    os.system(command)
    print("end")

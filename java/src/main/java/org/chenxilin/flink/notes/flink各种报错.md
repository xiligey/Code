# 1、ERROR StatusLogger No log4j2 configuration file found. Using default configuration: logging only errors to the console. Set system property 'org.apache.logging.log4j.simplelog.StatusLogger.level' to TRACE to show Log4j2 internal initialization logging.

## 问题描述

在idea中运行Flink WordCount 批处理任务时报错：

ERROR StatusLogger No log4j2 configuration file found. Using default configuration: logging only errors to the console. Set system property 'org.apache.logging.log4j.simplelog.StatusLogger.level' to TRACE to show Log4j2 internal initialization logging.
## 解决方案

没有log4j2那就添加一个咯，命名为log4j2.xml，对应org.apache.logging.log4j.Logger
```xml
<?xml version="1.0" encoding="UTF-8"?>
<Configuration status="WARN">
	<Properties>
		<property name="log_level" value="info" />
		<Property name="log_dir" value="log" />
		<property name="log_pattern"
			value="[%d{yyyy-MM-dd HH:mm:ss.SSS}] [%p] - [%t] %logger - %m%n" />
		<property name="file_name" value="test" />
		<property name="every_file_size" value="100 MB" />
	</Properties>
	<Appenders>
		<Console name="Console" target="SYSTEM_OUT">
			<PatternLayout pattern="${log_pattern}" />
		</Console>
		<RollingFile name="RollingFile"
			filename="${log_dir}/${file_name}.log"
			filepattern="${log_dir}/$${date:yyyy-MM}/${file_name}-%d{yyyy-MM-dd}-%i.log">
			<ThresholdFilter level="DEBUG" onMatch="ACCEPT"
				onMismatch="DENY" />
			<PatternLayout pattern="${log_pattern}" />
			<Policies>
				<SizeBasedTriggeringPolicy
					size="${every_file_size}" />
				<TimeBasedTriggeringPolicy modulate="true"
					interval="1" />
			</Policies>
			<DefaultRolloverStrategy max="20" />
		</RollingFile>
 
		<RollingFile name="RollingFileErr"
			fileName="${log_dir}/${file_name}-warnerr.log"
			filePattern="${log_dir}/$${date:yyyy-MM}/${file_name}-%d{yyyy-MM-dd}-warnerr-%i.log">
			<ThresholdFilter level="WARN" onMatch="ACCEPT"
				onMismatch="DENY" />
			<PatternLayout pattern="${log_pattern}" />
			<Policies>
				<SizeBasedTriggeringPolicy
					size="${every_file_size}" />
				<TimeBasedTriggeringPolicy modulate="true"
					interval="1" />
			</Policies>
		</RollingFile>
	</Appenders>
	<Loggers>
		<Root level="${log_level}">
			<AppenderRef ref="Console" />
			<AppenderRef ref="RollingFile" />
			<appender-ref ref="RollingFileErr" />
		</Root>
	</Loggers>
</Configuration>
```

那么文件是有了，该放在哪里呢？

在sourceDirectory或者testSourceDirectory路径下

## 但因此引发第二个报错

org.apache.logging.log4j.core.config.ConfigurationException: No type attribute provided for component pattern
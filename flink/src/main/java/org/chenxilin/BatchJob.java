package org.chenxilin;

import org.apache.flink.api.common.functions.FlatMapFunction;
import org.apache.flink.api.java.DataSet;
import org.apache.flink.api.java.ExecutionEnvironment;
import org.apache.flink.api.java.operators.DataSource;
import org.apache.flink.api.java.tuple.Tuple2;
import org.apache.flink.util.Collector;

import static org.chenxilin.common.Const.SPACE;

/**
 * Flink WordCount 批处理
 *
 * @author chenxilin
 */
public class BatchJob {
    public static void main(String[] args) throws Exception {
        // 创建flink环境
        ExecutionEnvironment env = ExecutionEnvironment.getExecutionEnvironment();
        // 读取数据
        String inputPath = "hello.txt";
        DataSource<String> text = env.readTextFile(inputPath);
        // 数据转换和处理
        DataSet<Tuple2<String, Integer>> ds = text.flatMap(new LineSplitter()).groupBy(0).sum(1);
        // 打印结果(print方法内部已经调用execute方法，所以不用再调用)
        ds.print();
        env.execute();
    }

    static class LineSplitter implements FlatMapFunction<String, Tuple2<String, Integer>> {
        @Override
        public void flatMap(String line, Collector<Tuple2<String, Integer>> collector) {
            for (String word : line.split(SPACE)) {
                collector.collect(new Tuple2<>(word, 1));
            }
        }
    }

}

package org.chenxilin.basic.database;

import java.sql.*;
import java.util.Properties;

/**
 * @author chenxilin
 */
public class MysqlOperator {
    public Statement statement;

    public static void main(String[] args) throws SQLException {
        String url = "jdbc:mysql://localhost:3306/ilog?useSSL=false";
        String user = "root";
        String password = "666666";
        MysqlOperator myHelper = new MysqlOperator(url, user, password);
        ResultSet s = myHelper.query("select * from test");
        myHelper.printResultSet(s);

        myHelper.update("UPDATE `ilog`.`test` SET `name` = '丁二' WHERE `id` = '4'");

        myHelper.close();
    }

    public MysqlOperator(String url, String user, String password) {
        try {
            this.statement = connect(url, user, password).createStatement();

        } catch (Exception e) {
            System.out.println("连接失败");
            e.printStackTrace();
        }
    }

    /**
     * 连接数据库
     */
    public Connection connect(String url, String user, String password) throws Exception {
        Class.forName("com.mysql.jdbc.Driver");
        return DriverManager.getConnection(url, user, password);
    }

    public Connection connect(String url) throws Exception {
        Class.forName("com.mysql.jdbc.Driver");
        return DriverManager.getConnection(url);
    }

    public Connection connect(String url, Properties info) throws Exception {
        Class.forName("com.mysql.jdbc.Driver");
        return DriverManager.getConnection(url, info);
    }

    /**
     * 查询数据库
     */
    public ResultSet query(String sql) throws SQLException {
        return statement.executeQuery(sql);
    }

    /**
     * 打印ResultSet
     */
    private void printResultSet(ResultSet resultSet) throws SQLException {
        while (resultSet.next()) {
            System.out.println("----------");
            System.out.println(resultSet.getInt(1));
            System.out.println(resultSet.getString(2));
            System.out.println(resultSet.getString(3));
        }
    }

    /**
     * 更新数据库(包括insert、update、delete三种操作)
     */
    public void update(String sql) throws SQLException {
        statement.executeUpdate(sql);
    }

    /**
     * 关闭数据库连接
     */
    public void close() throws SQLException {
        statement.close();
    }
}

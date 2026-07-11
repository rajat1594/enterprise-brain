[Skip navigation links](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/jdbc/package-summary.html#skip-navbar-top "Skip navigation links")
  * [Overview](https://spark.apache.org/docs/latest/api/java/index.html)
  * Package
  * Class
  * [Deprecated](https://spark.apache.org/docs/latest/api/java/deprecated-list.html)
  * [Index](https://spark.apache.org/docs/latest/api/java/index-all.html)
  * [Help](https://spark.apache.org/docs/latest/api/java/help-doc.html#package)


  * Package: 
  * Description | 
  * [Related Packages](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/jdbc/package-summary.html#related-package-summary) | 
  * [Classes and Interfaces](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/jdbc/package-summary.html#class-summary)


SEARCH:
# Package org.apache.spark.sql.jdbc
* * *
package org.apache.spark.sql.jdbc
  * Related Packages
Package
Description
[org.apache.spark.sql](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/package-summary.html)
  * All Classes and InterfacesInterfacesClasses
Class
Description
[AggregatedDialect](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/jdbc/AggregatedDialect.html "class in org.apache.spark.sql.jdbc")
AggregatedDialect can unify multiple dialects into one virtual Dialect.
[DatabricksDialect](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/jdbc/DatabricksDialect.html "class in org.apache.spark.sql.jdbc")
[DB2Dialect](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/jdbc/DB2Dialect.html "class in org.apache.spark.sql.jdbc")
[DerbyDialect](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/jdbc/DerbyDialect.html "class in org.apache.spark.sql.jdbc")
[JdbcConnectionProvider](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/jdbc/JdbcConnectionProvider.html "class in org.apache.spark.sql.jdbc")
::DeveloperApi:: Connection provider which opens connection toward various databases (database specific instance needed).
[JdbcDialect](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/jdbc/JdbcDialect.html "class in org.apache.spark.sql.jdbc")
Developer API Encapsulates everything (extensions, workarounds, quirks) to handle the SQL dialect of a certain database or jdbc driver.
[JdbcDialects](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/jdbc/JdbcDialects.html "class in org.apache.spark.sql.jdbc")
Developer API Registry of dialects that apply to every new jdbc `org.apache.spark.sql.DataFrame`.
[JdbcSQLQueryBuilder](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/jdbc/JdbcSQLQueryBuilder.html "class in org.apache.spark.sql.jdbc")
The builder to build a single SELECT query.
[JdbcType](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/jdbc/JdbcType.html "class in org.apache.spark.sql.jdbc")
Developer API A database type definition coupled with the jdbc type needed to send null values to the database.
[JoinPushdownAliasGenerator](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/jdbc/JoinPushdownAliasGenerator.html "class in org.apache.spark.sql.jdbc")
[MsSqlServerDialect](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/jdbc/MsSqlServerDialect.html "class in org.apache.spark.sql.jdbc")
[MySQLDialect](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/jdbc/MySQLDialect.html "class in org.apache.spark.sql.jdbc")
[NoLegacyJDBCError](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/jdbc/NoLegacyJDBCError.html "interface in org.apache.spark.sql.jdbc")
Make the `classifyException` method throw out the original exception
[NoopDialect](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/jdbc/NoopDialect.html "class in org.apache.spark.sql.jdbc")
NOOP dialect object, always returning the neutral element.
[OracleDialect](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/jdbc/OracleDialect.html "class in org.apache.spark.sql.jdbc")
[PostgresDialect](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/jdbc/PostgresDialect.html "class in org.apache.spark.sql.jdbc")
[SnowflakeDialect](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/jdbc/SnowflakeDialect.html "class in org.apache.spark.sql.jdbc")
[TeradataDialect](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/jdbc/TeradataDialect.html "class in org.apache.spark.sql.jdbc")



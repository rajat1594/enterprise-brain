[ ![](https://spark.apache.org/images/spark-logo-rev.svg) ](https://spark.apache.org/)
  * [Download](https://spark.apache.org/downloads.html)
  * [ Libraries ](https://spark.apache.org/sql/)
    * [SQL and DataFrames](https://spark.apache.org/sql/)
    * [Spark Connect](https://spark.apache.org/spark-connect/)
    * [Spark Streaming](https://spark.apache.org/streaming/)
    * [pandas on Spark](https://spark.apache.org/pandas-on-spark/)
    * [MLlib (machine learning)](https://spark.apache.org/mllib/)
    * [GraphX (graph)](https://spark.apache.org/graphx/)
    * * * *
    * [Third-Party Projects](https://spark.apache.org/third-party-projects.html)
  * [ Documentation ](https://spark.apache.org/sql/)
    * [Latest Release](https://spark.apache.org/docs/latest/)
    * [Older Versions and Other Resources](https://spark.apache.org/documentation.html)
    * [Frequently Asked Questions](https://spark.apache.org/faq.html)
  * [Examples](https://spark.apache.org/examples.html)
  * [ Community ](https://spark.apache.org/sql/)
    * [Mailing Lists & Resources](https://spark.apache.org/community.html)
    * [Contributing to Spark](https://spark.apache.org/contributing.html)
    * [Improvement Proposals (SPIP)](https://spark.apache.org/improvement-proposals.html)
    * [Issue Tracker](https://issues.apache.org/jira/browse/SPARK)
    * [Powered By](https://spark.apache.org/powered-by.html)
    * [Project Committers](https://spark.apache.org/committers.html)
    * [Project History](https://spark.apache.org/history.html)
  * [ Developers ](https://spark.apache.org/sql/)
    * [Useful Developer Tools](https://spark.apache.org/developer-tools.html)
    * [Versioning Policy](https://spark.apache.org/versioning-policy.html)
    * [Release Process](https://spark.apache.org/release-process.html)
    * [Security](https://spark.apache.org/security.html)
  * [ GitHub ](https://spark.apache.org/sql/)
    * [spark](https://github.com/apache/spark)
    * [spark-connect-go](https://github.com/apache/spark-connect-go)
    * [spark-connect-rust](https://github.com/apache/spark-connect-rust)
    * [spark-connect-swift](https://github.com/apache/spark-connect-swift)
    * [spark-docker](https://github.com/apache/spark-docker)
    * [spark-kubernetes-operator](https://github.com/apache/spark-kubernetes-operator)
    * [spark-website](https://github.com/apache/spark-website)

  * [ Apache Software Foundation ](https://spark.apache.org/sql/)
    * [Apache Homepage](https://www.apache.org/)
    * [License](https://www.apache.org/licenses/)
    * [Sponsorship](https://www.apache.org/foundation/sponsorship.html)
    * [Thanks](https://www.apache.org/foundation/thanks.html)
    * [Event](https://www.apache.org/events/current-event)

# Spark SQL & DataFrames
**Spark SQL** is Apache Spark's module for working with structured data.
## Integrated
Seamlessly mix SQL queries with Spark programs.
Spark SQL lets you query structured data inside Spark programs, using either SQL or a familiar [DataFrame API](https://spark.apache.org/docs/latest/sql-programming-guide.html). Usable in Java, Scala, Python and R.
results = spark.sql(
"SELECT * FROM people")
names = results.map(lambda p: p.name)

Apply functions to results of SQL queries.
## Uniform data access
Connect to any data source the same way.
DataFrames and SQL provide a common way to access a variety of data sources, including Hive, Avro, Parquet, ORC, JSON, and JDBC. You can even join data across these sources.
spark.read.json("s3n://...")
.registerTempTable("json")
results = spark.sql(
"""SELECT *
FROM people
JOIN json ...""")

Query and join different data sources.
## Hive integration
Run SQL or HiveQL queries on existing warehouses.
Spark SQL supports the HiveQL syntax as well as Hive SerDes and UDFs, allowing you to access existing Hive warehouses.
![](https://spark.apache.org/images/sql-hive-arch.png)
Spark SQL can use existing Hive metastores, SerDes, and UDFs.
## Standard connectivity
Connect through JDBC or ODBC.
A server mode provides industry standard JDBC and ODBC connectivity for business intelligence tools.
![](https://spark.apache.org/images/jdbc.png)
Use your existing BI tools to query big data.
### Performance & scalability
Spark SQL includes a cost-based optimizer, columnar storage and code generation to make queries fast. At the same time, it scales to thousands of nodes and multi hour queries using the Spark engine, which provides full mid-query fault tolerance. Don't worry about using a different engine for historical data.
### Community
Spark SQL is developed as part of Apache Spark. It thus gets tested and updated with each Spark release.
If you have questions about the system, ask on the [Spark mailing lists](https://spark.apache.org/community.html#mailing-lists).
The Spark SQL developers welcome contributions. If you'd like to help out, read [how to contribute to Spark](https://spark.apache.org/contributing.html), and send us a patch!
### Getting started
To get started with Spark SQL:
  * [Download Spark](https://spark.apache.org/downloads.html). It includes Spark SQL as a module.
  * Read the [Spark SQL and DataFrame guide](https://spark.apache.org/docs/latest/sql-programming-guide.html) to learn the API.

[ Download Apache Spark
Includes Spark SQL ](https://spark.apache.org/downloads.html)
##### Latest News
  * [Spark 4.0.3 released](https://spark.apache.org/news/spark-4-0-3-released.html) (Jun 11, 2026)
  * [Spark 4.1.2 released](https://spark.apache.org/news/spark-4-1-2-released.html) (May 21, 2026)
  * [Preview release of Spark 4.2.0](https://spark.apache.org/news/spark-4-2-0-preview5-released.html) (May 01, 2026)
  * [Preview release of Spark 4.2.0](https://spark.apache.org/news/spark-4-2-0-preview4-released.html) (Apr 09, 2026)

[Archive](https://spark.apache.org/news/index.html)
[ ![](https://www.apache.org/events/current-event-234x60.png) ](https://www.apache.org/events/current-event.html)
[ Download Spark ](https://spark.apache.org/downloads.html)
Built-in Libraries:
  * [SQL and DataFrames](https://spark.apache.org/sql/)
  * [Spark Streaming](https://spark.apache.org/streaming/)
  * [MLlib (machine learning)](https://spark.apache.org/mllib/)
  * [GraphX (graph)](https://spark.apache.org/graphx/)

[Third-Party Projects](https://spark.apache.org/third-party-projects.html)
* * *
Apache Spark, Spark, Apache, the Apache feather logo, and the Apache Spark project logo are either registered trademarks or trademarks of The Apache Software Foundation in the United States and other countries. See guidance on use of Apache Spark [trademarks](https://spark.apache.org/trademarks.html). All other marks mentioned may be trademarks or registered trademarks of their respective owners. Copyright © 2018 The Apache Software Foundation, Licensed under the [Apache License, Version 2.0](https://www.apache.org/licenses/).

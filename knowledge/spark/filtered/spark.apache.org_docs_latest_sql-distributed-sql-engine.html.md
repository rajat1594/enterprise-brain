[ ![](https://spark.apache.org/images/spark-logo-rev.svg)](https://spark.apache.org/docs/latest/index.html)4.1.2
  * [Overview](https://spark.apache.org/docs/latest/index.html)
  * [Programming Guides](https://spark.apache.org/docs/latest/sql-distributed-sql-engine.html)
[Quick Start](https://spark.apache.org/docs/latest/quick-start.html) [RDDs, Accumulators, Broadcasts Vars](https://spark.apache.org/docs/latest/rdd-programming-guide.html) [SQL, DataFrames, and Datasets](https://spark.apache.org/docs/latest/sql-programming-guide.html) [Structured Streaming](https://spark.apache.org/docs/latest/streaming/index.html) [Spark Streaming (DStreams)](https://spark.apache.org/docs/latest/streaming-programming-guide.html) [MLlib (Machine Learning)](https://spark.apache.org/docs/latest/ml-guide.html) [GraphX (Graph Processing)](https://spark.apache.org/docs/latest/graphx-programming-guide.html) [SparkR (R on Spark)](https://spark.apache.org/docs/latest/sparkr.html) [PySpark (Python on Spark)](https://spark.apache.org/docs/latest/api/python/getting_started/index.html) [Declarative Pipelines](https://spark.apache.org/docs/latest/declarative-pipelines-programming-guide.html)
  * [API Docs](https://spark.apache.org/docs/latest/sql-distributed-sql-engine.html)
[Python](https://spark.apache.org/docs/latest/api/python/index.html) [Scala](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html) [Java](https://spark.apache.org/docs/latest/api/java/index.html) [R](https://spark.apache.org/docs/latest/api/R/index.html) [SQL, Built-in Functions](https://spark.apache.org/docs/latest/api/sql/index.html)
  * [Deploying](https://spark.apache.org/docs/latest/sql-distributed-sql-engine.html)
[Overview](https://spark.apache.org/docs/latest/cluster-overview.html) [Submitting Applications](https://spark.apache.org/docs/latest/submitting-applications.html) [Spark Standalone](https://spark.apache.org/docs/latest/spark-standalone.html) [YARN](https://spark.apache.org/docs/latest/running-on-yarn.html) [Kubernetes](https://spark.apache.org/docs/latest/running-on-kubernetes.html)
  * [More](https://spark.apache.org/docs/latest/sql-distributed-sql-engine.html)
[Configuration](https://spark.apache.org/docs/latest/configuration.html) [Monitoring](https://spark.apache.org/docs/latest/monitoring.html) [Tuning Guide](https://spark.apache.org/docs/latest/tuning.html) [Job Scheduling](https://spark.apache.org/docs/latest/job-scheduling.html) [Security](https://spark.apache.org/docs/latest/security.html) [Hardware Provisioning](https://spark.apache.org/docs/latest/hardware-provisioning.html) [Migration Guide](https://spark.apache.org/docs/latest/migration-guide.html) [Building Spark](https://spark.apache.org/docs/latest/building-spark.html) [Contributing to Spark](https://spark.apache.org/contributing.html) [Third Party Projects](https://spark.apache.org/third-party-projects.html)
  * 

###  [Spark SQL Guide](https://spark.apache.org/docs/latest/sql-programming-guide.html)[](https://spark.apache.org/docs/latest/sql-distributed-sql-engine.html#spark-sql-guide)
  * [ Getting Started ](https://spark.apache.org/docs/latest/sql-getting-started.html)
  * [ Data Sources ](https://spark.apache.org/docs/latest/sql-data-sources.html)
  * [ Performance Tuning ](https://spark.apache.org/docs/latest/sql-performance-tuning.html)
  * [ Distributed SQL Engine ](https://spark.apache.org/docs/latest/sql-distributed-sql-engine.html)
    * [ Running the Thrift JDBC/ODBC server ](https://spark.apache.org/docs/latest/sql-distributed-sql-engine.html#running-the-thrift-jdbcodbc-server)
    * [ Running the Spark SQL CLI ](https://spark.apache.org/docs/latest/sql-distributed-sql-engine.html#running-the-spark-sql-cli)
  * [ PySpark Usage Guide for Pandas with Apache Arrow ](https://spark.apache.org/docs/latest/sql-pyspark-pandas-with-arrow.html)
  * [ Migration Guide ](https://spark.apache.org/docs/latest/sql-migration-guide.html)
  * [ SQL Reference ](https://spark.apache.org/docs/latest/sql-ref.html)
  * [ Error Conditions ](https://spark.apache.org/docs/latest/sql-error-conditions.html)


# Distributed SQL Engine[](https://spark.apache.org/docs/latest/sql-distributed-sql-engine.html#distributed-sql-engine)
  * [Running the Thrift JDBC/ODBC server](https://spark.apache.org/docs/latest/sql-distributed-sql-engine.html#running-the-thrift-jdbcodbc-server)
  * [Running the Spark SQL CLI](https://spark.apache.org/docs/latest/sql-distributed-sql-engine.html#running-the-spark-sql-cli)


Spark SQL can also act as a distributed query engine using its JDBC/ODBC or command-line interface. In this mode, end-users or applications can interact with Spark SQL directly to run SQL queries, without the need to write any code.
## Running the Thrift JDBC/ODBC server[](https://spark.apache.org/docs/latest/sql-distributed-sql-engine.html#running-the-thrift-jdbcodbc-server)
The Thrift JDBC/ODBC server implemented here corresponds to the [`HiveServer2`](https://cwiki.apache.org/confluence/display/Hive/Setting+Up+HiveServer2) in built-in Hive. You can test the JDBC server with the beeline script that comes with either Spark or compatible Hive.
To start the JDBC/ODBC server, run the following in the Spark directory:

```
./sbin/start-thriftserver.sh

```

This script accepts all `bin/spark-submit` command line options, plus a `--hiveconf` option to specify Hive properties. You may run `./sbin/start-thriftserver.sh --help` for a complete list of all available options. By default, the server listens on localhost:10000. You may override this behaviour via either environment variables, i.e.:

```
export HIVE_SERVER2_THRIFT_PORT=<listening-port>
export HIVE_SERVER2_THRIFT_BIND_HOST=<listening-host>
./sbin/start-thriftserver.sh \
  --master <master-uri> \
  ...
```

or system properties:

```
./sbin/start-thriftserver.sh \
  --hiveconf hive.server2.thrift.port=<listening-port> \
  --hiveconf hive.server2.thrift.bind.host=<listening-host> \
  --master <master-uri>
  ...
```

Now you can use beeline to test the Thrift JDBC/ODBC server:

```
./bin/beeline

```

Connect to the JDBC/ODBC server in beeline with:

```
beeline> !connect jdbc:hive2://localhost:10000

```

Beeline will ask you for a username and password. In non-secure mode, simply enter the username on your machine and a blank password. For secure mode, please follow the instructions given in the [beeline documentation](https://cwiki.apache.org/confluence/display/Hive/HiveServer2+Clients).
Configuration of Hive is done by placing your `hive-site.xml`, `core-site.xml` and `hdfs-site.xml` files in `conf/`.
You may also use the beeline script that comes with Hive.
Thrift JDBC server also supports sending thrift RPC messages over HTTP transport. Use the following setting to enable HTTP mode as system property or in `hive-site.xml` file in `conf/`:

```
hive.server2.transport.mode - Set this to value: http
hive.server2.thrift.http.port - HTTP port number to listen on; default is 10001
hive.server2.http.endpoint - HTTP endpoint; default is cliservice

```

To test, use beeline to connect to the JDBC/ODBC server in http mode with:

```
beeline> !connect jdbc:hive2://<host>:<port>/<database>;transportMode=http;httpPath=<http_endpoint>

```

If you closed a session and do CTAS, you must set `fs.%s.impl.disable.cache` to true in `hive-site.xml`. See more details in [[SPARK-21067]](https://issues.apache.org/jira/browse/SPARK-21067).
## Running the Spark SQL CLI[](https://spark.apache.org/docs/latest/sql-distributed-sql-engine.html#running-the-spark-sql-cli)
To use the Spark SQL command line interface (CLI) from the shell:

```
./bin/spark-sql

```

For details, please refer to [Spark SQL CLI](https://spark.apache.org/docs/latest/sql-distributed-sql-engine-spark-sql-cli.html)

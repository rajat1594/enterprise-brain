[ ![](https://spark.apache.org/images/spark-logo-rev.svg)](https://spark.apache.org/docs/latest/index.html)4.1.2
  * [Overview](https://spark.apache.org/docs/latest/index.html)
  * [Programming Guides](https://spark.apache.org/docs/latest/sql-distributed-sql-engine-spark-sql-cli.html)
[Quick Start](https://spark.apache.org/docs/latest/quick-start.html) [RDDs, Accumulators, Broadcasts Vars](https://spark.apache.org/docs/latest/rdd-programming-guide.html) [SQL, DataFrames, and Datasets](https://spark.apache.org/docs/latest/sql-programming-guide.html) [Structured Streaming](https://spark.apache.org/docs/latest/streaming/index.html) [Spark Streaming (DStreams)](https://spark.apache.org/docs/latest/streaming-programming-guide.html) [MLlib (Machine Learning)](https://spark.apache.org/docs/latest/ml-guide.html) [GraphX (Graph Processing)](https://spark.apache.org/docs/latest/graphx-programming-guide.html) [SparkR (R on Spark)](https://spark.apache.org/docs/latest/sparkr.html) [PySpark (Python on Spark)](https://spark.apache.org/docs/latest/api/python/getting_started/index.html) [Declarative Pipelines](https://spark.apache.org/docs/latest/declarative-pipelines-programming-guide.html)
  * [API Docs](https://spark.apache.org/docs/latest/sql-distributed-sql-engine-spark-sql-cli.html)
[Python](https://spark.apache.org/docs/latest/api/python/index.html) [Scala](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html) [Java](https://spark.apache.org/docs/latest/api/java/index.html) [R](https://spark.apache.org/docs/latest/api/R/index.html) [SQL, Built-in Functions](https://spark.apache.org/docs/latest/api/sql/index.html)
  * [Deploying](https://spark.apache.org/docs/latest/sql-distributed-sql-engine-spark-sql-cli.html)
[Overview](https://spark.apache.org/docs/latest/cluster-overview.html) [Submitting Applications](https://spark.apache.org/docs/latest/submitting-applications.html) [Spark Standalone](https://spark.apache.org/docs/latest/spark-standalone.html) [YARN](https://spark.apache.org/docs/latest/running-on-yarn.html) [Kubernetes](https://spark.apache.org/docs/latest/running-on-kubernetes.html)
  * [More](https://spark.apache.org/docs/latest/sql-distributed-sql-engine-spark-sql-cli.html)
[Configuration](https://spark.apache.org/docs/latest/configuration.html) [Monitoring](https://spark.apache.org/docs/latest/monitoring.html) [Tuning Guide](https://spark.apache.org/docs/latest/tuning.html) [Job Scheduling](https://spark.apache.org/docs/latest/job-scheduling.html) [Security](https://spark.apache.org/docs/latest/security.html) [Hardware Provisioning](https://spark.apache.org/docs/latest/hardware-provisioning.html) [Migration Guide](https://spark.apache.org/docs/latest/migration-guide.html) [Building Spark](https://spark.apache.org/docs/latest/building-spark.html) [Contributing to Spark](https://spark.apache.org/contributing.html) [Third Party Projects](https://spark.apache.org/third-party-projects.html)
  * 

###  [Spark SQL Guide](https://spark.apache.org/docs/latest/sql-programming-guide.html)[](https://spark.apache.org/docs/latest/sql-distributed-sql-engine-spark-sql-cli.html#spark-sql-guide)
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


# Spark SQL CLI[](https://spark.apache.org/docs/latest/sql-distributed-sql-engine-spark-sql-cli.html#spark-sql-cli)
  * [Spark SQL Command Line Options](https://spark.apache.org/docs/latest/sql-distributed-sql-engine-spark-sql-cli.html#spark-sql-command-line-options)
  * [The hiverc File](https://spark.apache.org/docs/latest/sql-distributed-sql-engine-spark-sql-cli.html#the-hiverc-file)
  * [Path interpretation](https://spark.apache.org/docs/latest/sql-distributed-sql-engine-spark-sql-cli.html#path-interpretation)
  * [Supported comment types](https://spark.apache.org/docs/latest/sql-distributed-sql-engine-spark-sql-cli.html#supported-comment-types)
  * [Spark SQL CLI Interactive Shell Commands](https://spark.apache.org/docs/latest/sql-distributed-sql-engine-spark-sql-cli.html#spark-sql-cli-interactive-shell-commands)
  * [Examples](https://spark.apache.org/docs/latest/sql-distributed-sql-engine-spark-sql-cli.html#examples)


The Spark SQL CLI is a convenient interactive command tool to run the Hive metastore service and execute SQL queries input from the command line. Note that the Spark SQL CLI cannot talk to the Thrift JDBC server.
To start the Spark SQL CLI, run the following in the Spark directory:

```
./bin/spark-sql

```

Configuration of Hive is done by placing your `hive-site.xml`, `core-site.xml` and `hdfs-site.xml` files in `conf/`.
## Spark SQL Command Line Options[](https://spark.apache.org/docs/latest/sql-distributed-sql-engine-spark-sql-cli.html#spark-sql-command-line-options)
You may run `./bin/spark-sql --help` for a complete list of all available options.

```
CLI options:
 -d,--define <key=value>          Variable substitution to apply to Hive
                                  commands. e.g. -d A=B or --define A=B
    --database <databasename>     Specify the database to use
 -e <quoted-query-string>         SQL from command line
 -f <filename>                    SQL from files
 -H,--help                        Print help information
    --hiveconf <property=value>   Use value for given property
    --hivevar <key=value>         Variable substitution to apply to Hive
                                  commands. e.g. --hivevar A=B
 -i <filename>                    Initialization SQL file
 -S,--silent                      Silent mode in interactive shell
 -v,--verbose                     Verbose mode (echo executed SQL to the
                                  console)

```

## The hiverc File[](https://spark.apache.org/docs/latest/sql-distributed-sql-engine-spark-sql-cli.html#the-hiverc-file)
When invoked without the `-i`, the Spark SQL CLI will attempt to load `$HIVE_HOME/bin/.hiverc` and `$HOME/.hiverc` as initialization files.
## Path interpretation[](https://spark.apache.org/docs/latest/sql-distributed-sql-engine-spark-sql-cli.html#path-interpretation)
Spark SQL CLI supports running SQL from initialization script file(`-i`) or normal SQL file(`-f`), If path url don’t have a scheme component, the path will be handled as local file. For example: `/path/to/spark-sql-cli.sql` equals to `file:///path/to/spark-sql-cli.sql`. User also can use Hadoop supported filesystems such as `s3://<mys3bucket>/path/to/spark-sql-cli.sql` or `hdfs://<namenode>:<port>/path/to/spark-sql-cli.sql`.
## Supported comment types[](https://spark.apache.org/docs/latest/sql-distributed-sql-engine-spark-sql-cli.html#supported-comment-types)  
| Comment  | Example  |  
| --- | --- |  
| simple comment  |  `       -- This is a simple comment.         
       SELECT 1;   `  |  
| bracketed comment  |  `         /* This is a bracketed comment. */           
         SELECT 1;     `  |  
| nested bracketed comment  |  `         /*  This is a /* nested bracketed comment*/ .*/           
         SELECT 1;     `  |  
## Spark SQL CLI Interactive Shell Commands[](https://spark.apache.org/docs/latest/sql-distributed-sql-engine-spark-sql-cli.html#spark-sql-cli-interactive-shell-commands)
When `./bin/spark-sql` is run without either the `-e` or `-f` option, it enters interactive shell mode. Use `;` (semicolon) to terminate commands. Notice:
  1. The CLI use `;` to terminate commands only when it’s at the end of line, and it’s not escaped by `\\;`.
  2. `;` is the only way to terminate commands. If the user types `SELECT 1` and presses enter, the console will just wait for input.
  3. If the user types multiple commands in one line like `SELECT 1; SELECT 2;`, the commands `SELECT 1` and `SELECT 2` will be executed separately.
  4. If `;` appears within a SQL statement (not the end of the line), then it has no special meanings: 

```
-- This is a ; comment
SELECT ';' as a;

```

This is just a comment line followed by a SQL query which returns a string literal.

```
/* This is a comment contains ;
*/ SELECT 1;

```

However, if ‘;’ is the end of the line, it terminates the SQL statement. The example above will be terminated into `/* This is a comment contains ` and `*/ SELECT 1`, Spark will submit these two commands separated and throw parser error (`unclosed bracketed comment` and `Syntax error at or near '*/'`).

  
| Command  | Description  |  
| --- | --- |  
|  `quit` or `exit`  | Exits the interactive shell.  |  
| `!<command>`  | Executes a shell command from the Spark SQL CLI shell.  |  
| `dfs <HDFS dfs command>`  | Executes a HDFS [dfs command](https://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-hdfs/HDFSCommands.html#dfs) from the Spark SQL CLI shell.  |  
| `<query string>`  | Executes a Spark SQL query and prints results to standard output.  |  
| `source <filepath>`  | Executes a script file inside the CLI.  |  
## Examples[](https://spark.apache.org/docs/latest/sql-distributed-sql-engine-spark-sql-cli.html#examples)
Example of running a query from the command line:

```
./bin/spark-sql -e 'SELECT COL FROM TBL'

```

Example of setting Hive configuration variables:

```
./bin/spark-sql -e 'SELECT COL FROM TBL' --hiveconf hive.exec.scratchdir=/home/my/hive_scratch

```

Example of setting Hive configuration variables and using it in the SQL query:

```
./bin/spark-sql -e 'SELECT ${hiveconf:aaa}' --hiveconf aaa=bbb --hiveconf hive.exec.scratchdir=/home/my/hive_scratch
spark-sql> SELECT ${aaa};
bbb

```

Example of setting Hive variables substitution:

```
./bin/spark-sql --hivevar aaa=bbb --define ccc=ddd
spark-sql> SELECT ${aaa}, ${ccc};
bbb ddd

```

Example of dumping data out from a query into a file using silent mode:

```
./bin/spark-sql -S -e 'SELECT COL FROM TBL' > result.txt

```

Example of running a script non-interactively:

```
./bin/spark-sql -f /path/to/spark-sql-script.sql

```

Example of running an initialization script before entering interactive mode:

```
./bin/spark-sql -i /path/to/spark-sql-init.sql

```

Example of entering interactive mode:

```
./bin/spark-sql
spark-sql> SELECT 1;
1
spark-sql> -- This is a simple comment.
spark-sql> SELECT 1;
1

```

Example of entering interactive mode with escape `;` in comment:

```
./bin/spark-sql
spark-sql>/* This is a comment contains \\;
         > It won't be terminated by \\; */
         > SELECT 1;
1

```


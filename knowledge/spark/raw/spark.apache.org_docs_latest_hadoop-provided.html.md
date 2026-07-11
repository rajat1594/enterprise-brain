[ ![](https://spark.apache.org/images/spark-logo-rev.svg)](https://spark.apache.org/docs/latest/index.html)4.1.2
  * [Overview](https://spark.apache.org/docs/latest/index.html)
  * [Programming Guides](https://spark.apache.org/docs/latest/hadoop-provided.html)
[Quick Start](https://spark.apache.org/docs/latest/quick-start.html) [RDDs, Accumulators, Broadcasts Vars](https://spark.apache.org/docs/latest/rdd-programming-guide.html) [SQL, DataFrames, and Datasets](https://spark.apache.org/docs/latest/sql-programming-guide.html) [Structured Streaming](https://spark.apache.org/docs/latest/streaming/index.html) [Spark Streaming (DStreams)](https://spark.apache.org/docs/latest/streaming-programming-guide.html) [MLlib (Machine Learning)](https://spark.apache.org/docs/latest/ml-guide.html) [GraphX (Graph Processing)](https://spark.apache.org/docs/latest/graphx-programming-guide.html) [SparkR (R on Spark)](https://spark.apache.org/docs/latest/sparkr.html) [PySpark (Python on Spark)](https://spark.apache.org/docs/latest/api/python/getting_started/index.html) [Declarative Pipelines](https://spark.apache.org/docs/latest/declarative-pipelines-programming-guide.html)
  * [API Docs](https://spark.apache.org/docs/latest/hadoop-provided.html)
[Python](https://spark.apache.org/docs/latest/api/python/index.html) [Scala](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html) [Java](https://spark.apache.org/docs/latest/api/java/index.html) [R](https://spark.apache.org/docs/latest/api/R/index.html) [SQL, Built-in Functions](https://spark.apache.org/docs/latest/api/sql/index.html)
  * [Deploying](https://spark.apache.org/docs/latest/hadoop-provided.html)
[Overview](https://spark.apache.org/docs/latest/cluster-overview.html) [Submitting Applications](https://spark.apache.org/docs/latest/submitting-applications.html) [Spark Standalone](https://spark.apache.org/docs/latest/spark-standalone.html) [YARN](https://spark.apache.org/docs/latest/running-on-yarn.html) [Kubernetes](https://spark.apache.org/docs/latest/running-on-kubernetes.html)
  * [More](https://spark.apache.org/docs/latest/hadoop-provided.html)
[Configuration](https://spark.apache.org/docs/latest/configuration.html) [Monitoring](https://spark.apache.org/docs/latest/monitoring.html) [Tuning Guide](https://spark.apache.org/docs/latest/tuning.html) [Job Scheduling](https://spark.apache.org/docs/latest/job-scheduling.html) [Security](https://spark.apache.org/docs/latest/security.html) [Hardware Provisioning](https://spark.apache.org/docs/latest/hardware-provisioning.html) [Migration Guide](https://spark.apache.org/docs/latest/migration-guide.html) [Building Spark](https://spark.apache.org/docs/latest/building-spark.html) [Contributing to Spark](https://spark.apache.org/contributing.html) [Third Party Projects](https://spark.apache.org/third-party-projects.html)
  * 

# Using Spark's "Hadoop Free" Build[](https://spark.apache.org/docs/latest/hadoop-provided.html#using-sparks-hadoop-free-build)
Spark uses Hadoop client libraries for HDFS and YARN. Starting in version Spark 1.4, the project packages “Hadoop free” builds that lets you more easily connect a single Spark binary to any Hadoop version. To use these builds, you need to modify `SPARK_DIST_CLASSPATH` to include Hadoop’s package jars. The most convenient place to do this is by adding an entry in `conf/spark-env.sh`.
This page describes how to connect Spark to Hadoop for different types of distributions.
# Apache Hadoop[](https://spark.apache.org/docs/latest/hadoop-provided.html#apache-hadoop)
For Apache distributions, you can use Hadoop’s ‘classpath’ command. For instance:

```
### in conf/spark-env.sh ###

# If 'hadoop' binary is on your PATH
export SPARK_DIST_CLASSPATH=$(hadoop classpath)

# With explicit path to 'hadoop' binary
export SPARK_DIST_CLASSPATH=$(/path/to/hadoop/bin/hadoop classpath)

# Passing a Hadoop configuration directory
export SPARK_DIST_CLASSPATH=$(hadoop --config /path/to/configs classpath)
```

# Hadoop Free Build Setup for Spark on Kubernetes[](https://spark.apache.org/docs/latest/hadoop-provided.html#hadoop-free-build-setup-for-spark-on-kubernetes)
To run the Hadoop free build of Spark on Kubernetes, the executor image must have the appropriate version of Hadoop binaries and the correct `SPARK_DIST_CLASSPATH` value set. See the example below for the relevant changes needed in the executor Dockerfile:

```
### Set environment variables in the executor dockerfile ###

ENV SPARK_HOME="/opt/spark"  
ENV HADOOP_HOME="/opt/hadoop"  
ENV PATH="$SPARK_HOME/bin:$HADOOP_HOME/bin:$PATH"  
...  

#Copy your target hadoop binaries to the executor hadoop home   

COPY /opt/hadoop3  $HADOOP_HOME  
...

#Copy and use the Spark provided entrypoint.sh. It sets your SPARK_DIST_CLASSPATH using the hadoop binary in $HADOOP_HOME and starts the executor. If you choose to customize the value of SPARK_DIST_CLASSPATH here, the value will be retained in entrypoint.sh

ENTRYPOINT [ "/opt/entrypoint.sh" ]
...  
```


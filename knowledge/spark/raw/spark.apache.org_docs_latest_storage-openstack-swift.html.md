[ ![](https://spark.apache.org/images/spark-logo-rev.svg)](https://spark.apache.org/docs/latest/index.html)4.1.2
  * [Overview](https://spark.apache.org/docs/latest/index.html)
  * [Programming Guides](https://spark.apache.org/docs/latest/storage-openstack-swift.html)
[Quick Start](https://spark.apache.org/docs/latest/quick-start.html) [RDDs, Accumulators, Broadcasts Vars](https://spark.apache.org/docs/latest/rdd-programming-guide.html) [SQL, DataFrames, and Datasets](https://spark.apache.org/docs/latest/sql-programming-guide.html) [Structured Streaming](https://spark.apache.org/docs/latest/streaming/index.html) [Spark Streaming (DStreams)](https://spark.apache.org/docs/latest/streaming-programming-guide.html) [MLlib (Machine Learning)](https://spark.apache.org/docs/latest/ml-guide.html) [GraphX (Graph Processing)](https://spark.apache.org/docs/latest/graphx-programming-guide.html) [SparkR (R on Spark)](https://spark.apache.org/docs/latest/sparkr.html) [PySpark (Python on Spark)](https://spark.apache.org/docs/latest/api/python/getting_started/index.html) [Declarative Pipelines](https://spark.apache.org/docs/latest/declarative-pipelines-programming-guide.html)
  * [API Docs](https://spark.apache.org/docs/latest/storage-openstack-swift.html)
[Python](https://spark.apache.org/docs/latest/api/python/index.html) [Scala](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html) [Java](https://spark.apache.org/docs/latest/api/java/index.html) [R](https://spark.apache.org/docs/latest/api/R/index.html) [SQL, Built-in Functions](https://spark.apache.org/docs/latest/api/sql/index.html)
  * [Deploying](https://spark.apache.org/docs/latest/storage-openstack-swift.html)
[Overview](https://spark.apache.org/docs/latest/cluster-overview.html) [Submitting Applications](https://spark.apache.org/docs/latest/submitting-applications.html) [Spark Standalone](https://spark.apache.org/docs/latest/spark-standalone.html) [YARN](https://spark.apache.org/docs/latest/running-on-yarn.html) [Kubernetes](https://spark.apache.org/docs/latest/running-on-kubernetes.html)
  * [More](https://spark.apache.org/docs/latest/storage-openstack-swift.html)
[Configuration](https://spark.apache.org/docs/latest/configuration.html) [Monitoring](https://spark.apache.org/docs/latest/monitoring.html) [Tuning Guide](https://spark.apache.org/docs/latest/tuning.html) [Job Scheduling](https://spark.apache.org/docs/latest/job-scheduling.html) [Security](https://spark.apache.org/docs/latest/security.html) [Hardware Provisioning](https://spark.apache.org/docs/latest/hardware-provisioning.html) [Migration Guide](https://spark.apache.org/docs/latest/migration-guide.html) [Building Spark](https://spark.apache.org/docs/latest/building-spark.html) [Contributing to Spark](https://spark.apache.org/contributing.html) [Third Party Projects](https://spark.apache.org/third-party-projects.html)
  * 

# Accessing OpenStack Swift from Spark[](https://spark.apache.org/docs/latest/storage-openstack-swift.html#accessing-openstack-swift-from-spark)
Spark’s support for Hadoop InputFormat allows it to process data in OpenStack Swift using the same URI formats as in Hadoop. You can specify a path in Swift as input through a URI of the form `swift://container.PROVIDER/path`. You will also need to set your Swift security credentials, through `core-site.xml` or via `SparkContext.hadoopConfiguration`. The current Swift driver requires Swift to use the Keystone authentication method, or its Rackspace-specific predecessor.
# Configuring Swift for Better Data Locality[](https://spark.apache.org/docs/latest/storage-openstack-swift.html#configuring-swift-for-better-data-locality)
Although not mandatory, it is recommended to configure the proxy server of Swift with `list_endpoints` to have better data locality. More information is [available here](https://github.com/openstack/swift/blob/master/swift/common/middleware/list_endpoints.py).
# Dependencies[](https://spark.apache.org/docs/latest/storage-openstack-swift.html#dependencies)
The Spark application should include `hadoop-openstack` dependency, which can be done by including the `hadoop-cloud` module for the specific version of spark used. For example, for Maven support, add the following to the `pom.xml` file:

```
<dependencyManagement>
  ...
  <dependency>
    <groupId>org.apache.spark</groupId>
    <artifactId>hadoop-cloud_2.13</artifactId>
    <version>${spark.version}</version>
  </dependency>
  ...
</dependencyManagement>
```

# Configuration Parameters[](https://spark.apache.org/docs/latest/storage-openstack-swift.html#configuration-parameters)
Create `core-site.xml` and place it inside Spark’s `conf` directory. The main category of parameters that should be configured is the authentication parameters required by Keystone.
The following table contains a list of Keystone mandatory parameters. `PROVIDER` can be any (alphanumeric) name.  
| Property Name  | Meaning  | Required  |  
| --- | --- | --- |  
| `fs.swift.service.PROVIDER.auth.url`  | Keystone Authentication URL  | Mandatory  |  
| `fs.swift.service.PROVIDER.auth.endpoint.prefix`  | Keystone endpoints prefix  | Optional  |  
| `fs.swift.service.PROVIDER.tenant`  | Tenant  | Mandatory  |  
| `fs.swift.service.PROVIDER.username`  | Username  | Mandatory  |  
| `fs.swift.service.PROVIDER.password`  | Password  | Mandatory  |  
| `fs.swift.service.PROVIDER.http.port`  | HTTP port  | Mandatory  |  
| `fs.swift.service.PROVIDER.region`  | Keystone region  | Mandatory  |  
| `fs.swift.service.PROVIDER.public`  | Indicates whether to use the public (off cloud) or private (in cloud; no transfer fees) endpoints  | Mandatory  |  
For example, assume `PROVIDER=SparkTest` and Keystone contains user `tester` with password `testing` defined for tenant `test`. Then `core-site.xml` should include:

```
<configuration>
  <property>
    <name>fs.swift.service.SparkTest.auth.url</name>
    <value>http://127.0.0.1:5000/v2.0/tokens</value>
  </property>
  <property>
    <name>fs.swift.service.SparkTest.auth.endpoint.prefix</name>
    <value>endpoints</value>
  </property>
    <name>fs.swift.service.SparkTest.http.port</name>
    <value>8080</value>
  </property>
  <property>
    <name>fs.swift.service.SparkTest.region</name>
    <value>RegionOne</value>
  </property>
  <property>
    <name>fs.swift.service.SparkTest.public</name>
    <value>true</value>
  </property>
  <property>
    <name>fs.swift.service.SparkTest.tenant</name>
    <value>test</value>
  </property>
  <property>
    <name>fs.swift.service.SparkTest.username</name>
    <value>tester</value>
  </property>
  <property>
    <name>fs.swift.service.SparkTest.password</name>
    <value>testing</value>
  </property>
</configuration>
```

Notice that `fs.swift.service.PROVIDER.tenant`, `fs.swift.service.PROVIDER.username`, `fs.swift.service.PROVIDER.password` contains sensitive information and keeping them in `core-site.xml` is not always a good approach. We suggest to keep those parameters in `core-site.xml` for testing purposes when running Spark via `spark-shell`. For job submissions they should be provided via `sparkContext.hadoopConfiguration`.

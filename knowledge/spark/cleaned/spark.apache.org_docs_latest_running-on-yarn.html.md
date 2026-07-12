[ ![](https://spark.apache.org/images/spark-logo-rev.svg)](https://spark.apache.org/docs/latest/index.html)4.1.2
  * [Overview](https://spark.apache.org/docs/latest/index.html)
  * [Programming Guides](https://spark.apache.org/docs/latest/running-on-yarn.html)
[Quick Start](https://spark.apache.org/docs/latest/quick-start.html) [RDDs, Accumulators, Broadcasts Vars](https://spark.apache.org/docs/latest/rdd-programming-guide.html) [SQL, DataFrames, and Datasets](https://spark.apache.org/docs/latest/sql-programming-guide.html) [Structured Streaming](https://spark.apache.org/docs/latest/streaming/index.html) [Spark Streaming (DStreams)](https://spark.apache.org/docs/latest/streaming-programming-guide.html) [MLlib (Machine Learning)](https://spark.apache.org/docs/latest/ml-guide.html) [GraphX (Graph Processing)](https://spark.apache.org/docs/latest/graphx-programming-guide.html) [SparkR (R on Spark)](https://spark.apache.org/docs/latest/sparkr.html) [PySpark (Python on Spark)](https://spark.apache.org/docs/latest/api/python/getting_started/index.html) [Declarative Pipelines](https://spark.apache.org/docs/latest/declarative-pipelines-programming-guide.html)
  * [API Docs](https://spark.apache.org/docs/latest/running-on-yarn.html)
[Python](https://spark.apache.org/docs/latest/api/python/index.html) [Scala](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html) [Java](https://spark.apache.org/docs/latest/api/java/index.html) [R](https://spark.apache.org/docs/latest/api/R/index.html) [SQL, Built-in Functions](https://spark.apache.org/docs/latest/api/sql/index.html)
  * [Deploying](https://spark.apache.org/docs/latest/running-on-yarn.html)
[Overview](https://spark.apache.org/docs/latest/cluster-overview.html) [Submitting Applications](https://spark.apache.org/docs/latest/submitting-applications.html) [Spark Standalone](https://spark.apache.org/docs/latest/spark-standalone.html) [YARN](https://spark.apache.org/docs/latest/running-on-yarn.html) [Kubernetes](https://spark.apache.org/docs/latest/running-on-kubernetes.html)
  * [More](https://spark.apache.org/docs/latest/running-on-yarn.html)
[Configuration](https://spark.apache.org/docs/latest/configuration.html) [Monitoring](https://spark.apache.org/docs/latest/monitoring.html) [Tuning Guide](https://spark.apache.org/docs/latest/tuning.html) [Job Scheduling](https://spark.apache.org/docs/latest/job-scheduling.html) [Security](https://spark.apache.org/docs/latest/security.html) [Hardware Provisioning](https://spark.apache.org/docs/latest/hardware-provisioning.html) [Migration Guide](https://spark.apache.org/docs/latest/migration-guide.html) [Building Spark](https://spark.apache.org/docs/latest/building-spark.html) [Contributing to Spark](https://spark.apache.org/contributing.html) [Third Party Projects](https://spark.apache.org/third-party-projects.html)
  *

# Running Spark on YARN[](https://spark.apache.org/docs/latest/running-on-yarn.html#running-spark-on-yarn)
  * [Security](https://spark.apache.org/docs/latest/running-on-yarn.html#security)
  * [Launching Spark on YARN](https://spark.apache.org/docs/latest/running-on-yarn.html#launching-spark-on-yarn)
    * [Adding Other JARs](https://spark.apache.org/docs/latest/running-on-yarn.html#adding-other-jars)
  * [Preparations](https://spark.apache.org/docs/latest/running-on-yarn.html#preparations)
  * [Configuration](https://spark.apache.org/docs/latest/running-on-yarn.html#configuration)
  * [Debugging your Application](https://spark.apache.org/docs/latest/running-on-yarn.html#debugging-your-application)
    * [Spark Properties](https://spark.apache.org/docs/latest/running-on-yarn.html#spark-properties)
    * [Available patterns for SHS custom executor log URL](https://spark.apache.org/docs/latest/running-on-yarn.html#available-patterns-for-shs-custom-executor-log-url)
  * [Resource Allocation and Configuration Overview](https://spark.apache.org/docs/latest/running-on-yarn.html#resource-allocation-and-configuration-overview)
  * [Stage Level Scheduling Overview](https://spark.apache.org/docs/latest/running-on-yarn.html#stage-level-scheduling-overview)
  * [Important notes](https://spark.apache.org/docs/latest/running-on-yarn.html#important-notes)
  * [Kerberos](https://spark.apache.org/docs/latest/running-on-yarn.html#kerberos)
    * [YARN-specific Kerberos Configuration](https://spark.apache.org/docs/latest/running-on-yarn.html#yarn-specific-kerberos-configuration)
    * [Troubleshooting Kerberos](https://spark.apache.org/docs/latest/running-on-yarn.html#troubleshooting-kerberos)
  * [Configuring the External Shuffle Service](https://spark.apache.org/docs/latest/running-on-yarn.html#configuring-the-external-shuffle-service)
  * [Launching your application with Apache Oozie](https://spark.apache.org/docs/latest/running-on-yarn.html#launching-your-application-with-apache-oozie)
  * [Using the Spark History Server to replace the Spark Web UI](https://spark.apache.org/docs/latest/running-on-yarn.html#using-the-spark-history-server-to-replace-the-spark-web-ui)
  * [Running multiple versions of the Spark Shuffle Service](https://spark.apache.org/docs/latest/running-on-yarn.html#running-multiple-versions-of-the-spark-shuffle-service)
  * [Configuring different JDKs for Spark Applications](https://spark.apache.org/docs/latest/running-on-yarn.html#configuring-different-jdks-for-spark-applications)

Support for running on [YARN (Hadoop NextGen)](http://hadoop.apache.org/docs/stable/hadoop-yarn/hadoop-yarn-site/YARN.html) was added to Spark in version 0.6.0, and improved in subsequent releases.
# Security[](https://spark.apache.org/docs/latest/running-on-yarn.html#security)
Security features like authentication are not enabled by default. When deploying a cluster that is open to the internet or an untrusted network, it’s important to secure access to the cluster to prevent unauthorized applications from running on the cluster. Please see [Spark Security](https://spark.apache.org/docs/latest/security.html) and the specific security sections in this doc before running Spark.
# Launching Spark on YARN[](https://spark.apache.org/docs/latest/running-on-yarn.html#launching-spark-on-yarn)
Apache Hadoop does not support Java 17 as of 3.4.1, while Apache Spark requires at least Java 17 since 4.0.0, so a different JDK should be configured for Spark applications. Please refer to [Configuring different JDKs for Spark Applications](https://spark.apache.org/docs/latest/running-on-yarn.html#configuring-different-jdks-for-spark-applications) for details.
Ensure that `HADOOP_CONF_DIR` or `YARN_CONF_DIR` points to the directory which contains the (client side) configuration files for the Hadoop cluster. These configs are used to write to HDFS and connect to the YARN ResourceManager. The configuration contained in this directory will be distributed to the YARN cluster so that all containers used by the application use the same configuration. If the configuration references Java system properties or environment variables not managed by YARN, they should also be set in the Spark application’s configuration (driver, executors, and the AM when running in client mode).
There are two deploy modes that can be used to launch Spark applications on YARN. In `cluster` mode, the Spark driver runs inside an application master process which is managed by YARN on the cluster, and the client can go away after initiating the application. In `client` mode, the driver runs in the client process, and the application master is only used for requesting resources from YARN.
Unlike other cluster managers supported by Spark in which the master’s address is specified in the `--master` parameter, in YARN mode the ResourceManager’s address is picked up from the Hadoop configuration. Thus, the `--master` parameter is `yarn`.
To launch a Spark application in `cluster` mode:

```
$ ./bin/spark-submit --class path.to.your.Class --master yarn --deploy-mode cluster [options] <app jar> [app options]

```

For example:

```
$ ./bin/spark-submit --class org.apache.spark.examples.SparkPi \
    --master yarn \
    --deploy-mode cluster \
    --driver-memory 4g \
    --executor-memory 2g \
    --executor-cores 1 \
    --queue thequeue \
    examples/jars/spark-examples*.jar \
    10

```

The above starts a YARN client program which starts the default Application Master. Then SparkPi will be run as a child thread of Application Master. The client will periodically poll the Application Master for status updates and display them in the console. The client will exit once your application has finished running. Refer to the [Debugging your Application](https://spark.apache.org/docs/latest/running-on-yarn.html#debugging-your-application) section below for how to see driver and executor logs.
To launch a Spark application in `client` mode, do the same, but replace `cluster` with `client`. The following shows how you can run `spark-shell` in `client` mode:

```
$ ./bin/spark-shell --master yarn --deploy-mode client

```

## Adding Other JARs[](https://spark.apache.org/docs/latest/running-on-yarn.html#adding-other-jars)
In `cluster` mode, the driver runs on a different machine than the client, so `SparkContext.addJar` won’t work out of the box with files that are local to the client. To make files on the client available to `SparkContext.addJar`, include them with the `--jars` option in the launch command.

```
$ ./bin/spark-submit --class my.main.Class \
    --master yarn \
    --deploy-mode cluster \
    --jars my-other-jar.jar,my-other-other-jar.jar \
    my-main-jar.jar \
    app_arg1 app_arg2

```

# Preparations[](https://spark.apache.org/docs/latest/running-on-yarn.html#preparations)
Running Spark on YARN requires a binary distribution of Spark which is built with YARN support. Binary distributions can be downloaded from the [downloads page](https://spark.apache.org/downloads.html) of the project website. There are two variants of Spark binary distributions you can download. One is pre-built with a certain version of Apache Hadoop; this Spark distribution contains built-in Hadoop runtime, so we call it `with-hadoop` Spark distribution. The other one is pre-built with user-provided Hadoop; since this Spark distribution doesn’t contain a built-in Hadoop runtime, it’s smaller, but users have to provide a Hadoop installation separately. We call this variant `no-hadoop` Spark distribution. For `with-hadoop` Spark distribution, since it contains a built-in Hadoop runtime already, by default, when a job is submitted to Hadoop Yarn cluster, to prevent jar conflict, it will not populate Yarn’s classpath into Spark. To override this behavior, you can set `spark.yarn.populateHadoopClasspath=true`. For `no-hadoop` Spark distribution, Spark will populate Yarn’s classpath by default in order to get Hadoop runtime. For `with-hadoop` Spark distribution, if your application depends on certain library that is only available in the cluster, you can try to populate the Yarn classpath by setting the property mentioned above. If you run into jar conflict issue by doing so, you will need to turn it off and include this library in your application jar.
To build Spark yourself, refer to [Building Spark](https://spark.apache.org/docs/latest/building-spark.html).
To make Spark runtime jars accessible from YARN side, you can specify `spark.yarn.archive` or `spark.yarn.jars`. For details please refer to [Spark Properties](https://spark.apache.org/docs/latest/running-on-yarn.html#spark-properties). If neither `spark.yarn.archive` nor `spark.yarn.jars` is specified, Spark will create a zip file with all jars under `$SPARK_HOME/jars` and upload it to the distributed cache.
# Configuration[](https://spark.apache.org/docs/latest/running-on-yarn.html#configuration)
Most of the configs are the same for Spark on YARN as for other deployment modes. See the [configuration page](https://spark.apache.org/docs/latest/configuration.html) for more information on those. These are configs that are specific to Spark on YARN.
# Debugging your Application[](https://spark.apache.org/docs/latest/running-on-yarn.html#debugging-your-application)
In YARN terminology, executors and application masters run inside “containers”. YARN has two modes for handling container logs after an application has completed. If log aggregation is turned on (with the `yarn.log-aggregation-enable` config), container logs are copied to HDFS and deleted on the local machine. These logs can be viewed from anywhere on the cluster with the `yarn logs` command.

```
yarn logs -applicationId <app ID>

```

will print out the contents of all log files from all containers from the given application. You can also view the container log files directly in HDFS using the HDFS shell or API. The directory where they are located can be found by looking at your YARN configs (`yarn.nodemanager.remote-app-log-dir` and `yarn.nodemanager.remote-app-log-dir-suffix`). The logs are also available on the Spark Web UI under the Executors Tab. You need to have both the Spark history server and the MapReduce history server running and configure `yarn.log.server.url` in `yarn-site.xml` properly. The log URL on the Spark history server UI will redirect you to the MapReduce history server to show the aggregated logs.
When log aggregation isn’t turned on, logs are retained locally on each machine under `YARN_APP_LOGS_DIR`, which is usually configured to `/tmp/logs` or `$HADOOP_HOME/logs/userlogs` depending on the Hadoop version and installation. Viewing logs for a container requires going to the host that contains them and looking in this directory. Subdirectories organize log files by application ID and container ID. The logs are also available on the Spark Web UI under the Executors Tab and doesn’t require running the MapReduce history server.
To review per-container launch environment, increase `yarn.nodemanager.delete.debug-delay-sec` to a large value (e.g. `36000`), and then access the application cache through `yarn.nodemanager.local-dirs` on the nodes on which containers are launched. This directory contains the launch script, JARs, and all environment variables used for launching each container. This process is useful for debugging classpath problems in particular. (Note that enabling this requires admin privileges on cluster settings and a restart of all node managers. Thus, this is not applicable to hosted clusters).
To use a custom log4j2 configuration for the application master or executors, here are the options:
  * upload a custom `log4j2.properties` using `spark-submit`, by adding it to the `--files` list of files to be uploaded with the application.
  * add `-Dlog4j.configurationFile=<location of configuration file>` to `spark.driver.extraJavaOptions` (for the driver) or `spark.executor.extraJavaOptions` (for executors). Note that if using a file, the `file:` protocol should be explicitly provided, and the file needs to exist locally on all the nodes.
  * update the `$SPARK_CONF_DIR/log4j2.properties` file and it will be automatically uploaded along with the other configurations. Note that other 2 options has higher priority than this option if multiple options are specified.

Note that for the first option, both executors and the application master will share the same log4j configuration, which may cause issues when they run on the same node (e.g. trying to write to the same log file).
If you need a reference to the proper location to put log files in the YARN so that YARN can properly display and aggregate them, use `spark.yarn.app.container.log.dir` in your `log4j2.properties`. For example, `appender.file_appender.fileName=${sys:spark.yarn.app.container.log.dir}/spark.log`. For streaming applications, configuring `RollingFileAppender` and setting file location to YARN’s log directory will avoid disk overflow caused by large log files, and logs can be accessed using YARN’s log utility.
To use a custom metrics.properties for the application master and executors, update the `$SPARK_CONF_DIR/metrics.properties` file. It will automatically be uploaded with other configurations, so you don’t need to specify it manually with `--files`.
#### Spark Properties[](https://spark.apache.org/docs/latest/running-on-yarn.html#spark-properties)
| Property Name  | Default  | Meaning  | Since Version  |
| --- | --- | --- | --- |
| `spark.yarn.am.memory`  | `512m`  |  Amount of memory to use for the YARN Application Master in client mode, in the same format as JVM memory strings (e.g. `512m`, `2g`). In cluster mode, use `spark.driver.memory` instead.  Use lower-case suffixes, e.g. `k`, `m`, `g`, `t`, and `p`, for kibi-, mebi-, gibi-, tebi-, and pebibytes, respectively.   | 1.3.0  |
| `spark.yarn.am.resource.{resource-type}.amount`  | `(none)`  |  Amount of resource to use for the YARN Application Master in client mode. In cluster mode, use `spark.yarn.driver.resource.<resource-type>.amount` instead. Please note that this feature can be used only with YARN 3.0+ For reference, see [YARN Resource Model documentation](https://hadoop.apache.org/docs/current/hadoop-yarn/hadoop-yarn-site/ResourceModel.html) Example: To request GPU resources from YARN, use: `spark.yarn.am.resource.yarn.io/gpu.amount`  | 3.0.0  |
| `spark.yarn.applicationType`  | `SPARK`  |  Defines more specific application types, e.g. `SPARK`, `SPARK-SQL`, `SPARK-STREAMING`, `SPARK-MLLIB` and `SPARK-GRAPH`. Please be careful not to exceed 20 characters.   | 3.1.0  |
| `spark.yarn.driver.resource.{resource-type}.amount`  | `(none)`  |  Amount of resource to use for the YARN Application Master in cluster mode. Please note that this feature can be used only with YARN 3.0+ For reference, see [YARN Resource Model documentation](https://hadoop.apache.org/docs/current/hadoop-yarn/hadoop-yarn-site/ResourceModel.html) Example: To request GPU resources from YARN, use: `spark.yarn.driver.resource.yarn.io/gpu.amount`  | 3.0.0  |
| `spark.yarn.executor.resource.{resource-type}.amount`  | `(none)`  |  Amount of resource to use per executor process. Please note that this feature can be used only with YARN 3.0+ For reference, see [YARN Resource Model documentation](https://hadoop.apache.org/docs/current/hadoop-yarn/hadoop-yarn-site/ResourceModel.html) Example: To request GPU resources from YARN, use: `spark.yarn.executor.resource.yarn.io/gpu.amount`  | 3.0.0  |
| `spark.yarn.resourceGpuDeviceName`  | `yarn.io/gpu`  |  Specify the mapping of the Spark resource type of `gpu` to the YARN resource representing a GPU. By default YARN uses `yarn.io/gpu` but if YARN has been configured with a custom resource type, this allows remapping it. Applies when using the `spark.{driver/executor}.resource.gpu.*` configs.   | 3.2.1  |
| `spark.yarn.resourceFpgaDeviceName`  | `yarn.io/fpga`  |  Specify the mapping of the Spark resource type of `fpga` to the YARN resource representing a FPGA. By default YARN uses `yarn.io/fpga` but if YARN has been configured with a custom resource type, this allows remapping it. Applies when using the `spark.{driver/executor}.resource.fpga.*` configs.   | 3.2.1  |
| `spark.yarn.am.cores`  | `1`  |  Number of cores to use for the YARN Application Master in client mode. In cluster mode, use `spark.driver.cores` instead.   | 1.3.0  |
| `spark.yarn.am.waitTime`  | `100s`  |  Only used in `cluster` mode. Time for the YARN Application Master to wait for the SparkContext to be initialized.   | 1.3.0  |
| `spark.yarn.submit.file.replication`  | The default HDFS replication (usually `3`)  |  HDFS replication level for the files uploaded into HDFS for the application. These include things like the Spark jar, the app jar, and any distributed cache files/archives.   | 0.8.1  |
| `spark.yarn.stagingDir`  | Current user's home directory in the filesystem  |  Staging directory used while submitting applications.   | 2.0.0  |
| `spark.yarn.preserve.staging.files`  | `false`  |  Set to `true` to preserve the staged files (Spark jar, app jar, distributed cache files) at the end of the job rather than delete them.   | 1.1.0  |
| `spark.yarn.scheduler.heartbeat.interval-ms`  | `3000`  |  The interval in ms in which the Spark application master heartbeats into the YARN ResourceManager. The value is capped at half the value of YARN's configuration for the expiry interval, i.e. `yarn.am.liveness-monitor.expiry-interval-ms`.   | 0.8.1  |
| `spark.yarn.scheduler.initial-allocation.interval`  | `200ms`  |  The initial interval in which the Spark application master eagerly heartbeats to the YARN ResourceManager when there are pending container allocation requests. It should be no larger than `spark.yarn.scheduler.heartbeat.interval-ms`. The allocation interval will doubled on successive eager heartbeats if pending containers still exist, until `spark.yarn.scheduler.heartbeat.interval-ms` is reached.   | 1.4.0  |
| `spark.yarn.historyServer.address`  | (none)  |  The address of the Spark history server, e.g. `host.com:18080`. The address should not contain a scheme (`http://`). Defaults to not being set since the history server is an optional service. This address is given to the YARN ResourceManager when the Spark application finishes to link the application from the ResourceManager UI to the Spark history server UI. For this property, YARN properties can be used as variables, and these are substituted by Spark at runtime. For example, if the Spark history server runs on the same node as the YARN ResourceManager, it can be set to `${hadoopconf-yarn.resourcemanager.hostname}:18080`.   | 1.0.0  |
| `spark.yarn.dist.archives`  | (none)  |  Comma separated list of archives to be extracted into the working directory of each executor.   | 1.0.0  |
| `spark.yarn.dist.files`  | (none)  |  Comma-separated list of files to be placed in the working directory of each executor.   | 1.0.0  |
| `spark.yarn.dist.jars`  | (none)  |  Comma-separated list of jars to be placed in the working directory of each executor.   | 2.0.0  |
| `spark.yarn.dist.forceDownloadSchemes`  | `(none)`  |  Comma-separated list of schemes for which resources will be downloaded to the local disk prior to being added to YARN's distributed cache. For use in cases where the YARN service does not support schemes that are supported by Spark, like http, https and ftp, or jars required to be in the local YARN client's classpath. Wildcard '*' is denoted to download resources for all the schemes.   | 2.3.0  |
| `spark.executor.instances`  | `2`  |  The number of executors for static allocation. With `spark.dynamicAllocation.enabled`, the initial set of executors will be at least this large.   | 1.0.0  |
| `spark.yarn.am.memoryOverhead`  | AM memory * 0.10, with minimum of 384   |  Same as `spark.driver.memoryOverhead`, but for the YARN Application Master in client mode.   | 1.3.0  |
| `spark.yarn.queue`  | `default`  |  The name of the YARN queue to which the application is submitted.   | 1.0.0  |
| `spark.yarn.jars`  | (none)  |  List of libraries containing Spark code to distribute to YARN containers. By default, Spark on YARN will use Spark jars installed locally, but the Spark jars can also be in a world-readable location on HDFS. This allows YARN to cache it on nodes so that it doesn't need to be distributed each time an application runs. To point to jars on HDFS, for example, set this configuration to `hdfs:///some/path`. Globs are allowed.   | 2.0.0  |
| `spark.yarn.archive`  | (none)  |  An archive containing needed Spark jars for distribution to the YARN cache. If set, this configuration replaces `spark.yarn.jars` and the archive is used in all the application's containers. The archive should contain jar files in its root directory. Like with the previous option, the archive can also be hosted on HDFS to speed up file distribution.   | 2.0.0  |
| `spark.yarn.appMasterEnv.[EnvironmentVariableName]`  | (none)  |  Add the environment variable specified by `EnvironmentVariableName` to the Application Master process launched on YARN. The user can specify multiple of these and to set multiple environment variables. In `cluster` mode this controls the environment of the Spark driver and in `client` mode it only controls the environment of the executor launcher.   | 1.1.0  |
| `spark.yarn.containerLauncherMaxThreads`  | `25`  |  The maximum number of threads to use in the YARN Application Master for launching executor containers.   | 1.2.0  |
| `spark.yarn.am.extraJavaOptions`  | (none)  |  A string of extra JVM options to pass to the YARN Application Master in client mode. In cluster mode, use `spark.driver.extraJavaOptions` instead. Note that it is illegal to set maximum heap size (-Xmx) settings with this option. Maximum heap size settings can be set with `spark.yarn.am.memory`  | 1.3.0  |
| `spark.yarn.am.extraLibraryPath`  | (none)  |  Set a special library path to use when launching the YARN Application Master in client mode.   | 1.4.0  |
| `spark.yarn.populateHadoopClasspath`  |  For `with-hadoop` Spark distribution, this is set to false; for `no-hadoop` distribution, this is set to true.   |  Whether to populate Hadoop classpath from `yarn.application.classpath` and `mapreduce.application.classpath` Note that if this is set to `false`, it requires a `with-Hadoop` Spark distribution that bundles Hadoop runtime or user has to provide a Hadoop installation separately.   | 2.4.6  |
| `spark.yarn.maxAppAttempts`  |  `yarn.resourcemanager.am.max-attempts` in YARN  |  The maximum number of attempts that will be made to submit the application. It should be no larger than the global number of max attempts in the YARN configuration.   | 1.3.0  |
| `spark.yarn.am.attemptFailuresValidityInterval`  | (none)  |  Defines the validity interval for AM failure tracking. If the AM has been running for at least the defined interval, the AM failure count will be reset. This feature is not enabled if not configured.   | 1.6.0  |
| `spark.yarn.am.clientModeTreatDisconnectAsFailed`  | false  |  Treat yarn-client unclean disconnects as failures. In yarn-client mode, normally the application will always finish with a final status of SUCCESS because in some cases, it is not possible to know if the Application was terminated intentionally by the user or if there was a real error. This config changes that behavior such that if the Application Master disconnects from the driver uncleanly (ie without the proper shutdown handshake) the application will terminate with a final status of FAILED. This will allow the caller to decide if it was truly a failure. Note that if this config is set and the user just terminate the client application badly it may show a status of FAILED when it wasn't really FAILED.   | 3.3.0  |
| `spark.yarn.am.clientModeExitOnError`  | false  |  In yarn-client mode, when this is true, if driver got application report with final status of KILLED or FAILED, driver will stop corresponding SparkContext and exit program with code 1. Note, if this is true and called from another application, it will terminate the parent application as well.   | 3.3.0  |
| `spark.yarn.am.tokenConfRegex`  | (none)  |  The value of this config is a regex expression used to grep a list of config entries from the job's configuration file (e.g., hdfs-site.xml) and send to RM, which uses them when renewing delegation tokens. A typical use case of this feature is to support delegation tokens in an environment where a YARN cluster needs to talk to multiple downstream HDFS clusters, where the YARN RM may not have configs (e.g., dfs.nameservices, dfs.ha.namenodes.*, dfs.namenode.rpc-address.*) to connect to these clusters. In this scenario, Spark users can specify the config value to be `^dfs.nameservices\$|^dfs.namenode.rpc-address.*\$|^dfs.ha.namenodes.*\$` to parse these HDFS configs from the job's local configuration files. This config is very similar to `mapreduce.job.send-token-conf`. Please check YARN-5910 for more details.   | 3.3.0  |
| `spark.yarn.submit.waitAppCompletion`  | `true`  |  In YARN cluster mode, controls whether the client waits to exit until the application completes. If set to `true`, the client process will stay alive reporting the application's status. Otherwise, the client process will exit after submission.   | 1.4.0  |
| `spark.yarn.am.nodeLabelExpression`  | (none)  |  A YARN node label expression that restricts the set of nodes AM will be scheduled on. Only versions of YARN greater than or equal to 2.6 support node label expressions, so when running against earlier versions, this property will be ignored.   | 1.6.0  |
| `spark.yarn.executor.nodeLabelExpression`  | (none)  |  A YARN node label expression that restricts the set of nodes executors will be scheduled on. Only versions of YARN greater than or equal to 2.6 support node label expressions, so when running against earlier versions, this property will be ignored.   | 1.4.0  |
| `spark.yarn.tags`  | (none)  |  Comma-separated list of strings to pass through as YARN application tags appearing in YARN ApplicationReports, which can be used for filtering when querying YARN apps.   | 1.5.0  |
| `spark.yarn.priority`  | (none)  |  Application priority for YARN to define pending applications ordering policy, those with higher integer value have a better opportunity to be activated. Currently, YARN only supports application priority when using FIFO ordering policy.   | 3.0.0  |
| `spark.yarn.config.gatewayPath`  | (none)  |  A path that is valid on the gateway host (the host where a Spark application is started) but may differ for paths for the same resource in other nodes in the cluster. Coupled with `spark.yarn.config.replacementPath`, this is used to support clusters with heterogeneous configurations, so that Spark can correctly launch remote processes.  The replacement path normally will contain a reference to some environment variable exported by YARN (and, thus, visible to Spark containers).  For example, if the gateway node has Hadoop libraries installed on `/disk1/hadoop`, and the location of the Hadoop install is exported by YARN as the `HADOOP_HOME` environment variable, setting this value to `/disk1/hadoop` and the replacement path to `$HADOOP_HOME` will make sure that paths used to launch remote processes properly reference the local YARN configuration.   | 1.5.0  |
| `spark.yarn.config.replacementPath`  | (none)  |  See `spark.yarn.config.gatewayPath`.   | 1.5.0  |
| `spark.yarn.rolledLog.includePattern`  | (none)  |  Java Regex to filter the log files which match the defined include pattern and those log files will be aggregated in a rolling fashion. This will be used with YARN's rolling log aggregation, to enable this feature in YARN side `yarn.nodemanager.log-aggregation.roll-monitoring-interval-seconds` should be configured in yarn-site.xml. The Spark log4j appender needs be changed to use FileAppender or another appender that can handle the files being removed while it is running. Based on the file name configured in the log4j configuration (like spark.log), the user should set the regex (spark*) to include all the log files that need to be aggregated.   | 2.0.0  |
| `spark.yarn.rolledLog.excludePattern`  | (none)  |  Java Regex to filter the log files which match the defined exclude pattern and those log files will not be aggregated in a rolling fashion. If the log file name matches both the include and the exclude pattern, this file will be excluded eventually.   | 2.0.0  |
| `spark.yarn.executor.launch.excludeOnFailure.enabled`  | false  |  Flag to enable exclusion of nodes having YARN resource allocation problems. The error limit for excluding can be configured by `spark.excludeOnFailure.application.maxFailedExecutorsPerNode`.   | 2.4.0  |
| `spark.yarn.exclude.nodes`  | (none)  |  Comma-separated list of YARN node names which are excluded from resource allocation.   | 3.0.0  |
| `spark.yarn.metrics.namespace`  | (none)  |  The root namespace for AM metrics reporting. If it is not set then the YARN application ID is used.   | 2.4.0  |
| `spark.yarn.report.interval`  | `1s`  |  Interval between reports of the current Spark job status in cluster mode.   | 0.9.0  |
| `spark.yarn.report.loggingFrequency`  | `30`  |  Maximum number of application reports processed until the next application status is logged. If there is a change of state, the application status will be logged regardless of the number of application reports processed.   | 3.5.0  |
| `spark.yarn.clientLaunchMonitorInterval`  | `1s`  |  Interval between requests for status the client mode AM when starting the app.   | 2.3.0  |
| `spark.yarn.includeDriverLogsLink`  | `false`  |  In cluster mode, whether the client application report includes links to the driver container's logs. This requires polling the ResourceManager's REST API, so it places some additional load on the RM.   | 3.1.0  |
| `spark.yarn.unmanagedAM.enabled`  | `false`  |  In client mode, whether to launch the Application Master service as part of the client using unmanaged am.   | 3.0.0  |
| `spark.yarn.shuffle.server.recovery.disabled`  | false  |  Set to true for applications that have higher security requirements and prefer that their secret is not saved in the db. The shuffle data of such applications will not be recovered after the External Shuffle Service restarts.   | 3.5.0  |
#### Available patterns for SHS custom executor log URL[](https://spark.apache.org/docs/latest/running-on-yarn.html#available-patterns-for-shs-custom-executor-log-url)
| Pattern  | Meaning  |
| --- | --- |
| {{HTTP_SCHEME}}  |  `http://` or `https://` according to YARN HTTP policy. (Configured via `yarn.http.policy`)  |
| {{NM_HOST}}  | The "host" of node where container was run.  |
| {{NM_PORT}}  | The "port" of node manager where container was run.  |
| {{NM_HTTP_PORT}}  | The "port" of node manager's http server where container was run.  |
| {{NM_HTTP_ADDRESS}}  | Http URI of the node on which the container is allocated.  |
| {{CLUSTER_ID}}  | The cluster ID of Resource Manager. (Configured via `yarn.resourcemanager.cluster-id`)  |
| {{CONTAINER_ID}}  | The ID of container.  |
| {{USER}}  |  `SPARK_USER` on system environment.  |
| {{FILE_NAME}}  |  `stdout`, `stderr`.  |
For example, suppose you would like to point log url link to Job History Server directly instead of let NodeManager http server redirects it, you can configure `spark.history.custom.executor.log.url` as below:
`{{HTTP_SCHEME}}<JHS_HOST>:<JHS_PORT>/jobhistory/logs/{{NM_HOST}}:{{NM_PORT}}/{{CONTAINER_ID}}/{{CONTAINER_ID}}/{{USER}}/{{FILE_NAME}}?start=-4096`
NOTE: you need to replace `<JHS_HOST>` and `<JHS_PORT>` with actual value.
# Resource Allocation and Configuration Overview[](https://spark.apache.org/docs/latest/running-on-yarn.html#resource-allocation-and-configuration-overview)
Please make sure to have read the Custom Resource Scheduling and Configuration Overview section on the [configuration page](https://spark.apache.org/docs/latest/configuration.html). This section only talks about the YARN specific aspects of resource scheduling.
YARN needs to be configured to support any resources the user wants to use with Spark. Resource scheduling on YARN was added in YARN 3.1.0. See the YARN documentation for more information on configuring resources and properly setting up isolation. Ideally the resources are setup isolated so that an executor can only see the resources it was allocated. If you do not have isolation enabled, the user is responsible for creating a discovery script that ensures the resource is not shared between executors.
YARN supports user defined resource types but has built in types for GPU (`yarn.io/gpu`) and FPGA (`yarn.io/fpga`). For that reason, if you are using either of those resources, Spark can translate your request for spark resources into YARN resources and you only have to specify the `spark.{driver/executor}.resource.` configs. Note, if you are using a custom resource type for GPUs or FPGAs with YARN you can change the Spark mapping using `spark.yarn.resourceGpuDeviceName` and `spark.yarn.resourceFpgaDeviceName`. If you are using a resource other than FPGA or GPU, the user is responsible for specifying the configs for both YARN (`spark.yarn.{driver/executor}.resource.`) and Spark (`spark.{driver/executor}.resource.`).
For example, the user wants to request 2 GPUs for each executor. The user can just specify `spark.executor.resource.gpu.amount=2` and Spark will handle requesting `yarn.io/gpu` resource type from YARN.
If the user has a user defined YARN resource, lets call it `acceleratorX` then the user must specify `spark.yarn.executor.resource.acceleratorX.amount=2` and `spark.executor.resource.acceleratorX.amount=2`.
YARN does not tell Spark the addresses of the resources allocated to each container. For that reason, the user must specify a discovery script that gets run by the executor on startup to discover what resources are available to that executor. You can find an example scripts in `examples/src/main/scripts/getGpusResources.sh`. The script must have execute permissions set and the user should setup permissions to not allow malicious users to modify it. The script should write to STDOUT a JSON string in the format of the ResourceInformation class. This has the resource name and an array of resource addresses available to just that executor.
# Stage Level Scheduling Overview[](https://spark.apache.org/docs/latest/running-on-yarn.html#stage-level-scheduling-overview)
Stage level scheduling is supported on YARN:
  * When dynamic allocation is disabled: It allows users to specify different task resource requirements at the stage level and will use the same executors requested at startup.
  * When dynamic allocation is enabled: It allows users to specify task and executor resource requirements at the stage level and will request the extra executors.

One thing to note that is YARN specific is that each ResourceProfile requires a different container priority on YARN. The mapping is simply the ResourceProfile id becomes the priority, on YARN lower numbers are higher priority. This means that profiles created earlier will have a higher priority in YARN. Normally this won’t matter as Spark finishes one stage before starting another one, the only case this might have an affect is in a job server type scenario, so its something to keep in mind. Note there is a difference in the way custom resources are handled between the base default profile and custom ResourceProfiles. To allow for the user to request YARN containers with extra resources without Spark scheduling on them, the user can specify resources via the `spark.yarn.executor.resource.` config. Those configs are only used in the base default profile though and do not get propagated into any other custom ResourceProfiles. This is because there would be no way to remove them if you wanted a stage to not have them. This results in your default profile getting custom resources defined in `spark.yarn.executor.resource.` plus spark defined resources of GPU or FPGA. Spark converts GPU and FPGA resources into the YARN built in types `yarn.io/gpu`) and `yarn.io/fpga`, but does not know the mapping of any other resources. Any other Spark custom resources are not propagated to YARN for the default profile. So if you want Spark to schedule based off a custom resource and have it requested from YARN, you must specify it in both YARN (`spark.yarn.{driver/executor}.resource.`) and Spark (`spark.{driver/executor}.resource.`) configs. Leave the Spark config off if you only want YARN containers with the extra resources but Spark not to schedule using them. Now for custom ResourceProfiles, it doesn’t currently have a way to only specify YARN resources without Spark scheduling off of them. This means for custom ResourceProfiles we propagate all the resources defined in the ResourceProfile to YARN. We still convert GPU and FPGA to the YARN build in types as well. This requires that the name of any custom resources you specify match what they are defined as in YARN.
# Important notes[](https://spark.apache.org/docs/latest/running-on-yarn.html#important-notes)
  * Whether core requests are honored in scheduling decisions depends on which scheduler is in use and how it is configured.
  * In `cluster` mode, the local directories used by the Spark executors and the Spark driver will be the local directories configured for YARN (Hadoop YARN config `yarn.nodemanager.local-dirs`). If the user specifies `spark.local.dir`, it will be ignored. In `client` mode, the Spark executors will use the local directories configured for YARN while the Spark driver will use those defined in `spark.local.dir`. This is because the Spark driver does not run on the YARN cluster in `client` mode, only the Spark executors do.
  * The `--files` and `--archives` options support specifying file names with the # similar to Hadoop. For example, you can specify: `--files localtest.txt#appSees.txt` and this will upload the file you have locally named `localtest.txt` into HDFS but this will be linked to by the name `appSees.txt`, and your application should use the name as `appSees.txt` to reference it when running on YARN.
  * The `--jars` option allows the `SparkContext.addJar` function to work if you are using it with local files and running in `cluster` mode. It does not need to be used if you are using it with HDFS, HTTP, HTTPS, or FTP files.

# Kerberos[](https://spark.apache.org/docs/latest/running-on-yarn.html#kerberos)
Standard Kerberos support in Spark is covered in the [Security](https://spark.apache.org/docs/latest/security.html#kerberos) page.
In YARN mode, when accessing Hadoop file systems, aside from the default file system in the hadoop configuration, Spark will also automatically obtain delegation tokens for the service hosting the staging directory of the Spark application.
## YARN-specific Kerberos Configuration[](https://spark.apache.org/docs/latest/running-on-yarn.html#yarn-specific-kerberos-configuration)
| Property Name  | Default  | Meaning  | Since Version  |
| --- | --- | --- | --- |
| `spark.kerberos.keytab`  | (none)  |  The full path to the file that contains the keytab for the principal specified above. This keytab will be copied to the node running the YARN Application Master via the YARN Distributed Cache, and will be used for renewing the login tickets and the delegation tokens periodically. Equivalent to the `--keytab` command line argument.
(Works also with the "local" master.)   | 3.0.0  |
| `spark.kerberos.principal`  | (none)  |  Principal to be used to login to KDC, while running on secure clusters. Equivalent to the `--principal` command line argument.
(Works also with the "local" master.)   | 3.0.0  |
| `spark.yarn.kerberos.relogin.period`  | 1m  |  How often to check whether the kerberos TGT should be renewed. This should be set to a value that is shorter than the TGT renewal period (or the TGT lifetime if TGT renewal is not enabled). The default value should be enough for most deployments.   | 2.3.0  |
| `spark.yarn.kerberos.renewal.excludeHadoopFileSystems`  | (none)  |  A comma-separated list of Hadoop filesystems for whose hosts will be excluded from delegation token renewal at resource scheduler. For example, `spark.yarn.kerberos.renewal.excludeHadoopFileSystems=hdfs://nn1.com:8032,     hdfs://nn2.com:8032`. This is known to work under YARN for now, so YARN Resource Manager won't renew tokens for the application. Note that as resource scheduler does not renew token, so any application running longer than the original token expiration that tries to use that token will likely fail.   | 3.2.0  |
## Troubleshooting Kerberos[](https://spark.apache.org/docs/latest/running-on-yarn.html#troubleshooting-kerberos)
Debugging Hadoop/Kerberos problems can be “difficult”. One useful technique is to enable extra logging of Kerberos operations in Hadoop by setting the `HADOOP_JAAS_DEBUG` environment variable.

```
export HADOOP_JAAS_DEBUG=true

```

The JDK classes can be configured to enable extra logging of their Kerberos and SPNEGO/REST authentication via the system properties `sun.security.krb5.debug` and `sun.security.spnego.debug=true`

```
-Dsun.security.krb5.debug=true -Dsun.security.spnego.debug=true

```

All these options can be enabled in the Application Master:

```
spark.yarn.appMasterEnv.HADOOP_JAAS_DEBUG true
spark.yarn.am.extraJavaOptions -Dsun.security.krb5.debug=true -Dsun.security.spnego.debug=true

```

Finally, if the log level for `org.apache.spark.deploy.yarn.Client` is set to `DEBUG`, the log will include a list of all tokens obtained, and their expiry details
# Configuring the External Shuffle Service[](https://spark.apache.org/docs/latest/running-on-yarn.html#configuring-the-external-shuffle-service)
To start the Spark Shuffle Service on each `NodeManager` in your YARN cluster, follow these instructions:
  1. Build Spark with the [YARN profile](https://spark.apache.org/docs/latest/building-spark.html#specifying-the-hadoop-version-and-enabling-yarn). Skip this step if you are using a pre-packaged distribution.
  2. Locate the `spark-<version>-yarn-shuffle.jar`. This should be under `$SPARK_HOME/common/network-yarn/target/scala-<version>` if you are building Spark yourself, and under `yarn` if you are using a distribution.
  3. Add this jar to the classpath of all `NodeManager`s in your cluster.
  4. In the `yarn-site.xml` on each node, add `spark_shuffle` to `yarn.nodemanager.aux-services`, then set `yarn.nodemanager.aux-services.spark_shuffle.class` to `org.apache.spark.network.yarn.YarnShuffleService`.
  5. Increase `NodeManager's` heap size by setting `YARN_HEAPSIZE` (1000 by default) in `etc/hadoop/yarn-env.sh` to avoid garbage collection issues during shuffle.
  6. Restart all `NodeManager`s in your cluster.

The following extra configuration options are available when the shuffle service is running on YARN:
| Property Name  | Default  | Meaning  | Since Version  |
| --- | --- | --- | --- |
| `spark.yarn.shuffle.stopOnFailure`  | `false`  |  Whether to stop the NodeManager when there's a failure in the Spark Shuffle Service's initialization. This prevents application failures caused by running containers on NodeManagers where the Spark Shuffle Service is not running.   | 2.1.0  |
| `spark.yarn.shuffle.service.metrics.namespace`  | `sparkShuffleService`  |  The namespace to use when emitting shuffle service metrics into Hadoop metrics2 system of the NodeManager.   | 3.2.0  |
| `spark.yarn.shuffle.service.logs.namespace`  | `(not set)`  |  A namespace which will be appended to the class name when forming the logger name to use for emitting logs from the YARN shuffle service, like `org.apache.spark.network.yarn.YarnShuffleService.logsNamespaceValue`. Since some logging frameworks may expect the logger name to look like a class name, it's generally recommended to provide a value which would be a valid Java package or class name and not include spaces.   | 3.3.0  |
| `spark.shuffle.service.db.backend`  | ROCKSDB  |  When work-preserving restart is enabled in YARN, this is used to specify the disk-base store used in shuffle service state store, supports `ROCKSDB` and `LEVELDB` (deprecated) with `ROCKSDB` as default value. The original data store in `RocksDB/LevelDB` will not be automatically converted to another kind of storage now. The original data store will be retained and the new type data store will be created when switching storage types.   | 3.4.0  |
Please note that the instructions above assume that the default shuffle service name, `spark_shuffle`, has been used. It is possible to use any name here, but the values used in the YARN NodeManager configurations must match the value of `spark.shuffle.service.name` in the Spark application.
The shuffle service will, by default, take all of its configurations from the Hadoop Configuration used by the NodeManager (e.g. `yarn-site.xml`). However, it is also possible to configure the shuffle service independently using a file named `spark-shuffle-site.xml` which should be placed onto the classpath of the shuffle service (which is, by default, shared with the classpath of the NodeManager). The shuffle service will treat this as a standard Hadoop Configuration resource and overlay it on top of the NodeManager’s configuration.
# Launching your application with Apache Oozie[](https://spark.apache.org/docs/latest/running-on-yarn.html#launching-your-application-with-apache-oozie)
Apache Oozie can launch Spark applications as part of a workflow. In a secure cluster, the launched application will need the relevant tokens to access the cluster’s services. If Spark is launched with a keytab, this is automatic. However, if Spark is to be launched without a keytab, the responsibility for setting up security must be handed over to Oozie.
The details of configuring Oozie for secure clusters and obtaining credentials for a job can be found on the [Oozie web site](http://oozie.apache.org/) in the “Authentication” section of the specific release’s documentation.
For Spark applications, the Oozie workflow must be set up for Oozie to request all tokens which the application needs, including:
  * The YARN resource manager.
  * The local Hadoop filesystem.
  * Any remote Hadoop filesystems used as a source or destination of I/O.
  * Hive —if used.
  * HBase —if used.
  * The YARN timeline server, if the application interacts with this.

To avoid Spark attempting —and then failing— to obtain Hive, HBase and remote HDFS tokens, the Spark configuration must be set to disable token collection for the services.
The Spark configuration must include the lines:

```
spark.security.credentials.hive.enabled   false
spark.security.credentials.hbase.enabled  false

```

The configuration option `spark.kerberos.access.hadoopFileSystems` must be unset.
# Using the Spark History Server to replace the Spark Web UI[](https://spark.apache.org/docs/latest/running-on-yarn.html#using-the-spark-history-server-to-replace-the-spark-web-ui)
It is possible to use the Spark History Server application page as the tracking URL for running applications when the application UI is disabled. This may be desirable on secure clusters, or to reduce the memory usage of the Spark driver. To set up tracking through the Spark History Server, do the following:
  * On the application side, set `spark.yarn.historyServer.allowTracking=true` in Spark’s configuration. This will tell Spark to use the history server’s URL as the tracking URL if the application’s UI is disabled.
  * On the Spark History Server, add `org.apache.spark.deploy.yarn.YarnProxyRedirectFilter` to the list of filters in the `spark.ui.filters` configuration.

Be aware that the history server information may not be up-to-date with the application’s state.
# Running multiple versions of the Spark Shuffle Service[](https://spark.apache.org/docs/latest/running-on-yarn.html#running-multiple-versions-of-the-spark-shuffle-service)
Please note that this section only applies when running on YARN versions >= 2.9.0.
In some cases it may be desirable to run multiple instances of the Spark Shuffle Service which are using different versions of Spark. This can be helpful, for example, when running a YARN cluster with a mixed workload of applications running multiple Spark versions, since a given version of the shuffle service is not always compatible with other versions of Spark. YARN versions since 2.9.0 support the ability to run shuffle services within an isolated classloader (see [YARN-4577](https://issues.apache.org/jira/browse/YARN-4577)), meaning multiple Spark versions can coexist within a single NodeManager. The `yarn.nodemanager.aux-services.<service-name>.classpath` and, starting from YARN 2.10.2/3.1.1/3.2.0, `yarn.nodemanager.aux-services.<service-name>.remote-classpath` options can be used to configure this. Note that YARN 3.3.0/3.3.1 have an issue which requires setting `yarn.nodemanager.aux-services.<service-name>.system-classes` as a workaround. See [YARN-11053](https://issues.apache.org/jira/browse/YARN-11053) for details. In addition to setting up separate classpaths, it’s necessary to ensure the two versions advertise to different ports. This can be achieved using the `spark-shuffle-site.xml` file described above. For example, you may have configuration like:

```
  yarn.nodemanager.aux-services = spark_shuffle_x,spark_shuffle_y
  yarn.nodemanager.aux-services.spark_shuffle_x.classpath = /path/to/spark-x-path/fat.jar:/path/to/spark-x-config
  yarn.nodemanager.aux-services.spark_shuffle_y.classpath = /path/to/spark-y-path/fat.jar:/path/to/spark-y-config

```

Or

```
  yarn.nodemanager.aux-services = spark_shuffle_x,spark_shuffle_y
  yarn.nodemanager.aux-services.spark_shuffle_x.classpath = /path/to/spark-x-path/*:/path/to/spark-x-config
  yarn.nodemanager.aux-services.spark_shuffle_y.classpath = /path/to/spark-y-path/*:/path/to/spark-y-config

```

The two `spark-*-config` directories each contain one file, `spark-shuffle-site.xml`. These are XML files in the [Hadoop Configuration format](https://hadoop.apache.org/docs/current/api/org/apache/hadoop/conf/Configuration.html) which each contain a few configurations to adjust the port number and metrics name prefix used:

```
<configuration>
  <property>
    <name>spark.shuffle.service.port</name>
    <value>7001</value>
  </property>
  <property>
    <name>spark.yarn.shuffle.service.metrics.namespace</name>
    <value>sparkShuffleServiceX</value>
  </property>
</configuration>

```

The values should both be different for the two different services.
Then, in the configuration of the Spark applications, one should be configured with:

```
  spark.shuffle.service.name = spark_shuffle_x
  spark.shuffle.service.port = 7001

```

and one should be configured with:

```
  spark.shuffle.service.name = spark_shuffle_y
  spark.shuffle.service.port = <other value>

```

# Configuring different JDKs for Spark Applications[](https://spark.apache.org/docs/latest/running-on-yarn.html#configuring-different-jdks-for-spark-applications)
In some cases it may be desirable to use a different JDK from YARN node manager to run Spark applications, this can be achieved by setting the `JAVA_HOME` environment variable for YARN containers and the `spark-submit` process.
Note that, Spark assumes that all JVM processes runs in one application use the same version of JDK, otherwise, you may encounter JDK serialization issues.
To configure a Spark application to use a JDK which has been pre-installed on all nodes at `/opt/openjdk-17`:

```
$ export JAVA_HOME=/opt/openjdk-17
$ ./bin/spark-submit --class path.to.your.Class \
    --master yarn \
    --conf spark.yarn.appMasterEnv.JAVA_HOME=/opt/openjdk-17 \
    --conf spark.executorEnv.JAVA_HOME=/opt/openjdk-17 \
    <app jar> [app options]

```

Optionally, the user may want to avoid installing a different JDK on the YARN cluster nodes, in such a case, it’s also possible to distribute the JDK using YARN’s Distributed Cache. For example, to use Java 21 to run a Spark application, prepare a JDK 21 tarball `openjdk-21.tar.gz` and untar it to `/opt` on the local node, then submit a Spark application:

```
$ export JAVA_HOME=/opt/openjdk-21
$ ./bin/spark-submit --class path.to.your.Class \
    --master yarn \
    --archives path/to/openjdk-21.tar.gz \
    --conf spark.yarn.appMasterEnv.JAVA_HOME=./openjdk-21.tar.gz/openjdk-21 \
    --conf spark.executorEnv.JAVA_HOME=./openjdk-21.tar.gz/openjdk-21 \
    <app jar> [app options]

```

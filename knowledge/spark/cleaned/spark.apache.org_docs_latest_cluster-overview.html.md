[ ![](https://spark.apache.org/images/spark-logo-rev.svg)](https://spark.apache.org/docs/latest/index.html)4.1.2
  * [Overview](https://spark.apache.org/docs/latest/index.html)
  * [Programming Guides](https://spark.apache.org/docs/latest/cluster-overview.html)
[Quick Start](https://spark.apache.org/docs/latest/quick-start.html) [RDDs, Accumulators, Broadcasts Vars](https://spark.apache.org/docs/latest/rdd-programming-guide.html) [SQL, DataFrames, and Datasets](https://spark.apache.org/docs/latest/sql-programming-guide.html) [Structured Streaming](https://spark.apache.org/docs/latest/streaming/index.html) [Spark Streaming (DStreams)](https://spark.apache.org/docs/latest/streaming-programming-guide.html) [MLlib (Machine Learning)](https://spark.apache.org/docs/latest/ml-guide.html) [GraphX (Graph Processing)](https://spark.apache.org/docs/latest/graphx-programming-guide.html) [SparkR (R on Spark)](https://spark.apache.org/docs/latest/sparkr.html) [PySpark (Python on Spark)](https://spark.apache.org/docs/latest/api/python/getting_started/index.html) [Declarative Pipelines](https://spark.apache.org/docs/latest/declarative-pipelines-programming-guide.html)
  * [API Docs](https://spark.apache.org/docs/latest/cluster-overview.html)
[Python](https://spark.apache.org/docs/latest/api/python/index.html) [Scala](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html) [Java](https://spark.apache.org/docs/latest/api/java/index.html) [R](https://spark.apache.org/docs/latest/api/R/index.html) [SQL, Built-in Functions](https://spark.apache.org/docs/latest/api/sql/index.html)
  * [Deploying](https://spark.apache.org/docs/latest/cluster-overview.html)
[Overview](https://spark.apache.org/docs/latest/cluster-overview.html) [Submitting Applications](https://spark.apache.org/docs/latest/submitting-applications.html) [Spark Standalone](https://spark.apache.org/docs/latest/spark-standalone.html) [YARN](https://spark.apache.org/docs/latest/running-on-yarn.html) [Kubernetes](https://spark.apache.org/docs/latest/running-on-kubernetes.html)
  * [More](https://spark.apache.org/docs/latest/cluster-overview.html)
[Configuration](https://spark.apache.org/docs/latest/configuration.html) [Monitoring](https://spark.apache.org/docs/latest/monitoring.html) [Tuning Guide](https://spark.apache.org/docs/latest/tuning.html) [Job Scheduling](https://spark.apache.org/docs/latest/job-scheduling.html) [Security](https://spark.apache.org/docs/latest/security.html) [Hardware Provisioning](https://spark.apache.org/docs/latest/hardware-provisioning.html) [Migration Guide](https://spark.apache.org/docs/latest/migration-guide.html) [Building Spark](https://spark.apache.org/docs/latest/building-spark.html) [Contributing to Spark](https://spark.apache.org/contributing.html) [Third Party Projects](https://spark.apache.org/third-party-projects.html)
  *

# Cluster Mode Overview[](https://spark.apache.org/docs/latest/cluster-overview.html#cluster-mode-overview)
This document gives a short overview of how Spark runs on clusters, to make it easier to understand the components involved. Read through the [application submission guide](https://spark.apache.org/docs/latest/submitting-applications.html) to learn about launching applications on a cluster.
# Components[](https://spark.apache.org/docs/latest/cluster-overview.html#components)
Spark applications run as independent sets of processes on a cluster, coordinated by the `SparkContext` object in your main program (called the _driver program_).
Specifically, to run on a cluster, the SparkContext can connect to several types of _cluster managers_ (either Spark’s own standalone cluster manager, YARN or Kubernetes), which allocate resources across applications. Once connected, Spark acquires _executors_ on nodes in the cluster, which are processes that run computations and store data for your application. Next, it sends your application code (defined by JAR or Python files passed to SparkContext) to the executors. Finally, SparkContext sends _tasks_ to the executors to run.
![Spark cluster components](https://spark.apache.org/docs/latest/img/cluster-overview.png)
There are several useful things to note about this architecture:
  1. Each application gets its own executor processes, which stay up for the duration of the whole application and run tasks in multiple threads. This has the benefit of isolating applications from each other, on both the scheduling side (each driver schedules its own tasks) and executor side (tasks from different applications run in different JVMs). However, it also means that data cannot be shared across different Spark applications (instances of SparkContext) without writing it to an external storage system.
  2. Spark is agnostic to the underlying cluster manager. As long as it can acquire executor processes, and these communicate with each other, it is relatively easy to run it even on a cluster manager that also supports other applications (e.g. YARN/Kubernetes).
  3. The driver program must listen for and accept incoming connections from its executors throughout its lifetime (e.g., see [spark.driver.port in the network config section](https://spark.apache.org/docs/latest/configuration.html#networking)). As such, the driver program must be network addressable from the worker nodes.
  4. Because the driver schedules tasks on the cluster, it should be run close to the worker nodes, preferably on the same local area network. If you’d like to send requests to the cluster remotely, it’s better to open an RPC to the driver and have it submit operations from nearby than to run a driver far away from the worker nodes.

# Cluster Manager Types[](https://spark.apache.org/docs/latest/cluster-overview.html#cluster-manager-types)
The system currently supports several cluster managers:
  * [Standalone](https://spark.apache.org/docs/latest/spark-standalone.html) – a simple cluster manager included with Spark that makes it easy to set up a cluster.
  * [Hadoop YARN](https://spark.apache.org/docs/latest/running-on-yarn.html) – the resource manager in Hadoop 3.
  * [Kubernetes](https://spark.apache.org/docs/latest/running-on-kubernetes.html) – an open-source system for automating deployment, scaling, and management of containerized applications.

# Submitting Applications[](https://spark.apache.org/docs/latest/cluster-overview.html#submitting-applications)
Applications can be submitted to a cluster of any type using the `spark-submit` script. The [application submission guide](https://spark.apache.org/docs/latest/submitting-applications.html) describes how to do this.
# Monitoring[](https://spark.apache.org/docs/latest/cluster-overview.html#monitoring)
Each driver program has a web UI, typically on port 4040, that displays information about running tasks, executors, and storage usage. Simply go to `http://<driver-node>:4040` in a web browser to access this UI. The [monitoring guide](https://spark.apache.org/docs/latest/monitoring.html) also describes other monitoring options.
# Job Scheduling[](https://spark.apache.org/docs/latest/cluster-overview.html#job-scheduling)
Spark gives control over resource allocation both _across_ applications (at the level of the cluster manager) and _within_ applications (if multiple computations are happening on the same SparkContext). The [job scheduling overview](https://spark.apache.org/docs/latest/job-scheduling.html) describes this in more detail.
# Glossary[](https://spark.apache.org/docs/latest/cluster-overview.html#glossary)
The following table summarizes terms you’ll see used to refer to cluster concepts:
| Term  | Meaning  |
| --- | --- |
| Application  | User program built on Spark. Consists of a _driver program_ and _executors_ on the cluster.  |
| Application jar  |  A jar containing the user's Spark application. In some cases users will want to create an "uber jar" containing their application along with its dependencies. The user's jar should never include Hadoop or Spark libraries, however, these will be added at runtime.   |
| Driver program  | The process running the main() function of the application and creating the SparkContext  |
| Cluster manager  | An external service for acquiring resources on the cluster (e.g. standalone manager, YARN, Kubernetes)  |
| Deploy mode  | Distinguishes where the driver process runs. In "cluster" mode, the framework launches the driver inside of the cluster. In "client" mode, the submitter launches the driver outside of the cluster.  |
| Worker node  | Any node that can run application code in the cluster  |
| Executor  | A process launched for an application on a worker node, that runs tasks and keeps data in memory or disk storage across them. Each application has its own executors.  |
| Task  | A unit of work that will be sent to one executor  |
| Job  | A parallel computation consisting of multiple tasks that gets spawned in response to a Spark action (e.g. `save`, `collect`); you'll see this term used in the driver's logs.  |
| Stage  | Each job gets divided into smaller sets of tasks called _stages_ that depend on each other (similar to the map and reduce stages in MapReduce); you'll see this term used in the driver's logs.  |

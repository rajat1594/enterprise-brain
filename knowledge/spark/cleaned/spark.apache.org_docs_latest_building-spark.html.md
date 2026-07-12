[ ![](https://spark.apache.org/images/spark-logo-rev.svg)](https://spark.apache.org/docs/latest/index.html)4.1.2
  * [Overview](https://spark.apache.org/docs/latest/index.html)
  * [Programming Guides](https://spark.apache.org/docs/latest/building-spark.html)
[Quick Start](https://spark.apache.org/docs/latest/quick-start.html) [RDDs, Accumulators, Broadcasts Vars](https://spark.apache.org/docs/latest/rdd-programming-guide.html) [SQL, DataFrames, and Datasets](https://spark.apache.org/docs/latest/sql-programming-guide.html) [Structured Streaming](https://spark.apache.org/docs/latest/streaming/index.html) [Spark Streaming (DStreams)](https://spark.apache.org/docs/latest/streaming-programming-guide.html) [MLlib (Machine Learning)](https://spark.apache.org/docs/latest/ml-guide.html) [GraphX (Graph Processing)](https://spark.apache.org/docs/latest/graphx-programming-guide.html) [SparkR (R on Spark)](https://spark.apache.org/docs/latest/sparkr.html) [PySpark (Python on Spark)](https://spark.apache.org/docs/latest/api/python/getting_started/index.html) [Declarative Pipelines](https://spark.apache.org/docs/latest/declarative-pipelines-programming-guide.html)
  * [API Docs](https://spark.apache.org/docs/latest/building-spark.html)
[Python](https://spark.apache.org/docs/latest/api/python/index.html) [Scala](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html) [Java](https://spark.apache.org/docs/latest/api/java/index.html) [R](https://spark.apache.org/docs/latest/api/R/index.html) [SQL, Built-in Functions](https://spark.apache.org/docs/latest/api/sql/index.html)
  * [Deploying](https://spark.apache.org/docs/latest/building-spark.html)
[Overview](https://spark.apache.org/docs/latest/cluster-overview.html) [Submitting Applications](https://spark.apache.org/docs/latest/submitting-applications.html) [Spark Standalone](https://spark.apache.org/docs/latest/spark-standalone.html) [YARN](https://spark.apache.org/docs/latest/running-on-yarn.html) [Kubernetes](https://spark.apache.org/docs/latest/running-on-kubernetes.html)
  * [More](https://spark.apache.org/docs/latest/building-spark.html)
[Configuration](https://spark.apache.org/docs/latest/configuration.html) [Monitoring](https://spark.apache.org/docs/latest/monitoring.html) [Tuning Guide](https://spark.apache.org/docs/latest/tuning.html) [Job Scheduling](https://spark.apache.org/docs/latest/job-scheduling.html) [Security](https://spark.apache.org/docs/latest/security.html) [Hardware Provisioning](https://spark.apache.org/docs/latest/hardware-provisioning.html) [Migration Guide](https://spark.apache.org/docs/latest/migration-guide.html) [Building Spark](https://spark.apache.org/docs/latest/building-spark.html) [Contributing to Spark](https://spark.apache.org/contributing.html) [Third Party Projects](https://spark.apache.org/third-party-projects.html)
  *

# Building Spark[](https://spark.apache.org/docs/latest/building-spark.html#building-spark)
  * [Building Apache Spark](https://spark.apache.org/docs/latest/building-spark.html#building-apache-spark)
    * [Apache Maven](https://spark.apache.org/docs/latest/building-spark.html#apache-maven)
      * [Setting up Maven’s Memory Usage](https://spark.apache.org/docs/latest/building-spark.html#setting-up-mavens-memory-usage)
      * [build/mvn](https://spark.apache.org/docs/latest/building-spark.html#buildmvn)
    * [Building a Runnable Distribution](https://spark.apache.org/docs/latest/building-spark.html#building-a-runnable-distribution)
    * [Specifying the Hadoop Version and Enabling YARN](https://spark.apache.org/docs/latest/building-spark.html#specifying-the-hadoop-version-and-enabling-yarn)
    * [Building With Hive and JDBC Support](https://spark.apache.org/docs/latest/building-spark.html#building-with-hive-and-jdbc-support)
    * [Packaging without Hadoop Dependencies for YARN](https://spark.apache.org/docs/latest/building-spark.html#packaging-without-hadoop-dependencies-for-yarn)
    * [Building with Kubernetes support](https://spark.apache.org/docs/latest/building-spark.html#building-with-kubernetes-support)
    * [Building submodules individually](https://spark.apache.org/docs/latest/building-spark.html#building-submodules-individually)
    * [Building with JVM Profile support](https://spark.apache.org/docs/latest/building-spark.html#building-with-jvm-profile-support)
    * [Continuous Compilation](https://spark.apache.org/docs/latest/building-spark.html#continuous-compilation)
    * [Building with SBT](https://spark.apache.org/docs/latest/building-spark.html#building-with-sbt)
      * [Setting up SBT’s Memory Usage](https://spark.apache.org/docs/latest/building-spark.html#setting-up-sbts-memory-usage)
    * [Speeding up Compilation](https://spark.apache.org/docs/latest/building-spark.html#speeding-up-compilation)
    * [Encrypted Filesystems](https://spark.apache.org/docs/latest/building-spark.html#encrypted-filesystems)
    * [IntelliJ IDEA or Eclipse](https://spark.apache.org/docs/latest/building-spark.html#intellij-idea-or-eclipse)
  * [Running Tests](https://spark.apache.org/docs/latest/building-spark.html#running-tests)
    * [Testing with SBT](https://spark.apache.org/docs/latest/building-spark.html#testing-with-sbt)
    * [Running Individual Tests](https://spark.apache.org/docs/latest/building-spark.html#running-individual-tests)
    * [PySpark pip installable](https://spark.apache.org/docs/latest/building-spark.html#pyspark-pip-installable)
    * [PySpark Tests with Maven or SBT](https://spark.apache.org/docs/latest/building-spark.html#pyspark-tests-with-maven-or-sbt)
    * [Running R Tests (deprecated)](https://spark.apache.org/docs/latest/building-spark.html#running-r-tests-deprecated)
    * [Running Docker-based Integration Test Suites](https://spark.apache.org/docs/latest/building-spark.html#running-docker-based-integration-test-suites)
  * [Building and testing on an IPv6-only environment](https://spark.apache.org/docs/latest/building-spark.html#building-and-testing-on-an-ipv6-only-environment)
  * [Building with a user-defined `protoc`](https://spark.apache.org/docs/latest/building-spark.html#building-with-a-user-defined-protoc)

# Building Apache Spark[](https://spark.apache.org/docs/latest/building-spark.html#building-apache-spark)
## Apache Maven[](https://spark.apache.org/docs/latest/building-spark.html#apache-maven)
The Maven-based build is the build of reference for Apache Spark. Building Spark using Maven requires Maven 3.9.9 and Java 17/21. Spark requires Scala 2.13; support for Scala 2.12 was removed in Spark 4.0.0.
### Setting up Maven’s Memory Usage[](https://spark.apache.org/docs/latest/building-spark.html#setting-up-mavens-memory-usage)
You’ll need to configure Maven to use more memory than usual by setting `MAVEN_OPTS`:

```
export MAVEN_OPTS="-Xss64m -Xmx2g -XX:ReservedCodeCacheSize=1g"

```

(The `ReservedCodeCacheSize` setting is optional but recommended.) If you don’t add these parameters to `MAVEN_OPTS`, you may see errors and warnings like the following:

```
[INFO] Compiling 203 Scala sources and 9 Java sources to /Users/me/Development/spark/core/target/scala-2.13/classes...
[ERROR] Java heap space -> [Help 1]

```

You can fix these problems by setting the `MAVEN_OPTS` variable as discussed before.
**Note:**
  * If using `build/mvn` with no `MAVEN_OPTS` set, the script will automatically add the above options to the `MAVEN_OPTS` environment variable.
  * The `test` phase of the Spark build will automatically add these options to `MAVEN_OPTS`, even when not using `build/mvn`.

### build/mvn[](https://spark.apache.org/docs/latest/building-spark.html#buildmvn)
Spark now comes packaged with a self-contained Maven installation to ease building and deployment of Spark from source located under the `build/` directory. This script will automatically download and setup all necessary build requirements ([Maven](https://maven.apache.org/), [Scala](https://www.scala-lang.org/)) locally within the `build/` directory itself. It honors any `mvn` binary if present already, however, will pull down its own copy of Scala regardless to ensure proper version requirements are met. `build/mvn` execution acts as a pass through to the `mvn` call allowing easy transition from previous build methods. As an example, one can build a version of Spark as follows:

```
./build/mvn -DskipTests clean package

```

Other build examples can be found below.
## Building a Runnable Distribution[](https://spark.apache.org/docs/latest/building-spark.html#building-a-runnable-distribution)
To create a Spark distribution like those distributed by the [Spark Downloads](https://spark.apache.org/downloads.html) page, and that is laid out so as to be runnable, use `./dev/make-distribution.sh` in the project root directory. By default, it uses Maven as building tool, and can be configured with Maven profile settings and so on like the direct Maven build. Example:

```
./dev/make-distribution.sh --name custom-spark --pip --r --tgz -Psparkr -Phive -Phive-thriftserver -Pyarn -Pkubernetes

```

This will build Spark distribution along with Python pip and R packages.
To switch to SBT (experimental), use `--sbt-enabled`. Example:

```
./dev/make-distribution.sh --name custom-spark --pip --r --tgz --sbt-enabled -Psparkr -Phive -Phive-thriftserver -Pyarn -Pkubernetes

```

For more information on usage, run `./dev/make-distribution.sh --help`
## Specifying the Hadoop Version and Enabling YARN[](https://spark.apache.org/docs/latest/building-spark.html#specifying-the-hadoop-version-and-enabling-yarn)
You can enable the `yarn` profile and specify the exact version of Hadoop to compile against through the `hadoop.version` property.
Example:

```
./build/mvn -Pyarn -Dhadoop.version=3.4.1 -DskipTests clean package

```

## Building With Hive and JDBC Support[](https://spark.apache.org/docs/latest/building-spark.html#building-with-hive-and-jdbc-support)
To enable Hive integration for Spark SQL along with its JDBC server and CLI, add the `-Phive` and `-Phive-thriftserver` profiles to your existing build options. By default Spark will build with Hive 2.3.10.

```
# With Hive 2.3.10 support
./build/mvn -Pyarn -Phive -Phive-thriftserver -DskipTests clean package

```

## Packaging without Hadoop Dependencies for YARN[](https://spark.apache.org/docs/latest/building-spark.html#packaging-without-hadoop-dependencies-for-yarn)
The assembly directory produced by `mvn package` will, by default, include all of Spark’s dependencies, including Hadoop and some of its ecosystem projects. On YARN deployments, this causes multiple versions of these to appear on executor classpaths: the version packaged in the Spark assembly and the version on each node, included with `yarn.application.classpath`. The `hadoop-provided` profile builds the assembly without including Hadoop-ecosystem projects, like ZooKeeper and Hadoop itself.
## Building with Kubernetes support[](https://spark.apache.org/docs/latest/building-spark.html#building-with-kubernetes-support)

```
./build/mvn -Pkubernetes -DskipTests clean package

```

## Building submodules individually[](https://spark.apache.org/docs/latest/building-spark.html#building-submodules-individually)
It’s possible to build Spark submodules using the `mvn -pl` option.
For instance, you can build the Spark Streaming module using:

```
./build/mvn -pl :spark-streaming_2.13 clean install

```

where `spark-streaming_2.13` is the `artifactId` as defined in `streaming/pom.xml` file.
## Building with JVM Profile support[](https://spark.apache.org/docs/latest/building-spark.html#building-with-jvm-profile-support)

```
./build/mvn -Pjvm-profiler -DskipTests clean package

```

**Note:** The `jvm-profiler` profile builds the assembly without including the dependency `ap-loader`, you can download it manually from maven central repo and use it together with `spark-profiler_2.13`.
## Continuous Compilation[](https://spark.apache.org/docs/latest/building-spark.html#continuous-compilation)
We use the scala-maven-plugin which supports incremental and continuous compilation. E.g.

```
./build/mvn scala:cc

```

should run continuous compilation (i.e. wait for changes). However, this has not been tested extensively. A couple of gotchas to note:
  * it only scans the paths `src/main` and `src/test` (see [docs](https://davidb.github.io/scala-maven-plugin/example_cc.html)), so it will only work from within certain submodules that have that structure.
  * you’ll typically need to run `mvn install` from the project root for compilation within specific submodules to work; this is because submodules that depend on other submodules do so via the `spark-parent` module).

Thus, the full flow for running continuous-compilation of the `core` submodule may look more like:

```
$ ./build/mvn install
$ cd core
$ ../build/mvn scala:cc

```

## Building with SBT[](https://spark.apache.org/docs/latest/building-spark.html#building-with-sbt)
Maven is the official build tool recommended for packaging Spark, and is the _build of reference_. But SBT is supported for day-to-day development since it can provide much faster iterative compilation. More advanced developers may wish to use SBT.
The SBT build is derived from the Maven POM files, and so the same Maven profiles and variables can be set to control the SBT build. For example:

```
./build/sbt package

```

To avoid the overhead of launching sbt each time you need to re-compile, you can launch sbt in interactive mode by running `build/sbt`, and then run all build commands at the command prompt.
### Setting up SBT’s Memory Usage[](https://spark.apache.org/docs/latest/building-spark.html#setting-up-sbts-memory-usage)
Configure the JVM options for SBT in `.jvmopts` at the project root, for example:

```
-Xmx2g
-XX:ReservedCodeCacheSize=1g

```

For the meanings of these two options, please carefully read the [Setting up Maven’s Memory Usage section](https://spark.apache.org/docs/latest/building-spark.html#setting-up-mavens-memory-usage).
## Speeding up Compilation[](https://spark.apache.org/docs/latest/building-spark.html#speeding-up-compilation)
Developers who compile Spark frequently may want to speed up compilation; e.g., by avoiding re-compilation of the assembly JAR (for developers who build with SBT). For more information about how to do this, refer to the [Useful Developer Tools page](https://spark.apache.org/developer-tools.html#reducing-build-times).
## Encrypted Filesystems[](https://spark.apache.org/docs/latest/building-spark.html#encrypted-filesystems)
When building on an encrypted filesystem (if your home directory is encrypted, for example), then the Spark build might fail with a “Filename too long” error. As a workaround, add the following in the configuration args of the `scala-maven-plugin` in the project `pom.xml`:

```
<arg>-Xmax-classfile-name</arg>
<arg>128</arg>

```

and in `project/SparkBuild.scala` add:

```
scalacOptions in Compile ++= Seq("-Xmax-classfile-name", "128"),

```

to the `sharedSettings` val. See also [this PR](https://github.com/apache/spark/pull/2883/files) if you are unsure of where to add these lines.
## IntelliJ IDEA or Eclipse[](https://spark.apache.org/docs/latest/building-spark.html#intellij-idea-or-eclipse)
For help in setting up IntelliJ IDEA or Eclipse for Spark development, and troubleshooting, refer to the [Useful Developer Tools page](https://spark.apache.org/developer-tools.html).
# Running Tests[](https://spark.apache.org/docs/latest/building-spark.html#running-tests)
Tests are run by default via the [ScalaTest Maven plugin](http://www.scalatest.org/user_guide/using_the_scalatest_maven_plugin). Note that tests should not be run as root or an admin user.
The following is an example of a command to run the tests:

```
./build/mvn test

```

## Testing with SBT[](https://spark.apache.org/docs/latest/building-spark.html#testing-with-sbt)
The following is an example of a command to run the tests:

```
./build/sbt test

```

## Running Individual Tests[](https://spark.apache.org/docs/latest/building-spark.html#running-individual-tests)
For information about how to run individual tests, refer to the [Useful Developer Tools page](https://spark.apache.org/developer-tools.html#running-individual-tests).
## PySpark pip installable[](https://spark.apache.org/docs/latest/building-spark.html#pyspark-pip-installable)
If you are building Spark for use in a Python environment and you wish to pip install it, you will first need to build the Spark JARs as described above. Then you can construct an sdist package suitable for setup.py and pip installable package.

```
cd python; python packaging/classic/setup.py sdist

```

**Note:** Due to packaging requirements you can not directly pip install from the Python directory, rather you must first build the sdist package as described above.
Alternatively, you can also run `make-distribution.sh` with the `--pip` option.
## PySpark Tests with Maven or SBT[](https://spark.apache.org/docs/latest/building-spark.html#pyspark-tests-with-maven-or-sbt)
If you are building PySpark and wish to run the PySpark tests you will need to build Spark with Hive support.

```
./build/mvn -DskipTests clean package -Phive
./python/run-tests

```

If you are building PySpark with SBT and wish to run the PySpark tests, you will need to build Spark with Hive support and also build the test components:

```
./build/sbt -Phive clean package
./build/sbt test:compile
./python/run-tests

```

The run-tests script also can be limited to a specific Python version or a specific module

```
./python/run-tests --python-executables=python --modules=pyspark-sql

```

## Running R Tests (deprecated)[](https://spark.apache.org/docs/latest/building-spark.html#running-r-tests-deprecated)
To run the SparkR tests you will need to install the [knitr](https://cran.r-project.org/package=knitr), [rmarkdown](https://cran.r-project.org/package=rmarkdown), [testthat](https://cran.r-project.org/package=testthat), [e1071](https://cran.r-project.org/package=e1071) and [survival](https://cran.r-project.org/package=survival) packages first:

```
Rscript -e "install.packages(c('knitr', 'rmarkdown', 'testthat', 'e1071', 'survival'), repos='https://cloud.r-project.org/')"

```

You can run just the SparkR tests using the command:

```
./R/run-tests.sh

```

## Running Docker-based Integration Test Suites[](https://spark.apache.org/docs/latest/building-spark.html#running-docker-based-integration-test-suites)
In order to run Docker integration tests, you have to install the `docker` engine on your box. The instructions for installation can be found at [the Docker site](https://docs.docker.com/engine/installation/). Once installed, the `docker` service needs to be started, if not already running. On Linux, this can be done by `sudo service docker start`.

```
./build/mvn install -DskipTests
./build/mvn test -Pdocker-integration-tests -pl :spark-docker-integration-tests_2.13

```

or

```
./build/sbt -Pdocker-integration-tests docker-integration-tests/test

```

# Building and testing on an IPv6-only environment[](https://spark.apache.org/docs/latest/building-spark.html#building-and-testing-on-an-ipv6-only-environment)
Use Apache Spark GitBox URL because GitHub doesn’t support IPv6 yet.

```
https://gitbox.apache.org/repos/asf/spark.git

```

To build and run tests on IPv6-only environment, the following configurations are required.

```
export SPARK_LOCAL_HOSTNAME="your-IPv6-address" # e.g. '[2600:1700:232e:3de0:...]'
export DEFAULT_ARTIFACT_REPOSITORY=https://ipv6.repo1.maven.org/maven2/
export MAVEN_OPTS="-Djava.net.preferIPv6Addresses=true"
export SBT_OPTS="-Djava.net.preferIPv6Addresses=true"
export SERIAL_SBT_TESTS=1

```

# Building with a user-defined `protoc`[](https://spark.apache.org/docs/latest/building-spark.html#building-with-a-user-defined-protoc)
When the user cannot use the official `protoc` binary files to build the `core` module in the compilation environment, for example, compiling `core` module on CentOS 6 or CentOS 7 which the default `glibc` version is less than 2.14, we can try to compile and test by specifying the user-defined `protoc` binary files as follows:

```
export SPARK_PROTOC_EXEC_PATH=/path-to-protoc-exe
./build/mvn -Puser-defined-protoc -DskipDefaultProtoc clean package

```

or

```
export SPARK_PROTOC_EXEC_PATH=/path-to-protoc-exe
./build/sbt -Puser-defined-protoc clean package

```

The user-defined `protoc` binary files can be produced in the user’s compilation environment by source code compilation, for compilation steps, please refer to [protobuf](https://github.com/protocolbuffers/protobuf).

[ ![](https://spark.apache.org/images/spark-logo-rev.svg)](https://spark.apache.org/docs/latest/index.html)4.1.2
  * [Overview](https://spark.apache.org/docs/latest/index.html)
  * [Programming Guides](https://spark.apache.org/docs/latest/ml-linalg-guide.html)
[Quick Start](https://spark.apache.org/docs/latest/quick-start.html) [RDDs, Accumulators, Broadcasts Vars](https://spark.apache.org/docs/latest/rdd-programming-guide.html) [SQL, DataFrames, and Datasets](https://spark.apache.org/docs/latest/sql-programming-guide.html) [Structured Streaming](https://spark.apache.org/docs/latest/streaming/index.html) [Spark Streaming (DStreams)](https://spark.apache.org/docs/latest/streaming-programming-guide.html) [MLlib (Machine Learning)](https://spark.apache.org/docs/latest/ml-guide.html) [GraphX (Graph Processing)](https://spark.apache.org/docs/latest/graphx-programming-guide.html) [SparkR (R on Spark)](https://spark.apache.org/docs/latest/sparkr.html) [PySpark (Python on Spark)](https://spark.apache.org/docs/latest/api/python/getting_started/index.html) [Declarative Pipelines](https://spark.apache.org/docs/latest/declarative-pipelines-programming-guide.html)
  * [API Docs](https://spark.apache.org/docs/latest/ml-linalg-guide.html)
[Python](https://spark.apache.org/docs/latest/api/python/index.html) [Scala](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html) [Java](https://spark.apache.org/docs/latest/api/java/index.html) [R](https://spark.apache.org/docs/latest/api/R/index.html) [SQL, Built-in Functions](https://spark.apache.org/docs/latest/api/sql/index.html)
  * [Deploying](https://spark.apache.org/docs/latest/ml-linalg-guide.html)
[Overview](https://spark.apache.org/docs/latest/cluster-overview.html) [Submitting Applications](https://spark.apache.org/docs/latest/submitting-applications.html) [Spark Standalone](https://spark.apache.org/docs/latest/spark-standalone.html) [YARN](https://spark.apache.org/docs/latest/running-on-yarn.html) [Kubernetes](https://spark.apache.org/docs/latest/running-on-kubernetes.html)
  * [More](https://spark.apache.org/docs/latest/ml-linalg-guide.html)
[Configuration](https://spark.apache.org/docs/latest/configuration.html) [Monitoring](https://spark.apache.org/docs/latest/monitoring.html) [Tuning Guide](https://spark.apache.org/docs/latest/tuning.html) [Job Scheduling](https://spark.apache.org/docs/latest/job-scheduling.html) [Security](https://spark.apache.org/docs/latest/security.html) [Hardware Provisioning](https://spark.apache.org/docs/latest/hardware-provisioning.html) [Migration Guide](https://spark.apache.org/docs/latest/migration-guide.html) [Building Spark](https://spark.apache.org/docs/latest/building-spark.html) [Contributing to Spark](https://spark.apache.org/contributing.html) [Third Party Projects](https://spark.apache.org/third-party-projects.html)
  *

###  [MLlib: Main Guide](https://spark.apache.org/docs/latest/ml-guide.html)[](https://spark.apache.org/docs/latest/ml-linalg-guide.html#mllib-main-guide)
  * [ Basic statistics ](https://spark.apache.org/docs/latest/ml-statistics.html)
  * [ Data sources ](https://spark.apache.org/docs/latest/ml-datasource.html)
  * [ Pipelines ](https://spark.apache.org/docs/latest/ml-pipeline.html)
  * [ Extracting, transforming and selecting features ](https://spark.apache.org/docs/latest/ml-features.html)
  * [ Classification and Regression ](https://spark.apache.org/docs/latest/ml-classification-regression.html)
  * [ Clustering ](https://spark.apache.org/docs/latest/ml-clustering.html)
  * [ Collaborative filtering ](https://spark.apache.org/docs/latest/ml-collaborative-filtering.html)
  * [ Frequent Pattern Mining ](https://spark.apache.org/docs/latest/ml-frequent-pattern-mining.html)
  * [ Model selection and tuning ](https://spark.apache.org/docs/latest/ml-tuning.html)
  * [ Advanced topics ](https://spark.apache.org/docs/latest/ml-advanced.html)

###  [MLlib: RDD-based API Guide](https://spark.apache.org/docs/latest/mllib-guide.html)[](https://spark.apache.org/docs/latest/ml-linalg-guide.html#mllib-rdd-based-api-guide)
  * [ Data types ](https://spark.apache.org/docs/latest/mllib-data-types.html)
  * [ Basic statistics ](https://spark.apache.org/docs/latest/mllib-statistics.html)
  * [ Classification and regression ](https://spark.apache.org/docs/latest/mllib-classification-regression.html)
  * [ Collaborative filtering ](https://spark.apache.org/docs/latest/mllib-collaborative-filtering.html)
  * [ Clustering ](https://spark.apache.org/docs/latest/mllib-clustering.html)
  * [ Dimensionality reduction ](https://spark.apache.org/docs/latest/mllib-dimensionality-reduction.html)
  * [ Feature extraction and transformation ](https://spark.apache.org/docs/latest/mllib-feature-extraction.html)
  * [ Frequent pattern mining ](https://spark.apache.org/docs/latest/mllib-frequent-pattern-mining.html)
  * [ Evaluation metrics ](https://spark.apache.org/docs/latest/mllib-evaluation-metrics.html)
  * [ PMML model export ](https://spark.apache.org/docs/latest/mllib-pmml-model-export.html)
  * [ Optimization (developer) ](https://spark.apache.org/docs/latest/mllib-optimization.html)

# MLlib Linear Algebra Acceleration Guide[](https://spark.apache.org/docs/latest/ml-linalg-guide.html#mllib-linear-algebra-acceleration-guide)
## Introduction[](https://spark.apache.org/docs/latest/ml-linalg-guide.html#introduction)
This guide provides necessary information to enable accelerated linear algebra processing for Spark MLlib.
Spark MLlib defines Vector and Matrix as basic data types for machine learning algorithms. On top of them, [BLAS](https://en.wikipedia.org/wiki/Basic_Linear_Algebra_Subprograms) and [LAPACK](https://en.wikipedia.org/wiki/LAPACK) operations are implemented and supported by [dev.ludovic.netlib](https://github.com/luhenry/netlib) (the algorithms may also call [Breeze](https://github.com/scalanlp/breeze)). `dev.ludovic.netlib` can use optimized native linear algebra libraries (referred to as “native libraries” or “BLAS libraries” hereafter) for faster numerical processing. [Intel MKL](https://software.intel.com/content/www/us/en/develop/tools/math-kernel-library.html) and [OpenBLAS](http://www.openblas.net) are two popular ones.
The official released Spark binaries don’t contain these native libraries.
The following sections describe how to install native libraries, configure them properly, and how to point `dev.ludovic.netlib` to these native libraries.
## Install native linear algebra libraries[](https://spark.apache.org/docs/latest/ml-linalg-guide.html#install-native-linear-algebra-libraries)
Intel MKL and OpenBLAS are two popular native linear algebra libraries. You can choose one of them based on your preference. We provide basic instructions as below.
### Intel MKL[](https://spark.apache.org/docs/latest/ml-linalg-guide.html#intel-mkl)
  * Download and install Intel MKL. The installation should be done on all nodes of the cluster. We assume the installation location is $MKLROOT (e.g. /opt/intel/mkl).
  * Create soft links to `libmkl_rt.so` with specific names in system library search paths. For instance, make sure `/usr/local/lib` is in system library search paths and run the following commands:

```
$ ln -sf $MKLROOT/lib/intel64/libmkl_rt.so /usr/local/lib/libblas.so.3
$ ln -sf $MKLROOT/lib/intel64/libmkl_rt.so /usr/local/lib/liblapack.so.3

```

### OpenBLAS[](https://spark.apache.org/docs/latest/ml-linalg-guide.html#openblas)
The installation should be done on all nodes of the cluster. Generic version of OpenBLAS are available with most distributions. You can install it with a distribution package manager like `apt` or `yum`.
For Debian / Ubuntu:

```
sudo apt-get install libopenblas-base
sudo update-alternatives --config libblas.so.3

```

For CentOS / RHEL:

```
sudo yum install openblas

```

## Check if native libraries are enabled for MLlib[](https://spark.apache.org/docs/latest/ml-linalg-guide.html#check-if-native-libraries-are-enabled-for-mllib)
To verify native libraries are properly loaded, start `spark-shell` and run the following code:

```
scala> import dev.ludovic.netlib.blas.NativeBLAS
scala> NativeBLAS.getInstance()

```

If they are correctly loaded, it should print `dev.ludovic.netlib.blas.NativeBLAS = dev.ludovic.netlib.blas.JNIBLAS@...`. Otherwise the warnings should be printed:

```
WARN InstanceBuilder: Failed to load implementation from:dev.ludovic.netlib.blas.JNIBLAS
...
java.lang.RuntimeException: Unable to load native implementation
  at dev.ludovic.netlib.blas.InstanceBuilder.nativeBlas(InstanceBuilder.java:59)
  at dev.ludovic.netlib.blas.NativeBLAS.getInstance(NativeBLAS.java:31)
  ...

```

You can also point `dev.ludovic.netlib` to specific libraries names and paths. For example, `-Ddev.ludovic.netlib.blas.nativeLib=libmkl_rt.so` or `-Ddev.ludovic.netlib.blas.nativeLibPath=$MKLROOT/lib/intel64/libmkl_rt.so` for Intel MKL. You have similar parameters for LAPACK and ARPACK: `-Ddev.ludovic.netlib.lapack.nativeLib=...`, `-Ddev.ludovic.netlib.lapack.nativeLibPath=...`, `-Ddev.ludovic.netlib.arpack.nativeLib=...`, and `-Ddev.ludovic.netlib.arpack.nativeLibPath=...`.
If native libraries are not properly configured in the system, the Java implementation (javaBLAS) will be used as fallback option.
## Spark Configuration[](https://spark.apache.org/docs/latest/ml-linalg-guide.html#spark-configuration)
The default behavior of multi-threading in either Intel MKL or OpenBLAS may not be optimal with Spark’s execution model [1](https://spark.apache.org/docs/latest/ml-linalg-guide.html#fn:1).
Therefore configuring these native libraries to use a single thread for operations may actually improve performance (see [SPARK-21305](https://issues.apache.org/jira/browse/SPARK-21305)). It is usually optimal to match this to the number of `spark.task.cpus`, which is `1` by default and typically left at `1`.
You can use the options in `config/spark-env.sh` to set thread number for Intel MKL or OpenBLAS:
  * For Intel MKL:

```
MKL_NUM_THREADS=1

```

  * For OpenBLAS:

```
OPENBLAS_NUM_THREADS=1

```

  1. Please refer to the following resources to understand how to configure the number of threads for these BLAS implementations: [Intel MKL](https://software.intel.com/en-us/articles/recommended-settings-for-calling-intel-mkl-routines-from-multi-threaded-applications) or [Intel oneMKL](https://software.intel.com/en-us/onemkl-linux-developer-guide-improving-performance-with-threading) and [OpenBLAS](https://github.com/xianyi/OpenBLAS/wiki/faq#multi-threaded). [↩](https://spark.apache.org/docs/latest/ml-linalg-guide.html#fnref:1)

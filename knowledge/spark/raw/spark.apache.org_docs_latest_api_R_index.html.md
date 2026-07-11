[Skip to contents](https://spark.apache.org/docs/latest/api/R/index.html#main)
[ ![](https://spark.apache.org/images/spark-logo-rev.svg)](https://spark.apache.org/) [SparkR](https://spark.apache.org/docs/latest/api/R/index.html) 4.1.2
  * [Reference](https://spark.apache.org/docs/latest/api/R/reference/index.html)
  * [Articles](https://spark.apache.org/docs/latest/api/R/index.html)
[SparkR - Practical Guide](https://spark.apache.org/docs/latest/api/R/articles/sparkr-vignettes.html)


  * 

# R on Spark (deprecated)[](https://spark.apache.org/docs/latest/api/R/index.html#r-on-spark-deprecated)
SparkR is an R package that provides a light-weight frontend to use Spark from R.
### Installing sparkR[](https://spark.apache.org/docs/latest/api/R/index.html#installing-sparkr)
Libraries of sparkR need to be created in `$SPARK_HOME/R/lib`. This can be done by running the script `$SPARK_HOME/R/install-dev.sh`. By default the above script uses the system wide installation of R. However, this can be changed to any user installed location of R by setting the environment variable `R_HOME` the full path of the base directory where R is installed, before running install-dev.sh script. Example:

```
[](https://spark.apache.org/docs/latest/api/R/index.html#cb1-1)# where /home/username/R is where R is installed and /home/username/R/bin contains the files R and RScript
[](https://spark.apache.org/docs/latest/api/R/index.html#cb1-2)export R_HOME=/home/username/R
[](https://spark.apache.org/docs/latest/api/R/index.html#cb1-3)./install-dev.sh
```

### SparkR development[](https://spark.apache.org/docs/latest/api/R/index.html#sparkr-development)
#### Build Spark[](https://spark.apache.org/docs/latest/api/R/index.html#build-spark)
Build Spark with [Maven](https://spark.apache.org/docs/latest/building-spark.html#buildmvn) or [SBT](https://spark.apache.org/docs/latest/building-spark.html#building-with-sbt), and include the `-Psparkr` profile to build the R package. For example to use the default Hadoop versions you can run

```
[](https://spark.apache.org/docs/latest/api/R/index.html#cb2-1)# Maven
[](https://spark.apache.org/docs/latest/api/R/index.html#cb2-2)./build/mvn -DskipTests -Psparkr package
[](https://spark.apache.org/docs/latest/api/R/index.html#cb2-3)
[](https://spark.apache.org/docs/latest/api/R/index.html#cb2-4)# SBT
[](https://spark.apache.org/docs/latest/api/R/index.html#cb2-5)./build/sbt -Psparkr package
```

#### Running sparkR[](https://spark.apache.org/docs/latest/api/R/index.html#running-sparkr)
You can start using SparkR by launching the SparkR shell with

```
[](https://spark.apache.org/docs/latest/api/R/index.html#cb3-1)./bin/sparkR
```

The `sparkR` script automatically creates a SparkContext with Spark by default in local mode. To specify the Spark master of a cluster for the automatically created SparkContext, you can run

```
[](https://spark.apache.org/docs/latest/api/R/index.html#cb4-1)./bin/sparkR --master "local[2]"
```

To set other options like driver memory, executor memory etc. you can pass in the [spark-submit](https://spark.apache.org/docs/latest/submitting-applications.html) arguments to `./bin/sparkR`
#### Using SparkR from RStudio[](https://spark.apache.org/docs/latest/api/R/index.html#using-sparkr-from-rstudio)
If you wish to use SparkR from RStudio, please refer [SparkR documentation](https://spark.apache.org/docs/latest/sparkr.html#starting-up-from-rstudio).
#### Making changes to SparkR[](https://spark.apache.org/docs/latest/api/R/index.html#making-changes-to-sparkr)
The [instructions](https://spark.apache.org/contributing.html) for making contributions to Spark also apply to SparkR. If you only make R file changes (i.e. no Scala changes) then you can just re-install the R package using `R/install-dev.sh` and test your changes. Once you have made your changes, please include unit tests for them and run existing unit tests using the `R/run-tests.sh` script as described below.
#### Generating documentation[](https://spark.apache.org/docs/latest/api/R/index.html#generating-documentation)
The SparkR documentation (Rd files and HTML files) are not a part of the source repository. To generate them you can run the script `R/create-docs.sh`. This script uses `roxygen2`, `knitr`, and `rmarkdown` to generate the docs and these packages need to be installed on the machine before using the script. Also, you may need to install these [prerequisites](https://github.com/apache/spark/tree/master/docs#prerequisites). See also, `R/DOCUMENTATION.md`
### Examples, Unit tests[](https://spark.apache.org/docs/latest/api/R/index.html#examples-unit-tests)
SparkR comes with several sample programs in the `examples/src/main/r` directory. To run one of them, use `./bin/spark-submit <filename> <args>`. For example:

```
[](https://spark.apache.org/docs/latest/api/R/index.html#cb5-1)./bin/spark-submit examples/src/main/r/dataframe.R
```

You can run R unit tests by following the instructions under [Running R Tests](https://spark.apache.org/docs/latest/building-spark.html#running-r-tests).
### Running on YARN[](https://spark.apache.org/docs/latest/api/R/index.html#running-on-yarn)
The `./bin/spark-submit` can also be used to submit jobs to YARN clusters. You will need to set YARN conf dir before doing so. For example on CDH you can run

```
[](https://spark.apache.org/docs/latest/api/R/index.html#cb6-1)export YARN_CONF_DIR=/etc/hadoop/conf
[](https://spark.apache.org/docs/latest/api/R/index.html#cb6-2)./bin/spark-submit --master yarn examples/src/main/r/dataframe.R
```

## Links
  * [View on CRAN](https://cloud.r-project.org/package=SparkR)
  * [Report a bug](https://spark.apache.org/contributing.html)


## License
  * Apache License (== 2.0)


## Citation
  * [Citing SparkR](https://spark.apache.org/docs/latest/api/R/authors.html#citation)


## Developers
  * [ The Apache Software Foundation](https://www.apache.org/)   
Author, maintainer, copyright holder 


Developed by [ The Apache Software Foundation](https://www.apache.org/).
Site built with [pkgdown](https://pkgdown.r-lib.org/) 2.0.1.
Using [preferably](https://preferably.amirmasoudabdol.name/?source=footer) template.

[Skip to contents](https://spark.apache.org/docs/latest/api/R/reference/index.html#main)
[ ![](https://spark.apache.org/images/spark-logo-rev.svg)](https://spark.apache.org/) [SparkR](https://spark.apache.org/docs/latest/api/R/index.html) 4.1.2
  * [Reference](https://spark.apache.org/docs/latest/api/R/reference/index.html)
  * [Articles](https://spark.apache.org/docs/latest/api/R/reference/index.html)
[SparkR - Practical Guide](https://spark.apache.org/docs/latest/api/R/articles/sparkr-vignettes.html)


  * 

![](https://spark.apache.org/docs/latest/api/R/reference/index.html)
# Function reference
## Distributed Data Frame[](https://spark.apache.org/docs/latest/api/R/reference/index.html#distributed-data-frame) 

`SparkDataFrame-class[](https://spark.apache.org/docs/latest/api/R/reference/SparkDataFrame.html)` 
    S4 class that represents a SparkDataFrame 

`groupedData()[](https://spark.apache.org/docs/latest/api/R/reference/GroupedData.html)` 
    S4 class that represents a GroupedData 

`agg()[](https://spark.apache.org/docs/latest/api/R/reference/summarize.html)` `summarize()[](https://spark.apache.org/docs/latest/api/R/reference/summarize.html)` 
    summarize 

`arrange()[](https://spark.apache.org/docs/latest/api/R/reference/arrange.html)` `orderBy([_<SparkDataFrame>_,_<characterOrColumn>_)](https://spark.apache.org/docs/latest/api/R/reference/arrange.html)`
    Arrange Rows by Variables 

`approxQuantile([_<SparkDataFrame>_,_<character>_,_<numeric>_,_<numeric>_)](https://spark.apache.org/docs/latest/api/R/reference/approxQuantile.html)`
    Calculates the approximate quantiles of numerical columns of a SparkDataFrame 

`as.data.frame()[](https://spark.apache.org/docs/latest/api/R/reference/as.data.frame.html)` 
    Download data from a SparkDataFrame into a R data.frame 

`attach([_<SparkDataFrame>_)](https://spark.apache.org/docs/latest/api/R/reference/attach.html)`
    Attach SparkDataFrame to R search path 

`broadcast()[](https://spark.apache.org/docs/latest/api/R/reference/broadcast.html)` 
    broadcast 

`cache()[](https://spark.apache.org/docs/latest/api/R/reference/cache.html)` 
    Cache 

`cacheTable()[](https://spark.apache.org/docs/latest/api/R/reference/cacheTable.html)` 
    Cache Table 

`checkpoint()[](https://spark.apache.org/docs/latest/api/R/reference/checkpoint.html)` 
    checkpoint 

`collect()[](https://spark.apache.org/docs/latest/api/R/reference/collect.html)` 
    Collects all the elements of a SparkDataFrame and coerces them into an R data.frame. 

`coltypes()[](https://spark.apache.org/docs/latest/api/R/reference/coltypes.html)` ``coltypes<-`()[](https://spark.apache.org/docs/latest/api/R/reference/coltypes.html)` 
    coltypes 

`colnames()[](https://spark.apache.org/docs/latest/api/R/reference/columns.html)` ``colnames<-`()[](https://spark.apache.org/docs/latest/api/R/reference/columns.html)` `columns()[](https://spark.apache.org/docs/latest/api/R/reference/columns.html)` `names([_<SparkDataFrame>_)](https://spark.apache.org/docs/latest/api/R/reference/columns.html)```names<-`([_<SparkDataFrame>_)](https://spark.apache.org/docs/latest/api/R/reference/columns.html)`
    Column Names of SparkDataFrame 

`count()[](https://spark.apache.org/docs/latest/api/R/reference/count.html)` `n()[](https://spark.apache.org/docs/latest/api/R/reference/count.html)` 
    Count 

`createDataFrame()[](https://spark.apache.org/docs/latest/api/R/reference/createDataFrame.html)` `as.DataFrame()[](https://spark.apache.org/docs/latest/api/R/reference/createDataFrame.html)` 
    Create a SparkDataFrame 

`createExternalTable()[](https://spark.apache.org/docs/latest/api/R/reference/createExternalTable-deprecated.html)` 
    (Deprecated) Create an external table 

`createOrReplaceTempView()[](https://spark.apache.org/docs/latest/api/R/reference/createOrReplaceTempView.html)` 
    Creates a temporary view using the given name. 

`createTable()[](https://spark.apache.org/docs/latest/api/R/reference/createTable.html)` 
    Creates a table based on the dataset in a data source 

`crossJoin([_<SparkDataFrame>_,_<SparkDataFrame>_)](https://spark.apache.org/docs/latest/api/R/reference/crossJoin.html)`
    CrossJoin 

`crosstab([_<SparkDataFrame>_,_<character>_,_<character>_)](https://spark.apache.org/docs/latest/api/R/reference/crosstab.html)`
    Computes a pair-wise frequency table of the given columns 

`cube()[](https://spark.apache.org/docs/latest/api/R/reference/cube.html)` 
    cube 

`describe()[](https://spark.apache.org/docs/latest/api/R/reference/describe.html)` 
    describe 

`distinct()[](https://spark.apache.org/docs/latest/api/R/reference/distinct.html)` `unique([_<SparkDataFrame>_)](https://spark.apache.org/docs/latest/api/R/reference/distinct.html)`
    Distinct 

`dim([_<SparkDataFrame>_)](https://spark.apache.org/docs/latest/api/R/reference/dim.html)`
    Returns the dimensions of SparkDataFrame 

`drop()[](https://spark.apache.org/docs/latest/api/R/reference/drop.html)` 
    drop 

`dropDuplicates()[](https://spark.apache.org/docs/latest/api/R/reference/dropDuplicates.html)` 
    dropDuplicates 

`dropna()[](https://spark.apache.org/docs/latest/api/R/reference/nafunctions.html)` `na.omit()[](https://spark.apache.org/docs/latest/api/R/reference/nafunctions.html)` `fillna()[](https://spark.apache.org/docs/latest/api/R/reference/nafunctions.html)` 
    A set of SparkDataFrame functions working with NA values 

`dtypes()[](https://spark.apache.org/docs/latest/api/R/reference/dtypes.html)` 
    DataTypes 

`except()[](https://spark.apache.org/docs/latest/api/R/reference/except.html)` 
    except 

`exceptAll()[](https://spark.apache.org/docs/latest/api/R/reference/exceptAll.html)` 
    exceptAll 

`explain()[](https://spark.apache.org/docs/latest/api/R/reference/explain.html)` 
    Explain 

`filter()[](https://spark.apache.org/docs/latest/api/R/reference/filter.html)` `where()[](https://spark.apache.org/docs/latest/api/R/reference/filter.html)` 
    Filter 

`getNumPartitions([_<SparkDataFrame>_)](https://spark.apache.org/docs/latest/api/R/reference/getNumPartitions.html)`
    getNumPartitions 

`group_by()[](https://spark.apache.org/docs/latest/api/R/reference/groupBy.html)` `groupBy()[](https://spark.apache.org/docs/latest/api/R/reference/groupBy.html)` 
    GroupBy 

`head([_<SparkDataFrame>_)](https://spark.apache.org/docs/latest/api/R/reference/head.html)`
    Head 

`hint()[](https://spark.apache.org/docs/latest/api/R/reference/hint.html)` 
    hint 

`histogram([_<SparkDataFrame>_,_<characterOrColumn>_)](https://spark.apache.org/docs/latest/api/R/reference/histogram.html)`
    Compute histogram statistics for given column 

`insertInto()[](https://spark.apache.org/docs/latest/api/R/reference/insertInto.html)` 
    insertInto 

`intersect()[](https://spark.apache.org/docs/latest/api/R/reference/intersect.html)` 
    Intersect 

`intersectAll()[](https://spark.apache.org/docs/latest/api/R/reference/intersectAll.html)` 
    intersectAll 

`isLocal()[](https://spark.apache.org/docs/latest/api/R/reference/isLocal.html)` 
    isLocal 

`isStreaming()[](https://spark.apache.org/docs/latest/api/R/reference/isStreaming.html)` 
    isStreaming 

`join([_<SparkDataFrame>_,_<SparkDataFrame>_)](https://spark.apache.org/docs/latest/api/R/reference/join.html)`
    Join 

`limit()[](https://spark.apache.org/docs/latest/api/R/reference/limit.html)` 
    Limit 

`localCheckpoint()[](https://spark.apache.org/docs/latest/api/R/reference/localCheckpoint.html)` 
    localCheckpoint 

`merge()[](https://spark.apache.org/docs/latest/api/R/reference/merge.html)` 
    Merges two data frames 

`mutate()[](https://spark.apache.org/docs/latest/api/R/reference/mutate.html)` `transform()[](https://spark.apache.org/docs/latest/api/R/reference/mutate.html)` 
    Mutate 

`ncol([_<SparkDataFrame>_)](https://spark.apache.org/docs/latest/api/R/reference/ncol.html)`
    Returns the number of columns in a SparkDataFrame 

`count([_<SparkDataFrame>_)](https://spark.apache.org/docs/latest/api/R/reference/nrow.html)``nrow([_<SparkDataFrame>_)](https://spark.apache.org/docs/latest/api/R/reference/nrow.html)`
    Returns the number of rows in a SparkDataFrame 

`orderBy()[](https://spark.apache.org/docs/latest/api/R/reference/orderBy.html)` 
    Ordering Columns in a WindowSpec 

`persist()[](https://spark.apache.org/docs/latest/api/R/reference/persist.html)` 
    Persist 

`pivot([_<GroupedData>_,_<character>_)](https://spark.apache.org/docs/latest/api/R/reference/pivot.html)`
    Pivot a column of the GroupedData and perform the specified aggregation. 

`printSchema()[](https://spark.apache.org/docs/latest/api/R/reference/printSchema.html)` 
    Print Schema of a SparkDataFrame 

`randomSplit()[](https://spark.apache.org/docs/latest/api/R/reference/randomSplit.html)` 
    randomSplit 

`rbind()[](https://spark.apache.org/docs/latest/api/R/reference/rbind.html)` 
    Union two or more SparkDataFrames 

`rename()[](https://spark.apache.org/docs/latest/api/R/reference/rename.html)` `withColumnRenamed()[](https://spark.apache.org/docs/latest/api/R/reference/rename.html)` 
    rename 

`registerTempTable()[](https://spark.apache.org/docs/latest/api/R/reference/registerTempTable-deprecated.html)` 
    (Deprecated) Register Temporary Table 

`repartition()[](https://spark.apache.org/docs/latest/api/R/reference/repartition.html)` 
    Repartition 

`repartitionByRange()[](https://spark.apache.org/docs/latest/api/R/reference/repartitionByRange.html)` 
    Repartition by range 

`rollup()[](https://spark.apache.org/docs/latest/api/R/reference/rollup.html)` 
    rollup 

`sample()[](https://spark.apache.org/docs/latest/api/R/reference/sample.html)` `sample_frac()[](https://spark.apache.org/docs/latest/api/R/reference/sample.html)` 
    Sample 

`sampleBy()[](https://spark.apache.org/docs/latest/api/R/reference/sampleBy.html)` 
    Returns a stratified sample without replacement 

`saveAsTable()[](https://spark.apache.org/docs/latest/api/R/reference/saveAsTable.html)` 
    Save the contents of the SparkDataFrame to a data source as a table 

`schema()[](https://spark.apache.org/docs/latest/api/R/reference/schema.html)` 
    Get schema object 

`select()[](https://spark.apache.org/docs/latest/api/R/reference/select.html)` ``$`([_<SparkDataFrame>_)](https://spark.apache.org/docs/latest/api/R/reference/select.html)```$<-`([_<SparkDataFrame>_)](https://spark.apache.org/docs/latest/api/R/reference/select.html)`
    Select 

`selectExpr()[](https://spark.apache.org/docs/latest/api/R/reference/selectExpr.html)` 
    SelectExpr 

`show([_<Column>_)](https://spark.apache.org/docs/latest/api/R/reference/show.html)``show([_<GroupedData>_)](https://spark.apache.org/docs/latest/api/R/reference/show.html)``show([_<SparkDataFrame>_)](https://spark.apache.org/docs/latest/api/R/reference/show.html)``show([_<WindowSpec>_)](https://spark.apache.org/docs/latest/api/R/reference/show.html)``show([_<StreamingQuery>_)](https://spark.apache.org/docs/latest/api/R/reference/show.html)`
    show 

`showDF()[](https://spark.apache.org/docs/latest/api/R/reference/showDF.html)` 
    showDF 

`str([_<SparkDataFrame>_)](https://spark.apache.org/docs/latest/api/R/reference/str.html)`
    Compactly display the structure of a dataset 

`storageLevel([_<SparkDataFrame>_)](https://spark.apache.org/docs/latest/api/R/reference/storageLevel.html)`
    StorageLevel 

`subset()[](https://spark.apache.org/docs/latest/api/R/reference/subset.html)` ``[[`([_<SparkDataFrame>_,_<numericOrcharacter>_)](https://spark.apache.org/docs/latest/api/R/reference/subset.html)```[[<-`([_<SparkDataFrame>_,_<numericOrcharacter>_)](https://spark.apache.org/docs/latest/api/R/reference/subset.html)```[`([_<SparkDataFrame>_)](https://spark.apache.org/docs/latest/api/R/reference/subset.html)`
    Subset 

`summary()[](https://spark.apache.org/docs/latest/api/R/reference/summary.html)` 
    summary 

`take()[](https://spark.apache.org/docs/latest/api/R/reference/take.html)` 
    Take the first NUM rows of a SparkDataFrame and return the results as a R data.frame 

`tableToDF()[](https://spark.apache.org/docs/latest/api/R/reference/tableToDF.html)` 
    Create a SparkDataFrame from a SparkSQL table or view 

`toJSON([_<SparkDataFrame>_)](https://spark.apache.org/docs/latest/api/R/reference/toJSON.html)`
    toJSON 

`union()[](https://spark.apache.org/docs/latest/api/R/reference/union.html)` 
    Return a new SparkDataFrame containing the union of rows 

`unionAll()[](https://spark.apache.org/docs/latest/api/R/reference/unionAll.html)` 
    Return a new SparkDataFrame containing the union of rows. 

`unionByName()[](https://spark.apache.org/docs/latest/api/R/reference/unionByName.html)` 
    Return a new SparkDataFrame containing the union of rows, matched by column names 

`unpersist()[](https://spark.apache.org/docs/latest/api/R/reference/unpersist.html)` 
    Unpersist 

`unpivot()[](https://spark.apache.org/docs/latest/api/R/reference/unpivot.html)` `melt([_<SparkDataFrame>_,_<ANY>_,_<ANY>_,_<character>_,_<character>_)](https://spark.apache.org/docs/latest/api/R/reference/unpivot.html)`
    Unpivot a DataFrame from wide format to long format. 

`with()[](https://spark.apache.org/docs/latest/api/R/reference/with.html)` 
    Evaluate a R expression in an environment constructed from a SparkDataFrame 

`withColumn()[](https://spark.apache.org/docs/latest/api/R/reference/withColumn.html)` 
    WithColumn
## Data import and export[](https://spark.apache.org/docs/latest/api/R/reference/index.html#data-import-and-export) 

`read.df()[](https://spark.apache.org/docs/latest/api/R/reference/read.df.html)` `loadDF()[](https://spark.apache.org/docs/latest/api/R/reference/read.df.html)` 
    Load a SparkDataFrame 

`read.jdbc()[](https://spark.apache.org/docs/latest/api/R/reference/read.jdbc.html)` 
    Create a SparkDataFrame representing the database table accessible via JDBC URL 

`read.json()[](https://spark.apache.org/docs/latest/api/R/reference/read.json.html)` 
    Create a SparkDataFrame from a JSON file. 

`read.orc()[](https://spark.apache.org/docs/latest/api/R/reference/read.orc.html)` 
    Create a SparkDataFrame from an ORC file. 

`read.parquet()[](https://spark.apache.org/docs/latest/api/R/reference/read.parquet.html)` 
    Create a SparkDataFrame from a Parquet file. 

`read.text()[](https://spark.apache.org/docs/latest/api/R/reference/read.text.html)` 
    Create a SparkDataFrame from a text file. 

`write.df()[](https://spark.apache.org/docs/latest/api/R/reference/write.df.html)` `saveDF()[](https://spark.apache.org/docs/latest/api/R/reference/write.df.html)` `write.df()[](https://spark.apache.org/docs/latest/api/R/reference/write.df.html)` 
    Save the contents of SparkDataFrame to a data source. 

`write.jdbc()[](https://spark.apache.org/docs/latest/api/R/reference/write.jdbc.html)` 
    Save the content of SparkDataFrame to an external database table via JDBC. 

`write.json()[](https://spark.apache.org/docs/latest/api/R/reference/write.json.html)` 
    Save the contents of SparkDataFrame as a JSON file 

`write.orc()[](https://spark.apache.org/docs/latest/api/R/reference/write.orc.html)` 
    Save the contents of SparkDataFrame as an ORC file, preserving the schema. 

`write.parquet()[](https://spark.apache.org/docs/latest/api/R/reference/write.parquet.html)` 
    Save the contents of SparkDataFrame as a Parquet file, preserving the schema. 

`write.text()[](https://spark.apache.org/docs/latest/api/R/reference/write.text.html)` 
    Save the content of SparkDataFrame in a text file at the specified path.
## Column functions[](https://spark.apache.org/docs/latest/api/R/reference/index.html#column-functions) 

`approx_count_distinct()[](https://spark.apache.org/docs/latest/api/R/reference/column_aggregate_functions.html)` `approxCountDistinct()[](https://spark.apache.org/docs/latest/api/R/reference/column_aggregate_functions.html)` `collect_list()[](https://spark.apache.org/docs/latest/api/R/reference/column_aggregate_functions.html)` `collect_set()[](https://spark.apache.org/docs/latest/api/R/reference/column_aggregate_functions.html)` `count_distinct()[](https://spark.apache.org/docs/latest/api/R/reference/column_aggregate_functions.html)` `countDistinct()[](https://spark.apache.org/docs/latest/api/R/reference/column_aggregate_functions.html)` `grouping_bit()[](https://spark.apache.org/docs/latest/api/R/reference/column_aggregate_functions.html)` `grouping_id()[](https://spark.apache.org/docs/latest/api/R/reference/column_aggregate_functions.html)` `kurtosis()[](https://spark.apache.org/docs/latest/api/R/reference/column_aggregate_functions.html)` `max_by()[](https://spark.apache.org/docs/latest/api/R/reference/column_aggregate_functions.html)` `min_by()[](https://spark.apache.org/docs/latest/api/R/reference/column_aggregate_functions.html)` `n_distinct()[](https://spark.apache.org/docs/latest/api/R/reference/column_aggregate_functions.html)` `percentile_approx()[](https://spark.apache.org/docs/latest/api/R/reference/column_aggregate_functions.html)` `product()[](https://spark.apache.org/docs/latest/api/R/reference/column_aggregate_functions.html)` `sd()[](https://spark.apache.org/docs/latest/api/R/reference/column_aggregate_functions.html)` `skewness()[](https://spark.apache.org/docs/latest/api/R/reference/column_aggregate_functions.html)` `stddev()[](https://spark.apache.org/docs/latest/api/R/reference/column_aggregate_functions.html)` `std()[](https://spark.apache.org/docs/latest/api/R/reference/column_aggregate_functions.html)` `stddev_pop()[](https://spark.apache.org/docs/latest/api/R/reference/column_aggregate_functions.html)` `stddev_samp()[](https://spark.apache.org/docs/latest/api/R/reference/column_aggregate_functions.html)` `sum_distinct()[](https://spark.apache.org/docs/latest/api/R/reference/column_aggregate_functions.html)` `sumDistinct()[](https://spark.apache.org/docs/latest/api/R/reference/column_aggregate_functions.html)` `var()[](https://spark.apache.org/docs/latest/api/R/reference/column_aggregate_functions.html)` `variance()[](https://spark.apache.org/docs/latest/api/R/reference/column_aggregate_functions.html)` `var_pop()[](https://spark.apache.org/docs/latest/api/R/reference/column_aggregate_functions.html)` `var_samp()[](https://spark.apache.org/docs/latest/api/R/reference/column_aggregate_functions.html)` `max([_<Column>_)](https://spark.apache.org/docs/latest/api/R/reference/column_aggregate_functions.html)``mean([_<Column>_)](https://spark.apache.org/docs/latest/api/R/reference/column_aggregate_functions.html)``min([_<Column>_)](https://spark.apache.org/docs/latest/api/R/reference/column_aggregate_functions.html)``sum([_<Column>_)](https://spark.apache.org/docs/latest/api/R/reference/column_aggregate_functions.html)`
    Aggregate functions for Column operations 

`from_avro()[](https://spark.apache.org/docs/latest/api/R/reference/column_avro_functions.html)` `to_avro()[](https://spark.apache.org/docs/latest/api/R/reference/column_avro_functions.html)` 
    Avro processing functions for Column operations 

`column_collection_functions[](https://spark.apache.org/docs/latest/api/R/reference/column_collection_functions.html)` 
    Collection functions for Column operations 

`add_months()[](https://spark.apache.org/docs/latest/api/R/reference/column_datetime_diff_functions.html)` `datediff()[](https://spark.apache.org/docs/latest/api/R/reference/column_datetime_diff_functions.html)` `date_add()[](https://spark.apache.org/docs/latest/api/R/reference/column_datetime_diff_functions.html)` `date_format()[](https://spark.apache.org/docs/latest/api/R/reference/column_datetime_diff_functions.html)` `date_sub()[](https://spark.apache.org/docs/latest/api/R/reference/column_datetime_diff_functions.html)` `from_utc_timestamp()[](https://spark.apache.org/docs/latest/api/R/reference/column_datetime_diff_functions.html)` `months_between()[](https://spark.apache.org/docs/latest/api/R/reference/column_datetime_diff_functions.html)` `next_day()[](https://spark.apache.org/docs/latest/api/R/reference/column_datetime_diff_functions.html)` `to_utc_timestamp()[](https://spark.apache.org/docs/latest/api/R/reference/column_datetime_diff_functions.html)` 
    Date time arithmetic functions for Column operations 

`bin()[](https://spark.apache.org/docs/latest/api/R/reference/column_math_functions.html)` `bround()[](https://spark.apache.org/docs/latest/api/R/reference/column_math_functions.html)` `cbrt()[](https://spark.apache.org/docs/latest/api/R/reference/column_math_functions.html)` `ceil()[](https://spark.apache.org/docs/latest/api/R/reference/column_math_functions.html)` `conv()[](https://spark.apache.org/docs/latest/api/R/reference/column_math_functions.html)` `cot()[](https://spark.apache.org/docs/latest/api/R/reference/column_math_functions.html)` `csc()[](https://spark.apache.org/docs/latest/api/R/reference/column_math_functions.html)` `hex()[](https://spark.apache.org/docs/latest/api/R/reference/column_math_functions.html)` `hypot()[](https://spark.apache.org/docs/latest/api/R/reference/column_math_functions.html)` `ln()[](https://spark.apache.org/docs/latest/api/R/reference/column_math_functions.html)` `pmod()[](https://spark.apache.org/docs/latest/api/R/reference/column_math_functions.html)` `rint()[](https://spark.apache.org/docs/latest/api/R/reference/column_math_functions.html)` `sec()[](https://spark.apache.org/docs/latest/api/R/reference/column_math_functions.html)` `shiftLeft()[](https://spark.apache.org/docs/latest/api/R/reference/column_math_functions.html)` `shiftleft()[](https://spark.apache.org/docs/latest/api/R/reference/column_math_functions.html)` `shiftRight()[](https://spark.apache.org/docs/latest/api/R/reference/column_math_functions.html)` `shiftright()[](https://spark.apache.org/docs/latest/api/R/reference/column_math_functions.html)` `shiftRightUnsigned()[](https://spark.apache.org/docs/latest/api/R/reference/column_math_functions.html)` `shiftrightunsigned()[](https://spark.apache.org/docs/latest/api/R/reference/column_math_functions.html)` `signum()[](https://spark.apache.org/docs/latest/api/R/reference/column_math_functions.html)` `degrees()[](https://spark.apache.org/docs/latest/api/R/reference/column_math_functions.html)` `toDegrees()[](https://spark.apache.org/docs/latest/api/R/reference/column_math_functions.html)` `radians()[](https://spark.apache.org/docs/latest/api/R/reference/column_math_functions.html)` `toRadians()[](https://spark.apache.org/docs/latest/api/R/reference/column_math_functions.html)` `unhex()[](https://spark.apache.org/docs/latest/api/R/reference/column_math_functions.html)` `width_bucket()[](https://spark.apache.org/docs/latest/api/R/reference/column_math_functions.html)` `abs([_<Column>_)](https://spark.apache.org/docs/latest/api/R/reference/column_math_functions.html)``acos([_<Column>_)](https://spark.apache.org/docs/latest/api/R/reference/column_math_functions.html)``acosh([_<Column>_)](https://spark.apache.org/docs/latest/api/R/reference/column_math_functions.html)``asin([_<Column>_)](https://spark.apache.org/docs/latest/api/R/reference/column_math_functions.html)``asinh([_<Column>_)](https://spark.apache.org/docs/latest/api/R/reference/column_math_functions.html)``atan([_<Column>_)](https://spark.apache.org/docs/latest/api/R/reference/column_math_functions.html)``atanh([_<Column>_)](https://spark.apache.org/docs/latest/api/R/reference/column_math_functions.html)``ceiling([_<Column>_)](https://spark.apache.org/docs/latest/api/R/reference/column_math_functions.html)``cos([_<Column>_)](https://spark.apache.org/docs/latest/api/R/reference/column_math_functions.html)``cosh([_<Column>_)](https://spark.apache.org/docs/latest/api/R/reference/column_math_functions.html)``exp([_<Column>_)](https://spark.apache.org/docs/latest/api/R/reference/column_math_functions.html)``expm1([_<Column>_)](https://spark.apache.org/docs/latest/api/R/reference/column_math_functions.html)``factorial([_<Column>_)](https://spark.apache.org/docs/latest/api/R/reference/column_math_functions.html)``floor([_<Column>_)](https://spark.apache.org/docs/latest/api/R/reference/column_math_functions.html)``log([_<Column>_)](https://spark.apache.org/docs/latest/api/R/reference/column_math_functions.html)``log10([_<Column>_)](https://spark.apache.org/docs/latest/api/R/reference/column_math_functions.html)``log1p([_<Column>_)](https://spark.apache.org/docs/latest/api/R/reference/column_math_functions.html)``log2([_<Column>_)](https://spark.apache.org/docs/latest/api/R/reference/column_math_functions.html)``round([_<Column>_)](https://spark.apache.org/docs/latest/api/R/reference/column_math_functions.html)``sign([_<Column>_)](https://spark.apache.org/docs/latest/api/R/reference/column_math_functions.html)``sin([_<Column>_)](https://spark.apache.org/docs/latest/api/R/reference/column_math_functions.html)``sinh([_<Column>_)](https://spark.apache.org/docs/latest/api/R/reference/column_math_functions.html)``sqrt([_<Column>_)](https://spark.apache.org/docs/latest/api/R/reference/column_math_functions.html)``tan([_<Column>_)](https://spark.apache.org/docs/latest/api/R/reference/column_math_functions.html)``tanh([_<Column>_)](https://spark.apache.org/docs/latest/api/R/reference/column_math_functions.html)``atan2([_<Column>_)](https://spark.apache.org/docs/latest/api/R/reference/column_math_functions.html)`
    Math functions for Column operations 

`assert_true()[](https://spark.apache.org/docs/latest/api/R/reference/column_misc_functions.html)` `crc32()[](https://spark.apache.org/docs/latest/api/R/reference/column_misc_functions.html)` `hash()[](https://spark.apache.org/docs/latest/api/R/reference/column_misc_functions.html)` `md5()[](https://spark.apache.org/docs/latest/api/R/reference/column_misc_functions.html)` `raise_error()[](https://spark.apache.org/docs/latest/api/R/reference/column_misc_functions.html)` `sha1()[](https://spark.apache.org/docs/latest/api/R/reference/column_misc_functions.html)` `sha2()[](https://spark.apache.org/docs/latest/api/R/reference/column_misc_functions.html)` `xxhash64()[](https://spark.apache.org/docs/latest/api/R/reference/column_misc_functions.html)` 
    Miscellaneous functions for Column operations 

`array_to_vector()[](https://spark.apache.org/docs/latest/api/R/reference/column_ml_functions.html)` `vector_to_array()[](https://spark.apache.org/docs/latest/api/R/reference/column_ml_functions.html)` 
    ML functions for Column operations 

`when()[](https://spark.apache.org/docs/latest/api/R/reference/column_nonaggregate_functions.html)` `bitwise_not()[](https://spark.apache.org/docs/latest/api/R/reference/column_nonaggregate_functions.html)` `bitwiseNOT()[](https://spark.apache.org/docs/latest/api/R/reference/column_nonaggregate_functions.html)` `create_array()[](https://spark.apache.org/docs/latest/api/R/reference/column_nonaggregate_functions.html)` `create_map()[](https://spark.apache.org/docs/latest/api/R/reference/column_nonaggregate_functions.html)` `expr()[](https://spark.apache.org/docs/latest/api/R/reference/column_nonaggregate_functions.html)` `greatest()[](https://spark.apache.org/docs/latest/api/R/reference/column_nonaggregate_functions.html)` `input_file_name()[](https://spark.apache.org/docs/latest/api/R/reference/column_nonaggregate_functions.html)` `isnan()[](https://spark.apache.org/docs/latest/api/R/reference/column_nonaggregate_functions.html)` `least()[](https://spark.apache.org/docs/latest/api/R/reference/column_nonaggregate_functions.html)` `lit()[](https://spark.apache.org/docs/latest/api/R/reference/column_nonaggregate_functions.html)` `monotonically_increasing_id()[](https://spark.apache.org/docs/latest/api/R/reference/column_nonaggregate_functions.html)` `nanvl()[](https://spark.apache.org/docs/latest/api/R/reference/column_nonaggregate_functions.html)` `negate()[](https://spark.apache.org/docs/latest/api/R/reference/column_nonaggregate_functions.html)` `negative()[](https://spark.apache.org/docs/latest/api/R/reference/column_nonaggregate_functions.html)` `positive()[](https://spark.apache.org/docs/latest/api/R/reference/column_nonaggregate_functions.html)` `rand()[](https://spark.apache.org/docs/latest/api/R/reference/column_nonaggregate_functions.html)` `randn()[](https://spark.apache.org/docs/latest/api/R/reference/column_nonaggregate_functions.html)` `spark_partition_id()[](https://spark.apache.org/docs/latest/api/R/reference/column_nonaggregate_functions.html)` `struct()[](https://spark.apache.org/docs/latest/api/R/reference/column_nonaggregate_functions.html)` `coalesce([_<Column>_)](https://spark.apache.org/docs/latest/api/R/reference/column_nonaggregate_functions.html)``is.nan([_<Column>_)](https://spark.apache.org/docs/latest/api/R/reference/column_nonaggregate_functions.html)``ifelse([_<Column>_)](https://spark.apache.org/docs/latest/api/R/reference/column_nonaggregate_functions.html)`
    Non-aggregate functions for Column operations 

`ascii()[](https://spark.apache.org/docs/latest/api/R/reference/column_string_functions.html)` `base64()[](https://spark.apache.org/docs/latest/api/R/reference/column_string_functions.html)` `bit_length()[](https://spark.apache.org/docs/latest/api/R/reference/column_string_functions.html)` `collate()[](https://spark.apache.org/docs/latest/api/R/reference/column_string_functions.html)` `collation()[](https://spark.apache.org/docs/latest/api/R/reference/column_string_functions.html)` `concat_ws()[](https://spark.apache.org/docs/latest/api/R/reference/column_string_functions.html)` `decode()[](https://spark.apache.org/docs/latest/api/R/reference/column_string_functions.html)` `encode()[](https://spark.apache.org/docs/latest/api/R/reference/column_string_functions.html)` `format_number()[](https://spark.apache.org/docs/latest/api/R/reference/column_string_functions.html)` `format_string()[](https://spark.apache.org/docs/latest/api/R/reference/column_string_functions.html)` `initcap()[](https://spark.apache.org/docs/latest/api/R/reference/column_string_functions.html)` `instr()[](https://spark.apache.org/docs/latest/api/R/reference/column_string_functions.html)` `levenshtein()[](https://spark.apache.org/docs/latest/api/R/reference/column_string_functions.html)` `locate()[](https://spark.apache.org/docs/latest/api/R/reference/column_string_functions.html)` `lower()[](https://spark.apache.org/docs/latest/api/R/reference/column_string_functions.html)` `lpad()[](https://spark.apache.org/docs/latest/api/R/reference/column_string_functions.html)` `ltrim()[](https://spark.apache.org/docs/latest/api/R/reference/column_string_functions.html)` `octet_length()[](https://spark.apache.org/docs/latest/api/R/reference/column_string_functions.html)` `overlay()[](https://spark.apache.org/docs/latest/api/R/reference/column_string_functions.html)` `regexp_extract()[](https://spark.apache.org/docs/latest/api/R/reference/column_string_functions.html)` `regexp_replace()[](https://spark.apache.org/docs/latest/api/R/reference/column_string_functions.html)` `repeat_string()[](https://spark.apache.org/docs/latest/api/R/reference/column_string_functions.html)` `rpad()[](https://spark.apache.org/docs/latest/api/R/reference/column_string_functions.html)` `rtrim()[](https://spark.apache.org/docs/latest/api/R/reference/column_string_functions.html)` `split_string()[](https://spark.apache.org/docs/latest/api/R/reference/column_string_functions.html)` `soundex()[](https://spark.apache.org/docs/latest/api/R/reference/column_string_functions.html)` `substring_index()[](https://spark.apache.org/docs/latest/api/R/reference/column_string_functions.html)` `translate()[](https://spark.apache.org/docs/latest/api/R/reference/column_string_functions.html)` `trim()[](https://spark.apache.org/docs/latest/api/R/reference/column_string_functions.html)` `unbase64()[](https://spark.apache.org/docs/latest/api/R/reference/column_string_functions.html)` `upper()[](https://spark.apache.org/docs/latest/api/R/reference/column_string_functions.html)` `length([_<Column>_)](https://spark.apache.org/docs/latest/api/R/reference/column_string_functions.html)`
    String functions for Column operations 

`cume_dist()[](https://spark.apache.org/docs/latest/api/R/reference/column_window_functions.html)` `dense_rank()[](https://spark.apache.org/docs/latest/api/R/reference/column_window_functions.html)` `lag()[](https://spark.apache.org/docs/latest/api/R/reference/column_window_functions.html)` `lead()[](https://spark.apache.org/docs/latest/api/R/reference/column_window_functions.html)` `nth_value()[](https://spark.apache.org/docs/latest/api/R/reference/column_window_functions.html)` `ntile()[](https://spark.apache.org/docs/latest/api/R/reference/column_window_functions.html)` `percent_rank()[](https://spark.apache.org/docs/latest/api/R/reference/column_window_functions.html)` `rank()[](https://spark.apache.org/docs/latest/api/R/reference/column_window_functions.html)` `row_number()[](https://spark.apache.org/docs/latest/api/R/reference/column_window_functions.html)` 
    Window functions for Column operations 

`alias([_<Column>_)](https://spark.apache.org/docs/latest/api/R/reference/alias.html)``alias([_<SparkDataFrame>_)](https://spark.apache.org/docs/latest/api/R/reference/alias.html)`
    alias 

`asc()[](https://spark.apache.org/docs/latest/api/R/reference/columnfunctions.html)` `asc_nulls_first()[](https://spark.apache.org/docs/latest/api/R/reference/columnfunctions.html)` `asc_nulls_last()[](https://spark.apache.org/docs/latest/api/R/reference/columnfunctions.html)` `contains()[](https://spark.apache.org/docs/latest/api/R/reference/columnfunctions.html)` `desc()[](https://spark.apache.org/docs/latest/api/R/reference/columnfunctions.html)` `desc_nulls_first()[](https://spark.apache.org/docs/latest/api/R/reference/columnfunctions.html)` `desc_nulls_last()[](https://spark.apache.org/docs/latest/api/R/reference/columnfunctions.html)` `getField()[](https://spark.apache.org/docs/latest/api/R/reference/columnfunctions.html)` `getItem()[](https://spark.apache.org/docs/latest/api/R/reference/columnfunctions.html)` `isNaN()[](https://spark.apache.org/docs/latest/api/R/reference/columnfunctions.html)` `isNull()[](https://spark.apache.org/docs/latest/api/R/reference/columnfunctions.html)` `isNotNull()[](https://spark.apache.org/docs/latest/api/R/reference/columnfunctions.html)` `like()[](https://spark.apache.org/docs/latest/api/R/reference/columnfunctions.html)` `rlike()[](https://spark.apache.org/docs/latest/api/R/reference/columnfunctions.html)` `ilike()[](https://spark.apache.org/docs/latest/api/R/reference/columnfunctions.html)` 
    A set of operations working with SparkDataFrame columns 

`avg()[](https://spark.apache.org/docs/latest/api/R/reference/avg.html)` 
    avg 

`between()[](https://spark.apache.org/docs/latest/api/R/reference/between.html)` 
    between 

`cast()[](https://spark.apache.org/docs/latest/api/R/reference/cast.html)` 
    Casts the column to a different data type. 

`column()[](https://spark.apache.org/docs/latest/api/R/reference/column.html)` 
    S4 class that represents a SparkDataFrame column 

`coalesce()[](https://spark.apache.org/docs/latest/api/R/reference/coalesce.html)` 
    Coalesce 

`corr()[](https://spark.apache.org/docs/latest/api/R/reference/corr.html)` 
    corr 

`cov()[](https://spark.apache.org/docs/latest/api/R/reference/cov.html)` `covar_samp()[](https://spark.apache.org/docs/latest/api/R/reference/cov.html)` `covar_pop()[](https://spark.apache.org/docs/latest/api/R/reference/cov.html)` 
    cov 

`dropFields()[](https://spark.apache.org/docs/latest/api/R/reference/dropFields.html)` 
    dropFields 

`endsWith()[](https://spark.apache.org/docs/latest/api/R/reference/endsWith.html)` 
    endsWith 

`first()[](https://spark.apache.org/docs/latest/api/R/reference/first.html)` 
    Return the first row of a SparkDataFrame 

`last()[](https://spark.apache.org/docs/latest/api/R/reference/last.html)` 
    last 

`not()[](https://spark.apache.org/docs/latest/api/R/reference/not.html)` ``!`([_<Column>_)](https://spark.apache.org/docs/latest/api/R/reference/not.html)`
    ! 

`otherwise()[](https://spark.apache.org/docs/latest/api/R/reference/otherwise.html)` 
    otherwise 

`startsWith()[](https://spark.apache.org/docs/latest/api/R/reference/startsWith.html)` 
    startsWith 

`substr([_<Column>_)](https://spark.apache.org/docs/latest/api/R/reference/substr.html)`
    substr 

`current_date()[](https://spark.apache.org/docs/latest/api/R/reference/column_datetime_functions.html)` `current_timestamp()[](https://spark.apache.org/docs/latest/api/R/reference/column_datetime_functions.html)` `date_trunc()[](https://spark.apache.org/docs/latest/api/R/reference/column_datetime_functions.html)` `dayofmonth()[](https://spark.apache.org/docs/latest/api/R/reference/column_datetime_functions.html)` `dayofweek()[](https://spark.apache.org/docs/latest/api/R/reference/column_datetime_functions.html)` `dayofyear()[](https://spark.apache.org/docs/latest/api/R/reference/column_datetime_functions.html)` `monthname()[](https://spark.apache.org/docs/latest/api/R/reference/column_datetime_functions.html)` `dayname()[](https://spark.apache.org/docs/latest/api/R/reference/column_datetime_functions.html)` `from_unixtime()[](https://spark.apache.org/docs/latest/api/R/reference/column_datetime_functions.html)` `hour()[](https://spark.apache.org/docs/latest/api/R/reference/column_datetime_functions.html)` `last_day()[](https://spark.apache.org/docs/latest/api/R/reference/column_datetime_functions.html)` `make_date()[](https://spark.apache.org/docs/latest/api/R/reference/column_datetime_functions.html)` `minute()[](https://spark.apache.org/docs/latest/api/R/reference/column_datetime_functions.html)` `month()[](https://spark.apache.org/docs/latest/api/R/reference/column_datetime_functions.html)` `quarter()[](https://spark.apache.org/docs/latest/api/R/reference/column_datetime_functions.html)` `second()[](https://spark.apache.org/docs/latest/api/R/reference/column_datetime_functions.html)` `timestamp_seconds()[](https://spark.apache.org/docs/latest/api/R/reference/column_datetime_functions.html)` `to_date()[](https://spark.apache.org/docs/latest/api/R/reference/column_datetime_functions.html)` `to_timestamp()[](https://spark.apache.org/docs/latest/api/R/reference/column_datetime_functions.html)` `unix_timestamp()[](https://spark.apache.org/docs/latest/api/R/reference/column_datetime_functions.html)` `weekofyear()[](https://spark.apache.org/docs/latest/api/R/reference/column_datetime_functions.html)` `window()[](https://spark.apache.org/docs/latest/api/R/reference/column_datetime_functions.html)` `year()[](https://spark.apache.org/docs/latest/api/R/reference/column_datetime_functions.html)` `trunc([_<Column>_)](https://spark.apache.org/docs/latest/api/R/reference/column_datetime_functions.html)`
    Date time functions for Column operations 

`withField()[](https://spark.apache.org/docs/latest/api/R/reference/withField.html)` 
    withField 

`over()[](https://spark.apache.org/docs/latest/api/R/reference/over.html)` 
    over 

`predict()[](https://spark.apache.org/docs/latest/api/R/reference/predict.html)` 
    Makes predictions from a MLlib model 

`partitionBy()[](https://spark.apache.org/docs/latest/api/R/reference/partitionBy.html)` 
    partitionBy 

`rangeBetween()[](https://spark.apache.org/docs/latest/api/R/reference/rangeBetween.html)` 
    rangeBetween 

`rowsBetween()[](https://spark.apache.org/docs/latest/api/R/reference/rowsBetween.html)` 
    rowsBetween 

`windowOrderBy()[](https://spark.apache.org/docs/latest/api/R/reference/windowOrderBy.html)` 
    windowOrderBy 

`windowPartitionBy()[](https://spark.apache.org/docs/latest/api/R/reference/windowPartitionBy.html)` 
    windowPartitionBy 

`WindowSpec-class[](https://spark.apache.org/docs/latest/api/R/reference/WindowSpec.html)` 
    S4 class that represents a WindowSpec 

``%in%`([_<Column>_)](https://spark.apache.org/docs/latest/api/R/reference/match.html)`
    Match a column with given values. 

``%<=>%`[](https://spark.apache.org/docs/latest/api/R/reference/eq_null_safe.html)` 
    %<=>%
## Schema Definitions[](https://spark.apache.org/docs/latest/api/R/reference/index.html#schema-definitions) 

`structField()[](https://spark.apache.org/docs/latest/api/R/reference/structField.html)` 
    structField 

`structType()[](https://spark.apache.org/docs/latest/api/R/reference/structType.html)` 
    structType
## Structured Streaming[](https://spark.apache.org/docs/latest/api/R/reference/index.html#structured-streaming) 

`StreamingQuery-class[](https://spark.apache.org/docs/latest/api/R/reference/StreamingQuery.html)` 
    S4 class that represents a StreamingQuery 

`awaitTermination()[](https://spark.apache.org/docs/latest/api/R/reference/awaitTermination.html)` 
    awaitTermination 

`isActive()[](https://spark.apache.org/docs/latest/api/R/reference/isActive.html)` 
    isActive 

`queryName()[](https://spark.apache.org/docs/latest/api/R/reference/queryName.html)` 
    queryName 

`lastProgress()[](https://spark.apache.org/docs/latest/api/R/reference/lastProgress.html)` 
    lastProgress 

`read.stream()[](https://spark.apache.org/docs/latest/api/R/reference/read.stream.html)` 
    Load a streaming SparkDataFrame 

`status()[](https://spark.apache.org/docs/latest/api/R/reference/status.html)` 
    status 

`stopQuery()[](https://spark.apache.org/docs/latest/api/R/reference/stopQuery.html)` 
    stopQuery 

`withWatermark()[](https://spark.apache.org/docs/latest/api/R/reference/withWatermark.html)` 
    withWatermark 

`write.stream()[](https://spark.apache.org/docs/latest/api/R/reference/write.stream.html)` 
    Write the streaming SparkDataFrame to a data source.
## Spark MLlib[](https://spark.apache.org/docs/latest/api/R/reference/index.html#spark-mllib)
MLlib is Spark’s machine learning (ML) library 

`AFTSurvivalRegressionModel-class[](https://spark.apache.org/docs/latest/api/R/reference/AFTSurvivalRegressionModel-class.html)` 
    S4 class that represents a AFTSurvivalRegressionModel 

`ALSModel-class[](https://spark.apache.org/docs/latest/api/R/reference/ALSModel-class.html)` 
    S4 class that represents an ALSModel 

`BisectingKMeansModel-class[](https://spark.apache.org/docs/latest/api/R/reference/BisectingKMeansModel-class.html)` 
    S4 class that represents a BisectingKMeansModel 

`DecisionTreeClassificationModel-class[](https://spark.apache.org/docs/latest/api/R/reference/DecisionTreeClassificationModel-class.html)` 
    S4 class that represents a DecisionTreeClassificationModel 

`DecisionTreeRegressionModel-class[](https://spark.apache.org/docs/latest/api/R/reference/DecisionTreeRegressionModel-class.html)` 
    S4 class that represents a DecisionTreeRegressionModel 

`FMClassificationModel-class[](https://spark.apache.org/docs/latest/api/R/reference/FMClassificationModel-class.html)` 
    S4 class that represents a FMClassificationModel 

`FMRegressionModel-class[](https://spark.apache.org/docs/latest/api/R/reference/FMRegressionModel-class.html)` 
    S4 class that represents a FMRegressionModel 

`FPGrowthModel-class[](https://spark.apache.org/docs/latest/api/R/reference/FPGrowthModel-class.html)` 
    S4 class that represents a FPGrowthModel 

`GBTClassificationModel-class[](https://spark.apache.org/docs/latest/api/R/reference/GBTClassificationModel-class.html)` 
    S4 class that represents a GBTClassificationModel 

`GBTRegressionModel-class[](https://spark.apache.org/docs/latest/api/R/reference/GBTRegressionModel-class.html)` 
    S4 class that represents a GBTRegressionModel 

`GaussianMixtureModel-class[](https://spark.apache.org/docs/latest/api/R/reference/GaussianMixtureModel-class.html)` 
    S4 class that represents a GaussianMixtureModel 

`GeneralizedLinearRegressionModel-class[](https://spark.apache.org/docs/latest/api/R/reference/GeneralizedLinearRegressionModel-class.html)` 
    S4 class that represents a generalized linear model 

`glm([_<formula>_,_<ANY>_,_<SparkDataFrame>_)](https://spark.apache.org/docs/latest/api/R/reference/glm.html)`
    Generalized Linear Models (R-compliant) 

`IsotonicRegressionModel-class[](https://spark.apache.org/docs/latest/api/R/reference/IsotonicRegressionModel-class.html)` 
    S4 class that represents an IsotonicRegressionModel 

`KMeansModel-class[](https://spark.apache.org/docs/latest/api/R/reference/KMeansModel-class.html)` 
    S4 class that represents a KMeansModel 

`KSTest-class[](https://spark.apache.org/docs/latest/api/R/reference/KSTest-class.html)` 
    S4 class that represents an KSTest 

`LDAModel-class[](https://spark.apache.org/docs/latest/api/R/reference/LDAModel-class.html)` 
    S4 class that represents an LDAModel 

`LinearRegressionModel-class[](https://spark.apache.org/docs/latest/api/R/reference/LinearRegressionModel-class.html)` 
    S4 class that represents a LinearRegressionModel 

`LinearSVCModel-class[](https://spark.apache.org/docs/latest/api/R/reference/LinearSVCModel-class.html)` 
    S4 class that represents an LinearSVCModel 

`LogisticRegressionModel-class[](https://spark.apache.org/docs/latest/api/R/reference/LogisticRegressionModel-class.html)` 
    S4 class that represents an LogisticRegressionModel 

`MultilayerPerceptronClassificationModel-class[](https://spark.apache.org/docs/latest/api/R/reference/MultilayerPerceptronClassificationModel-class.html)` 
    S4 class that represents a MultilayerPerceptronClassificationModel 

`NaiveBayesModel-class[](https://spark.apache.org/docs/latest/api/R/reference/NaiveBayesModel-class.html)` 
    S4 class that represents a NaiveBayesModel 

`PowerIterationClustering-class[](https://spark.apache.org/docs/latest/api/R/reference/PowerIterationClustering-class.html)` 
    S4 class that represents a PowerIterationClustering 

`PrefixSpan-class[](https://spark.apache.org/docs/latest/api/R/reference/PrefixSpan-class.html)` 
    S4 class that represents a PrefixSpan 

`RandomForestClassificationModel-class[](https://spark.apache.org/docs/latest/api/R/reference/RandomForestClassificationModel-class.html)` 
    S4 class that represents a RandomForestClassificationModel 

`RandomForestRegressionModel-class[](https://spark.apache.org/docs/latest/api/R/reference/RandomForestRegressionModel-class.html)` 
    S4 class that represents a RandomForestRegressionModel 

`fitted()[](https://spark.apache.org/docs/latest/api/R/reference/fitted.html)` 
    Get fitted result from a k-means model 

`freqItems([_<SparkDataFrame>_,_<character>_)](https://spark.apache.org/docs/latest/api/R/reference/freqItems.html)`
    Finding frequent items for columns, possibly with false positives 

`spark.als()[](https://spark.apache.org/docs/latest/api/R/reference/spark.als.html)` `summary([_<ALSModel>_)](https://spark.apache.org/docs/latest/api/R/reference/spark.als.html)``predict([_<ALSModel>_)](https://spark.apache.org/docs/latest/api/R/reference/spark.als.html)``write.ml([_<ALSModel>_,_<character>_)](https://spark.apache.org/docs/latest/api/R/reference/spark.als.html)`
    Alternating Least Squares (ALS) for Collaborative Filtering 

`spark.bisectingKmeans()[](https://spark.apache.org/docs/latest/api/R/reference/spark.bisectingKmeans.html)` `summary([_<BisectingKMeansModel>_)](https://spark.apache.org/docs/latest/api/R/reference/spark.bisectingKmeans.html)``predict([_<BisectingKMeansModel>_)](https://spark.apache.org/docs/latest/api/R/reference/spark.bisectingKmeans.html)``fitted([_<BisectingKMeansModel>_)](https://spark.apache.org/docs/latest/api/R/reference/spark.bisectingKmeans.html)``write.ml([_<BisectingKMeansModel>_,_<character>_)](https://spark.apache.org/docs/latest/api/R/reference/spark.bisectingKmeans.html)`
    Bisecting K-Means Clustering Model 

`spark.decisionTree()[](https://spark.apache.org/docs/latest/api/R/reference/spark.decisionTree.html)` `summary([_<DecisionTreeRegressionModel>_)](https://spark.apache.org/docs/latest/api/R/reference/spark.decisionTree.html)``print([_<summary.DecisionTreeRegressionModel>_)](https://spark.apache.org/docs/latest/api/R/reference/spark.decisionTree.html)``summary([_<DecisionTreeClassificationModel>_)](https://spark.apache.org/docs/latest/api/R/reference/spark.decisionTree.html)``print([_<summary.DecisionTreeClassificationModel>_)](https://spark.apache.org/docs/latest/api/R/reference/spark.decisionTree.html)``predict([_<DecisionTreeRegressionModel>_)](https://spark.apache.org/docs/latest/api/R/reference/spark.decisionTree.html)``predict([_<DecisionTreeClassificationModel>_)](https://spark.apache.org/docs/latest/api/R/reference/spark.decisionTree.html)``write.ml([_<DecisionTreeRegressionModel>_,_<character>_)](https://spark.apache.org/docs/latest/api/R/reference/spark.decisionTree.html)``write.ml([_<DecisionTreeClassificationModel>_,_<character>_)](https://spark.apache.org/docs/latest/api/R/reference/spark.decisionTree.html)`
    Decision Tree Model for Regression and Classification 

`spark.fmClassifier()[](https://spark.apache.org/docs/latest/api/R/reference/spark.fmClassifier.html)` `summary([_<FMClassificationModel>_)](https://spark.apache.org/docs/latest/api/R/reference/spark.fmClassifier.html)``predict([_<FMClassificationModel>_)](https://spark.apache.org/docs/latest/api/R/reference/spark.fmClassifier.html)``write.ml([_<FMClassificationModel>_,_<character>_)](https://spark.apache.org/docs/latest/api/R/reference/spark.fmClassifier.html)`
    Factorization Machines Classification Model 

`spark.fmRegressor()[](https://spark.apache.org/docs/latest/api/R/reference/spark.fmRegressor.html)` `summary([_<FMRegressionModel>_)](https://spark.apache.org/docs/latest/api/R/reference/spark.fmRegressor.html)``predict([_<FMRegressionModel>_)](https://spark.apache.org/docs/latest/api/R/reference/spark.fmRegressor.html)``write.ml([_<FMRegressionModel>_,_<character>_)](https://spark.apache.org/docs/latest/api/R/reference/spark.fmRegressor.html)`
    Factorization Machines Regression Model 

`spark.fpGrowth()[](https://spark.apache.org/docs/latest/api/R/reference/spark.fpGrowth.html)` `spark.freqItemsets()[](https://spark.apache.org/docs/latest/api/R/reference/spark.fpGrowth.html)` `spark.associationRules()[](https://spark.apache.org/docs/latest/api/R/reference/spark.fpGrowth.html)` `predict([_<FPGrowthModel>_)](https://spark.apache.org/docs/latest/api/R/reference/spark.fpGrowth.html)``write.ml([_<FPGrowthModel>_,_<character>_)](https://spark.apache.org/docs/latest/api/R/reference/spark.fpGrowth.html)`
    FP-growth 

`spark.gaussianMixture()[](https://spark.apache.org/docs/latest/api/R/reference/spark.gaussianMixture.html)` `summary([_<GaussianMixtureModel>_)](https://spark.apache.org/docs/latest/api/R/reference/spark.gaussianMixture.html)``predict([_<GaussianMixtureModel>_)](https://spark.apache.org/docs/latest/api/R/reference/spark.gaussianMixture.html)``write.ml([_<GaussianMixtureModel>_,_<character>_)](https://spark.apache.org/docs/latest/api/R/reference/spark.gaussianMixture.html)`
    Multivariate Gaussian Mixture Model (GMM) 

`spark.gbt()[](https://spark.apache.org/docs/latest/api/R/reference/spark.gbt.html)` `summary([_<GBTRegressionModel>_)](https://spark.apache.org/docs/latest/api/R/reference/spark.gbt.html)``print([_<summary.GBTRegressionModel>_)](https://spark.apache.org/docs/latest/api/R/reference/spark.gbt.html)``summary([_<GBTClassificationModel>_)](https://spark.apache.org/docs/latest/api/R/reference/spark.gbt.html)``print([_<summary.GBTClassificationModel>_)](https://spark.apache.org/docs/latest/api/R/reference/spark.gbt.html)``predict([_<GBTRegressionModel>_)](https://spark.apache.org/docs/latest/api/R/reference/spark.gbt.html)``predict([_<GBTClassificationModel>_)](https://spark.apache.org/docs/latest/api/R/reference/spark.gbt.html)``write.ml([_<GBTRegressionModel>_,_<character>_)](https://spark.apache.org/docs/latest/api/R/reference/spark.gbt.html)``write.ml([_<GBTClassificationModel>_,_<character>_)](https://spark.apache.org/docs/latest/api/R/reference/spark.gbt.html)`
    Gradient Boosted Tree Model for Regression and Classification 

`spark.glm()[](https://spark.apache.org/docs/latest/api/R/reference/spark.glm.html)` `summary([_<GeneralizedLinearRegressionModel>_)](https://spark.apache.org/docs/latest/api/R/reference/spark.glm.html)``print([_<summary.GeneralizedLinearRegressionModel>_)](https://spark.apache.org/docs/latest/api/R/reference/spark.glm.html)``predict([_<GeneralizedLinearRegressionModel>_)](https://spark.apache.org/docs/latest/api/R/reference/spark.glm.html)``write.ml([_<GeneralizedLinearRegressionModel>_,_<character>_)](https://spark.apache.org/docs/latest/api/R/reference/spark.glm.html)`
    Generalized Linear Models 

`spark.isoreg()[](https://spark.apache.org/docs/latest/api/R/reference/spark.isoreg.html)` `summary([_<IsotonicRegressionModel>_)](https://spark.apache.org/docs/latest/api/R/reference/spark.isoreg.html)``predict([_<IsotonicRegressionModel>_)](https://spark.apache.org/docs/latest/api/R/reference/spark.isoreg.html)``write.ml([_<IsotonicRegressionModel>_,_<character>_)](https://spark.apache.org/docs/latest/api/R/reference/spark.isoreg.html)`
    Isotonic Regression Model 

`spark.kmeans()[](https://spark.apache.org/docs/latest/api/R/reference/spark.kmeans.html)` `summary([_<KMeansModel>_)](https://spark.apache.org/docs/latest/api/R/reference/spark.kmeans.html)``predict([_<KMeansModel>_)](https://spark.apache.org/docs/latest/api/R/reference/spark.kmeans.html)``write.ml([_<KMeansModel>_,_<character>_)](https://spark.apache.org/docs/latest/api/R/reference/spark.kmeans.html)`
    K-Means Clustering Model 

`spark.kstest()[](https://spark.apache.org/docs/latest/api/R/reference/spark.kstest.html)` `summary([_<KSTest>_)](https://spark.apache.org/docs/latest/api/R/reference/spark.kstest.html)``print([_<summary.KSTest>_)](https://spark.apache.org/docs/latest/api/R/reference/spark.kstest.html)`
    (One-Sample) Kolmogorov-Smirnov Test 

`spark.lda()[](https://spark.apache.org/docs/latest/api/R/reference/spark.lda.html)` `spark.posterior()[](https://spark.apache.org/docs/latest/api/R/reference/spark.lda.html)` `spark.perplexity()[](https://spark.apache.org/docs/latest/api/R/reference/spark.lda.html)` `summary([_<LDAModel>_)](https://spark.apache.org/docs/latest/api/R/reference/spark.lda.html)``write.ml([_<LDAModel>_,_<character>_)](https://spark.apache.org/docs/latest/api/R/reference/spark.lda.html)`
    Latent Dirichlet Allocation 

`spark.lm()[](https://spark.apache.org/docs/latest/api/R/reference/spark.lm.html)` `summary([_<LinearRegressionModel>_)](https://spark.apache.org/docs/latest/api/R/reference/spark.lm.html)``predict([_<LinearRegressionModel>_)](https://spark.apache.org/docs/latest/api/R/reference/spark.lm.html)``write.ml([_<LinearRegressionModel>_,_<character>_)](https://spark.apache.org/docs/latest/api/R/reference/spark.lm.html)`
    Linear Regression Model 

`spark.logit()[](https://spark.apache.org/docs/latest/api/R/reference/spark.logit.html)` `summary([_<LogisticRegressionModel>_)](https://spark.apache.org/docs/latest/api/R/reference/spark.logit.html)``predict([_<LogisticRegressionModel>_)](https://spark.apache.org/docs/latest/api/R/reference/spark.logit.html)``write.ml([_<LogisticRegressionModel>_,_<character>_)](https://spark.apache.org/docs/latest/api/R/reference/spark.logit.html)`
    Logistic Regression Model 

`spark.mlp()[](https://spark.apache.org/docs/latest/api/R/reference/spark.mlp.html)` `summary([_<MultilayerPerceptronClassificationModel>_)](https://spark.apache.org/docs/latest/api/R/reference/spark.mlp.html)``predict([_<MultilayerPerceptronClassificationModel>_)](https://spark.apache.org/docs/latest/api/R/reference/spark.mlp.html)``write.ml([_<MultilayerPerceptronClassificationModel>_,_<character>_)](https://spark.apache.org/docs/latest/api/R/reference/spark.mlp.html)`
    Multilayer Perceptron Classification Model 

`spark.naiveBayes()[](https://spark.apache.org/docs/latest/api/R/reference/spark.naiveBayes.html)` `summary([_<NaiveBayesModel>_)](https://spark.apache.org/docs/latest/api/R/reference/spark.naiveBayes.html)``predict([_<NaiveBayesModel>_)](https://spark.apache.org/docs/latest/api/R/reference/spark.naiveBayes.html)``write.ml([_<NaiveBayesModel>_,_<character>_)](https://spark.apache.org/docs/latest/api/R/reference/spark.naiveBayes.html)`
    Naive Bayes Models 

`spark.assignClusters()[](https://spark.apache.org/docs/latest/api/R/reference/spark.powerIterationClustering.html)` 
    PowerIterationClustering 

`spark.findFrequentSequentialPatterns()[](https://spark.apache.org/docs/latest/api/R/reference/spark.prefixSpan.html)` 
    PrefixSpan 

`spark.randomForest()[](https://spark.apache.org/docs/latest/api/R/reference/spark.randomForest.html)` `summary([_<RandomForestRegressionModel>_)](https://spark.apache.org/docs/latest/api/R/reference/spark.randomForest.html)``print([_<summary.RandomForestRegressionModel>_)](https://spark.apache.org/docs/latest/api/R/reference/spark.randomForest.html)``summary([_<RandomForestClassificationModel>_)](https://spark.apache.org/docs/latest/api/R/reference/spark.randomForest.html)``print([_<summary.RandomForestClassificationModel>_)](https://spark.apache.org/docs/latest/api/R/reference/spark.randomForest.html)``predict([_<RandomForestRegressionModel>_)](https://spark.apache.org/docs/latest/api/R/reference/spark.randomForest.html)``predict([_<RandomForestClassificationModel>_)](https://spark.apache.org/docs/latest/api/R/reference/spark.randomForest.html)``write.ml([_<RandomForestRegressionModel>_,_<character>_)](https://spark.apache.org/docs/latest/api/R/reference/spark.randomForest.html)``write.ml([_<RandomForestClassificationModel>_,_<character>_)](https://spark.apache.org/docs/latest/api/R/reference/spark.randomForest.html)`
    Random Forest Model for Regression and Classification 

`spark.survreg()[](https://spark.apache.org/docs/latest/api/R/reference/spark.survreg.html)` `summary([_<AFTSurvivalRegressionModel>_)](https://spark.apache.org/docs/latest/api/R/reference/spark.survreg.html)``predict([_<AFTSurvivalRegressionModel>_)](https://spark.apache.org/docs/latest/api/R/reference/spark.survreg.html)``write.ml([_<AFTSurvivalRegressionModel>_,_<character>_)](https://spark.apache.org/docs/latest/api/R/reference/spark.survreg.html)`
    Accelerated Failure Time (AFT) Survival Regression Model 

`spark.svmLinear()[](https://spark.apache.org/docs/latest/api/R/reference/spark.svmLinear.html)` `predict([_<LinearSVCModel>_)](https://spark.apache.org/docs/latest/api/R/reference/spark.svmLinear.html)``summary([_<LinearSVCModel>_)](https://spark.apache.org/docs/latest/api/R/reference/spark.svmLinear.html)``write.ml([_<LinearSVCModel>_,_<character>_)](https://spark.apache.org/docs/latest/api/R/reference/spark.svmLinear.html)`
    Linear SVM Model 

`read.ml()[](https://spark.apache.org/docs/latest/api/R/reference/read.ml.html)` 
    Load a fitted MLlib model from the input path. 

`write.ml()[](https://spark.apache.org/docs/latest/api/R/reference/write.ml.html)` 
    Saves the MLlib model to the input path
## Distributed R[](https://spark.apache.org/docs/latest/api/R/reference/index.html#distributed-r) 

`dapply[](https://spark.apache.org/docs/latest/api/R/reference/dapply.html)` 
    dapply 

`dapplyCollect[](https://spark.apache.org/docs/latest/api/R/reference/dapplyCollect.html)` 
    dapplyCollect 

`gapply()[](https://spark.apache.org/docs/latest/api/R/reference/gapply.html)` 
    gapply 

`gapplyCollect()[](https://spark.apache.org/docs/latest/api/R/reference/gapplyCollect.html)` 
    gapplyCollect 

`spark.lapply()[](https://spark.apache.org/docs/latest/api/R/reference/spark.lapply.html)` 
    Run a function over a list of elements, distributing the computations with Spark
## SQL Catalog[](https://spark.apache.org/docs/latest/api/R/reference/index.html#sql-catalog) 

`currentCatalog()[](https://spark.apache.org/docs/latest/api/R/reference/currentCatalog.html)` 
    Returns the current default catalog 

`currentDatabase()[](https://spark.apache.org/docs/latest/api/R/reference/currentDatabase.html)` 
    Returns the current default database 

`databaseExists()[](https://spark.apache.org/docs/latest/api/R/reference/databaseExists.html)` 
    Checks if the database with the specified name exists. 

`dropTempTable()[](https://spark.apache.org/docs/latest/api/R/reference/dropTempTable-deprecated.html)` 
    (Deprecated) Drop Temporary Table 

`dropTempView()[](https://spark.apache.org/docs/latest/api/R/reference/dropTempView.html)` 
    Drops the temporary view with the given view name in the catalog. 

`functionExists()[](https://spark.apache.org/docs/latest/api/R/reference/functionExists.html)` 
    Checks if the function with the specified name exists. 

`getDatabase()[](https://spark.apache.org/docs/latest/api/R/reference/getDatabase.html)` 
    Get the database with the specified name 

`getFunc()[](https://spark.apache.org/docs/latest/api/R/reference/getFunc.html)` 
    Get the function with the specified name 

`getTable()[](https://spark.apache.org/docs/latest/api/R/reference/getTable.html)` 
    Get the table with the specified name 

`listCatalogs()[](https://spark.apache.org/docs/latest/api/R/reference/listCatalogs.html)` 
    Returns a list of catalog available 

`listColumns()[](https://spark.apache.org/docs/latest/api/R/reference/listColumns.html)` 
    Returns a list of columns for the given table/view in the specified database 

`listDatabases()[](https://spark.apache.org/docs/latest/api/R/reference/listDatabases.html)` 
    Returns a list of databases available 

`listFunctions()[](https://spark.apache.org/docs/latest/api/R/reference/listFunctions.html)` 
    Returns a list of functions registered in the specified database 

`listTables()[](https://spark.apache.org/docs/latest/api/R/reference/listTables.html)` 
    Returns a list of tables or views in the specified database 

`refreshByPath()[](https://spark.apache.org/docs/latest/api/R/reference/refreshByPath.html)` 
    Invalidates and refreshes all the cached data and metadata for SparkDataFrame containing path 

`refreshTable()[](https://spark.apache.org/docs/latest/api/R/reference/refreshTable.html)` 
    Invalidates and refreshes all the cached data and metadata of the given table 

`recoverPartitions()[](https://spark.apache.org/docs/latest/api/R/reference/recoverPartitions.html)` 
    Recovers all the partitions in the directory of a table and update the catalog 

`setCurrentCatalog()[](https://spark.apache.org/docs/latest/api/R/reference/setCurrentCatalog.html)` 
    Sets the current default catalog 

`setCurrentDatabase()[](https://spark.apache.org/docs/latest/api/R/reference/setCurrentDatabase.html)` 
    Sets the current default database 

`tableExists()[](https://spark.apache.org/docs/latest/api/R/reference/tableExists.html)` 
    Checks if the table with the specified name exists. 

`tableNames()[](https://spark.apache.org/docs/latest/api/R/reference/tableNames.html)` 
    Table Names 

`tables()[](https://spark.apache.org/docs/latest/api/R/reference/tables.html)` 
    Tables 

`uncacheTable()[](https://spark.apache.org/docs/latest/api/R/reference/uncacheTable.html)` 
    Uncache Table
## Spark Session and Context[](https://spark.apache.org/docs/latest/api/R/reference/index.html#spark-session-and-context) 

`cancelJobGroup()[](https://spark.apache.org/docs/latest/api/R/reference/cancelJobGroup.html)` 
    Cancel active jobs for the specified group 

`cancelJobsWithTag()[](https://spark.apache.org/docs/latest/api/R/reference/cancelJobsWithTag.html)` 
    Cancel active jobs that have the specified tag. 

`clearCache()[](https://spark.apache.org/docs/latest/api/R/reference/clearCache.html)` 
    Clear Cache 

`clearJobGroup()[](https://spark.apache.org/docs/latest/api/R/reference/clearJobGroup.html)` 
    Clear current job group ID and its description 

`getLocalProperty()[](https://spark.apache.org/docs/latest/api/R/reference/getLocalProperty.html)` 
    Get a local property set in this thread, or `NULL` if it is missing. See `setLocalProperty`. 

`install.spark()[](https://spark.apache.org/docs/latest/api/R/reference/install.spark.html)` 
    Download and Install Apache Spark to a Local Directory 

`setCheckpointDir()[](https://spark.apache.org/docs/latest/api/R/reference/setCheckpointDir.html)` 
    Set checkpoint directory 

`setJobDescription()[](https://spark.apache.org/docs/latest/api/R/reference/setJobDescription.html)` 
    Set a human readable description of the current job. 

`setInterruptOnCancel()[](https://spark.apache.org/docs/latest/api/R/reference/setInterruptOnCancel.html)` 
    Set the behavior of job cancellation from jobs started in this thread. 

`setJobGroup()[](https://spark.apache.org/docs/latest/api/R/reference/setJobGroup.html)` 
    Assigns a group ID to all the jobs started by this thread until the group ID is set to a different value or cleared. 

`addJobTag()[](https://spark.apache.org/docs/latest/api/R/reference/addJobTAg.html)` 
    Add a tag to be assigned to all the jobs started by this thread. 

`removeJobTag()[](https://spark.apache.org/docs/latest/api/R/reference/removeJobTAg.html)` 
    Remove a tag previously added to be assigned to all the jobs started by this thread. Noop if such a tag was not added earlier. 

`getJobTags()[](https://spark.apache.org/docs/latest/api/R/reference/getJobTags.html)` 
    Get the tags that are currently set to be assigned to all the jobs started by this thread. 

`clearJobTags()[](https://spark.apache.org/docs/latest/api/R/reference/clearJobTags.html)` 
    Clear the current thread's job tags. 

`setLocalProperty()[](https://spark.apache.org/docs/latest/api/R/reference/setLocalProperty.html)` 
    Set a local property that affects jobs submitted from this thread, such as the Spark fair scheduler pool. To remove/unset property simply set `value` to NULL e.g. setLocalProperty("key", NULL) 

`setLogLevel()[](https://spark.apache.org/docs/latest/api/R/reference/setLogLevel.html)` 
    Set new log level 

`spark.addFile()[](https://spark.apache.org/docs/latest/api/R/reference/spark.addFile.html)` 
    Add a file or directory to be downloaded with this Spark job on every node. 

`spark.getSparkFiles()[](https://spark.apache.org/docs/latest/api/R/reference/spark.getSparkFiles.html)` 
    Get the absolute path of a file added through spark.addFile. 

`spark.getSparkFilesRootDirectory()[](https://spark.apache.org/docs/latest/api/R/reference/spark.getSparkFilesRootDirectory.html)` 
    Get the root directory that contains files added through spark.addFile. 

`sparkR.conf()[](https://spark.apache.org/docs/latest/api/R/reference/sparkR.conf.html)` 
    Get Runtime Config from the current active SparkSession 

`sparkR.callJMethod()[](https://spark.apache.org/docs/latest/api/R/reference/sparkR.callJMethod.html)` 
    Call Java Methods 

`sparkR.callJStatic()[](https://spark.apache.org/docs/latest/api/R/reference/sparkR.callJStatic.html)` 
    Call Static Java Methods 

`sparkR.init()[](https://spark.apache.org/docs/latest/api/R/reference/sparkR.init-deprecated.html)` 
    (Deprecated) Initialize a new Spark Context 

`sparkR.newJObject()[](https://spark.apache.org/docs/latest/api/R/reference/sparkR.newJObject.html)` 
    Create Java Objects 

`sparkR.session()[](https://spark.apache.org/docs/latest/api/R/reference/sparkR.session.html)` 
    Get the existing SparkSession or initialize a new SparkSession. 

`sparkR.session.stop()[](https://spark.apache.org/docs/latest/api/R/reference/sparkR.session.stop.html)` `sparkR.stop()[](https://spark.apache.org/docs/latest/api/R/reference/sparkR.session.stop.html)` 
    Stop the Spark Session and Spark Context 

`sparkR.uiWebUrl()[](https://spark.apache.org/docs/latest/api/R/reference/sparkR.uiWebUrl.html)` 
    Get the URL of the SparkUI instance for the current active SparkSession 

`sparkR.version()[](https://spark.apache.org/docs/latest/api/R/reference/sparkR.version.html)` 
    Get version of Spark on which this application is running 

`sparkRHive.init()[](https://spark.apache.org/docs/latest/api/R/reference/sparkRHive.init-deprecated.html)` 
    (Deprecated) Initialize a new HiveContext 

`sparkRSQL.init()[](https://spark.apache.org/docs/latest/api/R/reference/sparkRSQL.init-deprecated.html)` 
    (Deprecated) Initialize a new SQLContext 

`sql()[](https://spark.apache.org/docs/latest/api/R/reference/sql.html)` 
    SQL Query
## On this page
Developed by [ The Apache Software Foundation](https://www.apache.org/).
Site built with [pkgdown](https://pkgdown.r-lib.org/) 2.0.1.
Using [preferably](https://preferably.amirmasoudabdol.name/?source=footer) template.

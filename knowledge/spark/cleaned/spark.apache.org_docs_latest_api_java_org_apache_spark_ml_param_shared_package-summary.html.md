[Skip navigation links](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/param/shared/package-summary.html#skip-navbar-top "Skip navigation links")
  * [Overview](https://spark.apache.org/docs/latest/api/java/index.html)
  * Package
  * Class
  * [Deprecated](https://spark.apache.org/docs/latest/api/java/deprecated-list.html)
  * [Index](https://spark.apache.org/docs/latest/api/java/index-all.html)
  * [Help](https://spark.apache.org/docs/latest/api/java/help-doc.html#package)

  * Package:
  * Description |
  * [Related Packages](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/param/shared/package-summary.html#related-package-summary) |
  * [Classes and Interfaces](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/param/shared/package-summary.html#class-summary)

SEARCH:
# Package org.apache.spark.ml.param.shared
* * *
package org.apache.spark.ml.param.shared
  * Related Packages
Package
Description
[org.apache.spark.ml.param](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/param/package-summary.html)
  * All Classes and InterfacesInterfacesClasses
Class
Description
[HasAggregationDepth](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/param/shared/HasAggregationDepth.html "interface in org.apache.spark.ml.param.shared")
Trait for shared param aggregationDepth (default: 2).
[HasBlockSize](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/param/shared/HasBlockSize.html "interface in org.apache.spark.ml.param.shared")
Trait for shared param blockSize.
[HasCheckpointInterval](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/param/shared/HasCheckpointInterval.html "interface in org.apache.spark.ml.param.shared")
Trait for shared param checkpointInterval.
[HasCollectSubModels](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/param/shared/HasCollectSubModels.html "interface in org.apache.spark.ml.param.shared")
Trait for shared param collectSubModels (default: false).
[HasDistanceMeasure](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/param/shared/HasDistanceMeasure.html "interface in org.apache.spark.ml.param.shared")
Trait for shared param distanceMeasure (default: "euclidean").
[HasElasticNetParam](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/param/shared/HasElasticNetParam.html "interface in org.apache.spark.ml.param.shared")
Trait for shared param elasticNetParam.
[HasFeaturesCol](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/param/shared/HasFeaturesCol.html "interface in org.apache.spark.ml.param.shared")
Trait for shared param featuresCol (default: "features").
[HasFitIntercept](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/param/shared/HasFitIntercept.html "interface in org.apache.spark.ml.param.shared")
Trait for shared param fitIntercept (default: true).
[HasHandleInvalid](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/param/shared/HasHandleInvalid.html "interface in org.apache.spark.ml.param.shared")
Trait for shared param handleInvalid.
[HasInputCol](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/param/shared/HasInputCol.html "interface in org.apache.spark.ml.param.shared")
Trait for shared param inputCol.
[HasInputCols](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/param/shared/HasInputCols.html "interface in org.apache.spark.ml.param.shared")
Trait for shared param inputCols.
[HasLabelCol](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/param/shared/HasLabelCol.html "interface in org.apache.spark.ml.param.shared")
Trait for shared param labelCol (default: "label").
[HasLoss](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/param/shared/HasLoss.html "interface in org.apache.spark.ml.param.shared")
Trait for shared param loss.
[HasMaxBlockSizeInMB](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/param/shared/HasMaxBlockSizeInMB.html "interface in org.apache.spark.ml.param.shared")
Trait for shared param maxBlockSizeInMB (default: 0.0).
[HasMaxIter](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/param/shared/HasMaxIter.html "interface in org.apache.spark.ml.param.shared")
Trait for shared param maxIter.
[HasNumFeatures](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/param/shared/HasNumFeatures.html "interface in org.apache.spark.ml.param.shared")
Trait for shared param numFeatures (default: 262144).
[HasOutputCol](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/param/shared/HasOutputCol.html "interface in org.apache.spark.ml.param.shared")
Trait for shared param outputCol (default: uid + "__output").
[HasOutputCols](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/param/shared/HasOutputCols.html "interface in org.apache.spark.ml.param.shared")
Trait for shared param outputCols.
[HasParallelism](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/param/shared/HasParallelism.html "interface in org.apache.spark.ml.param.shared")
Trait to define a level of parallelism for algorithms that are able to use multithreaded execution, and provide a thread-pool based execution context.
[HasPredictionCol](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/param/shared/HasPredictionCol.html "interface in org.apache.spark.ml.param.shared")
Trait for shared param predictionCol (default: "prediction").
[HasProbabilityCol](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/param/shared/HasProbabilityCol.html "interface in org.apache.spark.ml.param.shared")
Trait for shared param probabilityCol (default: "probability").
[HasRawPredictionCol](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/param/shared/HasRawPredictionCol.html "interface in org.apache.spark.ml.param.shared")
Trait for shared param rawPredictionCol (default: "rawPrediction").
[HasRegParam](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/param/shared/HasRegParam.html "interface in org.apache.spark.ml.param.shared")
Trait for shared param regParam.
[HasRelativeError](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/param/shared/HasRelativeError.html "interface in org.apache.spark.ml.param.shared")
Trait for shared param relativeError (default: 0.001).
[HasSeed](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/param/shared/HasSeed.html "interface in org.apache.spark.ml.param.shared")
Trait for shared param seed (default: this.getClass.getName.hashCode.toLong).
[HasSolver](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/param/shared/HasSolver.html "interface in org.apache.spark.ml.param.shared")
Trait for shared param solver.
[HasStandardization](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/param/shared/HasStandardization.html "interface in org.apache.spark.ml.param.shared")
Trait for shared param standardization (default: true).
[HasStepSize](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/param/shared/HasStepSize.html "interface in org.apache.spark.ml.param.shared")
Trait for shared param stepSize.
[HasThreshold](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/param/shared/HasThreshold.html "interface in org.apache.spark.ml.param.shared")
Trait for shared param threshold.
[HasThresholds](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/param/shared/HasThresholds.html "interface in org.apache.spark.ml.param.shared")
Trait for shared param thresholds.
[HasTol](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/param/shared/HasTol.html "interface in org.apache.spark.ml.param.shared")
Trait for shared param tol.
[HasValidationIndicatorCol](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/param/shared/HasValidationIndicatorCol.html "interface in org.apache.spark.ml.param.shared")
Trait for shared param validationIndicatorCol.
[HasVarianceCol](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/param/shared/HasVarianceCol.html "interface in org.apache.spark.ml.param.shared")
Trait for shared param varianceCol.
[HasWeightCol](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/param/shared/HasWeightCol.html "interface in org.apache.spark.ml.param.shared")
Trait for shared param weightCol.
[SharedParamsCodeGen](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/param/shared/SharedParamsCodeGen.html "class in org.apache.spark.ml.param.shared")
Code generator for shared params (sharedParams.scala).

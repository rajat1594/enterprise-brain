[ ![](https://spark.apache.org/images/spark-logo-rev.svg)](https://spark.apache.org/docs/latest/index.html)4.1.2
  * [Overview](https://spark.apache.org/docs/latest/index.html)
  * [Programming Guides](https://spark.apache.org/docs/latest/mllib-evaluation-metrics.html)
[Quick Start](https://spark.apache.org/docs/latest/quick-start.html) [RDDs, Accumulators, Broadcasts Vars](https://spark.apache.org/docs/latest/rdd-programming-guide.html) [SQL, DataFrames, and Datasets](https://spark.apache.org/docs/latest/sql-programming-guide.html) [Structured Streaming](https://spark.apache.org/docs/latest/streaming/index.html) [Spark Streaming (DStreams)](https://spark.apache.org/docs/latest/streaming-programming-guide.html) [MLlib (Machine Learning)](https://spark.apache.org/docs/latest/ml-guide.html) [GraphX (Graph Processing)](https://spark.apache.org/docs/latest/graphx-programming-guide.html) [SparkR (R on Spark)](https://spark.apache.org/docs/latest/sparkr.html) [PySpark (Python on Spark)](https://spark.apache.org/docs/latest/api/python/getting_started/index.html) [Declarative Pipelines](https://spark.apache.org/docs/latest/declarative-pipelines-programming-guide.html)
  * [API Docs](https://spark.apache.org/docs/latest/mllib-evaluation-metrics.html)
[Python](https://spark.apache.org/docs/latest/api/python/index.html) [Scala](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html) [Java](https://spark.apache.org/docs/latest/api/java/index.html) [R](https://spark.apache.org/docs/latest/api/R/index.html) [SQL, Built-in Functions](https://spark.apache.org/docs/latest/api/sql/index.html)
  * [Deploying](https://spark.apache.org/docs/latest/mllib-evaluation-metrics.html)
[Overview](https://spark.apache.org/docs/latest/cluster-overview.html) [Submitting Applications](https://spark.apache.org/docs/latest/submitting-applications.html) [Spark Standalone](https://spark.apache.org/docs/latest/spark-standalone.html) [YARN](https://spark.apache.org/docs/latest/running-on-yarn.html) [Kubernetes](https://spark.apache.org/docs/latest/running-on-kubernetes.html)
  * [More](https://spark.apache.org/docs/latest/mllib-evaluation-metrics.html)
[Configuration](https://spark.apache.org/docs/latest/configuration.html) [Monitoring](https://spark.apache.org/docs/latest/monitoring.html) [Tuning Guide](https://spark.apache.org/docs/latest/tuning.html) [Job Scheduling](https://spark.apache.org/docs/latest/job-scheduling.html) [Security](https://spark.apache.org/docs/latest/security.html) [Hardware Provisioning](https://spark.apache.org/docs/latest/hardware-provisioning.html) [Migration Guide](https://spark.apache.org/docs/latest/migration-guide.html) [Building Spark](https://spark.apache.org/docs/latest/building-spark.html) [Contributing to Spark](https://spark.apache.org/contributing.html) [Third Party Projects](https://spark.apache.org/third-party-projects.html)
  * 

###  [MLlib: Main Guide](https://spark.apache.org/docs/latest/ml-guide.html)[](https://spark.apache.org/docs/latest/mllib-evaluation-metrics.html#mllib-main-guide)
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


###  [MLlib: RDD-based API Guide](https://spark.apache.org/docs/latest/mllib-guide.html)[](https://spark.apache.org/docs/latest/mllib-evaluation-metrics.html#mllib-rdd-based-api-guide)
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


# Evaluation Metrics - RDD-based API[](https://spark.apache.org/docs/latest/mllib-evaluation-metrics.html#evaluation-metrics-rdd-based-api)
  * [Classification model evaluation](https://spark.apache.org/docs/latest/mllib-evaluation-metrics.html#classification-model-evaluation)
    * [Binary classification](https://spark.apache.org/docs/latest/mllib-evaluation-metrics.html#binary-classification)
      * [Threshold tuning](https://spark.apache.org/docs/latest/mllib-evaluation-metrics.html#threshold-tuning)
    * [Multiclass classification](https://spark.apache.org/docs/latest/mllib-evaluation-metrics.html#multiclass-classification)
      * [Label based metrics](https://spark.apache.org/docs/latest/mllib-evaluation-metrics.html#label-based-metrics)
    * [Multilabel classification](https://spark.apache.org/docs/latest/mllib-evaluation-metrics.html#multilabel-classification)
    * [Ranking systems](https://spark.apache.org/docs/latest/mllib-evaluation-metrics.html#ranking-systems)
  * [Regression model evaluation](https://spark.apache.org/docs/latest/mllib-evaluation-metrics.html#regression-model-evaluation)


`spark.mllib` comes with a number of machine learning algorithms that can be used to learn from and make predictions on data. When these algorithms are applied to build machine learning models, there is a need to evaluate the performance of the model on some criteria, which depends on the application and its requirements. `spark.mllib` also provides a suite of metrics for the purpose of evaluating the performance of machine learning models.
Specific machine learning algorithms fall under broader types of machine learning applications like classification, regression, clustering, etc. Each of these types have well-established metrics for performance evaluation and those metrics that are currently available in `spark.mllib` are detailed in this section.
## Classification model evaluation[](https://spark.apache.org/docs/latest/mllib-evaluation-metrics.html#classification-model-evaluation)
While there are many different types of classification algorithms, the evaluation of classification models all share similar principles. In a [supervised classification problem](https://en.wikipedia.org/wiki/Statistical_classification), there exists a true output and a model-generated predicted output for each data point. For this reason, the results for each data point can be assigned to one of four categories:
  * True Positive (TP) - label is positive and prediction is also positive
  * True Negative (TN) - label is negative and prediction is also negative
  * False Positive (FP) - label is negative but prediction is positive
  * False Negative (FN) - label is positive but prediction is negative


These four numbers are the building blocks for most classifier evaluation metrics. A fundamental point when considering classifier evaluation is that pure accuracy (i.e. was the prediction correct or incorrect) is not generally a good metric. The reason for this is because a dataset may be highly unbalanced. For example, if a model is designed to predict fraud from a dataset where 95% of the data points are _not fraud_ and 5% of the data points are _fraud_ , then a naive classifier that predicts _not fraud_ , regardless of input, will be 95% accurate. For this reason, metrics like [precision and recall](https://en.wikipedia.org/wiki/Precision_and_recall) are typically used because they take into account the _type_ of error. In most applications there is some desired balance between precision and recall, which can be captured by combining the two into a single metric, called the [F-measure](https://en.wikipedia.org/wiki/F1_score).
### Binary classification[](https://spark.apache.org/docs/latest/mllib-evaluation-metrics.html#binary-classification)
[Binary classifiers](https://en.wikipedia.org/wiki/Binary_classification) are used to separate the elements of a given dataset into one of two possible groups (e.g. fraud or not fraud) and is a special case of multiclass classification. Most binary classification metrics can be generalized to multiclass classification metrics.
#### Threshold tuning[](https://spark.apache.org/docs/latest/mllib-evaluation-metrics.html#threshold-tuning)
It is import to understand that many classification models actually output a “score” (often times a probability) for each class, where a higher score indicates higher likelihood. In the binary case, the model may output a probability for each class: $P(Y=1|X)$ and $P(Y=0|X)$. Instead of simply taking the higher probability, there may be some cases where the model might need to be tuned so that it only predicts a class when the probability is very high (e.g. only block a credit card transaction if the model predicts fraud with >90% probability). Therefore, there is a prediction _threshold_ which determines what the predicted class will be based on the probabilities that the model outputs.
Tuning the prediction threshold will change the precision and recall of the model and is an important part of model optimization. In order to visualize how precision, recall, and other metrics change as a function of the threshold it is common practice to plot competing metrics against one another, parameterized by threshold. A P-R curve plots (precision, recall) points for different threshold values, while a [receiver operating characteristic](https://en.wikipedia.org/wiki/Receiver_operating_characteristic), or ROC, curve plots (recall, false positive rate) points.
**Available metrics**  
| Metric  | Definition  |  
| --- | --- |  
| Precision (Positive Predictive Value)  | $PPV=\frac{TP}{TP + FP}$  |  
| Recall (True Positive Rate)  | $TPR=\frac{TP}{P}=\frac{TP}{TP + FN}$  |  
| F-measure  | $F(\beta) = \left(1 + \beta^2\right) \cdot \left(\frac{PPV \cdot TPR} {\beta^2 \cdot PPV + TPR}\right)$  |  
| Receiver Operating Characteristic (ROC)  | $FPR(T)=\int^\infty_{T} P_0(T)\,dT \\\ TPR(T)=\int^\infty_{T} P_1(T)\,dT$  |  
| Area Under ROC Curve  | $AUROC=\int^1_{0} \frac{TP}{P} d\left(\frac{FP}{N}\right)$  |  
| Area Under Precision-Recall Curve  | $AUPRC=\int^1_{0} \frac{TP}{TP+FP} d\left(\frac{TP}{P}\right)$  |  
**Examples**
  * **Python**
  * **Scala**
  * **Java**


The following code snippets illustrate how to load a sample dataset, train a binary classification algorithm on the data, and evaluate the performance of the algorithm by several binary evaluation metrics. 
Refer to the [`BinaryClassificationMetrics` Python docs](https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.mllib.evaluation.BinaryClassificationMetrics.html) and [`LogisticRegressionWithLBFGS` Python docs](https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.mllib.classification.LogisticRegressionWithLBFGS.html) for more details on the API.

```
from pyspark.mllib.classification import LogisticRegressionWithLBFGS
from pyspark.mllib.evaluation import BinaryClassificationMetrics
from pyspark.mllib.util import MLUtils

# Several of the methods available in scala are currently missing from pyspark
# Load training data in LIBSVM format
data = MLUtils.loadLibSVMFile(sc, "data/mllib/sample_binary_classification_data.txt")

# Split data into training (60%) and test (40%)
training, test = data.randomSplit([0.6, 0.4], seed=11)
training.cache()

# Run training algorithm to build the model
model = LogisticRegressionWithLBFGS.train(training)

# Compute raw scores on the test set
predictionAndLabels = test.map(lambda lp: (float(model.predict(lp.features)), lp.label))

# Instantiate metrics object
metrics = BinaryClassificationMetrics(predictionAndLabels)

# Area under precision-recall curve
print("Area under PR = %s" % metrics.areaUnderPR)

# Area under ROC curve
print("Area under ROC = %s" % metrics.areaUnderROC)
```

Find full example code at "examples/src/main/python/mllib/binary_classification_metrics_example.py" in the Spark repo.
Refer to the [`LogisticRegressionWithLBFGS` Scala docs](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/mllib/classification/LogisticRegressionWithLBFGS.html) and [`BinaryClassificationMetrics` Scala docs](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/mllib/evaluation/BinaryClassificationMetrics.html) for details on the API.

```
import org.apache.spark.mllib.classification.LogisticRegressionWithLBFGS
import org.apache.spark.mllib.evaluation.BinaryClassificationMetrics
import org.apache.spark.mllib.regression.LabeledPoint
import org.apache.spark.mllib.util.MLUtils

// Load training data in LIBSVM format
val data = MLUtils.loadLibSVMFile(sc, "data/mllib/sample_binary_classification_data.txt")

// Split data into training (60%) and test (40%)
val Array(training, test) = data.randomSplit(Array(0.6, 0.4), seed = 11L)
training.cache()

// Run training algorithm to build the model
val model = new LogisticRegressionWithLBFGS()
  .setNumClasses(2)
  .run(training)

// Clear the prediction threshold so the model will return probabilities
model.clearThreshold()

// Compute raw scores on the test set
val predictionAndLabels = test.map { case LabeledPoint(label, features) =>
  val prediction = model.predict(features)
  (prediction, label)
}

// Instantiate metrics object
val metrics = new BinaryClassificationMetrics(predictionAndLabels)

// Precision by threshold
val precision = metrics.precisionByThreshold()
precision.collect().foreach { case (t, p) =>
  println(s"Threshold: $t, Precision: $p")
}

// Recall by threshold
val recall = metrics.recallByThreshold()
recall.collect().foreach { case (t, r) =>
  println(s"Threshold: $t, Recall: $r")
}

// Precision-Recall Curve
val PRC = metrics.pr()

// F-measure
val f1Score = metrics.fMeasureByThreshold()
f1Score.collect().foreach { case (t, f) =>
  println(s"Threshold: $t, F-score: $f, Beta = 1")
}

val beta = 0.5
val fScore = metrics.fMeasureByThreshold(beta)
fScore.collect().foreach { case (t, f) =>
  println(s"Threshold: $t, F-score: $f, Beta = 0.5")
}

// AUPRC
val auPRC = metrics.areaUnderPR()
println(s"Area under precision-recall curve = $auPRC")

// Compute thresholds used in ROC and PR curves
val thresholds = precision.map(_._1)

// ROC Curve
val roc = metrics.roc()

// AUROC
val auROC = metrics.areaUnderROC()
println(s"Area under ROC = $auROC")
```

Find full example code at "examples/src/main/scala/org/apache/spark/examples/mllib/BinaryClassificationMetricsExample.scala" in the Spark repo.
Refer to the [`LogisticRegressionModel` Java docs](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/classification/LogisticRegressionModel.html) and [`LogisticRegressionWithLBFGS` Java docs](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/classification/LogisticRegressionWithLBFGS.html) for details on the API.

```
import scala.Tuple2;

import org.apache.spark.api.java.*;
import org.apache.spark.mllib.classification.LogisticRegressionModel;
import org.apache.spark.mllib.classification.LogisticRegressionWithLBFGS;
import org.apache.spark.mllib.evaluation.BinaryClassificationMetrics;
import org.apache.spark.mllib.regression.LabeledPoint;
import org.apache.spark.mllib.util.MLUtils;

String path = "data/mllib/sample_binary_classification_data.txt";
JavaRDD<LabeledPoint> data = MLUtils.loadLibSVMFile(sc, path).toJavaRDD();

// Split initial RDD into two... [60% training data, 40% testing data].
JavaRDD<LabeledPoint>[] splits =
  data.randomSplit(new double[]{0.6, 0.4}, 11L);
JavaRDD<LabeledPoint> training = splits[0].cache();
JavaRDD<LabeledPoint> test = splits[1];

// Run training algorithm to build the model.
LogisticRegressionModel model = new LogisticRegressionWithLBFGS()
  .setNumClasses(2)
  .run(training.rdd());

// Clear the prediction threshold so the model will return probabilities
model.clearThreshold();

// Compute raw scores on the test set.
JavaPairRDD<Object, Object> predictionAndLabels = test.mapToPair(p ->
  new Tuple2<>(model.predict(p.features()), p.label()));

// Get evaluation metrics.
BinaryClassificationMetrics metrics =
  new BinaryClassificationMetrics(predictionAndLabels.rdd());

// Precision by threshold
JavaRDD<Tuple2<Object, Object>> precision = metrics.precisionByThreshold().toJavaRDD();
System.out.println("Precision by threshold: " + precision.collect());

// Recall by threshold
JavaRDD<?> recall = metrics.recallByThreshold().toJavaRDD();
System.out.println("Recall by threshold: " + recall.collect());

// F Score by threshold
JavaRDD<?> f1Score = metrics.fMeasureByThreshold().toJavaRDD();
System.out.println("F1 Score by threshold: " + f1Score.collect());

JavaRDD<?> f2Score = metrics.fMeasureByThreshold(2.0).toJavaRDD();
System.out.println("F2 Score by threshold: " + f2Score.collect());

// Precision-recall curve
JavaRDD<?> prc = metrics.pr().toJavaRDD();
System.out.println("Precision-recall curve: " + prc.collect());

// Thresholds
JavaRDD<Double> thresholds = precision.map(t -> Double.parseDouble(t._1().toString()));

// ROC Curve
JavaRDD<?> roc = metrics.roc().toJavaRDD();
System.out.println("ROC curve: " + roc.collect());

// AUPRC
System.out.println("Area under precision-recall curve = " + metrics.areaUnderPR());

// AUROC
System.out.println("Area under ROC = " + metrics.areaUnderROC());

// Save and load model
model.save(sc, "target/tmp/LogisticRegressionModel");
LogisticRegressionModel.load(sc, "target/tmp/LogisticRegressionModel");
```

Find full example code at "examples/src/main/java/org/apache/spark/examples/mllib/JavaBinaryClassificationMetricsExample.java" in the Spark repo.
### Multiclass classification[](https://spark.apache.org/docs/latest/mllib-evaluation-metrics.html#multiclass-classification)
A [multiclass classification](https://en.wikipedia.org/wiki/Multiclass_classification) describes a classification problem where there are $M \gt 2$ possible labels for each data point (the case where $M=2$ is the binary classification problem). For example, classifying handwriting samples to the digits 0 to 9, having 10 possible classes.
For multiclass metrics, the notion of positives and negatives is slightly different. Predictions and labels can still be positive or negative, but they must be considered under the context of a particular class. Each label and prediction take on the value of one of the multiple classes and so they are said to be positive for their particular class and negative for all other classes. So, a true positive occurs whenever the prediction and the label match, while a true negative occurs when neither the prediction nor the label take on the value of a given class. By this convention, there can be multiple true negatives for a given data sample. The extension of false negatives and false positives from the former definitions of positive and negative labels is straightforward.
#### Label based metrics[](https://spark.apache.org/docs/latest/mllib-evaluation-metrics.html#label-based-metrics)
Opposed to binary classification where there are only two possible labels, multiclass classification problems have many possible labels and so the concept of label-based metrics is introduced. Accuracy measures precision across all labels - the number of times any class was predicted correctly (true positives) normalized by the number of data points. Precision by label considers only one class, and measures the number of time a specific label was predicted correctly normalized by the number of times that label appears in the output.
**Available metrics**
Define the class, or label, set as
\\[L = \\{\ell_0, \ell_1, \ldots, \ell_{M-1} \\}\\] 
The true output vector $\mathbf{y}$ consists of $N$ elements
\\[\mathbf{y}_0, \mathbf{y}_1, \ldots, \mathbf{y}_{N-1} \in L\\] 
A multiclass prediction algorithm generates a prediction vector $\hat{\mathbf{y}}$ of $N$ elements
\\[\hat{\mathbf{y}}_0, \hat{\mathbf{y}}_1, \ldots, \hat{\mathbf{y}}_{N-1} \in L\\] 
For this section, a modified delta function $\hat{\delta}(x)$ will prove useful
\\[\hat{\delta}(x) = \begin{cases}1 & \text{if $x = 0$}, \\\ 0 & \text{otherwise}.\end{cases}\\]   
| Metric  | Definition  |  
| --- | --- |  
| Confusion Matrix  |  $C_{ij} = \sum_{k=0}^{N-1} \hat{\delta}(\mathbf{y}_k-\ell_i) \cdot \hat{\delta}(\hat{\mathbf{y}}_k - \ell_j)\\\ \\\ \left( \begin{array}{ccc} \sum_{k=0}^{N-1} \hat{\delta}(\mathbf{y}_k-\ell_1) \cdot \hat{\delta}(\hat{\mathbf{y}}_k - \ell_1) & \ldots & \sum_{k=0}^{N-1} \hat{\delta}(\mathbf{y}_k-\ell_1) \cdot \hat{\delta}(\hat{\mathbf{y}}_k - \ell_N) \\\ \vdots & \ddots & \vdots \\\ \sum_{k=0}^{N-1} \hat{\delta}(\mathbf{y}_k-\ell_N) \cdot \hat{\delta}(\hat{\mathbf{y}}_k - \ell_1) & \ldots & \sum_{k=0}^{N-1} \hat{\delta}(\mathbf{y}_k-\ell_N) \cdot \hat{\delta}(\hat{\mathbf{y}}_k - \ell_N) \end{array} \right)$   |  
| Accuracy  | $ACC = \frac{TP}{TP + FP} = \frac{1}{N}\sum_{i=0}^{N-1} \hat{\delta}\left(\hat{\mathbf{y}}_i - \mathbf{y}_i\right)$  |  
| Precision by label  | $PPV(\ell) = \frac{TP}{TP + FP} = \frac{\sum_{i=0}^{N-1} \hat{\delta}(\hat{\mathbf{y}}_i - \ell) \cdot \hat{\delta}(\mathbf{y}_i - \ell)} {\sum_{i=0}^{N-1} \hat{\delta}(\hat{\mathbf{y}}_i - \ell)}$  |  
| Recall by label  | $TPR(\ell)=\frac{TP}{P} = \frac{\sum_{i=0}^{N-1} \hat{\delta}(\hat{\mathbf{y}}_i - \ell) \cdot \hat{\delta}(\mathbf{y}_i - \ell)} {\sum_{i=0}^{N-1} \hat{\delta}(\mathbf{y}_i - \ell)}$  |  
| F-measure by label  | $F(\beta, \ell) = \left(1 + \beta^2\right) \cdot \left(\frac{PPV(\ell) \cdot TPR(\ell)} {\beta^2 \cdot PPV(\ell) + TPR(\ell)}\right)$  |  
| Weighted precision  | $PPV_{w}= \frac{1}{N} \sum\nolimits_{\ell \in L} PPV(\ell) \cdot \sum_{i=0}^{N-1} \hat{\delta}(\mathbf{y}_i-\ell)$  |  
| Weighted recall  | $TPR_{w}= \frac{1}{N} \sum\nolimits_{\ell \in L} TPR(\ell) \cdot \sum_{i=0}^{N-1} \hat{\delta}(\mathbf{y}_i-\ell)$  |  
| Weighted F-measure  | $F_{w}(\beta)= \frac{1}{N} \sum\nolimits_{\ell \in L} F(\beta, \ell) \cdot \sum_{i=0}^{N-1} \hat{\delta}(\mathbf{y}_i-\ell)$  |  
**Examples**
  * **Python**
  * **Scala**
  * **Java**


The following code snippets illustrate how to load a sample dataset, train a multiclass classification algorithm on the data, and evaluate the performance of the algorithm by several multiclass classification evaluation metrics. 
Refer to the [`MulticlassMetrics` Python docs](https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.mllib.evaluation.MulticlassMetrics.html) for more details on the API.

```
from pyspark.mllib.classification import LogisticRegressionWithLBFGS
from pyspark.mllib.util import MLUtils
from pyspark.mllib.evaluation import MulticlassMetrics

# Load training data in LIBSVM format
data = MLUtils.loadLibSVMFile(sc, "data/mllib/sample_multiclass_classification_data.txt")

# Split data into training (60%) and test (40%)
training, test = data.randomSplit([0.6, 0.4], seed=11)
training.cache()

# Run training algorithm to build the model
model = LogisticRegressionWithLBFGS.train(training, numClasses=3)

# Compute raw scores on the test set
predictionAndLabels = test.map(lambda lp: (float(model.predict(lp.features)), lp.label))

# Instantiate metrics object
metrics = MulticlassMetrics(predictionAndLabels)

# Overall statistics
precision = metrics.precision(1.0)
recall = metrics.recall(1.0)
f1Score = metrics.fMeasure(1.0)
print("Summary Stats")
print("Precision = %s" % precision)
print("Recall = %s" % recall)
print("F1 Score = %s" % f1Score)

# Statistics by class
labels = data.map(lambda lp: lp.label).distinct().collect()
for label in sorted(labels):
    print("Class %s precision = %s" % (label, metrics.precision(label)))
    print("Class %s recall = %s" % (label, metrics.recall(label)))
    print("Class %s F1 Measure = %s" % (label, metrics.fMeasure(label, beta=1.0)))

# Weighted stats
print("Weighted recall = %s" % metrics.weightedRecall)
print("Weighted precision = %s" % metrics.weightedPrecision)
print("Weighted F(1) Score = %s" % metrics.weightedFMeasure())
print("Weighted F(0.5) Score = %s" % metrics.weightedFMeasure(beta=0.5))
print("Weighted false positive rate = %s" % metrics.weightedFalsePositiveRate)
```

Find full example code at "examples/src/main/python/mllib/multi_class_metrics_example.py" in the Spark repo.
Refer to the [`MulticlassMetrics` Scala docs](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/mllib/evaluation/MulticlassMetrics.html) for details on the API.

```
import org.apache.spark.mllib.classification.LogisticRegressionWithLBFGS
import org.apache.spark.mllib.evaluation.MulticlassMetrics
import org.apache.spark.mllib.regression.LabeledPoint
import org.apache.spark.mllib.util.MLUtils

// Load training data in LIBSVM format
val data = MLUtils.loadLibSVMFile(sc, "data/mllib/sample_multiclass_classification_data.txt")

// Split data into training (60%) and test (40%)
val Array(training, test) = data.randomSplit(Array(0.6, 0.4), seed = 11L)
training.cache()

// Run training algorithm to build the model
val model = new LogisticRegressionWithLBFGS()
  .setNumClasses(3)
  .run(training)

// Compute raw scores on the test set
val predictionAndLabels = test.map { case LabeledPoint(label, features) =>
  val prediction = model.predict(features)
  (prediction, label)
}

// Instantiate metrics object
val metrics = new MulticlassMetrics(predictionAndLabels)

// Confusion matrix
println("Confusion matrix:")
println(metrics.confusionMatrix)

// Overall Statistics
val accuracy = metrics.accuracy
println("Summary Statistics")
println(s"Accuracy = $accuracy")

// Precision by label
val labels = metrics.labels
labels.foreach { l =>
  println(s"Precision($l) = " + metrics.precision(l))
}

// Recall by label
labels.foreach { l =>
  println(s"Recall($l) = " + metrics.recall(l))
}

// False positive rate by label
labels.foreach { l =>
  println(s"FPR($l) = " + metrics.falsePositiveRate(l))
}

// F-measure by label
labels.foreach { l =>
  println(s"F1-Score($l) = " + metrics.fMeasure(l))
}

// Weighted stats
println(s"Weighted precision: ${metrics.weightedPrecision}")
println(s"Weighted recall: ${metrics.weightedRecall}")
println(s"Weighted F1 score: ${metrics.weightedFMeasure}")
println(s"Weighted false positive rate: ${metrics.weightedFalsePositiveRate}")
```

Find full example code at "examples/src/main/scala/org/apache/spark/examples/mllib/MulticlassMetricsExample.scala" in the Spark repo.
Refer to the [`MulticlassMetrics` Java docs](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/evaluation/MulticlassMetrics.html) for details on the API.

```
import scala.Tuple2;

import org.apache.spark.api.java.*;
import org.apache.spark.mllib.classification.LogisticRegressionModel;
import org.apache.spark.mllib.classification.LogisticRegressionWithLBFGS;
import org.apache.spark.mllib.evaluation.MulticlassMetrics;
import org.apache.spark.mllib.regression.LabeledPoint;
import org.apache.spark.mllib.util.MLUtils;
import org.apache.spark.mllib.linalg.Matrix;

String path = "data/mllib/sample_multiclass_classification_data.txt";
JavaRDD<LabeledPoint> data = MLUtils.loadLibSVMFile(sc, path).toJavaRDD();

// Split initial RDD into two... [60% training data, 40% testing data].
JavaRDD<LabeledPoint>[] splits = data.randomSplit(new double[]{0.6, 0.4}, 11L);
JavaRDD<LabeledPoint> training = splits[0].cache();
JavaRDD<LabeledPoint> test = splits[1];

// Run training algorithm to build the model.
LogisticRegressionModel model = new LogisticRegressionWithLBFGS()
  .setNumClasses(3)
  .run(training.rdd());

// Compute raw scores on the test set.
JavaPairRDD<Object, Object> predictionAndLabels = test.mapToPair(p ->
  new Tuple2<>(model.predict(p.features()), p.label()));

// Get evaluation metrics.
MulticlassMetrics metrics = new MulticlassMetrics(predictionAndLabels.rdd());

// Confusion matrix
Matrix confusion = metrics.confusionMatrix();
System.out.println("Confusion matrix: \n" + confusion);

// Overall statistics
System.out.println("Accuracy = " + metrics.accuracy());

// Stats by labels
for (int i = 0; i < metrics.labels().length; i++) {
  System.out.format("Class %f precision = %f\n", metrics.labels()[i],metrics.precision(
    metrics.labels()[i]));
  System.out.format("Class %f recall = %f\n", metrics.labels()[i], metrics.recall(
    metrics.labels()[i]));
  System.out.format("Class %f F1 score = %f\n", metrics.labels()[i], metrics.fMeasure(
    metrics.labels()[i]));
}

//Weighted stats
System.out.format("Weighted precision = %f\n", metrics.weightedPrecision());
System.out.format("Weighted recall = %f\n", metrics.weightedRecall());
System.out.format("Weighted F1 score = %f\n", metrics.weightedFMeasure());
System.out.format("Weighted false positive rate = %f\n", metrics.weightedFalsePositiveRate());

// Save and load model
model.save(sc, "target/tmp/LogisticRegressionModel");
LogisticRegressionModel sameModel = LogisticRegressionModel.load(sc,
  "target/tmp/LogisticRegressionModel");
```

Find full example code at "examples/src/main/java/org/apache/spark/examples/mllib/JavaMulticlassClassificationMetricsExample.java" in the Spark repo.
### Multilabel classification[](https://spark.apache.org/docs/latest/mllib-evaluation-metrics.html#multilabel-classification)
A [multilabel classification](https://en.wikipedia.org/wiki/Multi-label_classification) problem involves mapping each sample in a dataset to a set of class labels. In this type of classification problem, the labels are not mutually exclusive. For example, when classifying a set of news articles into topics, a single article might be both science and politics.
Because the labels are not mutually exclusive, the predictions and true labels are now vectors of label _sets_ , rather than vectors of labels. Multilabel metrics, therefore, extend the fundamental ideas of precision, recall, etc. to operations on sets. For example, a true positive for a given class now occurs when that class exists in the predicted set and it exists in the true label set, for a specific data point.
**Available metrics**
Here we define a set $D$ of $N$ documents
\\[D = \left\\{d_0, d_1, ..., d_{N-1}\right\\}\\] 
Define $L_0, L_1, …, L_{N-1}$ to be a family of label sets and $P_0, P_1, …, P_{N-1}$ to be a family of prediction sets where $L_i$ and $P_i$ are the label set and prediction set, respectively, that correspond to document $d_i$.
The set of all unique labels is given by
\\[L = \bigcup_{k=0}^{N-1} L_k\\] 
The following definition of indicator function $I_A(x)$ on a set $A$ will be necessary
\\[I_A(x) = \begin{cases}1 & \text{if $x \in A$}, \\\ 0 & \text{otherwise}.\end{cases}\\]   
| Metric  | Definition  |  
| --- | --- |  
| Precision  | $\frac{1}{N} \sum_{i=0}^{N-1} \frac{\left|P_i \cap L_i\right|}{\left|P_i\right|}$  |  
| Recall  | $\frac{1}{N} \sum_{i=0}^{N-1} \frac{\left|L_i \cap P_i\right|}{\left|L_i\right|}$  |  
| Accuracy  |  $\frac{1}{N} \sum_{i=0}^{N - 1} \frac{\left|L_i \cap P_i \right|} {\left|L_i\right| + \left|P_i\right| - \left|L_i \cap P_i \right|}$   |  
| Precision by label  | $PPV(\ell)=\frac{TP}{TP + FP}= \frac{\sum_{i=0}^{N-1} I_{P_i}(\ell) \cdot I_{L_i}(\ell)} {\sum_{i=0}^{N-1} I_{P_i}(\ell)}$  |  
| Recall by label  | $TPR(\ell)=\frac{TP}{P}= \frac{\sum_{i=0}^{N-1} I_{P_i}(\ell) \cdot I_{L_i}(\ell)} {\sum_{i=0}^{N-1} I_{L_i}(\ell)}$  |  
| F1-measure by label  | $F1(\ell) = 2 \cdot \left(\frac{PPV(\ell) \cdot TPR(\ell)} {PPV(\ell) + TPR(\ell)}\right)$  |  
| Hamming Loss  |  $\frac{1}{N \cdot \left|L\right|} \sum_{i=0}^{N - 1} \left|L_i\right| + \left|P_i\right| - 2\left|L_i \cap P_i\right|$   |  
| Subset Accuracy  | $\frac{1}{N} \sum_{i=0}^{N-1} I_{\\{L_i\\}}(P_i)$  |  
| F1 Measure  | $\frac{1}{N} \sum_{i=0}^{N-1} 2 \frac{\left|P_i \cap L_i\right|}{\left|P_i\right| \cdot \left|L_i\right|}$  |  
| Micro precision  | $\frac{TP}{TP + FP}=\frac{\sum_{i=0}^{N-1} \left|P_i \cap L_i\right|} {\sum_{i=0}^{N-1} \left|P_i \cap L_i\right| + \sum_{i=0}^{N-1} \left|P_i - L_i\right|}$  |  
| Micro recall  | $\frac{TP}{TP + FN}=\frac{\sum_{i=0}^{N-1} \left|P_i \cap L_i\right|} {\sum_{i=0}^{N-1} \left|P_i \cap L_i\right| + \sum_{i=0}^{N-1} \left|L_i - P_i\right|}$  |  
| Micro F1 Measure  |  $2 \cdot \frac{TP}{2 \cdot TP + FP + FN}=2 \cdot \frac{\sum_{i=0}^{N-1} \left|P_i \cap L_i\right|}{2 \cdot \sum_{i=0}^{N-1} \left|P_i \cap L_i\right| + \sum_{i=0}^{N-1} \left|L_i - P_i\right| + \sum_{i=0}^{N-1} \left|P_i - L_i\right|}$   |  
**Examples**
The following code snippets illustrate how to evaluate the performance of a multilabel classifier. The examples use the fake prediction and label data for multilabel classification that is shown below.
Document predictions:
  * doc 0 - predict 0, 1 - class 0, 2
  * doc 1 - predict 0, 2 - class 0, 1
  * doc 2 - predict none - class 0
  * doc 3 - predict 2 - class 2
  * doc 4 - predict 2, 0 - class 2, 0
  * doc 5 - predict 0, 1, 2 - class 0, 1
  * doc 6 - predict 1 - class 1, 2


Predicted classes:
  * class 0 - doc 0, 1, 4, 5 (total 4)
  * class 1 - doc 0, 5, 6 (total 3)
  * class 2 - doc 1, 3, 4, 5 (total 4)


True classes:
  * class 0 - doc 0, 1, 2, 4, 5 (total 5)
  * class 1 - doc 1, 5, 6 (total 3)
  * class 2 - doc 0, 3, 4, 6 (total 4)


  * **Python**
  * **Scala**
  * **Java**


Refer to the [`MultilabelMetrics` Python docs](https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.mllib.evaluation.MultilabelMetrics.html) for more details on the API.

```
from pyspark.mllib.evaluation import MultilabelMetrics

scoreAndLabels = sc.parallelize([
    ([0.0, 1.0], [0.0, 2.0]),
    ([0.0, 2.0], [0.0, 1.0]),
    ([], [0.0]),
    ([2.0], [2.0]),
    ([2.0, 0.0], [2.0, 0.0]),
    ([0.0, 1.0, 2.0], [0.0, 1.0]),
    ([1.0], [1.0, 2.0])])

# Instantiate metrics object
metrics = MultilabelMetrics(scoreAndLabels)

# Summary stats
print("Recall = %s" % metrics.recall())
print("Precision = %s" % metrics.precision())
print("F1 measure = %s" % metrics.f1Measure())
print("Accuracy = %s" % metrics.accuracy)

# Individual label stats
labels = scoreAndLabels.flatMap(lambda x: x[1]).distinct().collect()
for label in labels:
    print("Class %s precision = %s" % (label, metrics.precision(label)))
    print("Class %s recall = %s" % (label, metrics.recall(label)))
    print("Class %s F1 Measure = %s" % (label, metrics.f1Measure(label)))

# Micro stats
print("Micro precision = %s" % metrics.microPrecision)
print("Micro recall = %s" % metrics.microRecall)
print("Micro F1 measure = %s" % metrics.microF1Measure)

# Hamming loss
print("Hamming loss = %s" % metrics.hammingLoss)

# Subset accuracy
print("Subset accuracy = %s" % metrics.subsetAccuracy)
```

Find full example code at "examples/src/main/python/mllib/multi_label_metrics_example.py" in the Spark repo.
Refer to the [`MultilabelMetrics` Scala docs](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/mllib/evaluation/MultilabelMetrics.html) for details on the API.

```
import org.apache.spark.mllib.evaluation.MultilabelMetrics
import org.apache.spark.rdd.RDD

val scoreAndLabels: RDD[(Array[Double], Array[Double])] = sc.parallelize(
  Seq((Array(0.0, 1.0), Array(0.0, 2.0)),
    (Array(0.0, 2.0), Array(0.0, 1.0)),
    (Array.empty[Double], Array(0.0)),
    (Array(2.0), Array(2.0)),
    (Array(2.0, 0.0), Array(2.0, 0.0)),
    (Array(0.0, 1.0, 2.0), Array(0.0, 1.0)),
    (Array(1.0), Array(1.0, 2.0))), 2)

// Instantiate metrics object
val metrics = new MultilabelMetrics(scoreAndLabels)

// Summary stats
println(s"Recall = ${metrics.recall}")
println(s"Precision = ${metrics.precision}")
println(s"F1 measure = ${metrics.f1Measure}")
println(s"Accuracy = ${metrics.accuracy}")

// Individual label stats
metrics.labels.foreach(label =>
  println(s"Class $label precision = ${metrics.precision(label)}"))
metrics.labels.foreach(label => println(s"Class $label recall = ${metrics.recall(label)}"))
metrics.labels.foreach(label => println(s"Class $label F1-score = ${metrics.f1Measure(label)}"))

// Micro stats
println(s"Micro recall = ${metrics.microRecall}")
println(s"Micro precision = ${metrics.microPrecision}")
println(s"Micro F1 measure = ${metrics.microF1Measure}")

// Hamming loss
println(s"Hamming loss = ${metrics.hammingLoss}")

// Subset accuracy
println(s"Subset accuracy = ${metrics.subsetAccuracy}")
```

Find full example code at "examples/src/main/scala/org/apache/spark/examples/mllib/MultiLabelMetricsExample.scala" in the Spark repo.
Refer to the [`MultilabelMetrics` Java docs](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/evaluation/MultilabelMetrics.html) for details on the API.

```
import java.util.Arrays;
import java.util.List;

import scala.Tuple2;

import org.apache.spark.api.java.*;
import org.apache.spark.mllib.evaluation.MultilabelMetrics;
import org.apache.spark.SparkConf;

List<Tuple2<double[], double[]>> data = Arrays.asList(
  new Tuple2<>(new double[]{0.0, 1.0}, new double[]{0.0, 2.0}),
  new Tuple2<>(new double[]{0.0, 2.0}, new double[]{0.0, 1.0}),
  new Tuple2<>(new double[]{}, new double[]{0.0}),
  new Tuple2<>(new double[]{2.0}, new double[]{2.0}),
  new Tuple2<>(new double[]{2.0, 0.0}, new double[]{2.0, 0.0}),
  new Tuple2<>(new double[]{0.0, 1.0, 2.0}, new double[]{0.0, 1.0}),
  new Tuple2<>(new double[]{1.0}, new double[]{1.0, 2.0})
);
JavaRDD<Tuple2<double[], double[]>> scoreAndLabels = sc.parallelize(data);

// Instantiate metrics object
MultilabelMetrics metrics = new MultilabelMetrics(scoreAndLabels.rdd());

// Summary stats
System.out.format("Recall = %f\n", metrics.recall());
System.out.format("Precision = %f\n", metrics.precision());
System.out.format("F1 measure = %f\n", metrics.f1Measure());
System.out.format("Accuracy = %f\n", metrics.accuracy());

// Stats by labels
for (int i = 0; i < metrics.labels().length - 1; i++) {
  System.out.format("Class %1.1f precision = %f\n", metrics.labels()[i], metrics.precision(
    metrics.labels()[i]));
  System.out.format("Class %1.1f recall = %f\n", metrics.labels()[i], metrics.recall(
    metrics.labels()[i]));
  System.out.format("Class %1.1f F1 score = %f\n", metrics.labels()[i], metrics.f1Measure(
    metrics.labels()[i]));
}

// Micro stats
System.out.format("Micro recall = %f\n", metrics.microRecall());
System.out.format("Micro precision = %f\n", metrics.microPrecision());
System.out.format("Micro F1 measure = %f\n", metrics.microF1Measure());

// Hamming loss
System.out.format("Hamming loss = %f\n", metrics.hammingLoss());

// Subset accuracy
System.out.format("Subset accuracy = %f\n", metrics.subsetAccuracy());
```

Find full example code at "examples/src/main/java/org/apache/spark/examples/mllib/JavaMultiLabelClassificationMetricsExample.java" in the Spark repo.
### Ranking systems[](https://spark.apache.org/docs/latest/mllib-evaluation-metrics.html#ranking-systems)
The role of a ranking algorithm (often thought of as a [recommender system](https://en.wikipedia.org/wiki/Recommender_system)) is to return to the user a set of relevant items or documents based on some training data. The definition of relevance may vary and is usually application specific. Ranking system metrics aim to quantify the effectiveness of these rankings or recommendations in various contexts. Some metrics compare a set of recommended documents to a ground truth set of relevant documents, while other metrics may incorporate numerical ratings explicitly.
**Available metrics**
A ranking system usually deals with a set of $M$ users
\\[U = \left\\{u_0, u_1, ..., u_{M-1}\right\\}\\] 
Each user ($u_i$) having a set of $N_i$ ground truth relevant documents
\\[D_i = \left\\{d_0, d_1, ..., d_{N_i-1}\right\\}\\] 
And a list of $Q_i$ recommended documents, in order of decreasing relevance
\\[R_i = \left[r_0, r_1, ..., r_{Q_i-1}\right]\\] 
The goal of the ranking system is to produce the most relevant set of documents for each user. The relevance of the sets and the effectiveness of the algorithms can be measured using the metrics listed below.
It is necessary to define a function which, provided a recommended document and a set of ground truth relevant documents, returns a relevance score for the recommended document.
\\[rel_D(r) = \begin{cases}1 & \text{if $r \in D$}, \\\ 0 & \text{otherwise}.\end{cases}\\]   
| Metric  | Definition  | Notes  |  
| --- | --- | --- |  
|  Precision at k   |  $p(k)=\frac{1}{M} \sum_{i=0}^{M-1} {\frac{1}{k} \sum_{j=0}^{\text{min}(Q_i, k) - 1} rel_{D_i}(R_i(j))}$   |  [Precision at k](https://en.wikipedia.org/wiki/Evaluation_measures_\(information_retrieval\)#Precision_at_k) is a measure of how many of the first k recommended documents are in the set of true relevant documents averaged across all users. In this metric, the order of the recommendations is not taken into account.   |  
| Mean Average Precision  |  $MAP=\frac{1}{M} \sum_{i=0}^{M-1} {\frac{1}{N_i} \sum_{j=0}^{Q_i-1} \frac{rel_{D_i}(R_i(j))}{j + 1}}$   |  [MAP](https://en.wikipedia.org/wiki/Evaluation_measures_\(information_retrieval\)#Mean_average_precision) is a measure of how many of the recommended documents are in the set of true relevant documents, where the order of the recommendations is taken into account (i.e. penalty for highly relevant documents is higher).   |  
| Normalized Discounted Cumulative Gain  |  $NDCG(k)=\frac{1}{M} \sum_{i=0}^{M-1} {\frac{1}{IDCG(D_i, k)}\sum_{j=0}^{n-1} \frac{rel_{D_i}(R_i(j))}{\text{log}(j+2)}} \\\ \text{Where} \\\ \hspace{5 mm} n = \text{min}\left(\text{max}\left(Q_i, N_i\right),k\right) \\\ \hspace{5 mm} IDCG(D, k) = \sum_{j=0}^{\text{min}(\left|D\right|, k) - 1} \frac{1}{\text{log}(j+2)}$   |  [NDCG at k](https://en.wikipedia.org/wiki/Discounted_cumulative_gain#Normalized_DCG) is a measure of how many of the first k recommended documents are in the set of true relevant documents averaged across all users. In contrast to precision at k, this metric takes into account the order of the recommendations (documents are assumed to be in order of decreasing relevance).   |  
**Examples**
The following code snippets illustrate how to load a sample dataset, train an alternating least squares recommendation model on the data, and evaluate the performance of the recommender by several ranking metrics. A brief summary of the methodology is provided below.
MovieLens ratings are on a scale of 1-5:
  * 5: Must see
  * 4: Will enjoy
  * 3: It’s okay
  * 2: Fairly bad
  * 1: Awful


So we should not recommend a movie if the predicted rating is less than 3. To map ratings to confidence scores, we use:
  * 5 -> 2.5
  * 4 -> 1.5
  * 3 -> 0.5
  * 2 -> -0.5
  * 1 -> -1.5.


This mappings means unobserved entries are generally between It’s okay and Fairly bad. The semantics of 0 in this expanded world of non-positive weights are “the same as never having interacted at all.”
  * **Python**
  * **Scala**
  * **Java**


Refer to the [`RegressionMetrics` Python docs](https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.mllib.evaluation.RegressionMetrics.html) and [`RankingMetrics` Python docs](https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.mllib.evaluation.RankingMetrics.html) for more details on the API.

```
from pyspark.mllib.recommendation import ALS, Rating
from pyspark.mllib.evaluation import RegressionMetrics

# Read in the ratings data
lines = sc.textFile("data/mllib/sample_movielens_data.txt")

def parseLine(line):
    fields = line.split("::")
    return Rating(int(fields[0]), int(fields[1]), float(fields[2]) - 2.5)
ratings = lines.map(lambda r: parseLine(r))

# Train a model on to predict user-product ratings
model = ALS.train(ratings, 10, 10, 0.01)

# Get predicted ratings on all existing user-product pairs
testData = ratings.map(lambda p: (p.user, p.product))
predictions = model.predictAll(testData).map(lambda r: ((r.user, r.product), r.rating))

ratingsTuple = ratings.map(lambda r: ((r.user, r.product), r.rating))
scoreAndLabels = predictions.join(ratingsTuple).map(lambda tup: tup[1])

# Instantiate regression metrics to compare predicted and actual ratings
metrics = RegressionMetrics(scoreAndLabels)

# Root mean squared error
print("RMSE = %s" % metrics.rootMeanSquaredError)

# R-squared
print("R-squared = %s" % metrics.r2)
```

Find full example code at "examples/src/main/python/mllib/ranking_metrics_example.py" in the Spark repo.
Refer to the [`RegressionMetrics` Scala docs](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/mllib/evaluation/RegressionMetrics.html) and [`RankingMetrics` Scala docs](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/mllib/evaluation/RankingMetrics.html) for details on the API.

```
import org.apache.spark.mllib.evaluation.{RankingMetrics, RegressionMetrics}
import org.apache.spark.mllib.recommendation.{ALS, Rating}

// Read in the ratings data
val ratings = spark.read.textFile("data/mllib/sample_movielens_data.txt").rdd.map { line =>
  val fields = line.split("::")
  Rating(fields(0).toInt, fields(1).toInt, fields(2).toDouble - 2.5)
}.cache()

// Map ratings to 1 or 0, 1 indicating a movie that should be recommended
val binarizedRatings = ratings.map(r => Rating(r.user, r.product,
  if (r.rating > 0) 1.0 else 0.0)).cache()

// Summarize ratings
val numRatings = ratings.count()
val numUsers = ratings.map(_.user).distinct().count()
val numMovies = ratings.map(_.product).distinct().count()
println(s"Got $numRatings ratings from $numUsers users on $numMovies movies.")

// Build the model
val numIterations = 10
val rank = 10
val lambda = 0.01
val model = ALS.train(ratings, rank, numIterations, lambda)

// Define a function to scale ratings from 0 to 1
def scaledRating(r: Rating): Rating = {
  val scaledRating = math.max(math.min(r.rating, 1.0), 0.0)
  Rating(r.user, r.product, scaledRating)
}

// Get sorted top ten predictions for each user and then scale from [0, 1]
val userRecommended = model.recommendProductsForUsers(10).map { case (user, recs) =>
  (user, recs.map(scaledRating))
}

// Assume that any movie a user rated 3 or higher (which maps to a 1) is a relevant document
// Compare with top ten most relevant documents
val userMovies = binarizedRatings.groupBy(_.user)
val relevantDocuments = userMovies.join(userRecommended).map { case (user, (actual,
predictions)) =>
  (predictions.map(_.product), actual.filter(_.rating > 0.0).map(_.product).toArray)
}

// Instantiate metrics object
val metrics = new RankingMetrics(relevantDocuments)

// Precision at K
Array(1, 3, 5).foreach { k =>
  println(s"Precision at $k = ${metrics.precisionAt(k)}")
}

// Mean average precision
println(s"Mean average precision = ${metrics.meanAveragePrecision}")

// Mean average precision at k
println(s"Mean average precision at 2 = ${metrics.meanAveragePrecisionAt(2)}")

// Normalized discounted cumulative gain
Array(1, 3, 5).foreach { k =>
  println(s"NDCG at $k = ${metrics.ndcgAt(k)}")
}

// Recall at K
Array(1, 3, 5).foreach { k =>
  println(s"Recall at $k = ${metrics.recallAt(k)}")
}

// Get predictions for each data point
val allPredictions = model.predict(ratings.map(r => (r.user, r.product))).map(r => ((r.user,
  r.product), r.rating))
val allRatings = ratings.map(r => ((r.user, r.product), r.rating))
val predictionsAndLabels = allPredictions.join(allRatings).map { case ((user, product),
(predicted, actual)) =>
  (predicted, actual)
}

// Get the RMSE using regression metrics
val regressionMetrics = new RegressionMetrics(predictionsAndLabels)
println(s"RMSE = ${regressionMetrics.rootMeanSquaredError}")

// R-squared
println(s"R-squared = ${regressionMetrics.r2}")
```

Find full example code at "examples/src/main/scala/org/apache/spark/examples/mllib/RankingMetricsExample.scala" in the Spark repo.
Refer to the [`RegressionMetrics` Java docs](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/evaluation/RegressionMetrics.html) and [`RankingMetrics` Java docs](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/evaluation/RankingMetrics.html) for details on the API.

```
import java.util.*;

import scala.Tuple2;

import org.apache.spark.api.java.*;
import org.apache.spark.mllib.evaluation.RegressionMetrics;
import org.apache.spark.mllib.evaluation.RankingMetrics;
import org.apache.spark.mllib.recommendation.ALS;
import org.apache.spark.mllib.recommendation.MatrixFactorizationModel;
import org.apache.spark.mllib.recommendation.Rating;

String path = "data/mllib/sample_movielens_data.txt";
JavaRDD<String> data = sc.textFile(path);
JavaRDD<Rating> ratings = data.map(line -> {
    String[] parts = line.split("::");
    return new Rating(Integer.parseInt(parts[0]), Integer.parseInt(parts[1]), Double
        .parseDouble(parts[2]) - 2.5);
  });
ratings.cache();

// Train an ALS model
MatrixFactorizationModel model = ALS.train(JavaRDD.toRDD(ratings), 10, 10, 0.01);

// Get top 10 recommendations for every user and scale ratings from 0 to 1
JavaRDD<Tuple2<Object, Rating[]>> userRecs = model.recommendProductsForUsers(10).toJavaRDD();
JavaRDD<Tuple2<Object, Rating[]>> userRecsScaled = userRecs.map(t -> {
    Rating[] scaledRatings = new Rating[t._2().length];
    for (int i = 0; i < scaledRatings.length; i++) {
      double newRating = Math.max(Math.min(t._2()[i].rating(), 1.0), 0.0);
      scaledRatings[i] = new Rating(t._2()[i].user(), t._2()[i].product(), newRating);
    }
    return new Tuple2<>(t._1(), scaledRatings);
  });
JavaPairRDD<Object, Rating[]> userRecommended = JavaPairRDD.fromJavaRDD(userRecsScaled);

// Map ratings to 1 or 0, 1 indicating a movie that should be recommended
JavaRDD<Rating> binarizedRatings = ratings.map(r -> {
    double binaryRating;
    if (r.rating() > 0.0) {
      binaryRating = 1.0;
    } else {
      binaryRating = 0.0;
    }
    return new Rating(r.user(), r.product(), binaryRating);
  });

// Group ratings by common user
JavaPairRDD<Object, Iterable<Rating>> userMovies = binarizedRatings.groupBy(Rating::user);

// Get true relevant documents from all user ratings
JavaPairRDD<Object, List<Integer>> userMoviesList = userMovies.mapValues(docs -> {
    List<Integer> products = new ArrayList<>();
    for (Rating r : docs) {
      if (r.rating() > 0.0) {
        products.add(r.product());
      }
    }
    return products;
  });

// Extract the product id from each recommendation
JavaPairRDD<Object, List<Integer>> userRecommendedList = userRecommended.mapValues(docs -> {
    List<Integer> products = new ArrayList<>();
    for (Rating r : docs) {
      products.add(r.product());
    }
    return products;
  });
JavaRDD<Tuple2<List<Integer>, List<Integer>>> relevantDocs = userMoviesList.join(
  userRecommendedList).values();

// Instantiate the metrics object
RankingMetrics<Integer> metrics = RankingMetrics.of(relevantDocs);

// Precision, NDCG and Recall at k
Integer[] kVector = {1, 3, 5};
for (Integer k : kVector) {
  System.out.format("Precision at %d = %f\n", k, metrics.precisionAt(k));
  System.out.format("NDCG at %d = %f\n", k, metrics.ndcgAt(k));
  System.out.format("Recall at %d = %f\n", k, metrics.recallAt(k));
}

// Mean average precision
System.out.format("Mean average precision = %f\n", metrics.meanAveragePrecision());

//Mean average precision at k
System.out.format("Mean average precision at 2 = %f\n", metrics.meanAveragePrecisionAt(2));

// Evaluate the model using numerical ratings and regression metrics
JavaRDD<Tuple2<Object, Object>> userProducts =
    ratings.map(r -> new Tuple2<>(r.user(), r.product()));

JavaPairRDD<Tuple2<Integer, Integer>, Object> predictions = JavaPairRDD.fromJavaRDD(
  model.predict(JavaRDD.toRDD(userProducts)).toJavaRDD().map(r ->
    new Tuple2<>(new Tuple2<>(r.user(), r.product()), r.rating())));
JavaRDD<Tuple2<Object, Object>> ratesAndPreds =
  JavaPairRDD.fromJavaRDD(ratings.map(r ->
    new Tuple2<Tuple2<Integer, Integer>, Object>(
      new Tuple2<>(r.user(), r.product()),
      r.rating())
  )).join(predictions).values();

// Create regression metrics object
RegressionMetrics regressionMetrics = new RegressionMetrics(ratesAndPreds.rdd());

// Root mean squared error
System.out.format("RMSE = %f\n", regressionMetrics.rootMeanSquaredError());

// R-squared
System.out.format("R-squared = %f\n", regressionMetrics.r2());
```

Find full example code at "examples/src/main/java/org/apache/spark/examples/mllib/JavaRankingMetricsExample.java" in the Spark repo.
## Regression model evaluation[](https://spark.apache.org/docs/latest/mllib-evaluation-metrics.html#regression-model-evaluation)
[Regression analysis](https://en.wikipedia.org/wiki/Regression_analysis) is used when predicting a continuous output variable from a number of independent variables.
**Available metrics**  
| Metric  | Definition  |  
| --- | --- |  
| Mean Squared Error (MSE)  | $MSE = \frac{\sum_{i=0}^{N-1} (\mathbf{y}_i - \hat{\mathbf{y}}_i)^2}{N}$  |  
| Root Mean Squared Error (RMSE)  | $RMSE = \sqrt{\frac{\sum_{i=0}^{N-1} (\mathbf{y}_i - \hat{\mathbf{y}}_i)^2}{N}}$  |  
| Mean Absolute Error (MAE)  | $MAE=\frac{1}{N}\sum_{i=0}^{N-1} \left|\mathbf{y}_i - \hat{\mathbf{y}}_i\right|$  |  
| Coefficient of Determination $(R^2)$  | $R^2=1 - \frac{MSE}{\text{VAR}(\mathbf{y}) \cdot (N-1)}=1-\frac{\sum_{i=0}^{N-1} (\mathbf{y}_i - \hat{\mathbf{y}}_i)^2}{\sum_{i=0}^{N-1}(\mathbf{y}_i-\bar{\mathbf{y}})^2}$  |  
| Explained Variance  | $1 - \frac{\text{VAR}(\mathbf{y} - \mathbf{\hat{y}})}{\text{VAR}(\mathbf{y})}$  |

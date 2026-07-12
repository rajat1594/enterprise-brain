[Log in](https://issues.apache.org/jira/login.jsp?os_destination=%2Fbrowse%2FSPARK-23674)[Skip to main content](https://issues.apache.org/jira/browse/SPARK-23674#main)[Skip to sidebar](https://issues.apache.org/jira/browse/SPARK-23674#sidebar)
Linked Applications
Loading…
[![ASF Jira](https://issues.apache.org/jira/s/-vddc6b/820010/g3jj3a/_/jira-logo-scaled.png)](https://issues.apache.org/jira/secure/MyJiraHome.jspa)
  * [Dashboards](https://issues.apache.org/jira/secure/Dashboard.jspa "View and manage your dashboards")
  * [Projects](https://issues.apache.org/jira/browse/SPARK "View recent projects and browse a list of projects")
  * [Issues](https://issues.apache.org/jira/issues/ "Search for issues and view recent issues")

  *   * [Help](https://docs.atlassian.com/jira/jcore-docs-0820/ "Help")
    * [Jira Core help](https://docs.atlassian.com/jira/jcore-docs-0820/ "Go to the online documentation for Jira Core")
    * [Keyboard Shortcuts](https://issues.apache.org/jira/secure/ViewKeyboardShortcuts!default.jspa "Get more information about Jira's Keyboard Shortcuts \( Type '?' \)")
    * [About Jira](https://issues.apache.org/jira/secure/AboutPage.jspa "Get more information about Jira")
    * [Jira Credits](https://issues.apache.org/jira/secure/credits/AroundTheWorld!default.jspa "See who did what")
  * [Log In](https://issues.apache.org/jira/login.jsp?os_destination=%2Fbrowse%2FSPARK-23674)

Public signup for this instance is **disabled**. Go to our [Self serve sign up page](https://selfserve.apache.org/jira-account.html) to request an account. Report potential security issues [privately](https://apache.org/security/#reporting-a-vulnerability)
[![Spark](https://issues.apache.org/jira/secure/projectavatar?pid=12315420&avatarId=27346)![Project Type: software](https://issues.apache.org/jira/browse/SPARK-23674)](https://issues.apache.org/jira/projects/SPARK/summary "Spark")
#
[Spark](https://issues.apache.org/jira/projects/SPARK/summary "Spark")
  * [Issues](https://issues.apache.org/jira/projects/SPARK/issues)
  * [Reports](https://issues.apache.org/jira/projects/SPARK?selectedItem=com.atlassian.jira.jira-projects-plugin:report-page)
  * [Components](https://issues.apache.org/jira/projects/SPARK?selectedItem=com.atlassian.jira.jira-projects-plugin:components-page)
  * [Roadmap](https://issues.apache.org/jira/projects/SPARK?selectedItem=biz.everit.jira.epic-roadmap:erfj-sidebar-roadmap)

![Uploaded image for project: 'Spark'](https://issues.apache.org/jira/secure/projectavatar?pid=12315420&avatarId=27346)
  1. [Spark](https://issues.apache.org/jira/browse/SPARK)
  2. [SPARK-23674](https://issues.apache.org/jira/browse/SPARK-23674)

# Add Spark ML Listener for Tracking ML Pipeline Status
[Log In](https://issues.apache.org/jira/login.jsp?os_destination=%2Fbrowse%2FSPARK-23674 "Log In")
[ Export](https://issues.apache.org/jira/browse/SPARK-23674)
[XML](https://issues.apache.org/jira/si/jira.issueviews:issue-xml/SPARK-23674/SPARK-23674.xml)[Word](https://issues.apache.org/jira/si/jira.issueviews:issue-word/SPARK-23674/SPARK-23674.doc)[Printable](https://issues.apache.org/jira/si/jira.issueviews:issue-html/SPARK-23674/SPARK-23674.html)[JSON](https://issues.apache.org/jira/si/com.atlassian.jira.plugins.jira-importers-plugin:issue-json/SPARK-23674/SPARK-23674.json)

#### Details
  * ** Type: ** ![](https://issues.apache.org/jira/secure/viewavatar?size=xsmall&avatarId=21140&avatarType=issuetype) Improvement
  * **Status:** Closed
  * ** Priority: ** ![](https://issues.apache.org/jira/images/icons/priorities/major.svg) Major
  * **Resolution:** Fixed
  * ** Affects Version/s: ** 2.3.0
  * ** Fix Version/s:  ** [3.0.0](https://issues.apache.org/jira/issues/?jql=project+%3D+SPARK+AND+fixVersion+%3D+3.0.0 "3.0.0 ")
  * ** Component/s: ** [ML](https://issues.apache.org/jira/issues/?jql=project+%3D+SPARK+AND+component+%3D+ML "ML Features under the spark.ml package")
  * ** Labels: **
None

#### Description
Currently, Spark provides status monitoring for different components of Spark, like spark history server, streaming listener, sql listener and etc. The use case would be (1) front UI to track the status of training coverage rate during iteration, then DS can understand how the job converge when training, like K-means, Logistic and other linear regression model. (2) tracking the data lineage for the input and output of training data.
In this proposal, we hope to provide Spark ML pipeline listener to track the status of Spark ML pipeline status includes:
  1. ML pipeline create and saved
  2. ML pipeline model created, saved and load
  3. ML model training status monitoring

#### Attachments
#### Issue Links

is related to

![Improvement - An improvement or enhancement to an existing feature or task.](https://issues.apache.org/jira/secure/viewavatar?size=xsmall&avatarId=21140&avatarType=issuetype) [SPARK-26960](https://issues.apache.org/jira/browse/SPARK-26960) Reduce flakiness of Spark ML Listener test suite by waiting for listener bus to clear
  * ![Major - Major loss of function.](https://issues.apache.org/jira/images/icons/priorities/major.svg)
  * Closed

links to

![Pull request #20823](https://assets-cdn.github.com/favicon.ico) [[Github] Pull Request #20823 (jmwdpk)](https://github.com/apache/spark/pull/20823)
![Pull request #23261](https://assets-cdn.github.com/favicon.ico) [[Github] Pull Request #23261 (HyukjinKwon)](https://github.com/apache/spark/pull/23261)
![Pull request #23261](https://assets-cdn.github.com/favicon.ico) [[Github] Pull Request #23261 (HyukjinKwon)](https://github.com/apache/spark/pull/23261)
![Pull request #23263](https://assets-cdn.github.com/favicon.ico) [[Github] Pull Request #23263 (HyukjinKwon)](https://github.com/apache/spark/pull/23263)
![Web Link](https://github.com/favicon.ico) [GitHub Pull Request #20823](https://github.com/apache/spark/pull/20823)
![Web Link](https://github.com/favicon.ico) [GitHub Pull Request #23263](https://github.com/apache/spark/pull/23263)
Show 2 more links (2 links to)
#### Activity
  * [All](https://issues.apache.org/jira/browse/SPARK-23674?page=com.atlassian.jira.plugin.system.issuetabpanels:all-tabpanel)
  * Comments
  * [Work Log](https://issues.apache.org/jira/browse/SPARK-23674?page=com.atlassian.jira.plugin.system.issuetabpanels:worklog-tabpanel)
  * [History](https://issues.apache.org/jira/browse/SPARK-23674?page=com.atlassian.jira.plugin.system.issuetabpanels:changehistory-tabpanel)
  * [Activity](https://issues.apache.org/jira/browse/SPARK-23674?page=com.atlassian.streams.streams-jira-plugin:activity-stream-issue-tab)
  * [Transitions](https://issues.apache.org/jira/browse/SPARK-23674?page=com.googlecode.jira-suite-utilities:transitions-summary-tabpanel)

[ Ascending order - Click to sort in descending order ](https://issues.apache.org/jira/browse/SPARK-23674?actionOrder=desc "Ascending order - Click to sort in descending order")
[![jmwdpk](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Ming Jiang](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=jmwdpk) added a comment - [13/Mar/18 21:19](https://issues.apache.org/jira/browse/SPARK-23674?focusedCommentId=16397668&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16397668)
Hello,
I will work on this and propose a pr, thanks!
[![jmwdpk](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Ming Jiang](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=jmwdpk) added a comment - [13/Mar/18 21:19](https://issues.apache.org/jira/browse/SPARK-23674?focusedCommentId=16397668&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16397668) Hello, I will work on this and propose a pr, thanks!
[![apachespark](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Apache Spark](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=apachespark) added a comment - [14/Mar/18 17:59](https://issues.apache.org/jira/browse/SPARK-23674?focusedCommentId=16398996&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16398996)
User 'jmwdpk' has created a pull request for this issue:
<https://github.com/apache/spark/pull/20823>
[![apachespark](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Apache Spark](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=apachespark) added a comment - [14/Mar/18 17:59](https://issues.apache.org/jira/browse/SPARK-23674?focusedCommentId=16398996&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16398996) User 'jmwdpk' has created a pull request for this issue: https://github.com/apache/spark/pull/20823
[![apachespark](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Apache Spark](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=apachespark) added a comment - [08/Dec/18 06:51](https://issues.apache.org/jira/browse/SPARK-23674?focusedCommentId=16713567&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16713567)
User 'HyukjinKwon' has created a pull request for this issue:
<https://github.com/apache/spark/pull/23261>
[![apachespark](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Apache Spark](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=apachespark) added a comment - [08/Dec/18 06:51](https://issues.apache.org/jira/browse/SPARK-23674?focusedCommentId=16713567&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16713567) User 'HyukjinKwon' has created a pull request for this issue: https://github.com/apache/spark/pull/23261
[![apachespark](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Apache Spark](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=apachespark) added a comment - [08/Dec/18 06:52](https://issues.apache.org/jira/browse/SPARK-23674?focusedCommentId=16713568&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16713568)
User 'HyukjinKwon' has created a pull request for this issue:
<https://github.com/apache/spark/pull/23261>
[![apachespark](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Apache Spark](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=apachespark) added a comment - [08/Dec/18 06:52](https://issues.apache.org/jira/browse/SPARK-23674?focusedCommentId=16713568&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16713568) User 'HyukjinKwon' has created a pull request for this issue: https://github.com/apache/spark/pull/23261
[![apachespark](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Apache Spark](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=apachespark) added a comment - [08/Dec/18 09:45](https://issues.apache.org/jira/browse/SPARK-23674?focusedCommentId=16713610&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16713610)
User 'HyukjinKwon' has created a pull request for this issue:
<https://github.com/apache/spark/pull/23263>
[![apachespark](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Apache Spark](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=apachespark) added a comment - [08/Dec/18 09:45](https://issues.apache.org/jira/browse/SPARK-23674?focusedCommentId=16713610&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16713610) User 'HyukjinKwon' has created a pull request for this issue: https://github.com/apache/spark/pull/23263
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [12/Dec/18 07:03](https://issues.apache.org/jira/browse/SPARK-23674?focusedCommentId=16718526&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16718526)
felixcheung closed pull request #23263: [~~SPARK-23674~~](https://issues.apache.org/jira/browse/SPARK-23674 "Add Spark ML Listener for Tracking ML Pipeline Status")[ML] Adds Spark ML Events
URL: <https://github.com/apache/spark/pull/23263>
This is a PR merged from a forked repository.
As GitHub hides the original diff on merge, it is displayed below for
the sake of provenance:
As this is a foreign pull request (from a fork), the diff is supplied
below (as it won't show otherwise due to GitHub magic):
diff --git a/mllib/src/main/scala/org/apache/spark/ml/Estimator.scala b/mllib/src/main/scala/org/apache/spark/ml/Estimator.scala
index 1247882d6c1bd..a3c4db06862f8 100644
— a/mllib/src/main/scala/org/apache/spark/ml/Estimator.scala
+++ b/mllib/src/main/scala/org/apache/spark/ml/Estimator.scala
@@ -65,7 +65,19 @@ abstract class Estimator[M <: Model[M]] extends PipelineStage {
  * Fits a model to the input data.
*/
@Since("2.0.0")

  * def fit(dataset: Dataset[_]): M
+ def fit(dataset: Dataset[_]): M = MLEvents.withFitEvent(this, dataset) { + fitImpl(dataset) + }
+
+ /**
+ * `fit()` handles events and then calls this method. Subclasses should override this
+ * method to implement the actual fiting a model to the input data.
+ */
+ @Since("3.0.0")
+ protected def fitImpl(dataset: Dataset[_]): M =
{ + // Keep this default body for backward compatibility. + throw new UnsupportedOperationException("fitImpl is not implemented.") + }

/**
  * Fits multiple models to the input data with multiple sets of parameters.
diff --git a/mllib/src/main/scala/org/apache/spark/ml/Pipeline.scala b/mllib/src/main/scala/org/apache/spark/ml/Pipeline.scala
index 103082b7b9766..1c781faff129e 100644
    *       * a/mllib/src/main/scala/org/apache/spark/ml/Pipeline.scala
+++ b/mllib/src/main/scala/org/apache/spark/ml/Pipeline.scala
@@ -132,7 +132,8 @@ class Pipeline @Since("1.4.0") (
  * @return fitted pipeline
*/
@Since("2.0.0")

  * override def fit(dataset: Dataset[_]): PipelineModel = {
+ override def fit(dataset: Dataset[_]): PipelineModel = super.fit(dataset)
+ override protected def fitImpl(dataset: Dataset[_]): PipelineModel = {
transformSchema(dataset.schema, logging = true)
val theStages = $(stages)
// Search for the last estimator.
@@ -210,7 +211,7 @@ object Pipeline extends MLReadable[Pipeline] {
/** Checked against metadata when loading model */
private val className = classOf[Pipeline].getName

  * override def load(path: String): Pipeline =
Unknown macro: {+ override protected def loadImpl(path}

@Since("2.0.0")
  * override def transform(dataset: Dataset[_]): DataFrame = {
+ override def transform(dataset: Dataset[_]): DataFrame = super.transform(dataset)
+ override protected def transformImpl(dataset: Dataset[_]): DataFrame = { transformSchema(dataset.schema, logging = true) stages.foldLeft(dataset.toDF)((cur, transformer) => transformer.transform(cur)) }
@@ -344,7 +346,7 @@ object PipelineModel extends MLReadable[PipelineModel] {
/** Checked against metadata when loading model */
private val className = classOf[PipelineModel].getName

  * override def load(path: String): PipelineModel = {
+ override protected def loadImpl(path: String): PipelineModel = {
val (uid: String, stages: Array[PipelineStage]) = SharedReadWrite.load(className, sc, path)
val transformers = stages map {
case stage: Transformer => stage
diff --git a/mllib/src/main/scala/org/apache/spark/ml/Predictor.scala b/mllib/src/main/scala/org/apache/spark/ml/Predictor.scala
index d8f3dfa874439..3731ddae0160c 100644
    *       * a/mllib/src/main/scala/org/apache/spark/ml/Predictor.scala
+++ b/mllib/src/main/scala/org/apache/spark/ml/Predictor.scala
@@ -94,7 +94,10 @@ abstract class Predictor[
/** @group setParam */
def setPredictionCol(value: String): Learner = set(predictionCol, value).asInstanceOf[Learner]

  * override def fit(dataset: Dataset[_]): M = {
+ // Explictly call parent's load. Otherwise, MiMa complains.
+ override def fit(dataset: Dataset[_]): M = super.fit(dataset)
+
+ override protected def fitImpl(dataset: Dataset[_]): M = {
// This handles a few items such as schema validation.
// Developers only need to implement train().
transformSchema(dataset.schema, logging = true)
@@ -199,7 +202,8 @@ abstract class PredictionModel[FeaturesType, M <: PredictionModel[FeaturesType,

  * @param dataset input dataset
  * @return transformed dataset with [[predictionCol]] of type `Double`
*/

  * override def transform(dataset: Dataset[_]): DataFrame = {
+ override def transform(
+ dataset: Dataset[_]): DataFrame = MLEvents.withTransformEvent(this, dataset)
Unknown macro: { transformSchema(dataset.schema, logging = true) if ($(predictionCol).nonEmpty) { transformImpl(dataset) @@ -210,7 +214,7 @@ abstract class PredictionModel[FeaturesType, M <: PredictionModel[FeaturesType, } }

  * protected def transformImpl(dataset: Dataset[_]): DataFrame = {
+ override protected def transformImpl(dataset: Dataset[_]): DataFrame = {
val predictUDF = udf { (features: Any) => predict(features.asInstanceOf[FeaturesType]) }
diff --git a/mllib/src/main/scala/org/apache/spark/ml/Transformer.scala b/mllib/src/main/scala/org/apache/spark/ml/Transformer.scala
index a3a2b55adc25d..2467383227a66 100644
    *       * a/mllib/src/main/scala/org/apache/spark/ml/Transformer.scala
+++ b/mllib/src/main/scala/org/apache/spark/ml/Transformer.scala
@@ -68,7 +68,19 @@ abstract class Transformer extends PipelineStage {

  * Transforms the input dataset.
*/
@Since("2.0.0")

  * def transform(dataset: Dataset[_]): DataFrame
+ def transform(dataset: Dataset[_]): DataFrame = MLEvents.withTransformEvent(this, dataset) { + transformImpl(dataset) + }
+
+ /**
+ * `transform()` handles events and then calls this method. Subclasses should override this
+ * method to implement the actual transformation.
+ */
+ @Since("3.0.0")
+ protected def transformImpl(dataset: Dataset[_]): DataFrame =
{ + // Keep this default body for backward compatibility. + throw new UnsupportedOperationException("transformImpl is not implemented.") + }

override def copy(extra: ParamMap): Transformer
}
@@ -116,7 +128,7 @@ abstract class UnaryTransformer[IN, OUT, T <: UnaryTransformer[IN, OUT, T]]
StructType(outputFields)
}
  * override def transform(dataset: Dataset[_]): DataFrame = {
+ override protected def transformImpl(dataset: Dataset[_]): DataFrame = {
transformSchema(dataset.schema, logging = true)
val transformUDF = udf(this.createTransformFunc, outputDataType)
dataset.withColumn($(outputCol), transformUDF(dataset($(inputCol))))
diff --git a/mllib/src/main/scala/org/apache/spark/ml/classification/Classifier.scala b/mllib/src/main/scala/org/apache/spark/ml/classification/Classifier.scala
index 7e5790ab70ee9..4de6ae7990490 100644
    *       * a/mllib/src/main/scala/org/apache/spark/ml/classification/Classifier.scala
+++ b/mllib/src/main/scala/org/apache/spark/ml/classification/Classifier.scala
@@ -19,7 +19,7 @@ package org.apache.spark.ml.classification

import org.apache.spark.SparkException
import org.apache.spark.annotation.
{DeveloperApi, Since}
-import org.apache.spark.ml.
{PredictionModel, Predictor, PredictorParams}
+import org.apache.spark.ml.
{MLEvents, PredictionModel, Predictor, PredictorParams}
import org.apache.spark.ml.feature.LabeledPoint
import org.apache.spark.ml.linalg.
{Vector, VectorUDT}
import org.apache.spark.ml.param.shared.HasRawPredictionCol
@@ -156,7 +156,8 @@ abstract class ClassificationModel[FeaturesType, M <: ClassificationModel[Featur
  * @param dataset input dataset
  * @return transformed dataset
*/

  * override def transform(dataset: Dataset[_]): DataFrame = {
+ override def transform(
+ dataset: Dataset[_]): DataFrame = MLEvents.withTransformEvent(this, dataset) {
transformSchema(dataset.schema, logging = true)

// Output selected columns only.
diff --git a/mllib/src/main/scala/org/apache/spark/ml/classification/DecisionTreeClassifier.scala b/mllib/src/main/scala/org/apache/spark/ml/classification/DecisionTreeClassifier.scala
index d9292a5476767..ab91b942a06ce 100644
— a/mllib/src/main/scala/org/apache/spark/ml/classification/DecisionTreeClassifier.scala
+++ b/mllib/src/main/scala/org/apache/spark/ml/classification/DecisionTreeClassifier.scala
@@ -275,7 +275,7 @@ object DecisionTreeClassificationModel extends MLReadable[DecisionTreeClassifica
/** Checked against metadata when loading model */
private val className = classOf[DecisionTreeClassificationModel].getName
  * override def load(path: String): DecisionTreeClassificationModel = {
+ override protected def loadImpl(path: String): DecisionTreeClassificationModel = {
implicit val format = DefaultFormats
val metadata = DefaultParamsReader.loadMetadata(path, sc, className)
val numFeatures = (metadata.metadata \ "numFeatures").extract[Int]
diff --git a/mllib/src/main/scala/org/apache/spark/ml/classification/GBTClassifier.scala b/mllib/src/main/scala/org/apache/spark/ml/classification/GBTClassifier.scala
index abe2d1febfdf8..5f4bac04f16bb 100644
    *       * a/mllib/src/main/scala/org/apache/spark/ml/classification/GBTClassifier.scala
+++ b/mllib/src/main/scala/org/apache/spark/ml/classification/GBTClassifier.scala
@@ -410,7 +410,7 @@ object GBTClassificationModel extends MLReadable[GBTClassificationModel] {
private val className = classOf[GBTClassificationModel].getName
private val treeClassName = classOf[DecisionTreeRegressionModel].getName

  * override def load(path: String): GBTClassificationModel = {
+ override protected def loadImpl(path: String): GBTClassificationModel = {
implicit val format = DefaultFormats
val (metadata: Metadata, treesData: Array[(Metadata, Node)], treeWeights: Array[Double]) =
EnsembleModelReadWrite.loadImpl(path, sparkSession, className, treeClassName)
diff --git a/mllib/src/main/scala/org/apache/spark/ml/classification/LinearSVC.scala b/mllib/src/main/scala/org/apache/spark/ml/classification/LinearSVC.scala
index ff801abef9a94..b6e9b8833022d 100644
    *       * a/mllib/src/main/scala/org/apache/spark/ml/classification/LinearSVC.scala
+++ b/mllib/src/main/scala/org/apache/spark/ml/classification/LinearSVC.scala
@@ -373,7 +373,7 @@ object LinearSVCModel extends MLReadable[LinearSVCModel] {
/** Checked against metadata when loading model */
private val className = classOf[LinearSVCModel].getName

  * override def load(path: String): LinearSVCModel = {
+ override protected def loadImpl(path: String): LinearSVCModel = {
val metadata = DefaultParamsReader.loadMetadata(path, sc, className)
val dataPath = new Path(path, "data").toString
val data = sparkSession.read.format("parquet").load(dataPath)
diff --git a/mllib/src/main/scala/org/apache/spark/ml/classification/LogisticRegression.scala b/mllib/src/main/scala/org/apache/spark/ml/classification/LogisticRegression.scala
index 27a7db0b2f5d4..1367253aa4f9f 100644
    *       * a/mllib/src/main/scala/org/apache/spark/ml/classification/LogisticRegression.scala
+++ b/mllib/src/main/scala/org/apache/spark/ml/classification/LogisticRegression.scala
@@ -1248,7 +1248,7 @@ object LogisticRegressionModel extends MLReadable[LogisticRegressionModel] {
/** Checked against metadata when loading model */
private val className = classOf[LogisticRegressionModel].getName

  * override def load(path: String): LogisticRegressionModel = {
+ override protected def loadImpl(path: String): LogisticRegressionModel = {
val metadata = DefaultParamsReader.loadMetadata(path, sc, className)
val (major, minor) = VersionUtils.majorMinorVersion(metadata.sparkVersion)

diff --git a/mllib/src/main/scala/org/apache/spark/ml/classification/MultilayerPerceptronClassifier.scala b/mllib/src/main/scala/org/apache/spark/ml/classification/MultilayerPerceptronClassifier.scala
index 47b8a8df637b9..a912ad268ba7e 100644
— a/mllib/src/main/scala/org/apache/spark/ml/classification/MultilayerPerceptronClassifier.scala
+++ b/mllib/src/main/scala/org/apache/spark/ml/classification/MultilayerPerceptronClassifier.scala
@@ -359,7 +359,7 @@ object MultilayerPerceptronClassificationModel
/** Checked against metadata when loading model */
private val className = classOf[MultilayerPerceptronClassificationModel].getName
  * override def load(path: String): MultilayerPerceptronClassificationModel = {
+ override protected def loadImpl(path: String): MultilayerPerceptronClassificationModel = {
val metadata = DefaultParamsReader.loadMetadata(path, sc, className)

val dataPath = new Path(path, "data").toString
diff --git a/mllib/src/main/scala/org/apache/spark/ml/classification/NaiveBayes.scala b/mllib/src/main/scala/org/apache/spark/ml/classification/NaiveBayes.scala
index 1a7a5e7a52344..04bb1265962c2 100644
— a/mllib/src/main/scala/org/apache/spark/ml/classification/NaiveBayes.scala
+++ b/mllib/src/main/scala/org/apache/spark/ml/classification/NaiveBayes.scala
@@ -399,7 +399,7 @@ object NaiveBayesModel extends MLReadable[NaiveBayesModel] {
/** Checked against metadata when loading model */
private val className = classOf[NaiveBayesModel].getName
  * override def load(path: String): NaiveBayesModel = {
+ override protected def loadImpl(path: String): NaiveBayesModel = { val metadata = DefaultParamsReader.loadMetadata(path, sc, className) val dataPath = new Path(path, "data").toString diff --git a/mllib/src/main/scala/org/apache/spark/ml/classification/OneVsRest.scala b/mllib/src/main/scala/org/apache/spark/ml/classification/OneVsRest.scala index e1fceb1fc96a4..6b0a4d0832007 100644 --- a/mllib/src/main/scala/org/apache/spark/ml/classification/OneVsRest.scala +++ b/mllib/src/main/scala/org/apache/spark/ml/classification/OneVsRest.scala @@ -165,7 +165,8 @@ final class OneVsRestModel private[ml] ( }

@Since("2.0.0")
  * override def transform(dataset: Dataset[_]): DataFrame = {
+ override def transform(dataset: Dataset[_]): DataFrame = super.transform(dataset)
+ override protected def transformImpl(dataset: Dataset[_]): DataFrame = {
// Check schema
transformSchema(dataset.schema, logging = true)

@@ -289,7 +290,7 @@ object OneVsRestModel extends MLReadable[OneVsRestModel] {
/** Checked against metadata when loading model */
private val className = classOf[OneVsRestModel].getName
  * override def load(path: String): OneVsRestModel = {
+ override protected def loadImpl(path: String): OneVsRestModel = { implicit val format = DefaultFormats val (metadata, classifier) = OneVsRestParams.loadImpl(path, sc, className) val labelMetadata = Metadata.fromJson((metadata.metadata \ "labelMetadata").extract[String]) @@ -372,7 +373,8 @@ final class OneVsRest @Since("1.4.0") ( }

@Since("2.0.0")
  * override def fit(dataset: Dataset[_]): OneVsRestModel = instrumented { instr =>
+ override def fit(dataset: Dataset[_]): OneVsRestModel = super.fit(dataset)
+ override protected def fitImpl(dataset: Dataset[_]): OneVsRestModel = instrumented { instr =>
transformSchema(dataset.schema)

instr.logPipelineStage(this)
@@ -492,7 +494,7 @@ object OneVsRest extends MLReadable[OneVsRest] {
/** Checked against metadata when loading model */
private val className = classOf[OneVsRest].getName
  * override def load(path: String): OneVsRest = {
+ override protected def loadImpl(path: String): OneVsRest = {
val (metadata, classifier) = OneVsRestParams.loadImpl(path, sc, className)
val ovr = new OneVsRest(metadata.uid)
metadata.getAndSetParams(ovr)
diff --git a/mllib/src/main/scala/org/apache/spark/ml/classification/ProbabilisticClassifier.scala b/mllib/src/main/scala/org/apache/spark/ml/classification/ProbabilisticClassifier.scala
index 730fcab333e11..24781005682dd 100644
    *       * a/mllib/src/main/scala/org/apache/spark/ml/classification/ProbabilisticClassifier.scala
+++ b/mllib/src/main/scala/org/apache/spark/ml/classification/ProbabilisticClassifier.scala
@@ -18,6 +18,7 @@
package org.apache.spark.ml.classification

import org.apache.spark.annotation.DeveloperApi
+import org.apache.spark.ml.MLEvents
import org.apache.spark.ml.linalg.
{DenseVector, Vector, VectorUDT}
import org.apache.spark.ml.param.shared._
import org.apache.spark.ml.util.SchemaUtils
@@ -100,7 +101,8 @@ abstract class ProbabilisticClassificationModel[
  * @param dataset input dataset
  * @return transformed dataset
*/

  * override def transform(dataset: Dataset[_]): DataFrame = {
+ override def transform(
+ dataset: Dataset[_]): DataFrame = MLEvents.withTransformEvent(this, dataset) {
transformSchema(dataset.schema, logging = true)
if (isDefined(thresholds)) {
require($(thresholds).length == numClasses, this.getClass.getSimpleName +
diff --git a/mllib/src/main/scala/org/apache/spark/ml/classification/RandomForestClassifier.scala b/mllib/src/main/scala/org/apache/spark/ml/classification/RandomForestClassifier.scala
index 0a3bfd1f85e08..145b73e1816ec 100644
    *       * a/mllib/src/main/scala/org/apache/spark/ml/classification/RandomForestClassifier.scala
+++ b/mllib/src/main/scala/org/apache/spark/ml/classification/RandomForestClassifier.scala
@@ -310,7 +310,7 @@ object RandomForestClassificationModel extends MLReadable[RandomForestClassifica
private val className = classOf[RandomForestClassificationModel].getName
private val treeClassName = classOf[DecisionTreeClassificationModel].getName

  * override def load(path: String): RandomForestClassificationModel = {
+ override protected def loadImpl(path: String): RandomForestClassificationModel = {
implicit val format = DefaultFormats
val (metadata: Metadata, treesData: Array[(Metadata, Node)], _) =
EnsembleModelReadWrite.loadImpl(path, sparkSession, className, treeClassName)
diff --git a/mllib/src/main/scala/org/apache/spark/ml/clustering/BisectingKMeans.scala b/mllib/src/main/scala/org/apache/spark/ml/clustering/BisectingKMeans.scala
index 1a94aefa3f563..b4c1246e780f2 100644
    *       * a/mllib/src/main/scala/org/apache/spark/ml/clustering/BisectingKMeans.scala
+++ b/mllib/src/main/scala/org/apache/spark/ml/clustering/BisectingKMeans.scala
@@ -105,7 +105,8 @@ class BisectingKMeansModel private[ml] (
def setPredictionCol(value: String): this.type = set(predictionCol, value)

@Since("2.0.0")
  * override def transform(dataset: Dataset[_]): DataFrame = {
+ override def transform(dataset: Dataset[_]): DataFrame = super.transform(dataset)
+ override protected def transformImpl(dataset: Dataset[_]): DataFrame = {
transformSchema(dataset.schema, logging = true)
val predictUDF = udf((vector: Vector) => predict(vector))
dataset.withColumn($(predictionCol),
@@ -191,7 +192,7 @@ object BisectingKMeansModel extends MLReadable[BisectingKMeansModel] {
/** Checked against metadata when loading model */
private val className = classOf[BisectingKMeansModel].getName

  * override def load(path: String): BisectingKMeansModel = {
+ override protected def loadImpl(path: String): BisectingKMeansModel = {
val metadata = DefaultParamsReader.loadMetadata(path, sc, className)
val dataPath = new Path(path, "data").toString
val mllibModel = MLlibBisectingKMeansModel.load(sc, dataPath)
@@ -261,7 +262,9 @@ class BisectingKMeans @Since("2.0.0") (
def setDistanceMeasure(value: String): this.type = set(distanceMeasure, value)

@Since("2.0.0")
  * override def fit(dataset: Dataset[_]): BisectingKMeansModel = instrumented { instr =>
+ override def fit(dataset: Dataset[_]): BisectingKMeansModel = super.fit(dataset)
+ override protected def fitImpl(
+ dataset: Dataset[_]): BisectingKMeansModel = instrumented { instr => transformSchema(dataset.schema, logging = true) val rdd = DatasetUtils.columnToOldVector(dataset, getFeaturesCol) diff --git a/mllib/src/main/scala/org/apache/spark/ml/clustering/GaussianMixture.scala b/mllib/src/main/scala/org/apache/spark/ml/clustering/GaussianMixture.scala index 88abc1605d69f..4908f03574d14 100644 --- a/mllib/src/main/scala/org/apache/spark/ml/clustering/GaussianMixture.scala +++ b/mllib/src/main/scala/org/apache/spark/ml/clustering/GaussianMixture.scala @@ -106,7 +106,8 @@ class GaussianMixtureModel private[ml] ( }

@Since("2.0.0")
  * override def transform(dataset: Dataset[_]): DataFrame = {
+ override def transform(dataset: Dataset[_]): DataFrame = super.transform(dataset)
+ override protected def transformImpl(dataset: Dataset[_]): DataFrame = {
transformSchema(dataset.schema, logging = true)
val predUDF = udf((vector: Vector) => predict(vector))
val probUDF = udf((vector: Vector) => predictProbability(vector))
@@ -218,7 +219,7 @@ object GaussianMixtureModel extends MLReadable[GaussianMixtureModel] {
/** Checked against metadata when loading model */
private val className = classOf[GaussianMixtureModel].getName

  * override def load(path: String): GaussianMixtureModel = {
+ override protected def loadImpl(path: String): GaussianMixtureModel = {
val metadata = DefaultParamsReader.loadMetadata(path, sc, className)

val dataPath = new Path(path, "data").toString
@@ -336,7 +337,9 @@ class GaussianMixture @Since("2.0.0") (
private val numSamples = 5
@Since("2.0.0")
  * override def fit(dataset: Dataset[_]): GaussianMixtureModel = instrumented { instr =>
+ override def fit(dataset: Dataset[_]): GaussianMixtureModel = super.fit(dataset)
+ override protected def fitImpl(
+ dataset: Dataset[_]): GaussianMixtureModel = instrumented { instr =>
transformSchema(dataset.schema, logging = true)

val sc = dataset.sparkSession.sparkContext
diff --git a/mllib/src/main/scala/org/apache/spark/ml/clustering/KMeans.scala b/mllib/src/main/scala/org/apache/spark/ml/clustering/KMeans.scala
index 2eed84d51782a..1c8a17c04f99e 100644
— a/mllib/src/main/scala/org/apache/spark/ml/clustering/KMeans.scala
+++ b/mllib/src/main/scala/org/apache/spark/ml/clustering/KMeans.scala
@@ -124,7 +124,8 @@ class KMeansModel private[ml] (
def setPredictionCol(value: String): this.type = set(predictionCol, value)
@Since("2.0.0")
  * override def transform(dataset: Dataset[_]): DataFrame = {
+ override def transform(dataset: Dataset[_]): DataFrame = super.transform(dataset)
+ override protected def transformImpl(dataset: Dataset[_]): DataFrame = {
transformSchema(dataset.schema, logging = true)

val predictUDF = udf((vector: Vector) => predict(vector))
@@ -238,7 +239,7 @@ object KMeansModel extends MLReadable[KMeansModel] {
/** Checked against metadata when loading model */
private val className = classOf[KMeansModel].getName
  * override def load(path: String): KMeansModel = {
+ override protected def loadImpl(path: String): KMeansModel = {
// Import implicits for Dataset Encoder
val sparkSession = super.sparkSession
import sparkSession.implicits._
@@ -321,7 +322,8 @@ class KMeans @Since("1.5.0") (
def setSeed(value: Long): this.type = set(seed, value)

@Since("2.0.0")
  * override def fit(dataset: Dataset[_]): KMeansModel = instrumented { instr =>
+ override def fit(dataset: Dataset[_]): KMeansModel = super.fit(dataset)
+ override protected def fitImpl(dataset: Dataset[_]): KMeansModel = instrumented { instr =>
transformSchema(dataset.schema, logging = true)

val handlePersistence = dataset.storageLevel == StorageLevel.NONE
diff --git a/mllib/src/main/scala/org/apache/spark/ml/clustering/LDA.scala b/mllib/src/main/scala/org/apache/spark/ml/clustering/LDA.scala
index 84e73dc19a392..fde97d57fdb75 100644
— a/mllib/src/main/scala/org/apache/spark/ml/clustering/LDA.scala
+++ b/mllib/src/main/scala/org/apache/spark/ml/clustering/LDA.scala
@@ -455,7 +455,8 @@ abstract class LDAModel private[ml] (
  * This implementation may be changed in the future.
*/
@Since("2.0.0")

  * override def transform(dataset: Dataset[_]): DataFrame = {
+ override def transform(dataset: Dataset[_]): DataFrame = super.transform(dataset)
+ override protected def transformImpl(dataset: Dataset[_]): DataFrame = {
if ($(topicDistributionCol).nonEmpty) {

// TODO: Make the transformer natively in ml framework to avoid extra conversion.
@@ -619,7 +620,7 @@ object LocalLDAModel extends MLReadable[LocalLDAModel] {
private val className = classOf[LocalLDAModel].getName
  * override def load(path: String): LocalLDAModel = {
+ override protected def loadImpl(path: String): LocalLDAModel = {
val metadata = DefaultParamsReader.loadMetadata(path, sc, className)
val dataPath = new Path(path, "data").toString
val data = sparkSession.read.parquet(dataPath)
@@ -772,7 +773,7 @@ object DistributedLDAModel extends MLReadable[DistributedLDAModel] {

private val className = classOf[DistributedLDAModel].getName
  * override def load(path: String): DistributedLDAModel = {
+ override protected def loadImpl(path: String): DistributedLDAModel = {
val metadata = DefaultParamsReader.loadMetadata(path, sc, className)
val modelPath = new Path(path, "oldModel").toString
val oldModel = OldDistributedLDAModel.load(sc, modelPath)
@@ -895,7 +896,8 @@ class LDA @Since("1.6.0") (
override def copy(extra: ParamMap): LDA = defaultCopy(extra)

@Since("2.0.0")
  * override def fit(dataset: Dataset[_]): LDAModel = instrumented { instr =>
+ override def fit(dataset: Dataset[_]): LDAModel = super.fit(dataset)
+ override protected def fitImpl(dataset: Dataset[_]): LDAModel = instrumented { instr =>
transformSchema(dataset.schema, logging = true)

instr.logPipelineStage(this)
@@ -952,7 +954,7 @@ object LDA extends MLReadable[LDA] {
private val className = classOf[LDA].getName
  * override def load(path: String): LDA = {
+ override protected def loadImpl(path: String): LDA = {
val metadata = DefaultParamsReader.loadMetadata(path, sc, className)
val model = new LDA(metadata.uid)
LDAParams.getAndSetParams(model, metadata)
diff --git a/mllib/src/main/scala/org/apache/spark/ml/events.scala b/mllib/src/main/scala/org/apache/spark/ml/events.scala
new file mode 100644
index 0000000000000..fe009394ca081
    *       * /dev/null
+++ b/mllib/src/main/scala/org/apache/spark/ml/events.scala
@@ -0,0 +1,109 @@
+/*
+ * Licensed to the Apache Software Foundation (ASF) under one or more
+ * contributor license agreements. See the NOTICE file distributed with
+ * this work for additional information regarding copyright ownership.
+ * The ASF licenses this file to You under the Apache License, Version 2.0
+ * (the "License"); you may not use this file except in compliance with
+ * the License. You may obtain a copy of the License at
+ *
+ * <http://www.apache.org/licenses/LICENSE-2.0>
+ *
+ * Unless required by applicable law or agreed to in writing, software
+ * distributed under the License is distributed on an "AS IS" BASIS,
+ * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
+ * See the License for the specific language governing permissions and
+ * limitations under the License.
+ */
+
+package org.apache.spark.ml
+
+import org.apache.spark.SparkContext
+import org.apache.spark.annotation.Unstable
+import org.apache.spark.ml.util. {MLReader, MLWriter}
+import org.apache.spark.scheduler.SparkListenerEvent
+import org.apache.spark.sql.
{DataFrame, Dataset}
+
+/**
+ * Event emitted by ML operations. Events are either fired before and/or
+ * after each operation (the event should document this).
+ */
+@Unstable
+sealed trait MLEvent extends SparkListenerEvent
+
+/**
+ * Event fired before `Transformer.transform`.
+ */
+@Unstable
+case class TransformStart(transformer: Transformer, input: Dataset[_]) extends MLEvent
+/**
+ * Event fired after `Transformer.transform`.
+ */
+@Unstable
+case class TransformEnd(transformer: Transformer, output: Dataset[_]) extends MLEvent
+
+/**
+ * Event fired before `Estimator.fit`.
+ */
+@Unstable
+case class FitStart[M <: Model[M]](estimator: Estimator[M], dataset: Dataset[_]) extends MLEvent
+/**
+ * Event fired after `Estimator.fit`.
+ */
+@Unstable
+case class FitEnd[M <: Model[M]](estimator: Estimator[M], model: M) extends MLEvent
+
+/**
+ * Event fired before `MLReader.load`.
+ */
+@Unstable
+case class LoadInstanceStart[T](reader: MLReader[T], path: String) extends MLEvent
+/**
+ * Event fired after `MLReader.load`.
+ */
+@Unstable
+case class LoadInstanceEnd[T](reader: MLReader[T], instance: T) extends MLEvent
+
+/**
+ * Event fired before `MLWriter.save`.
+ */
+@Unstable
+case class SaveInstanceStart(writer: MLWriter, path: String) extends MLEvent
+/**
+ * Event fired after `MLWriter.save`.
+ */
+@Unstable
+case class SaveInstanceEnd(writer: MLWriter, path: String) extends MLEvent
+
+
+private[ml] object MLEvents
Unknown macro: {+ private def listenerBus = SparkContext.getOrCreate().listenerBus++ def withFitEvent[M <}
diff --git a/mllib/src/main/scala/org/apache/spark/ml/feature/Binarizer.scala b/mllib/src/main/scala/org/apache/spark/ml/feature/Binarizer.scala
index 2b0862c60fdf7..3a02b640e359a 100644
      * a/mllib/src/main/scala/org/apache/spark/ml/feature/Binarizer.scala
+++ b/mllib/src/main/scala/org/apache/spark/ml/feature/Binarizer.scala
@@ -70,7 +70,8 @@ final class Binarizer @Since("1.4.0") (@Since("1.4.0") override val uid: String)
def setOutputCol(value: String): this.type = set(outputCol, value)

@Since("2.0.0")
  * override def transform(dataset: Dataset[_]): DataFrame = {
+ override def transform(dataset: Dataset[_]): DataFrame = super.transform(dataset)
+ override protected def transformImpl(dataset: Dataset[_]): DataFrame = {
val outputSchema = transformSchema(dataset.schema, logging = true)
val schema = dataset.schema
val inputType = schema($(inputCol)).dataType
diff --git a/mllib/src/main/scala/org/apache/spark/ml/feature/BucketedRandomProjectionLSH.scala b/mllib/src/main/scala/org/apache/spark/ml/feature/BucketedRandomProjectionLSH.scala
index 0554455a66d7f..f705418432a48 100644
    *       * a/mllib/src/main/scala/org/apache/spark/ml/feature/BucketedRandomProjectionLSH.scala
+++ b/mllib/src/main/scala/org/apache/spark/ml/feature/BucketedRandomProjectionLSH.scala
@@ -225,7 +225,7 @@ object BucketedRandomProjectionLSHModel extends MLReadable[BucketedRandomProject
/** Checked against metadata when loading model */
private val className = classOf[BucketedRandomProjectionLSHModel].getName

  * override def load(path: String): BucketedRandomProjectionLSHModel = {
+ override protected def loadImpl(path: String): BucketedRandomProjectionLSHModel = {
val metadata = DefaultParamsReader.loadMetadata(path, sc, className)

val dataPath = new Path(path, "data").toString
diff --git a/mllib/src/main/scala/org/apache/spark/ml/feature/Bucketizer.scala b/mllib/src/main/scala/org/apache/spark/ml/feature/Bucketizer.scala
index 0b989b0d7d253..eaa9ae8d81c45 100644
— a/mllib/src/main/scala/org/apache/spark/ml/feature/Bucketizer.scala
+++ b/mllib/src/main/scala/org/apache/spark/ml/feature/Bucketizer.scala
@@ -143,7 +143,8 @@ final class Bucketizer @Since("1.4.0") (@Since("1.4.0") override val uid: String
def setOutputCols(value: Array[String]): this.type = set(outputCols, value)
@Since("2.0.0")
  * override def transform(dataset: Dataset[_]): DataFrame = {
+ override def transform(dataset: Dataset[_]): DataFrame = super.transform(dataset)
+ override protected def transformImpl(dataset: Dataset[_]): DataFrame = {
val transformedSchema = transformSchema(dataset.schema)

val (inputColumns, outputColumns) = if (isSet(inputCols)) {
diff --git a/mllib/src/main/scala/org/apache/spark/ml/feature/ChiSqSelector.scala b/mllib/src/main/scala/org/apache/spark/ml/feature/ChiSqSelector.scala
index dbfb199ccd58f..ba8482d50a9cf 100644
— a/mllib/src/main/scala/org/apache/spark/ml/feature/ChiSqSelector.scala
+++ b/mllib/src/main/scala/org/apache/spark/ml/feature/ChiSqSelector.scala
@@ -197,7 +197,8 @@ final class ChiSqSelector @Since("1.6.0") (@Since("1.6.0") override val uid: Str
def setLabelCol(value: String): this.type = set(labelCol, value)
@Since("2.0.0")
  * override def fit(dataset: Dataset[_]): ChiSqSelectorModel = {
+ override def fit(dataset: Dataset[_]): ChiSqSelectorModel = super.fit(dataset)
+ override protected def fitImpl(dataset: Dataset[_]): ChiSqSelectorModel = {
transformSchema(dataset.schema, logging = true)
val input: RDD[OldLabeledPoint] =
dataset.select(col($(labelCol)).cast(DoubleType), col($(featuresCol))).rdd.map {
@@ -263,7 +264,8 @@ final class ChiSqSelectorModel private[ml] (
def setOutputCol(value: String): this.type = set(outputCol, value)

@Since("2.0.0")
  * override def transform(dataset: Dataset[_]): DataFrame = {
+ override def transform(dataset: Dataset[_]): DataFrame = super.transform(dataset)
+ override protected def transformImpl(dataset: Dataset[_]): DataFrame = {
val transformedSchema = transformSchema(dataset.schema, logging = true)
val newField = transformedSchema.last

@@ -327,7 +329,7 @@ object ChiSqSelectorModel extends MLReadable[ChiSqSelectorModel] {
private val className = classOf[ChiSqSelectorModel].getName
  * override def load(path: String): ChiSqSelectorModel = {
+ override protected def loadImpl(path: String): ChiSqSelectorModel = {
val metadata = DefaultParamsReader.loadMetadata(path, sc, className)
val dataPath = new Path(path, "data").toString
val data = sparkSession.read.parquet(dataPath).select("selectedFeatures").head()
diff --git a/mllib/src/main/scala/org/apache/spark/ml/feature/CountVectorizer.scala b/mllib/src/main/scala/org/apache/spark/ml/feature/CountVectorizer.scala
index dc8eb8261dbe2..a9ea509ada077 100644
    *       * a/mllib/src/main/scala/org/apache/spark/ml/feature/CountVectorizer.scala
+++ b/mllib/src/main/scala/org/apache/spark/ml/feature/CountVectorizer.scala
@@ -181,7 +181,8 @@ class CountVectorizer @Since("1.5.0") (@Since("1.5.0") override val uid: String)
def setBinary(value: Boolean): this.type = set(binary, value)

@Since("2.0.0")
  * override def fit(dataset: Dataset[_]): CountVectorizerModel = {
+ override def fit(dataset: Dataset[_]): CountVectorizerModel = super.fit(dataset)
+ override protected def fitImpl(dataset: Dataset[_]): CountVectorizerModel = {
transformSchema(dataset.schema, logging = true)
val vocSize = $(vocabSize)
val input = dataset.select($(inputCol)).rdd.map(_.getAs[Seq[String]](0))
@@ -291,7 +292,8 @@ class CountVectorizerModel(
private var broadcastDict: Option[Broadcast[Map[String, Int]]] = None

@Since("2.0.0")
  * override def transform(dataset: Dataset[_]): DataFrame = {
+ override def transform(dataset: Dataset[_]): DataFrame = super.transform(dataset)
+ override protected def transformImpl(dataset: Dataset[_]): DataFrame = {
transformSchema(dataset.schema, logging = true)
if (broadcastDict.isEmpty) {
val dict = vocabulary.zipWithIndex.toMap
@@ -358,7 +360,7 @@ object CountVectorizerModel extends MLReadable[CountVectorizerModel] {

private val className = classOf[CountVectorizerModel].getName
  * override def load(path: String): CountVectorizerModel = {
+ override protected def loadImpl(path: String): CountVectorizerModel = {
val metadata = DefaultParamsReader.loadMetadata(path, sc, className)
val dataPath = new Path(path, "data").toString
val data = sparkSession.read.parquet(dataPath)
diff --git a/mllib/src/main/scala/org/apache/spark/ml/feature/FeatureHasher.scala b/mllib/src/main/scala/org/apache/spark/ml/feature/FeatureHasher.scala
index dc18e1d34880a..a58a1ff8e053c 100644
    *       * a/mllib/src/main/scala/org/apache/spark/ml/feature/FeatureHasher.scala
+++ b/mllib/src/main/scala/org/apache/spark/ml/feature/FeatureHasher.scala
@@ -140,7 +140,8 @@ class FeatureHasher(@Since("2.3.0") override val uid: String) extends Transforme
def setCategoricalCols(value: Array[String]): this.type = set(categoricalCols, value)

@Since("2.3.0")
  * override def transform(dataset: Dataset[_]): DataFrame = {
+ override def transform(dataset: Dataset[_]): DataFrame = super.transform(dataset)
+ override protected def transformImpl(dataset: Dataset[_]): DataFrame = {
val hashFunc: Any => Int = FeatureHasher.murmur3Hash
val n = $(numFeatures)
val localInputCols = $(inputCols)
diff --git a/mllib/src/main/scala/org/apache/spark/ml/feature/HashingTF.scala b/mllib/src/main/scala/org/apache/spark/ml/feature/HashingTF.scala
index dbda5b8d8fd4a..57b6bb1dbe432 100644
    *       * a/mllib/src/main/scala/org/apache/spark/ml/feature/HashingTF.scala
+++ b/mllib/src/main/scala/org/apache/spark/ml/feature/HashingTF.scala
@@ -91,7 +91,8 @@ class HashingTF @Since("1.4.0") (@Since("1.4.0") override val uid: String)
def setBinary(value: Boolean): this.type = set(binary, value)

@Since("2.0.0")
  * override def transform(dataset: Dataset[_]): DataFrame = {
+ override def transform(dataset: Dataset[_]): DataFrame = super.transform(dataset)
+ override protected def transformImpl(dataset: Dataset[_]): DataFrame = {
val outputSchema = transformSchema(dataset.schema)
val hashingTF = new feature.HashingTF($(numFeatures)).setBinary($(binary))
// TODO: Make the hashingTF.transform natively in ml framework to avoid extra conversion.
diff --git a/mllib/src/main/scala/org/apache/spark/ml/feature/IDF.scala b/mllib/src/main/scala/org/apache/spark/ml/feature/IDF.scala
index 58897cca4e5c6..9c91cc0417e48 100644
    *       * a/mllib/src/main/scala/org/apache/spark/ml/feature/IDF.scala
+++ b/mllib/src/main/scala/org/apache/spark/ml/feature/IDF.scala
@@ -84,7 +84,8 @@ final class IDF @Since("1.4.0") (@Since("1.4.0") override val uid: String)
def setMinDocFreq(value: Int): this.type = set(minDocFreq, value)

@Since("2.0.0")
  * override def fit(dataset: Dataset[_]): IDFModel = {
+ override def fit(dataset: Dataset[_]): IDFModel = super.fit(dataset)
+ override protected def fitImpl(dataset: Dataset[_]): IDFModel = {
transformSchema(dataset.schema, logging = true)
val input: RDD[OldVector] = dataset.select($(inputCol)).rdd.map {
case Row(v: Vector) => OldVectors.fromML(v)
@@ -129,7 +130,8 @@ class IDFModel private[ml] (
def setOutputCol(value: String): this.type = set(outputCol, value)

@Since("2.0.0")
  * override def transform(dataset: Dataset[_]): DataFrame = {
+ override def transform(dataset: Dataset[_]): DataFrame = super.transform(dataset)
+ override protected def transformImpl(dataset: Dataset[_]): DataFrame = {
transformSchema(dataset.schema, logging = true)
// TODO: Make the idfModel.transform natively in ml framework to avoid extra conversion.
val idf = udf { vec: Vector => idfModel.transform(OldVectors.fromML(vec)).asML }
@@ -174,7 +176,7 @@ object IDFModel extends MLReadable[IDFModel] {

private val className = classOf[IDFModel].getName
  * override def load(path: String): IDFModel = {
+ override protected def loadImpl(path: String): IDFModel = {
val metadata = DefaultParamsReader.loadMetadata(path, sc, className)
val dataPath = new Path(path, "data").toString
val data = sparkSession.read.parquet(dataPath)
diff --git a/mllib/src/main/scala/org/apache/spark/ml/feature/Imputer.scala b/mllib/src/main/scala/org/apache/spark/ml/feature/Imputer.scala
index 1c074e204ad99..761947a7c394c 100644
    *       * a/mllib/src/main/scala/org/apache/spark/ml/feature/Imputer.scala
+++ b/mllib/src/main/scala/org/apache/spark/ml/feature/Imputer.scala
@@ -120,7 +120,10 @@ class Imputer @Since("2.2.0") (@Since("2.2.0") override val uid: String)

setDefault(strategy -> Imputer.mean, missingValue -> Double.NaN)
  * override def fit(dataset: Dataset[_]): ImputerModel = {
+ // Explicitly call parent's load. Otherwise, MiMa complains.
+ override def fit(dataset: Dataset[_]): ImputerModel = super.fit(dataset)
+
+ override protected def fitImpl(dataset: Dataset[_]): ImputerModel = {
transformSchema(dataset.schema, logging = true)
val spark = dataset.sparkSession

@@ -211,7 +214,7 @@ class ImputerModel private[ml] (
/** @group setParam */
def setOutputCols(value: Array[String]): this.type = set(outputCols, value)
  * override def transform(dataset: Dataset[_]): DataFrame = {
+ override protected def transformImpl(dataset: Dataset[_]): DataFrame = {
transformSchema(dataset.schema, logging = true)
val surrogates = surrogateDF.select($(inputCols).map(col): _*).head().toSeq

@@ -257,7 +260,7 @@ object ImputerModel extends MLReadable[ImputerModel] {
private val className = classOf[ImputerModel].getName
  * override def load(path: String): ImputerModel = {
+ override protected def loadImpl(path: String): ImputerModel = { val metadata = DefaultParamsReader.loadMetadata(path, sc, className) val dataPath = new Path(path, "data").toString val surrogateDF = sqlContext.read.parquet(dataPath) diff --git a/mllib/src/main/scala/org/apache/spark/ml/feature/Interaction.scala b/mllib/src/main/scala/org/apache/spark/ml/feature/Interaction.scala index 611f1b691b782..319927e9dd228 100644 --- a/mllib/src/main/scala/org/apache/spark/ml/feature/Interaction.scala +++ b/mllib/src/main/scala/org/apache/spark/ml/feature/Interaction.scala @@ -67,7 +67,8 @@ class Interaction @Since("1.6.0") (@Since("1.6.0") override val uid: String) ext }

@Since("2.0.0")
  * override def transform(dataset: Dataset[_]): DataFrame = {
+ override def transform(dataset: Dataset[_]): DataFrame = super.transform(dataset)
+ override protected def transformImpl(dataset: Dataset[_]): DataFrame = {
transformSchema(dataset.schema, logging = true)
val inputFeatures = $(inputCols).map(c => dataset.schema(c))
val featureEncoders = getFeatureEncoders(inputFeatures)
diff --git a/mllib/src/main/scala/org/apache/spark/ml/feature/LSH.scala b/mllib/src/main/scala/org/apache/spark/ml/feature/LSH.scala
index b20852383a6ff..b7cc016ebcaf1 100644
    *       * a/mllib/src/main/scala/org/apache/spark/ml/feature/LSH.scala
+++ b/mllib/src/main/scala/org/apache/spark/ml/feature/LSH.scala
@@ -95,7 +95,7 @@ private[ml] abstract class LSHModel[T <: LSHModel[T]]
*/
protected[ml] def hashDistance(x: Seq[Vector], y: Seq[Vector]): Double

  * override def transform(dataset: Dataset[_]): DataFrame = {
+ override protected def transformImpl(dataset: Dataset[_]): DataFrame = {
transformSchema(dataset.schema, logging = true)
val transformUDF = udf(hashFunction(_: Vector), DataTypes.createArrayType(new VectorUDT))
dataset.withColumn($(outputCol), transformUDF(dataset($(inputCol))))
@@ -323,7 +323,7 @@ private[ml] abstract class LSH[T <: LSHModel[T]]
*/
protected[this] def createRawLSHModel(inputDim: Int): T

  * override def fit(dataset: Dataset[_]): T = {
+ override protected def fitImpl(dataset: Dataset[_]): T = {
transformSchema(dataset.schema, logging = true)
val inputDim = dataset.select(col($(inputCol))).head().get(0).asInstanceOf[Vector].size
val model = createRawLSHModel(inputDim).setParent(this)
diff --git a/mllib/src/main/scala/org/apache/spark/ml/feature/MaxAbsScaler.scala b/mllib/src/main/scala/org/apache/spark/ml/feature/MaxAbsScaler.scala
index 90eceb0d61b40..295d3d0ccab3d 100644
    *       * a/mllib/src/main/scala/org/apache/spark/ml/feature/MaxAbsScaler.scala
+++ b/mllib/src/main/scala/org/apache/spark/ml/feature/MaxAbsScaler.scala
@@ -68,7 +68,8 @@ class MaxAbsScaler @Since("2.0.0") (@Since("2.0.0") override val uid: String)
def setOutputCol(value: String): this.type = set(outputCol, value)

@Since("2.0.0")
  * override def fit(dataset: Dataset[_]): MaxAbsScalerModel = {
+ override def fit(dataset: Dataset[_]): MaxAbsScalerModel = super.fit(dataset)
+ override protected def fitImpl(dataset: Dataset[_]): MaxAbsScalerModel = {
transformSchema(dataset.schema, logging = true)
val input: RDD[OldVector] = dataset.select($(inputCol)).rdd.map {
case Row(v: Vector) => OldVectors.fromML(v)
@@ -119,7 +120,8 @@ class MaxAbsScalerModel private[ml] (
def setOutputCol(value: String): this.type = set(outputCol, value)

@Since("2.0.0")
  * override def transform(dataset: Dataset[_]): DataFrame = {
+ override def transform(dataset: Dataset[_]): DataFrame = super.transform(dataset)
+ override protected def transformImpl(dataset: Dataset[_]): DataFrame = {
transformSchema(dataset.schema, logging = true)
// TODO: this looks hack, we may have to handle sparse and dense vectors separately.
val maxAbsUnzero = Vectors.dense(maxAbs.toArray.map(x => if (x == 0) 1 else x))
@@ -165,7 +167,7 @@ object MaxAbsScalerModel extends MLReadable[MaxAbsScalerModel] {

private val className = classOf[MaxAbsScalerModel].getName
  * override def load(path: String): MaxAbsScalerModel = {
+ override protected def loadImpl(path: String): MaxAbsScalerModel = {
val metadata = DefaultParamsReader.loadMetadata(path, sc, className)
val dataPath = new Path(path, "data").toString
val Row(maxAbs: Vector) = sparkSession.read.parquet(dataPath)
diff --git a/mllib/src/main/scala/org/apache/spark/ml/feature/MinHashLSH.scala b/mllib/src/main/scala/org/apache/spark/ml/feature/MinHashLSH.scala
index 21cde66d8db6b..168accb1a1722 100644
    *       * a/mllib/src/main/scala/org/apache/spark/ml/feature/MinHashLSH.scala
+++ b/mllib/src/main/scala/org/apache/spark/ml/feature/MinHashLSH.scala
@@ -194,7 +194,7 @@ object MinHashLSHModel extends MLReadable[MinHashLSHModel] {
/** Checked against metadata when loading model */
private val className = classOf[MinHashLSHModel].getName

  * override def load(path: String): MinHashLSHModel = {
+ override protected def loadImpl(path: String): MinHashLSHModel = {
val metadata = DefaultParamsReader.loadMetadata(path, sc, className)

val dataPath = new Path(path, "data").toString
diff --git a/mllib/src/main/scala/org/apache/spark/ml/feature/MinMaxScaler.scala b/mllib/src/main/scala/org/apache/spark/ml/feature/MinMaxScaler.scala
index 2e0ae4af66f06..d76fc5ec05c52 100644
— a/mllib/src/main/scala/org/apache/spark/ml/feature/MinMaxScaler.scala
+++ b/mllib/src/main/scala/org/apache/spark/ml/feature/MinMaxScaler.scala
@@ -115,7 +115,8 @@ class MinMaxScaler @Since("1.5.0") (@Since("1.5.0") override val uid: String)
def setMax(value: Double): this.type = set(max, value)
@Since("2.0.0")
  * override def fit(dataset: Dataset[_]): MinMaxScalerModel = {
+ override def fit(dataset: Dataset[_]): MinMaxScalerModel = super.fit(dataset)
+ override protected def fitImpl(dataset: Dataset[_]): MinMaxScalerModel = {
transformSchema(dataset.schema, logging = true)
val input: RDD[OldVector] = dataset.select($(inputCol)).rdd.map {
case Row(v: Vector) => OldVectors.fromML(v)
@@ -174,7 +175,8 @@ class MinMaxScalerModel private[ml] (
def setMax(value: Double): this.type = set(max, value)

@Since("2.0.0")
  * override def transform(dataset: Dataset[_]): DataFrame = {
+ override def transform(dataset: Dataset[_]): DataFrame = super.transform(dataset)
+ override protected def transformImpl(dataset: Dataset[_]): DataFrame = {
transformSchema(dataset.schema, logging = true)
val originalRange = (originalMax.asBreeze - originalMin.asBreeze).toArray
val minArray = originalMin.toArray
@@ -234,7 +236,7 @@ object MinMaxScalerModel extends MLReadable[MinMaxScalerModel] {

private val className = classOf[MinMaxScalerModel].getName
  * override def load(path: String): MinMaxScalerModel = {
+ override protected def loadImpl(path: String): MinMaxScalerModel = { val metadata = DefaultParamsReader.loadMetadata(path, sc, className) val dataPath = new Path(path, "data").toString val data = sparkSession.read.parquet(dataPath) diff --git a/mllib/src/main/scala/org/apache/spark/ml/feature/OneHotEncoder.scala b/mllib/src/main/scala/org/apache/spark/ml/feature/OneHotEncoder.scala index ec9792cbbda8f..4e4a259c95cce 100644 --- a/mllib/src/main/scala/org/apache/spark/ml/feature/OneHotEncoder.scala +++ b/mllib/src/main/scala/org/apache/spark/ml/feature/OneHotEncoder.scala @@ -147,7 +147,8 @@ class OneHotEncoder @Since("3.0.0") (@Since("3.0.0") override val uid: String) }

@Since("3.0.0")
  * override def fit(dataset: Dataset[_]): OneHotEncoderModel = {
+ override def fit(dataset: Dataset[_]): OneHotEncoderModel = super.fit(dataset)
+ override protected def fitImpl(dataset: Dataset[_]): OneHotEncoderModel = { transformSchema(dataset.schema) // Compute the plain number of categories without `handleInvalid` and @@ -324,7 +325,8 @@ class OneHotEncoderModel private[ml] ( }

@Since("3.0.0")
  * override def transform(dataset: Dataset[_]): DataFrame = {
+ override def transform(dataset: Dataset[_]): DataFrame = super.transform(dataset)
+ override protected def transformImpl(dataset: Dataset[_]): DataFrame = {
val transformedSchema = transformSchema(dataset.schema, logging = true)
val keepInvalid = $(handleInvalid) == OneHotEncoder.KEEP_INVALID

@@ -378,7 +380,7 @@ object OneHotEncoderModel extends MLReadable[OneHotEncoderModel] {
private val className = classOf[OneHotEncoderModel].getName
  * override def load(path: String): OneHotEncoderModel = {
+ override protected def loadImpl(path: String): OneHotEncoderModel = {
val metadata = DefaultParamsReader.loadMetadata(path, sc, className)
val dataPath = new Path(path, "data").toString
val data = sparkSession.read.parquet(dataPath)
diff --git a/mllib/src/main/scala/org/apache/spark/ml/feature/PCA.scala b/mllib/src/main/scala/org/apache/spark/ml/feature/PCA.scala
index 8172491a517d1..0a79b49b984c3 100644
    *       * a/mllib/src/main/scala/org/apache/spark/ml/feature/PCA.scala
+++ b/mllib/src/main/scala/org/apache/spark/ml/feature/PCA.scala
@@ -90,7 +90,8 @@ class PCA @Since("1.5.0") (

  * Computes a [[PCAModel]] that contains the principal components of the input vectors.
*/
@Since("2.0.0")

  * override def fit(dataset: Dataset[_]): PCAModel = {
+ override def fit(dataset: Dataset[_]): PCAModel = super.fit(dataset)
+ override protected def fitImpl(dataset: Dataset[_]): PCAModel = {
transformSchema(dataset.schema, logging = true)
val input: RDD[OldVector] = dataset.select($(inputCol)).rdd.map {
case Row(v: Vector) => OldVectors.fromML(v)
@@ -147,7 +148,8 @@ class PCAModel private[ml] (

  * to `PCA.fit()`.
*/
@Since("2.0.0")

  * override def transform(dataset: Dataset[_]): DataFrame = {
+ override def transform(dataset: Dataset[_]): DataFrame = super.transform(dataset)
+ override protected def transformImpl(dataset: Dataset[_]): DataFrame = {
transformSchema(dataset.schema, logging = true)
val pcaModel = new feature.PCAModel($(k),
OldMatrices.fromML(pc).asInstanceOf[OldDenseMatrix],
@@ -203,7 +205,7 @@ object PCAModel extends MLReadable[PCAModel] {

  * @param path path to serialized model data
  * @return a [[PCAModel]]
*/

  * override def load(path: String): PCAModel = {
+ override protected def loadImpl(path: String): PCAModel = { val metadata = DefaultParamsReader.loadMetadata(path, sc, className) val dataPath = new Path(path, "data").toString diff --git a/mllib/src/main/scala/org/apache/spark/ml/feature/QuantileDiscretizer.scala b/mllib/src/main/scala/org/apache/spark/ml/feature/QuantileDiscretizer.scala index 5bfaa3b7f3f52..0f29ae9687c02 100644 --- a/mllib/src/main/scala/org/apache/spark/ml/feature/QuantileDiscretizer.scala +++ b/mllib/src/main/scala/org/apache/spark/ml/feature/QuantileDiscretizer.scala @@ -199,7 +199,8 @@ final class QuantileDiscretizer @Since("1.6.0") (@Since("1.6.0") override val ui }

@Since("2.0.0")
  * override def fit(dataset: Dataset[_]): Bucketizer = {
+ override def fit(dataset: Dataset[_]): Bucketizer = super.fit(dataset)
+ override protected def fitImpl(dataset: Dataset[_]): Bucketizer = {
transformSchema(dataset.schema, logging = true)
val bucketizer = new Bucketizer(uid).setHandleInvalid($(handleInvalid))
if (isSet(inputCols)) { diff --git a/mllib/src/main/scala/org/apache/spark/ml/feature/RFormula.scala b/mllib/src/main/scala/org/apache/spark/ml/feature/RFormula.scala index d7eb13772aa64..f5132f09f95f4 100644 --- a/mllib/src/main/scala/org/apache/spark/ml/feature/RFormula.scala +++ b/mllib/src/main/scala/org/apache/spark/ml/feature/RFormula.scala @@ -193,7 +193,8 @@ class RFormula @Since("1.5.0") (@Since("1.5.0") override val uid: String) }

@Since("2.0.0")
  * override def fit(dataset: Dataset[_]): RFormulaModel = {
+ override def fit(dataset: Dataset[_]): RFormulaModel = super.fit(dataset)
+ override protected def fitImpl(dataset: Dataset[_]): RFormulaModel = {
transformSchema(dataset.schema, logging = true)
require(isDefined(formula), "Formula must be defined first.")
val parsedFormula = RFormulaParser.parse($(formula))
@@ -338,7 +339,8 @@ class RFormulaModel private[feature](
extends Model[RFormulaModel] with RFormulaBase with MLWritable {

@Since("2.0.0")
  * override def transform(dataset: Dataset[_]): DataFrame = {
+ override def transform(dataset: Dataset[_]): DataFrame = super.transform(dataset)
+ override protected def transformImpl(dataset: Dataset[_]): DataFrame = { checkCanTransform(dataset.schema) transformLabel(pipelineModel.transform(dataset)) }
@@ -431,7 +433,7 @@ object RFormulaModel extends MLReadable[RFormulaModel] {
/** Checked against metadata when loading model */
private val className = classOf[RFormulaModel].getName

  * override def load(path: String): RFormulaModel = {
+ override protected def loadImpl(path: String): RFormulaModel = {
val metadata = DefaultParamsReader.loadMetadata(path, sc, className)

val dataPath = new Path(path, "data").toString
@@ -462,7 +464,7 @@ private class ColumnPruner(override val uid: String, val columnsToPrune: Set[Str
def this(columnsToPrune: Set[String]) =
this(Identifiable.randomUID("columnPruner"), columnsToPrune)
  * override def transform(dataset: Dataset[_]): DataFrame = {
+ override protected def transformImpl(dataset: Dataset[_]): DataFrame = { val columnsToKeep = dataset.columns.filter(!columnsToPrune.contains(_)) dataset.select(columnsToKeep.map(dataset.col): _*) }
@@ -502,7 +504,7 @@ private object ColumnPruner extends MLReadable[ColumnPruner] {
/** Checked against metadata when loading model */
private val className = classOf[ColumnPruner].getName

  * override def load(path: String): ColumnPruner = {
+ override protected def loadImpl(path: String): ColumnPruner = {
val metadata = DefaultParamsReader.loadMetadata(path, sc, className)

val dataPath = new Path(path, "data").toString
@@ -535,7 +537,7 @@ private class VectorAttributeRewriter(
def this(vectorCol: String, prefixesToRewrite: Map[String, String]) =
this(Identifiable.randomUID("vectorAttrRewriter"), vectorCol, prefixesToRewrite)
  * override def transform(dataset: Dataset[_]): DataFrame = {
+ override protected def transformImpl(dataset: Dataset[_]): DataFrame = {
val metadata = {
val group = AttributeGroup.fromStructField(dataset.schema(vectorCol))
val attrs = group.attributes.get.map { attr =>
@@ -593,7 +595,7 @@ private object VectorAttributeRewriter extends MLReadable[VectorAttributeRewrite
/** Checked against metadata when loading model */
private val className = classOf[VectorAttributeRewriter].getName

  * override def load(path: String): VectorAttributeRewriter = {
+ override protected def loadImpl(path: String): VectorAttributeRewriter = {
val metadata = DefaultParamsReader.loadMetadata(path, sc, className)

val dataPath = new Path(path, "data").toString
diff --git a/mllib/src/main/scala/org/apache/spark/ml/feature/SQLTransformer.scala b/mllib/src/main/scala/org/apache/spark/ml/feature/SQLTransformer.scala
index 0fb1d8c5dc579..d453ab3723c0c 100644
— a/mllib/src/main/scala/org/apache/spark/ml/feature/SQLTransformer.scala
+++ b/mllib/src/main/scala/org/apache/spark/ml/feature/SQLTransformer.scala
@@ -64,7 +64,8 @@ class SQLTransformer @Since("1.6.0") (@Since("1.6.0") override val uid: String)
private val tableIdentifier: String = "__THIS_ _"
@Since("2.0.0")
  * override def transform(dataset: Dataset[_]): DataFrame = {
+ override def transform(dataset: Dataset[_]): DataFrame = super.transform(dataset)
+ override protected def transformImpl(dataset: Dataset[_]): DataFrame = {
transformSchema(dataset.schema, logging = true)
val tableName = Identifiable.randomUID(uid)
dataset.createOrReplaceTempView(tableName)
diff --git a/mllib/src/main/scala/org/apache/spark/ml/feature/StandardScaler.scala b/mllib/src/main/scala/org/apache/spark/ml/feature/StandardScaler.scala
index 91b0707dec3f3..c96726faab4f5 100644
    *       * a/mllib/src/main/scala/org/apache/spark/ml/feature/StandardScaler.scala
+++ b/mllib/src/main/scala/org/apache/spark/ml/feature/StandardScaler.scala
@@ -108,7 +108,8 @@ class StandardScaler @Since("1.4.0") (
def setWithStd(value: Boolean): this.type = set(withStd, value)

@Since("2.0.0")
  * override def fit(dataset: Dataset[_]): StandardScalerModel = {
+ override def fit(dataset: Dataset[_]): StandardScalerModel = super.fit(dataset)
+ override protected def fitImpl(dataset: Dataset[_]): StandardScalerModel = {
transformSchema(dataset.schema, logging = true)
val input: RDD[OldVector] = dataset.select($(inputCol)).rdd.map {
case Row(v: Vector) => OldVectors.fromML(v)
@@ -158,7 +159,8 @@ class StandardScalerModel private[ml] (
def setOutputCol(value: String): this.type = set(outputCol, value)

@Since("2.0.0")
  * override def transform(dataset: Dataset[_]): DataFrame = {
+ override def transform(dataset: Dataset[_]): DataFrame = super.transform(dataset)
+ override protected def transformImpl(dataset: Dataset[_]): DataFrame = {
transformSchema(dataset.schema, logging = true)
val scaler = new feature.StandardScalerModel(std, mean, $(withStd), $(withMean))

@@ -204,7 +206,7 @@ object StandardScalerModel extends MLReadable[StandardScalerModel] {
private val className = classOf[StandardScalerModel].getName
  * override def load(path: String): StandardScalerModel = {
+ override protected def loadImpl(path: String): StandardScalerModel = {
val metadata = DefaultParamsReader.loadMetadata(path, sc, className)
val dataPath = new Path(path, "data").toString
val data = sparkSession.read.parquet(dataPath)
diff --git a/mllib/src/main/scala/org/apache/spark/ml/feature/StopWordsRemover.scala b/mllib/src/main/scala/org/apache/spark/ml/feature/StopWordsRemover.scala
index 6669d402cd996..8110cccf27167 100755
    *       * a/mllib/src/main/scala/org/apache/spark/ml/feature/StopWordsRemover.scala
+++ b/mllib/src/main/scala/org/apache/spark/ml/feature/StopWordsRemover.scala
@@ -109,7 +109,8 @@ class StopWordsRemover @Since("1.5.0") (@Since("1.5.0") override val uid: String
caseSensitive -> false, locale -> Locale.getDefault.toString)

@Since("2.0.0")
  * override def transform(dataset: Dataset[_]): DataFrame = {
+ override def transform(dataset: Dataset[_]): DataFrame = super.transform(dataset)
+ override protected def transformImpl(dataset: Dataset[_]): DataFrame = {
val outputSchema = transformSchema(dataset.schema)
val t = if ($(caseSensitive)) {
val stopWordsSet = $(stopWords).toSet
diff --git a/mllib/src/main/scala/org/apache/spark/ml/feature/StringIndexer.scala b/mllib/src/main/scala/org/apache/spark/ml/feature/StringIndexer.scala
index a833d8b270cf1..74843bac1ea82 100644
    *       * a/mllib/src/main/scala/org/apache/spark/ml/feature/StringIndexer.scala
+++ b/mllib/src/main/scala/org/apache/spark/ml/feature/StringIndexer.scala
@@ -131,7 +131,8 @@ class StringIndexer @Since("1.4.0") (
def setOutputCol(value: String): this.type = set(outputCol, value)

@Since("2.0.0")
  * override def fit(dataset: Dataset[_]): StringIndexerModel = {
+ override def fit(dataset: Dataset[_]): StringIndexerModel = super.fit(dataset)
+ override protected def fitImpl(dataset: Dataset[_]): StringIndexerModel = {
transformSchema(dataset.schema, logging = true)
val values = dataset.na.drop(Array($(inputCol)))
.select(col($(inputCol)).cast(StringType))
@@ -218,7 +219,8 @@ class StringIndexerModel (
def setOutputCol(value: String): this.type = set(outputCol, value)

@Since("2.0.0")
  * override def transform(dataset: Dataset[_]): DataFrame = {
+ override def transform(dataset: Dataset[_]): DataFrame = super.transform(dataset)
+ override protected def transformImpl(dataset: Dataset[_]): DataFrame = {
if (!dataset.schema.fieldNames.contains($(inputCol))) {
logInfo(s"Input column ${$(inputCol)} does not exist during transformation. " +
"Skip StringIndexerModel.")
@@ -307,7 +309,7 @@ object StringIndexerModel extends MLReadable[StringIndexerModel] {

private val className = classOf[StringIndexerModel].getName
  * override def load(path: String): StringIndexerModel = {
+ override protected def loadImpl(path: String): StringIndexerModel = { val metadata = DefaultParamsReader.loadMetadata(path, sc, className) val dataPath = new Path(path, "data").toString val data = sparkSession.read.parquet(dataPath) @@ -386,7 +388,8 @@ class IndexToString @Since("2.2.0") (@Since("1.5.0") override val uid: String) }

@Since("2.0.0")
  * override def transform(dataset: Dataset[_]): DataFrame = {
+ override def transform(dataset: Dataset[_]): DataFrame = super.transform(dataset)
+ override protected def transformImpl(dataset: Dataset[_]): DataFrame = {
transformSchema(dataset.schema, logging = true)
val inputColSchema = dataset.schema($(inputCol))
// If the labels array is empty use column metadata
diff --git a/mllib/src/main/scala/org/apache/spark/ml/feature/VectorAssembler.scala b/mllib/src/main/scala/org/apache/spark/ml/feature/VectorAssembler.scala
index 57e23d5072b88..6add5f8d8c4e6 100644
    *       * a/mllib/src/main/scala/org/apache/spark/ml/feature/VectorAssembler.scala
+++ b/mllib/src/main/scala/org/apache/spark/ml/feature/VectorAssembler.scala
@@ -82,7 +82,8 @@ class VectorAssembler @Since("1.4.0") (@Since("1.4.0") override val uid: String)
setDefault(handleInvalid, VectorAssembler.ERROR_INVALID)

@Since("2.0.0")
  * override def transform(dataset: Dataset[_]): DataFrame = {
+ override def transform(dataset: Dataset[_]): DataFrame = super.transform(dataset)
+ override protected def transformImpl(dataset: Dataset[_]): DataFrame = {
transformSchema(dataset.schema, logging = true)
// Schema transformation.
val schema = dataset.schema
diff --git a/mllib/src/main/scala/org/apache/spark/ml/feature/VectorIndexer.scala b/mllib/src/main/scala/org/apache/spark/ml/feature/VectorIndexer.scala
index 0e7396a621dbd..fd6e79c4e21fb 100644
    *       * a/mllib/src/main/scala/org/apache/spark/ml/feature/VectorIndexer.scala
+++ b/mllib/src/main/scala/org/apache/spark/ml/feature/VectorIndexer.scala
@@ -140,7 +140,8 @@ class VectorIndexer @Since("1.4.0") (
def setHandleInvalid(value: String): this.type = set(handleInvalid, value)

@Since("2.0.0")
  * override def fit(dataset: Dataset[_]): VectorIndexerModel = {
+ override def fit(dataset: Dataset[_]): VectorIndexerModel = super.fit(dataset)
+ override protected def fitImpl(dataset: Dataset[_]): VectorIndexerModel = {
transformSchema(dataset.schema, logging = true)
val firstRow = dataset.select($(inputCol)).take(1)
require(firstRow.length == 1, s"VectorIndexer cannot be fit on an empty dataset.")
@@ -425,7 +426,8 @@ class VectorIndexerModel private[ml] (
def setOutputCol(value: String): this.type = set(outputCol, value)

@Since("2.0.0")
  * override def transform(dataset: Dataset[_]): DataFrame = {
+ override def transform(dataset: Dataset[_]): DataFrame = super.transform(dataset)
+ override protected def transformImpl(dataset: Dataset[_]): DataFrame = {
transformSchema(dataset.schema, logging = true)
val newField = prepOutputField(dataset.schema)
val transformUDF = udf { (vector: Vector) => transformFunc(vector) }
@@ -528,7 +530,7 @@ object VectorIndexerModel extends MLReadable[VectorIndexerModel] {

private val className = classOf[VectorIndexerModel].getName
  * override def load(path: String): VectorIndexerModel = {
+ override protected def loadImpl(path: String): VectorIndexerModel = {
val metadata = DefaultParamsReader.loadMetadata(path, sc, className)
val dataPath = new Path(path, "data").toString
val data = sparkSession.read.parquet(dataPath)
diff --git a/mllib/src/main/scala/org/apache/spark/ml/feature/VectorSizeHint.scala b/mllib/src/main/scala/org/apache/spark/ml/feature/VectorSizeHint.scala
index f5947d61fe349..854fd1b4d3776 100644
    *       * a/mllib/src/main/scala/org/apache/spark/ml/feature/VectorSizeHint.scala
+++ b/mllib/src/main/scala/org/apache/spark/ml/feature/VectorSizeHint.scala
@@ -96,7 +96,8 @@ class VectorSizeHint @Since("2.3.0") (@Since("2.3.0") override val uid: String)
setDefault(handleInvalid, VectorSizeHint.ERROR_INVALID)

@Since("2.3.0")
  * override def transform(dataset: Dataset[_]): DataFrame = {
+ override def transform(dataset: Dataset[_]): DataFrame = super.transform(dataset)
+ override protected def transformImpl(dataset: Dataset[_]): DataFrame = {
val localInputCol = getInputCol
val localSize = getSize
val localHandleInvalid = getHandleInvalid
diff --git a/mllib/src/main/scala/org/apache/spark/ml/feature/VectorSlicer.scala b/mllib/src/main/scala/org/apache/spark/ml/feature/VectorSlicer.scala
index e3e462d07e10c..cd1d49c1a2cb0 100644
    *       * a/mllib/src/main/scala/org/apache/spark/ml/feature/VectorSlicer.scala
+++ b/mllib/src/main/scala/org/apache/spark/ml/feature/VectorSlicer.scala
@@ -98,7 +98,8 @@ final class VectorSlicer @Since("1.5.0") (@Since("1.5.0") override val uid: Stri
def setOutputCol(value: String): this.type = set(outputCol, value)

@Since("2.0.0")
  * override def transform(dataset: Dataset[_]): DataFrame = {
+ override def transform(dataset: Dataset[_]): DataFrame = super.transform(dataset)
+ override protected def transformImpl(dataset: Dataset[_]): DataFrame = {
// Validity checks
transformSchema(dataset.schema)
val inputAttr = AttributeGroup.fromStructField(dataset.schema($(inputCol)))
diff --git a/mllib/src/main/scala/org/apache/spark/ml/feature/Word2Vec.scala b/mllib/src/main/scala/org/apache/spark/ml/feature/Word2Vec.scala
index fc9996d69ba72..31e5b00765c68 100644
    *       * a/mllib/src/main/scala/org/apache/spark/ml/feature/Word2Vec.scala
+++ b/mllib/src/main/scala/org/apache/spark/ml/feature/Word2Vec.scala
@@ -171,7 +171,8 @@ final class Word2Vec @Since("1.4.0") (
def setMaxSentenceLength(value: Int): this.type = set(maxSentenceLength, value)

@Since("2.0.0")
  * override def fit(dataset: Dataset[_]): Word2VecModel = {
+ override def fit(dataset: Dataset[_]): Word2VecModel = super.fit(dataset)
+ override protected def fitImpl(dataset: Dataset[_]): Word2VecModel = {
transformSchema(dataset.schema, logging = true)
val input = dataset.select($(inputCol)).rdd.map(_.getAs[Seq[String]](0))
val wordVectors = new feature.Word2Vec()
@@ -286,7 +287,8 @@ class Word2VecModel private[ml] (

  * is performed by averaging all word vectors it contains.
*/
@Since("2.0.0")

  * override def transform(dataset: Dataset[_]): DataFrame = {
+ override def transform(dataset: Dataset[_]): DataFrame = super.transform(dataset)
+ override protected def transformImpl(dataset: Dataset[_]): DataFrame = {
transformSchema(dataset.schema, logging = true)
val vectors = wordVectors.getVectors
.mapValues(vv => Vectors.dense(vv.map(_.toDouble)))
@@ -385,7 +387,7 @@ object Word2VecModel extends MLReadable[Word2VecModel] {

private val className = classOf[Word2VecModel].getName
  * override def load(path: String): Word2VecModel = {
+ override protected def loadImpl(path: String): Word2VecModel = {
val spark = sparkSession
import spark.implicits._

diff --git a/mllib/src/main/scala/org/apache/spark/ml/fpm/FPGrowth.scala b/mllib/src/main/scala/org/apache/spark/ml/fpm/FPGrowth.scala
index 7322815c12ab8..d2ca4bc53957f 100644
— a/mllib/src/main/scala/org/apache/spark/ml/fpm/FPGrowth.scala
+++ b/mllib/src/main/scala/org/apache/spark/ml/fpm/FPGrowth.scala
@@ -157,7 +157,8 @@ class FPGrowth @Since("2.2.0") (
def setPredictionCol(value: String): this.type = set(predictionCol, value)
@Since("2.2.0")
  * override def fit(dataset: Dataset[_]): FPGrowthModel = {
+ override def fit(dataset: Dataset[_]): FPGrowthModel = super.fit(dataset)
+ override protected def fitImpl(dataset: Dataset[_]): FPGrowthModel = { transformSchema(dataset.schema, logging = true) genericFit(dataset) }
@@ -277,7 +278,8 @@ class FPGrowthModel private[ml] (

  * efficiency. This may bring pressure to driver memory for large set of association rules.
*/
@Since("2.2.0")

  * override def transform(dataset: Dataset[_]): DataFrame = {
+ override def transform(dataset: Dataset[_]): DataFrame = super.transform(dataset)
+ override protected def transformImpl(dataset: Dataset[_]): DataFrame = { transformSchema(dataset.schema, logging = true) genericTransform(dataset) }
@@ -342,7 +344,7 @@ object FPGrowthModel extends MLReadable[FPGrowthModel] {
/** Checked against metadata when loading model */
private val className = classOf[FPGrowthModel].getName

  * override def load(path: String): FPGrowthModel = {
+ override protected def loadImpl(path: String): FPGrowthModel = {
implicit val format = DefaultFormats
val metadata = DefaultParamsReader.loadMetadata(path, sc, className)
val (major, minor) = VersionUtils.majorMinorVersion(metadata.sparkVersion)
diff --git a/mllib/src/main/scala/org/apache/spark/ml/r/AFTSurvivalRegressionWrapper.scala b/mllib/src/main/scala/org/apache/spark/ml/r/AFTSurvivalRegressionWrapper.scala
index 1b5f77a9ae897..d45a5fa14df90 100644
    *       * a/mllib/src/main/scala/org/apache/spark/ml/r/AFTSurvivalRegressionWrapper.scala
+++ b/mllib/src/main/scala/org/apache/spark/ml/r/AFTSurvivalRegressionWrapper.scala
@@ -136,7 +136,7 @@ private[r] object AFTSurvivalRegressionWrapper extends MLReadable[AFTSurvivalReg

class AFTSurvivalRegressionWrapperReader extends MLReader[AFTSurvivalRegressionWrapper] {
  * override def load(path: String): AFTSurvivalRegressionWrapper = {
+ override protected def loadImpl(path: String): AFTSurvivalRegressionWrapper = {
implicit val format = DefaultFormats
val rMetadataPath = new Path(path, "rMetadata").toString
val pipelinePath = new Path(path, "pipeline").toString
diff --git a/mllib/src/main/scala/org/apache/spark/ml/r/ALSWrapper.scala b/mllib/src/main/scala/org/apache/spark/ml/r/ALSWrapper.scala
index ad13cced4667b..8d12d80ab4734 100644
    *       * a/mllib/src/main/scala/org/apache/spark/ml/r/ALSWrapper.scala
+++ b/mllib/src/main/scala/org/apache/spark/ml/r/ALSWrapper.scala
@@ -102,7 +102,7 @@ private[r] object ALSWrapper extends MLReadable[ALSWrapper] {

class ALSWrapperReader extends MLReader[ALSWrapper] {
  * override def load(path: String): ALSWrapper = {
+ override protected def loadImpl(path: String): ALSWrapper = {
implicit val format = DefaultFormats
val rMetadataPath = new Path(path, "rMetadata").toString
val modelPath = new Path(path, "model").toString
diff --git a/mllib/src/main/scala/org/apache/spark/ml/r/BisectingKMeansWrapper.scala b/mllib/src/main/scala/org/apache/spark/ml/r/BisectingKMeansWrapper.scala
index 71712c1c5eec5..8478c7b6e8c77 100644
    *       * a/mllib/src/main/scala/org/apache/spark/ml/r/BisectingKMeansWrapper.scala
+++ b/mllib/src/main/scala/org/apache/spark/ml/r/BisectingKMeansWrapper.scala
@@ -126,7 +126,7 @@ private[r] object BisectingKMeansWrapper extends MLReadable[BisectingKMeansWrapp

class BisectingKMeansWrapperReader extends MLReader[BisectingKMeansWrapper] {
  * override def load(path: String): BisectingKMeansWrapper = {
+ override protected def loadImpl(path: String): BisectingKMeansWrapper = {
implicit val format = DefaultFormats
val rMetadataPath = new Path(path, "rMetadata").toString
val pipelinePath = new Path(path, "pipeline").toString
diff --git a/mllib/src/main/scala/org/apache/spark/ml/r/DecisionTreeClassificationWrapper.scala b/mllib/src/main/scala/org/apache/spark/ml/r/DecisionTreeClassificationWrapper.scala
index a90cae5869b2a..ad9476c1c000c 100644
    *       * a/mllib/src/main/scala/org/apache/spark/ml/r/DecisionTreeClassificationWrapper.scala
+++ b/mllib/src/main/scala/org/apache/spark/ml/r/DecisionTreeClassificationWrapper.scala
@@ -137,7 +137,7 @@ private[r] object DecisionTreeClassifierWrapper extends MLReadable[DecisionTreeC

class DecisionTreeClassifierWrapperReader extends MLReader[DecisionTreeClassifierWrapper] {
  * override def load(path: String): DecisionTreeClassifierWrapper = {
+ override protected def loadImpl(path: String): DecisionTreeClassifierWrapper = {
implicit val format = DefaultFormats
val rMetadataPath = new Path(path, "rMetadata").toString
val pipelinePath = new Path(path, "pipeline").toString
diff --git a/mllib/src/main/scala/org/apache/spark/ml/r/DecisionTreeRegressionWrapper.scala b/mllib/src/main/scala/org/apache/spark/ml/r/DecisionTreeRegressionWrapper.scala
index de712d67e6df5..efe7884d5a170 100644
    *       * a/mllib/src/main/scala/org/apache/spark/ml/r/DecisionTreeRegressionWrapper.scala
+++ b/mllib/src/main/scala/org/apache/spark/ml/r/DecisionTreeRegressionWrapper.scala
@@ -120,7 +120,7 @@ private[r] object DecisionTreeRegressorWrapper extends MLReadable[DecisionTreeRe

class DecisionTreeRegressorWrapperReader extends MLReader[DecisionTreeRegressorWrapper] {
  * override def load(path: String): DecisionTreeRegressorWrapper = {
+ override protected def loadImpl(path: String): DecisionTreeRegressorWrapper = {
implicit val format = DefaultFormats
val rMetadataPath = new Path(path, "rMetadata").toString
val pipelinePath = new Path(path, "pipeline").toString
diff --git a/mllib/src/main/scala/org/apache/spark/ml/r/FPGrowthWrapper.scala b/mllib/src/main/scala/org/apache/spark/ml/r/FPGrowthWrapper.scala
index b8151d8d90702..27a859678372f 100644
    *       * a/mllib/src/main/scala/org/apache/spark/ml/r/FPGrowthWrapper.scala
+++ b/mllib/src/main/scala/org/apache/spark/ml/r/FPGrowthWrapper.scala
@@ -61,7 +61,7 @@ private[r] object FPGrowthWrapper extends MLReadable[FPGrowthWrapper] {
override def read: MLReader[FPGrowthWrapper] = new FPGrowthWrapperReader

class FPGrowthWrapperReader extends MLReader[FPGrowthWrapper] {
  * override def load(path: String): FPGrowthWrapper = {
+ override protected def loadImpl(path: String): FPGrowthWrapper = {
val modelPath = new Path(path, "model").toString
val fPGrowthModel = FPGrowthModel.load(modelPath)

diff --git a/mllib/src/main/scala/org/apache/spark/ml/r/GBTClassificationWrapper.scala b/mllib/src/main/scala/org/apache/spark/ml/r/GBTClassificationWrapper.scala
index ecaeec5a7791a..ff55d32019030 100644
— a/mllib/src/main/scala/org/apache/spark/ml/r/GBTClassificationWrapper.scala
+++ b/mllib/src/main/scala/org/apache/spark/ml/r/GBTClassificationWrapper.scala
@@ -144,7 +144,7 @@ private[r] object GBTClassifierWrapper extends MLReadable[GBTClassifierWrapper]
class GBTClassifierWrapperReader extends MLReader[GBTClassifierWrapper] {
  * override def load(path: String): GBTClassifierWrapper = {
+ override protected def loadImpl(path: String): GBTClassifierWrapper = {
implicit val format = DefaultFormats
val rMetadataPath = new Path(path, "rMetadata").toString
val pipelinePath = new Path(path, "pipeline").toString
diff --git a/mllib/src/main/scala/org/apache/spark/ml/r/GBTRegressionWrapper.scala b/mllib/src/main/scala/org/apache/spark/ml/r/GBTRegressionWrapper.scala
index b568d7859221f..fef2c5755e8f9 100644
    *       * a/mllib/src/main/scala/org/apache/spark/ml/r/GBTRegressionWrapper.scala
+++ b/mllib/src/main/scala/org/apache/spark/ml/r/GBTRegressionWrapper.scala
@@ -128,7 +128,7 @@ private[r] object GBTRegressorWrapper extends MLReadable[GBTRegressorWrapper] {

class GBTRegressorWrapperReader extends MLReader[GBTRegressorWrapper] {
  * override def load(path: String): GBTRegressorWrapper = {
+ override protected def loadImpl(path: String): GBTRegressorWrapper = {
implicit val format = DefaultFormats
val rMetadataPath = new Path(path, "rMetadata").toString
val pipelinePath = new Path(path, "pipeline").toString
diff --git a/mllib/src/main/scala/org/apache/spark/ml/r/GaussianMixtureWrapper.scala b/mllib/src/main/scala/org/apache/spark/ml/r/GaussianMixtureWrapper.scala
index 9a98a8b18b141..656a0062cd14f 100644
    *       * a/mllib/src/main/scala/org/apache/spark/ml/r/GaussianMixtureWrapper.scala
+++ b/mllib/src/main/scala/org/apache/spark/ml/r/GaussianMixtureWrapper.scala
@@ -120,7 +120,7 @@ private[r] object GaussianMixtureWrapper extends MLReadable[GaussianMixtureWrapp

class GaussianMixtureWrapperReader extends MLReader[GaussianMixtureWrapper] {
  * override def load(path: String): GaussianMixtureWrapper = {
+ override protected def loadImpl(path: String): GaussianMixtureWrapper = {
implicit val format = DefaultFormats
val rMetadataPath = new Path(path, "rMetadata").toString
val pipelinePath = new Path(path, "pipeline").toString
diff --git a/mllib/src/main/scala/org/apache/spark/ml/r/GeneralizedLinearRegressionWrapper.scala b/mllib/src/main/scala/org/apache/spark/ml/r/GeneralizedLinearRegressionWrapper.scala
index 64575b0cb0cb5..c974519211288 100644
    *       * a/mllib/src/main/scala/org/apache/spark/ml/r/GeneralizedLinearRegressionWrapper.scala
+++ b/mllib/src/main/scala/org/apache/spark/ml/r/GeneralizedLinearRegressionWrapper.scala
@@ -179,7 +179,7 @@ private[r] object GeneralizedLinearRegressionWrapper
class GeneralizedLinearRegressionWrapperReader
extends MLReader[GeneralizedLinearRegressionWrapper] {

  * override def load(path: String): GeneralizedLinearRegressionWrapper = {
+ override protected def loadImpl(path: String): GeneralizedLinearRegressionWrapper = {
implicit val format = DefaultFormats
val rMetadataPath = new Path(path, "rMetadata").toString
val pipelinePath = new Path(path, "pipeline").toString
diff --git a/mllib/src/main/scala/org/apache/spark/ml/r/IsotonicRegressionWrapper.scala b/mllib/src/main/scala/org/apache/spark/ml/r/IsotonicRegressionWrapper.scala
index d31ebb46afb97..dc1f3e62056f6 100644
    *       * a/mllib/src/main/scala/org/apache/spark/ml/r/IsotonicRegressionWrapper.scala
+++ b/mllib/src/main/scala/org/apache/spark/ml/r/IsotonicRegressionWrapper.scala
@@ -106,7 +106,7 @@ private[r] object IsotonicRegressionWrapper

class IsotonicRegressionWrapperReader extends MLReader[IsotonicRegressionWrapper] {
  * override def load(path: String): IsotonicRegressionWrapper = {
+ override protected def loadImpl(path: String): IsotonicRegressionWrapper = {
implicit val format = DefaultFormats
val rMetadataPath = new Path(path, "rMetadata").toString
val pipelinePath = new Path(path, "pipeline").toString
diff --git a/mllib/src/main/scala/org/apache/spark/ml/r/KMeansWrapper.scala b/mllib/src/main/scala/org/apache/spark/ml/r/KMeansWrapper.scala
index 8d596863b459e..2b239d7a786ce 100644
    *       * a/mllib/src/main/scala/org/apache/spark/ml/r/KMeansWrapper.scala
+++ b/mllib/src/main/scala/org/apache/spark/ml/r/KMeansWrapper.scala
@@ -129,7 +129,7 @@ private[r] object KMeansWrapper extends MLReadable[KMeansWrapper] {

class KMeansWrapperReader extends MLReader[KMeansWrapper] {
  * override def load(path: String): KMeansWrapper = {
+ override protected def loadImpl(path: String): KMeansWrapper = {
implicit val format = DefaultFormats
val rMetadataPath = new Path(path, "rMetadata").toString
val pipelinePath = new Path(path, "pipeline").toString
diff --git a/mllib/src/main/scala/org/apache/spark/ml/r/LDAWrapper.scala b/mllib/src/main/scala/org/apache/spark/ml/r/LDAWrapper.scala
index e096bf1f29f3e..210baec3cb33c 100644
    *       * a/mllib/src/main/scala/org/apache/spark/ml/r/LDAWrapper.scala
+++ b/mllib/src/main/scala/org/apache/spark/ml/r/LDAWrapper.scala
@@ -206,7 +206,7 @@ private[r] object LDAWrapper extends MLReadable[LDAWrapper] {

class LDAWrapperReader extends MLReader[LDAWrapper] {
  * override def load(path: String): LDAWrapper = {
+ override protected def loadImpl(path: String): LDAWrapper = {
implicit val format = DefaultFormats
val rMetadataPath = new Path(path, "rMetadata").toString
val pipelinePath = new Path(path, "pipeline").toString
diff --git a/mllib/src/main/scala/org/apache/spark/ml/r/LinearSVCWrapper.scala b/mllib/src/main/scala/org/apache/spark/ml/r/LinearSVCWrapper.scala
index 7a22a71c3a819..7ec2717f515de 100644
    *       * a/mllib/src/main/scala/org/apache/spark/ml/r/LinearSVCWrapper.scala
+++ b/mllib/src/main/scala/org/apache/spark/ml/r/LinearSVCWrapper.scala
@@ -144,7 +144,7 @@ private[r] object LinearSVCWrapper

class LinearSVCWrapperReader extends MLReader[LinearSVCWrapper] {
  * override def load(path: String): LinearSVCWrapper = {
+ override protected def loadImpl(path: String): LinearSVCWrapper = {
implicit val format = DefaultFormats
val rMetadataPath = new Path(path, "rMetadata").toString
val pipelinePath = new Path(path, "pipeline").toString
diff --git a/mllib/src/main/scala/org/apache/spark/ml/r/LogisticRegressionWrapper.scala b/mllib/src/main/scala/org/apache/spark/ml/r/LogisticRegressionWrapper.scala
index 18acf7d21656f..a7dfcb3953e19 100644
    *       * a/mllib/src/main/scala/org/apache/spark/ml/r/LogisticRegressionWrapper.scala
+++ b/mllib/src/main/scala/org/apache/spark/ml/r/LogisticRegressionWrapper.scala
@@ -199,7 +199,7 @@ private[r] object LogisticRegressionWrapper

class LogisticRegressionWrapperReader extends MLReader[LogisticRegressionWrapper] {
  * override def load(path: String): LogisticRegressionWrapper = {
+ override protected def loadImpl(path: String): LogisticRegressionWrapper = {
implicit val format = DefaultFormats
val rMetadataPath = new Path(path, "rMetadata").toString
val pipelinePath = new Path(path, "pipeline").toString
diff --git a/mllib/src/main/scala/org/apache/spark/ml/r/MultilayerPerceptronClassifierWrapper.scala b/mllib/src/main/scala/org/apache/spark/ml/r/MultilayerPerceptronClassifierWrapper.scala
index 62f642142701b..6ac25957b9c81 100644
    *       * a/mllib/src/main/scala/org/apache/spark/ml/r/MultilayerPerceptronClassifierWrapper.scala
+++ b/mllib/src/main/scala/org/apache/spark/ml/r/MultilayerPerceptronClassifierWrapper.scala
@@ -124,7 +124,7 @@ private[r] object MultilayerPerceptronClassifierWrapper
class MultilayerPerceptronClassifierWrapperReader
extends MLReader[MultilayerPerceptronClassifierWrapper]{

  * override def load(path: String): MultilayerPerceptronClassifierWrapper = {
+ override protected def loadImpl(path: String): MultilayerPerceptronClassifierWrapper = {
implicit val format = DefaultFormats
val pipelinePath = new Path(path, "pipeline").toString

diff --git a/mllib/src/main/scala/org/apache/spark/ml/r/NaiveBayesWrapper.scala b/mllib/src/main/scala/org/apache/spark/ml/r/NaiveBayesWrapper.scala
index fbf9f462ff5f6..e84b1fc297e5e 100644
— a/mllib/src/main/scala/org/apache/spark/ml/r/NaiveBayesWrapper.scala
+++ b/mllib/src/main/scala/org/apache/spark/ml/r/NaiveBayesWrapper.scala
@@ -109,7 +109,7 @@ private[r] object NaiveBayesWrapper extends MLReadable[NaiveBayesWrapper] {
class NaiveBayesWrapperReader extends MLReader[NaiveBayesWrapper] {
  * override def load(path: String): NaiveBayesWrapper = {
+ override protected def loadImpl(path: String): NaiveBayesWrapper = {
implicit val format = DefaultFormats
val rMetadataPath = new Path(path, "rMetadata").toString
val pipelinePath = new Path(path, "pipeline").toString
diff --git a/mllib/src/main/scala/org/apache/spark/ml/r/RWrappers.scala b/mllib/src/main/scala/org/apache/spark/ml/r/RWrappers.scala
index ba6445a730306..7dd93f1420f6f 100644
    *       * a/mllib/src/main/scala/org/apache/spark/ml/r/RWrappers.scala
+++ b/mllib/src/main/scala/org/apache/spark/ml/r/RWrappers.scala
@@ -30,7 +30,7 @@ import org.apache.spark.ml.util.MLReader
*/
private[r] object RWrappers extends MLReader[Object] {

  * override def load(path: String): Object = {
+ override protected def loadImpl(path: String): Object = {
implicit val format = DefaultFormats
val rMetadataPath = new Path(path, "rMetadata").toString
val rMetadataStr = sc.textFile(rMetadataPath, 1).first()
diff --git a/mllib/src/main/scala/org/apache/spark/ml/r/RandomForestClassificationWrapper.scala b/mllib/src/main/scala/org/apache/spark/ml/r/RandomForestClassificationWrapper.scala
index 132345fb9a6d9..c905319ba0ec2 100644
    *       * a/mllib/src/main/scala/org/apache/spark/ml/r/RandomForestClassificationWrapper.scala
+++ b/mllib/src/main/scala/org/apache/spark/ml/r/RandomForestClassificationWrapper.scala
@@ -145,7 +145,7 @@ private[r] object RandomForestClassifierWrapper extends MLReadable[RandomForestC

class RandomForestClassifierWrapperReader extends MLReader[RandomForestClassifierWrapper] {
  * override def load(path: String): RandomForestClassifierWrapper = {
+ override protected def loadImpl(path: String): RandomForestClassifierWrapper = {
implicit val format = DefaultFormats
val rMetadataPath = new Path(path, "rMetadata").toString
val pipelinePath = new Path(path, "pipeline").toString
diff --git a/mllib/src/main/scala/org/apache/spark/ml/r/RandomForestRegressionWrapper.scala b/mllib/src/main/scala/org/apache/spark/ml/r/RandomForestRegressionWrapper.scala
index 038bd79c7022b..1f432da570560 100644
    *       * a/mllib/src/main/scala/org/apache/spark/ml/r/RandomForestRegressionWrapper.scala
+++ b/mllib/src/main/scala/org/apache/spark/ml/r/RandomForestRegressionWrapper.scala
@@ -128,7 +128,7 @@ private[r] object RandomForestRegressorWrapper extends MLReadable[RandomForestRe

class RandomForestRegressorWrapperReader extends MLReader[RandomForestRegressorWrapper] {
  * override def load(path: String): RandomForestRegressorWrapper = {
+ override protected def loadImpl(path: String): RandomForestRegressorWrapper = { implicit val format = DefaultFormats val rMetadataPath = new Path(path, "rMetadata").toString val pipelinePath = new Path(path, "pipeline").toString diff --git a/mllib/src/main/scala/org/apache/spark/ml/recommendation/ALS.scala b/mllib/src/main/scala/org/apache/spark/ml/recommendation/ALS.scala index 50ef4330ddc80..fbcf39dcbe3ba 100644 --- a/mllib/src/main/scala/org/apache/spark/ml/recommendation/ALS.scala +++ b/mllib/src/main/scala/org/apache/spark/ml/recommendation/ALS.scala @@ -303,7 +303,8 @@ class ALSModel private[ml] ( }

@Since("2.0.0")
  * override def transform(dataset: Dataset[_]): DataFrame = {
+ override def transform(dataset: Dataset[_]): DataFrame = super.transform(dataset)
+ override protected def transformImpl(dataset: Dataset[_]): DataFrame = {
transformSchema(dataset.schema)
// create a new column named map(predictionCol) by running the predict UDF.
val predictions = dataset
@@ -519,7 +520,7 @@ object ALSModel extends MLReadable[ALSModel] {
/** Checked against metadata when loading model */
private val className = classOf[ALSModel].getName

  * override def load(path: String): ALSModel = {
+ override protected def loadImpl(path: String): ALSModel = { val metadata = DefaultParamsReader.loadMetadata(path, sc, className) implicit val format = DefaultFormats val rank = (metadata.metadata \ "rank").extract[Int] @@ -655,7 +656,8 @@ class ALS(@Since("1.4.0") override val uid: String) extends Estimator[ALSModel] }

@Since("2.0.0")
  * override def fit(dataset: Dataset[_]): ALSModel = instrumented { instr =>
+ override def fit(dataset: Dataset[_]): ALSModel = super.fit(dataset)
+ override protected def fitImpl(dataset: Dataset[_]): ALSModel = instrumented { instr => transformSchema(dataset.schema) import dataset.sparkSession.implicits._ diff --git a/mllib/src/main/scala/org/apache/spark/ml/regression/AFTSurvivalRegression.scala b/mllib/src/main/scala/org/apache/spark/ml/regression/AFTSurvivalRegression.scala index 8d6e36697d2cc..ebda26e8ffc8e 100644 --- a/mllib/src/main/scala/org/apache/spark/ml/regression/AFTSurvivalRegression.scala +++ b/mllib/src/main/scala/org/apache/spark/ml/regression/AFTSurvivalRegression.scala @@ -211,7 +211,9 @@ class AFTSurvivalRegression @Since("1.6.0") (@Since("1.6.0") override val uid: S }

@Since("2.0.0")
  * override def fit(dataset: Dataset[_]): AFTSurvivalRegressionModel = instrumented { instr =>
+ override def fit(dataset: Dataset[_]): AFTSurvivalRegressionModel = super.fit(dataset)
+ override protected def fitImpl(
+ dataset: Dataset[_]): AFTSurvivalRegressionModel = instrumented { instr => transformSchema(dataset.schema, logging = true) val instances = extractAFTPoints(dataset) val handlePersistence = dataset.storageLevel == StorageLevel.NONE @@ -353,7 +355,8 @@ class AFTSurvivalRegressionModel private[ml] ( }

@Since("2.0.0")
  * override def transform(dataset: Dataset[_]): DataFrame = {
+ override def transform(dataset: Dataset[_]): DataFrame = super.transform(dataset)
+ override protected def transformImpl(dataset: Dataset[_]): DataFrame = {
transformSchema(dataset.schema, logging = true)
val predictUDF = udf { features: Vector => predict(features) }
val predictQuantilesUDF = udf
{ features: Vector => predictQuantiles(features)}
@@ -412,7 +415,7 @@ object AFTSurvivalRegressionModel extends MLReadable[AFTSurvivalRegressionModel]
/** Checked against metadata when loading model */
private val className = classOf[AFTSurvivalRegressionModel].getName

  * override def load(path: String): AFTSurvivalRegressionModel = {
+ override protected def loadImpl(path: String): AFTSurvivalRegressionModel = {
val metadata = DefaultParamsReader.loadMetadata(path, sc, className)

val dataPath = new Path(path, "data").toString
diff --git a/mllib/src/main/scala/org/apache/spark/ml/regression/DecisionTreeRegressor.scala b/mllib/src/main/scala/org/apache/spark/ml/regression/DecisionTreeRegressor.scala
index faadc4d7b4ccc..155c979e28250 100644
— a/mllib/src/main/scala/org/apache/spark/ml/regression/DecisionTreeRegressor.scala
+++ b/mllib/src/main/scala/org/apache/spark/ml/regression/DecisionTreeRegressor.scala
@@ -22,7 +22,7 @@ import org.json4s.
{DefaultFormats, JObject}
import org.json4s.JsonDSL._
import org.apache.spark.annotation.Since
-import org.apache.spark.ml.
{PredictionModel, Predictor}
+import org.apache.spark.ml.
{MLEvents, PredictionModel, Predictor}
import org.apache.spark.ml.feature.LabeledPoint
import org.apache.spark.ml.linalg.Vector
import org.apache.spark.ml.param.ParamMap
@@ -188,7 +188,8 @@ class DecisionTreeRegressionModel private[ml] (
}
@Since("2.0.0")
  * override def transform(dataset: Dataset[_]): DataFrame = {
+ override def transform(
+ dataset: Dataset[_]): DataFrame = MLEvents.withTransformEvent(this, dataset) { transformSchema(dataset.schema, logging = true) transformImpl(dataset) }
@@ -275,7 +276,7 @@ object DecisionTreeRegressionModel extends MLReadable[DecisionTreeRegressionMode
/** Checked against metadata when loading model */
private val className = classOf[DecisionTreeRegressionModel].getName

  * override def load(path: String): DecisionTreeRegressionModel = {
+ override protected def loadImpl(path: String): DecisionTreeRegressionModel = {
implicit val format = DefaultFormats
val metadata = DefaultParamsReader.loadMetadata(path, sc, className)
val numFeatures = (metadata.metadata \ "numFeatures").extract[Int]
diff --git a/mllib/src/main/scala/org/apache/spark/ml/regression/GBTRegressor.scala b/mllib/src/main/scala/org/apache/spark/ml/regression/GBTRegressor.scala
index 9a5b7d59e9aef..befef2737b9bf 100644
    *       * a/mllib/src/main/scala/org/apache/spark/ml/regression/GBTRegressor.scala
+++ b/mllib/src/main/scala/org/apache/spark/ml/regression/GBTRegressor.scala
@@ -337,7 +337,7 @@ object GBTRegressionModel extends MLReadable[GBTRegressionModel] {
private val className = classOf[GBTRegressionModel].getName
private val treeClassName = classOf[DecisionTreeRegressionModel].getName

  * override def load(path: String): GBTRegressionModel = {
+ override protected def loadImpl(path: String): GBTRegressionModel = {
implicit val format = DefaultFormats
val (metadata: Metadata, treesData: Array[(Metadata, Node)], treeWeights: Array[Double]) =
EnsembleModelReadWrite.loadImpl(path, sparkSession, className, treeClassName)
diff --git a/mllib/src/main/scala/org/apache/spark/ml/regression/GeneralizedLinearRegression.scala b/mllib/src/main/scala/org/apache/spark/ml/regression/GeneralizedLinearRegression.scala
index abb60ea205751..648167fe3e012 100644
    *       * a/mllib/src/main/scala/org/apache/spark/ml/regression/GeneralizedLinearRegression.scala
+++ b/mllib/src/main/scala/org/apache/spark/ml/regression/GeneralizedLinearRegression.scala
@@ -26,7 +26,7 @@ import org.apache.hadoop.fs.Path
import org.apache.spark.SparkException
import org.apache.spark.annotation. {Experimental, Since}
import org.apache.spark.internal.Logging
-import org.apache.spark.ml.PredictorParams
+import org.apache.spark.ml.
{MLEvents, PredictorParams}
import org.apache.spark.ml.attribute.AttributeGroup
import org.apache.spark.ml.feature.
{Instance, OffsetInstance}
import org.apache.spark.ml.linalg.
{BLAS, Vector, Vectors}
@@ -1034,7 +1034,8 @@ class GeneralizedLinearRegressionModel private[ml] (
BLAS.dot(features, coefficients) + intercept + offset
}

  * override def transform(dataset: Dataset[_]): DataFrame = {
+ override def transform(
+ dataset: Dataset[_]): DataFrame = MLEvents.withTransformEvent(this, dataset) { transformSchema(dataset.schema) transformImpl(dataset) }
@@ -1140,7 +1141,7 @@ object GeneralizedLinearRegressionModel extends MLReadable[GeneralizedLinearRegr
/** Checked against metadata when loading model */
private val className = classOf[GeneralizedLinearRegressionModel].getName

  * override def load(path: String): GeneralizedLinearRegressionModel = {
+ override protected def loadImpl(path: String): GeneralizedLinearRegressionModel = {
val metadata = DefaultParamsReader.loadMetadata(path, sc, className)

val dataPath = new Path(path, "data").toString
diff --git a/mllib/src/main/scala/org/apache/spark/ml/regression/IsotonicRegression.scala b/mllib/src/main/scala/org/apache/spark/ml/regression/IsotonicRegression.scala
index 8b9233dcdc4d1..422eaf8d4b9b3 100644
— a/mllib/src/main/scala/org/apache/spark/ml/regression/IsotonicRegression.scala
+++ b/mllib/src/main/scala/org/apache/spark/ml/regression/IsotonicRegression.scala
@@ -162,7 +162,9 @@ class IsotonicRegression @Since("1.5.0") (@Since("1.5.0") override val uid: Stri
override def copy(extra: ParamMap): IsotonicRegression = defaultCopy(extra)
@Since("2.0.0")
  * override def fit(dataset: Dataset[_]): IsotonicRegressionModel = instrumented { instr =>
+ override def fit(dataset: Dataset[_]): IsotonicRegressionModel = super.fit(dataset)
+ override protected def fitImpl(
+ dataset: Dataset[_]): IsotonicRegressionModel = instrumented { instr => transformSchema(dataset.schema, logging = true) // Extract columns from data. If dataset is persisted, do not persist oldDataset. val instances = extractWeightedLabeledPoints(dataset) @@ -239,7 +241,8 @@ class IsotonicRegressionModel private[ml] ( }

@Since("2.0.0")
  * override def transform(dataset: Dataset[_]): DataFrame = {
+ override def transform(dataset: Dataset[_]): DataFrame = super.transform(dataset)
+ override protected def transformImpl(dataset: Dataset[_]): DataFrame = {
transformSchema(dataset.schema, logging = true)
val predict = dataset.schema($(featuresCol)).dataType match {
case DoubleType =>
@@ -296,7 +299,7 @@ object IsotonicRegressionModel extends MLReadable[IsotonicRegressionModel] {
/** Checked against metadata when loading model */
private val className = classOf[IsotonicRegressionModel].getName

  * override def load(path: String): IsotonicRegressionModel = {
+ override protected def loadImpl(path: String): IsotonicRegressionModel = {
val metadata = DefaultParamsReader.loadMetadata(path, sc, className)

val dataPath = new Path(path, "data").toString
diff --git a/mllib/src/main/scala/org/apache/spark/ml/regression/LinearRegression.scala b/mllib/src/main/scala/org/apache/spark/ml/regression/LinearRegression.scala
index ce6c12cc368dd..395ebd60c1728 100644
— a/mllib/src/main/scala/org/apache/spark/ml/regression/LinearRegression.scala
+++ b/mllib/src/main/scala/org/apache/spark/ml/regression/LinearRegression.scala
@@ -782,7 +782,7 @@ object LinearRegressionModel extends MLReadable[LinearRegressionModel] {
/** Checked against metadata when loading model */
private val className = classOf[LinearRegressionModel].getName
  * override def load(path: String): LinearRegressionModel = {
+ override protected def loadImpl(path: String): LinearRegressionModel = {
val metadata = DefaultParamsReader.loadMetadata(path, sc, className)

val dataPath = new Path(path, "data").toString
diff --git a/mllib/src/main/scala/org/apache/spark/ml/regression/RandomForestRegressor.scala b/mllib/src/main/scala/org/apache/spark/ml/regression/RandomForestRegressor.scala
index afa9a646412b3..d1132f09d1975 100644
— a/mllib/src/main/scala/org/apache/spark/ml/regression/RandomForestRegressor.scala
+++ b/mllib/src/main/scala/org/apache/spark/ml/regression/RandomForestRegressor.scala
@@ -268,7 +268,7 @@ object RandomForestRegressionModel extends MLReadable[RandomForestRegressionMode
private val className = classOf[RandomForestRegressionModel].getName
private val treeClassName = classOf[DecisionTreeRegressionModel].getName
  * override def load(path: String): RandomForestRegressionModel = {
+ override protected def loadImpl(path: String): RandomForestRegressionModel = {
implicit val format = DefaultFormats
val (metadata: Metadata, treesData: Array[(Metadata, Node)], treeWeights: Array[Double]) =
EnsembleModelReadWrite.loadImpl(path, sparkSession, className, treeClassName)
diff --git a/mllib/src/main/scala/org/apache/spark/ml/tuning/CrossValidator.scala b/mllib/src/main/scala/org/apache/spark/ml/tuning/CrossValidator.scala
index e60a14f976a5c..dd5124a9fd584 100644
    *       * a/mllib/src/main/scala/org/apache/spark/ml/tuning/CrossValidator.scala
+++ b/mllib/src/main/scala/org/apache/spark/ml/tuning/CrossValidator.scala
@@ -119,7 +119,8 @@ class CrossValidator @Since("1.2.0") (@Since("1.4.0") override val uid: String)
def setCollectSubModels(value: Boolean): this.type = set(collectSubModels, value)

@Since("2.0.0")
  * override def fit(dataset: Dataset[_]): CrossValidatorModel = instrumented { instr =>
+ override def fit(dataset: Dataset[_]): CrossValidatorModel = super.fit(dataset)
+ override protected def fitImpl(dataset: Dataset[_]): CrossValidatorModel = instrumented { instr =>
val schema = dataset.schema
transformSchema(schema, logging = true)
val sparkSession = dataset.sparkSession
@@ -226,7 +227,7 @@ object CrossValidator extends MLReadable[CrossValidator] {
/** Checked against metadata when loading model */
private val className = classOf[CrossValidator].getName

  * override def load(path: String): CrossValidator = {
+ override protected def loadImpl(path: String): CrossValidator = {
implicit val format = DefaultFormats

val (metadata, estimator, evaluator, estimatorParamMaps) =
@@ -299,7 +300,8 @@ class CrossValidatorModel private[ml] (
def hasSubModels: Boolean = _subModels.isDefined
@Since("2.0.0")
  * override def transform(dataset: Dataset[_]): DataFrame = {
+ override def transform(dataset: Dataset[_]): DataFrame = super.transform(dataset)
+ override protected def transformImpl(dataset: Dataset[_]): DataFrame = { transformSchema(dataset.schema, logging = true) bestModel.transform(dataset) }
@@ -392,7 +394,10 @@ object CrossValidatorModel extends MLReadable[CrossValidatorModel] {
/** Checked against metadata when loading model */
private val className = classOf[CrossValidatorModel].getName

- override def load(path: String): CrossValidatorModel = {
+ // Explicitly call parent's load. Otherwise, MiMa complains.
+ override def load(path: String): CrossValidatorModel = super.load(path)
+
+ override protected def loadImpl(path: String): CrossValidatorModel = {
implicit val format = DefaultFormats

val (metadata, estimator, evaluator, estimatorParamMaps) =
diff --git a/mllib/src/main/scala/org/apache/spark/ml/tuning/TrainValidationSplit.scala b/mllib/src/main/scala/org/apache/spark/ml/tuning/TrainValidationSplit.scala
index 8b251197afbef..7fc662de85a77 100644
— a/mllib/src/main/scala/org/apache/spark/ml/tuning/TrainValidationSplit.scala
+++ b/mllib/src/main/scala/org/apache/spark/ml/tuning/TrainValidationSplit.scala
@@ -118,7 +118,9 @@ class TrainValidationSplit @Since("1.5.0") (@Since("1.5.0") override val uid: St
def setCollectSubModels(value: Boolean): this.type = set(collectSubModels, value)

@Since("2.0.0")
- override def fit(dataset: Dataset[_]): TrainValidationSplitModel = instrumented { instr =>
+ override def fit(dataset: Dataset[_]): TrainValidationSplitModel = super.fit(dataset)
+ override protected def fitImpl(
+ dataset: Dataset[_]): TrainValidationSplitModel = instrumented { instr =>
val schema = dataset.schema
transformSchema(schema, logging = true)
val est = $(estimator)
@@ -220,7 +222,7 @@ object TrainValidationSplit extends MLReadable[TrainValidationSplit] {
/** Checked against metadata when loading model */
private val className = classOf[TrainValidationSplit].getName

- override def load(path: String): TrainValidationSplit = {
+ override protected def loadImpl(path: String): TrainValidationSplit = {
implicit val format = DefaultFormats

val (metadata, estimator, evaluator, estimatorParamMaps) =
@@ -290,7 +292,8 @@ class TrainValidationSplitModel private[ml] (
def hasSubModels: Boolean = _subModels.isDefined

@Since("2.0.0")
- override def transform(dataset: Dataset[_]): DataFrame = {
+ override def transform(dataset: Dataset[_]): DataFrame = super.transform(dataset)
+ override protected def transformImpl(dataset: Dataset[_]): DataFrame = { transformSchema(dataset.schema, logging = true) bestModel.transform(dataset) }
@@ -380,7 +383,10 @@ object TrainValidationSplitModel extends MLReadable[TrainValidationSplitModel] {
/** Checked against metadata when loading model */
private val className = classOf[TrainValidationSplitModel].getName

  * override def load(path: String): TrainValidationSplitModel = {
+ // Explicitly call parent's load. Otherwise, MiMa complains.
+ override def load(path: String): TrainValidationSplitModel = super.load(path)
+
+ override protected def loadImpl(path: String): TrainValidationSplitModel = {
implicit val format = DefaultFormats

val (metadata, estimator, evaluator, estimatorParamMaps) =
diff --git a/mllib/src/main/scala/org/apache/spark/ml/util/ReadWrite.scala b/mllib/src/main/scala/org/apache/spark/ml/util/ReadWrite.scala
index fbc7be25a5640..0a45fa8e267ed 100644
— a/mllib/src/main/scala/org/apache/spark/ml/util/ReadWrite.scala
+++ b/mllib/src/main/scala/org/apache/spark/ml/util/ReadWrite.scala
@@ -163,7 +163,7 @@ abstract class MLWriter extends BaseReadWrite with Logging {
*/
@Since("1.6.0")
@throws[IOException]("If the input path already exists but overwrite is not enabled.")
  * def save(path: String): Unit = {
+ def save(path: String): Unit = MLEvents.withSaveInstanceEvent(this, path) { new FileSystemOverwrite().handleOverwrite(path, shouldOverwrite, sc) saveImpl(path) }
@@ -329,7 +329,19 @@ abstract class MLReader[T] extends BaseReadWrite {

  * Loads the ML component from the input path.
*/
@Since("1.6.0")

  * def load(path: String): T
+ def load(path: String): T = MLEvents.withLoadInstanceEvent(this, path) { + loadImpl(path) + }
+
+ /**
+ * `load()` handles events and then calls this method. Subclasses should override this
+ * method to implement the actual loading of the instance.
+ */
+ @Since("3.0.0")
+ protected def loadImpl(path: String): T =
{ + // Keep this default body for backward compatibility. + throw new UnsupportedOperationException("loadImpl is not implemented.") + }

// override for Java compatibility
override def session(sparkSession: SparkSession): this.type = super.session(sparkSession)
@@ -467,7 +479,7 @@ private[ml] object DefaultParamsWriter {
*/
private[ml] class DefaultParamsReader[T] extends MLReader[T] {
  * override def load(path: String): T = {
+ override protected def loadImpl(path: String): T = {
val metadata = DefaultParamsReader.loadMetadata(path, sc)
val cls = Utils.classForName(metadata.className)
val instance =
diff --git a/mllib/src/test/scala/org/apache/spark/ml/MLEventsSuite.scala b/mllib/src/test/scala/org/apache/spark/ml/MLEventsSuite.scala
new file mode 100644
index 0000000000000..e63eef870d985
    *       * /dev/null
+++ b/mllib/src/test/scala/org/apache/spark/ml/MLEventsSuite.scala
@@ -0,0 +1,183 @@
+/*
+ * Licensed to the Apache Software Foundation (ASF) under one or more
+ * contributor license agreements. See the NOTICE file distributed with
+ * this work for additional information regarding copyright ownership.
+ * The ASF licenses this file to You under the Apache License, Version 2.0
+ * (the "License"); you may not use this file except in compliance with
+ * the License. You may obtain a copy of the License at
+ *
+ * <http://www.apache.org/licenses/LICENSE-2.0>
+ *
+ * Unless required by applicable law or agreed to in writing, software
+ * distributed under the License is distributed on an "AS IS" BASIS,
+ * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
+ * See the License for the specific language governing permissions and
+ * limitations under the License.
+ */
+
+package org.apache.spark.ml
+
+import scala.collection.mutable
+import scala.concurrent.duration._
+import scala.language.postfixOps
+
+import org.apache.hadoop.fs.Path
+import org.mockito.Matchers. {any, eq => meq}
+import org.mockito.Mockito.when
+import org.scalatest.BeforeAndAfterEach
+import org.scalatest.concurrent.Eventually
+import org.scalatest.mockito.MockitoSugar.mock
+
+import org.apache.spark.SparkFunSuite
+import org.apache.spark.ml.param.ParamMap
+import org.apache.spark.mllib.util.MLlibTestSparkContext
+import org.apache.spark.scheduler.
{SparkListener, SparkListenerEvent}
+import org.apache.spark.sql._
+
+
+class MLEventsSuite
+ extends SparkFunSuite
+ with BeforeAndAfterEach
+ with MLlibTestSparkContext
+ with Eventually {
+
+ private val dirName: String = "pipeline"
+ private val events = mutable.ArrayBuffer.empty[MLEvent]
+ private val listener: SparkListener = new SparkListener
Unknown macro: {+ override def onOtherEvent(event}
+
+ override def beforeAll(): Unit =
{ + super.beforeAll() + spark.sparkContext.addSparkListener(listener) + }
+
+ override def afterEach(): Unit =
Unknown macro: {+ try { + events.clear() + } finally { + super.afterEach() + }+ }
+
+ override def afterAll(): Unit = {
+ try
Unknown macro: {+ if (spark != null) { + spark.sparkContext.removeSparkListener(listener) + }+ }
finally
{ + super.afterAll() + }
+ }
+
+ abstract class MyModel extends Model[MyModel]
+
+ test("pipeline fit events")
Unknown macro: {+ val estimator0 = mock[Estimator[MyModel]]+ val model0 = mock[MyModel]+ val transformer1 = mock[Transformer]+ val estimator2 = mock[Estimator[MyModel]]+ val model2 = mock[MyModel]+ val transformer3 = mock[Transformer]++ when(estimator0.copy(any[ParamMap])).thenReturn(estimator0)+ when(model0.copy(any[ParamMap])).thenReturn(model0)+ when(transformer1.copy(any[ParamMap])).thenReturn(transformer1)+ when(estimator2.copy(any[ParamMap])).thenReturn(estimator2)+ when(model2.copy(any[ParamMap])).thenReturn(model2)+ when(transformer3.copy(any[ParamMap])).thenReturn(transformer3)++ val dataset0 = mock[DataFrame]+ val dataset1 = mock[DataFrame]+ val dataset2 = mock[DataFrame]+ val dataset3 = mock[DataFrame]+ val dataset4 = mock[DataFrame]++ when(dataset0.toDF).thenReturn(dataset0)+ when(dataset1.toDF).thenReturn(dataset1)+ when(dataset2.toDF).thenReturn(dataset2)+ when(dataset3.toDF).thenReturn(dataset3)+ when(dataset4.toDF).thenReturn(dataset4)++ when(estimator0.fit(meq(dataset0))).thenReturn(model0)+ when(model0.transform(meq(dataset0))).thenReturn(dataset1)+ when(model0.parent).thenReturn(estimator0)+ when(transformer1.transform(meq(dataset1))).thenReturn(dataset2)+ when(estimator2.fit(meq(dataset2))).thenReturn(model2)+ when(model2.transform(meq(dataset2))).thenReturn(dataset3)+ when(model2.parent).thenReturn(estimator2)+ when(transformer3.transform(meq(dataset3))).thenReturn(dataset4)++ val pipeline = new Pipeline()+ .setStages(Array(estimator0, transformer1, estimator2, transformer3))+ val pipelineModel = pipeline.fit(dataset0)++ val expected =+ FitStart(pipeline, dataset0) }
+
+ test("pipeline read/write events") {
+ withTempDir
Unknown macro: { dir =>+ val path = new Path(dir.getCanonicalPath, dirName).toUri.toString+ val writableStage = new WritableStage("writableStage")+ val newPipeline = new Pipeline().setStages(Array(writableStage))+ val pipelineWriter = newPipeline.write+ pipelineWriter.save(path)++ val expected =+ SaveInstanceStart(pipelineWriter, path) }
+ }
+}

----------------------------------------------------------------
This is an automated message from the Apache Git Service.
To respond to the message, please log on GitHub and use the
URL above to go to the specific comment.
For queries about this service, please contact Infrastructure at:
users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [12/Dec/18 07:03](https://issues.apache.org/jira/browse/SPARK-23674?focusedCommentId=16718526&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16718526) felixcheung closed pull request #23263: SPARK-23674 [ML] Adds Spark ML Events URL: https://github.com/apache/spark/pull/23263 This is a PR merged from a forked repository. As GitHub hides the original diff on merge, it is displayed below for the sake of provenance: As this is a foreign pull request (from a fork), the diff is supplied below (as it won't show otherwise due to GitHub magic): diff --git a/mllib/src/main/scala/org/apache/spark/ml/Estimator.scala b/mllib/src/main/scala/org/apache/spark/ml/Estimator.scala index 1247882d6c1bd..a3c4db06862f8 100644 — a/mllib/src/main/scala/org/apache/spark/ml/Estimator.scala +++ b/mllib/src/main/scala/org/apache/spark/ml/Estimator.scala @@ -65,7 +65,19 @@ abstract class Estimator[M <: Model [M] ] extends PipelineStage { Fits a model to the input data. */ @Since("2.0.0") def fit(dataset: Dataset [_] ): M + def fit(dataset: Dataset [_] ): M = MLEvents.withFitEvent(this, dataset) { + fitImpl(dataset) + } + + /** + * `fit()` handles events and then calls this method. Subclasses should override this + * method to implement the actual fiting a model to the input data. + */ + @Since("3.0.0") + protected def fitImpl(dataset: Dataset [_] ): M = { + // Keep this default body for backward compatibility. + throw new UnsupportedOperationException("fitImpl is not implemented.") + } /** Fits multiple models to the input data with multiple sets of parameters. diff --git a/mllib/src/main/scala/org/apache/spark/ml/Pipeline.scala b/mllib/src/main/scala/org/apache/spark/ml/Pipeline.scala index 103082b7b9766..1c781faff129e 100644 a/mllib/src/main/scala/org/apache/spark/ml/Pipeline.scala +++ b/mllib/src/main/scala/org/apache/spark/ml/Pipeline.scala @@ -132,7 +132,8 @@ class Pipeline @Since("1.4.0") ( @return fitted pipeline */ @Since("2.0.0") override def fit(dataset: Dataset [_] ): PipelineModel = { + override def fit(dataset: Dataset [_] ): PipelineModel = super.fit(dataset) + override protected def fitImpl(dataset: Dataset [_] ): PipelineModel = { transformSchema(dataset.schema, logging = true) val theStages = $(stages) // Search for the last estimator. @@ -210,7 +211,7 @@ object Pipeline extends MLReadable [Pipeline] { /** Checked against metadata when loading model */ private val className = classOf [Pipeline] .getName override def load(path: String): Pipeline = Unknown macro: {+ override protected def loadImpl(path} @Since("2.0.0") override def transform(dataset: Dataset [_] ): DataFrame = { + override def transform(dataset: Dataset [_] ): DataFrame = super.transform(dataset) + override protected def transformImpl(dataset: Dataset [_] ): DataFrame = { transformSchema(dataset.schema, logging = true) stages.foldLeft(dataset.toDF)((cur, transformer) => transformer.transform(cur)) } @@ -344,7 +346,7 @@ object PipelineModel extends MLReadable [PipelineModel] { /** Checked against metadata when loading model */ private val className = classOf [PipelineModel] .getName override def load(path: String): PipelineModel = { + override protected def loadImpl(path: String): PipelineModel = { val (uid: String, stages: Array [PipelineStage] ) = SharedReadWrite.load(className, sc, path) val transformers = stages map { case stage: Transformer => stage diff --git a/mllib/src/main/scala/org/apache/spark/ml/Predictor.scala b/mllib/src/main/scala/org/apache/spark/ml/Predictor.scala index d8f3dfa874439..3731ddae0160c 100644 a/mllib/src/main/scala/org/apache/spark/ml/Predictor.scala +++ b/mllib/src/main/scala/org/apache/spark/ml/Predictor.scala @@ -94,7 +94,10 @@ abstract class Predictor[ /** @group setParam */ def setPredictionCol(value: String): Learner = set(predictionCol, value).asInstanceOf [Learner] override def fit(dataset: Dataset [_] ): M = { + // Explictly call parent's load. Otherwise, MiMa complains. + override def fit(dataset: Dataset [_] ): M = super.fit(dataset) + + override protected def fitImpl(dataset: Dataset [_] ): M = { // This handles a few items such as schema validation. // Developers only need to implement train(). transformSchema(dataset.schema, logging = true) @@ -199,7 +202,8 @@ abstract class PredictionModel[FeaturesType, M <: PredictionModel[FeaturesType, @param dataset input dataset @return transformed dataset with [ [predictionCol] ] of type `Double` */ override def transform(dataset: Dataset [_] ): DataFrame = { + override def transform( + dataset: Dataset [_] ): DataFrame = MLEvents.withTransformEvent(this, dataset) Unknown macro: { transformSchema(dataset.schema, logging = true) if ($(predictionCol).nonEmpty) { transformImpl(dataset) @@ -210,7 +214,7 @@ abstract class PredictionModel[FeaturesType, M <: PredictionModel[FeaturesType, } } protected def transformImpl(dataset: Dataset [_] ): DataFrame = { + override protected def transformImpl(dataset: Dataset [_] ): DataFrame = { val predictUDF = udf { (features: Any) => predict(features.asInstanceOf[FeaturesType]) } diff --git a/mllib/src/main/scala/org/apache/spark/ml/Transformer.scala b/mllib/src/main/scala/org/apache/spark/ml/Transformer.scala index a3a2b55adc25d..2467383227a66 100644 a/mllib/src/main/scala/org/apache/spark/ml/Transformer.scala +++ b/mllib/src/main/scala/org/apache/spark/ml/Transformer.scala @@ -68,7 +68,19 @@ abstract class Transformer extends PipelineStage { Transforms the input dataset. */ @Since("2.0.0") def transform(dataset: Dataset [_] ): DataFrame + def transform(dataset: Dataset [_] ): DataFrame = MLEvents.withTransformEvent(this, dataset) { + transformImpl(dataset) + } + + /** + * `transform()` handles events and then calls this method. Subclasses should override this + * method to implement the actual transformation. + */ + @Since("3.0.0") + protected def transformImpl(dataset: Dataset [_] ): DataFrame = { + // Keep this default body for backward compatibility. + throw new UnsupportedOperationException("transformImpl is not implemented.") + } override def copy(extra: ParamMap): Transformer } @@ -116,7 +128,7 @@ abstract class UnaryTransformer[IN, OUT, T <: UnaryTransformer [IN, OUT, T] ] StructType(outputFields) } override def transform(dataset: Dataset [_] ): DataFrame = { + override protected def transformImpl(dataset: Dataset [_] ): DataFrame = { transformSchema(dataset.schema, logging = true) val transformUDF = udf(this.createTransformFunc, outputDataType) dataset.withColumn($(outputCol), transformUDF(dataset($(inputCol)))) diff --git a/mllib/src/main/scala/org/apache/spark/ml/classification/Classifier.scala b/mllib/src/main/scala/org/apache/spark/ml/classification/Classifier.scala index 7e5790ab70ee9..4de6ae7990490 100644 a/mllib/src/main/scala/org/apache/spark/ml/classification/Classifier.scala +++ b/mllib/src/main/scala/org/apache/spark/ml/classification/Classifier.scala @@ -19,7 +19,7 @@ package org.apache.spark.ml.classification import org.apache.spark.SparkException import org.apache.spark.annotation. {DeveloperApi, Since} -import org.apache.spark.ml. {PredictionModel, Predictor, PredictorParams} +import org.apache.spark.ml. {MLEvents, PredictionModel, Predictor, PredictorParams} import org.apache.spark.ml.feature.LabeledPoint import org.apache.spark.ml.linalg. {Vector, VectorUDT} import org.apache.spark.ml.param.shared.HasRawPredictionCol @@ -156,7 +156,8 @@ abstract class ClassificationModel[FeaturesType, M <: ClassificationModel[Featur @param dataset input dataset @return transformed dataset */ override def transform(dataset: Dataset [_] ): DataFrame = { + override def transform( + dataset: Dataset [_] ): DataFrame = MLEvents.withTransformEvent(this, dataset) { transformSchema(dataset.schema, logging = true) // Output selected columns only. diff --git a/mllib/src/main/scala/org/apache/spark/ml/classification/DecisionTreeClassifier.scala b/mllib/src/main/scala/org/apache/spark/ml/classification/DecisionTreeClassifier.scala index d9292a5476767..ab91b942a06ce 100644 — a/mllib/src/main/scala/org/apache/spark/ml/classification/DecisionTreeClassifier.scala +++ b/mllib/src/main/scala/org/apache/spark/ml/classification/DecisionTreeClassifier.scala @@ -275,7 +275,7 @@ object DecisionTreeClassificationModel extends MLReadable[DecisionTreeClassifica /** Checked against metadata when loading model */ private val className = classOf [DecisionTreeClassificationModel] .getName override def load(path: String): DecisionTreeClassificationModel = { + override protected def loadImpl(path: String): DecisionTreeClassificationModel = { implicit val format = DefaultFormats val metadata = DefaultParamsReader.loadMetadata(path, sc, className) val numFeatures = (metadata.metadata \ "numFeatures").extract [Int] diff --git a/mllib/src/main/scala/org/apache/spark/ml/classification/GBTClassifier.scala b/mllib/src/main/scala/org/apache/spark/ml/classification/GBTClassifier.scala index abe2d1febfdf8..5f4bac04f16bb 100644 a/mllib/src/main/scala/org/apache/spark/ml/classification/GBTClassifier.scala +++ b/mllib/src/main/scala/org/apache/spark/ml/classification/GBTClassifier.scala @@ -410,7 +410,7 @@ object GBTClassificationModel extends MLReadable [GBTClassificationModel] { private val className = classOf [GBTClassificationModel] .getName private val treeClassName = classOf [DecisionTreeRegressionModel] .getName override def load(path: String): GBTClassificationModel = { + override protected def loadImpl(path: String): GBTClassificationModel = { implicit val format = DefaultFormats val (metadata: Metadata, treesData: Array [(Metadata, Node)] , treeWeights: Array [Double] ) = EnsembleModelReadWrite.loadImpl(path, sparkSession, className, treeClassName) diff --git a/mllib/src/main/scala/org/apache/spark/ml/classification/LinearSVC.scala b/mllib/src/main/scala/org/apache/spark/ml/classification/LinearSVC.scala index ff801abef9a94..b6e9b8833022d 100644 a/mllib/src/main/scala/org/apache/spark/ml/classification/LinearSVC.scala +++ b/mllib/src/main/scala/org/apache/spark/ml/classification/LinearSVC.scala @@ -373,7 +373,7 @@ object LinearSVCModel extends MLReadable [LinearSVCModel] { /** Checked against metadata when loading model */ private val className = classOf [LinearSVCModel] .getName override def load(path: String): LinearSVCModel = { + override protected def loadImpl(path: String): LinearSVCModel = { val metadata = DefaultParamsReader.loadMetadata(path, sc, className) val dataPath = new Path(path, "data").toString val data = sparkSession.read.format("parquet").load(dataPath) diff --git a/mllib/src/main/scala/org/apache/spark/ml/classification/LogisticRegression.scala b/mllib/src/main/scala/org/apache/spark/ml/classification/LogisticRegression.scala index 27a7db0b2f5d4..1367253aa4f9f 100644 a/mllib/src/main/scala/org/apache/spark/ml/classification/LogisticRegression.scala +++ b/mllib/src/main/scala/org/apache/spark/ml/classification/LogisticRegression.scala @@ -1248,7 +1248,7 @@ object LogisticRegressionModel extends MLReadable [LogisticRegressionModel] { /** Checked against metadata when loading model */ private val className = classOf [LogisticRegressionModel] .getName override def load(path: String): LogisticRegressionModel = { + override protected def loadImpl(path: String): LogisticRegressionModel = { val metadata = DefaultParamsReader.loadMetadata(path, sc, className) val (major, minor) = VersionUtils.majorMinorVersion(metadata.sparkVersion) diff --git a/mllib/src/main/scala/org/apache/spark/ml/classification/MultilayerPerceptronClassifier.scala b/mllib/src/main/scala/org/apache/spark/ml/classification/MultilayerPerceptronClassifier.scala index 47b8a8df637b9..a912ad268ba7e 100644 — a/mllib/src/main/scala/org/apache/spark/ml/classification/MultilayerPerceptronClassifier.scala +++ b/mllib/src/main/scala/org/apache/spark/ml/classification/MultilayerPerceptronClassifier.scala @@ -359,7 +359,7 @@ object MultilayerPerceptronClassificationModel /** Checked against metadata when loading model */ private val className = classOf [MultilayerPerceptronClassificationModel] .getName override def load(path: String): MultilayerPerceptronClassificationModel = { + override protected def loadImpl(path: String): MultilayerPerceptronClassificationModel = { val metadata = DefaultParamsReader.loadMetadata(path, sc, className) val dataPath = new Path(path, "data").toString diff --git a/mllib/src/main/scala/org/apache/spark/ml/classification/NaiveBayes.scala b/mllib/src/main/scala/org/apache/spark/ml/classification/NaiveBayes.scala index 1a7a5e7a52344..04bb1265962c2 100644 — a/mllib/src/main/scala/org/apache/spark/ml/classification/NaiveBayes.scala +++ b/mllib/src/main/scala/org/apache/spark/ml/classification/NaiveBayes.scala @@ -399,7 +399,7 @@ object NaiveBayesModel extends MLReadable [NaiveBayesModel] { /** Checked against metadata when loading model */ private val className = classOf [NaiveBayesModel] .getName override def load(path: String): NaiveBayesModel = { + override protected def loadImpl(path: String): NaiveBayesModel = { val metadata = DefaultParamsReader.loadMetadata(path, sc, className) val dataPath = new Path(path, "data").toString diff --git a/mllib/src/main/scala/org/apache/spark/ml/classification/OneVsRest.scala b/mllib/src/main/scala/org/apache/spark/ml/classification/OneVsRest.scala index e1fceb1fc96a4..6b0a4d0832007 100644 --- a/mllib/src/main/scala/org/apache/spark/ml/classification/OneVsRest.scala +++ b/mllib/src/main/scala/org/apache/spark/ml/classification/OneVsRest.scala @@ -165,7 +165,8 @@ final class OneVsRestModel private[ml] ( } @Since("2.0.0") override def transform(dataset: Dataset [_] ): DataFrame = { + override def transform(dataset: Dataset [_] ): DataFrame = super.transform(dataset) + override protected def transformImpl(dataset: Dataset [_] ): DataFrame = { // Check schema transformSchema(dataset.schema, logging = true) @@ -289,7 +290,7 @@ object OneVsRestModel extends MLReadable [OneVsRestModel] { /** Checked against metadata when loading model */ private val className = classOf [OneVsRestModel] .getName override def load(path: String): OneVsRestModel = { + override protected def loadImpl(path: String): OneVsRestModel = { implicit val format = DefaultFormats val (metadata, classifier) = OneVsRestParams.loadImpl(path, sc, className) val labelMetadata = Metadata.fromJson((metadata.metadata \ "labelMetadata").extract[String]) @@ -372,7 +373,8 @@ final class OneVsRest @Since("1.4.0") ( } @Since("2.0.0") override def fit(dataset: Dataset [_] ): OneVsRestModel = instrumented { instr => + override def fit(dataset: Dataset [_] ): OneVsRestModel = super.fit(dataset) + override protected def fitImpl(dataset: Dataset [_] ): OneVsRestModel = instrumented { instr => transformSchema(dataset.schema) instr.logPipelineStage(this) @@ -492,7 +494,7 @@ object OneVsRest extends MLReadable [OneVsRest] { /** Checked against metadata when loading model */ private val className = classOf [OneVsRest] .getName override def load(path: String): OneVsRest = { + override protected def loadImpl(path: String): OneVsRest = { val (metadata, classifier) = OneVsRestParams.loadImpl(path, sc, className) val ovr = new OneVsRest(metadata.uid) metadata.getAndSetParams(ovr) diff --git a/mllib/src/main/scala/org/apache/spark/ml/classification/ProbabilisticClassifier.scala b/mllib/src/main/scala/org/apache/spark/ml/classification/ProbabilisticClassifier.scala index 730fcab333e11..24781005682dd 100644 a/mllib/src/main/scala/org/apache/spark/ml/classification/ProbabilisticClassifier.scala +++ b/mllib/src/main/scala/org/apache/spark/ml/classification/ProbabilisticClassifier.scala @@ -18,6 +18,7 @@ package org.apache.spark.ml.classification import org.apache.spark.annotation.DeveloperApi +import org.apache.spark.ml.MLEvents import org.apache.spark.ml.linalg. {DenseVector, Vector, VectorUDT} import org.apache.spark.ml.param.shared._ import org.apache.spark.ml.util.SchemaUtils @@ -100,7 +101,8 @@ abstract class ProbabilisticClassificationModel[ @param dataset input dataset @return transformed dataset */ override def transform(dataset: Dataset [_] ): DataFrame = { + override def transform( + dataset: Dataset [_] ): DataFrame = MLEvents.withTransformEvent(this, dataset) { transformSchema(dataset.schema, logging = true) if (isDefined(thresholds)) { require($(thresholds).length == numClasses, this.getClass.getSimpleName + diff --git a/mllib/src/main/scala/org/apache/spark/ml/classification/RandomForestClassifier.scala b/mllib/src/main/scala/org/apache/spark/ml/classification/RandomForestClassifier.scala index 0a3bfd1f85e08..145b73e1816ec 100644 a/mllib/src/main/scala/org/apache/spark/ml/classification/RandomForestClassifier.scala +++ b/mllib/src/main/scala/org/apache/spark/ml/classification/RandomForestClassifier.scala @@ -310,7 +310,7 @@ object RandomForestClassificationModel extends MLReadable[RandomForestClassifica private val className = classOf [RandomForestClassificationModel] .getName private val treeClassName = classOf [DecisionTreeClassificationModel] .getName override def load(path: String): RandomForestClassificationModel = { + override protected def loadImpl(path: String): RandomForestClassificationModel = { implicit val format = DefaultFormats val (metadata: Metadata, treesData: Array [(Metadata, Node)] , _) = EnsembleModelReadWrite.loadImpl(path, sparkSession, className, treeClassName) diff --git a/mllib/src/main/scala/org/apache/spark/ml/clustering/BisectingKMeans.scala b/mllib/src/main/scala/org/apache/spark/ml/clustering/BisectingKMeans.scala index 1a94aefa3f563..b4c1246e780f2 100644 a/mllib/src/main/scala/org/apache/spark/ml/clustering/BisectingKMeans.scala +++ b/mllib/src/main/scala/org/apache/spark/ml/clustering/BisectingKMeans.scala @@ -105,7 +105,8 @@ class BisectingKMeansModel private [ml] ( def setPredictionCol(value: String): this.type = set(predictionCol, value) @Since("2.0.0") override def transform(dataset: Dataset [_] ): DataFrame = { + override def transform(dataset: Dataset [_] ): DataFrame = super.transform(dataset) + override protected def transformImpl(dataset: Dataset [_] ): DataFrame = { transformSchema(dataset.schema, logging = true) val predictUDF = udf((vector: Vector) => predict(vector)) dataset.withColumn($(predictionCol), @@ -191,7 +192,7 @@ object BisectingKMeansModel extends MLReadable [BisectingKMeansModel] { /** Checked against metadata when loading model */ private val className = classOf [BisectingKMeansModel] .getName override def load(path: String): BisectingKMeansModel = { + override protected def loadImpl(path: String): BisectingKMeansModel = { val metadata = DefaultParamsReader.loadMetadata(path, sc, className) val dataPath = new Path(path, "data").toString val mllibModel = MLlibBisectingKMeansModel.load(sc, dataPath) @@ -261,7 +262,9 @@ class BisectingKMeans @Since("2.0.0") ( def setDistanceMeasure(value: String): this.type = set(distanceMeasure, value) @Since("2.0.0") override def fit(dataset: Dataset [_] ): BisectingKMeansModel = instrumented { instr => + override def fit(dataset: Dataset [_] ): BisectingKMeansModel = super.fit(dataset) + override protected def fitImpl( + dataset: Dataset [_] ): BisectingKMeansModel = instrumented { instr => transformSchema(dataset.schema, logging = true) val rdd = DatasetUtils.columnToOldVector(dataset, getFeaturesCol) diff --git a/mllib/src/main/scala/org/apache/spark/ml/clustering/GaussianMixture.scala b/mllib/src/main/scala/org/apache/spark/ml/clustering/GaussianMixture.scala index 88abc1605d69f..4908f03574d14 100644 --- a/mllib/src/main/scala/org/apache/spark/ml/clustering/GaussianMixture.scala +++ b/mllib/src/main/scala/org/apache/spark/ml/clustering/GaussianMixture.scala @@ -106,7 +106,8 @@ class GaussianMixtureModel private[ml] ( } @Since("2.0.0") override def transform(dataset: Dataset [_] ): DataFrame = { + override def transform(dataset: Dataset [_] ): DataFrame = super.transform(dataset) + override protected def transformImpl(dataset: Dataset [_] ): DataFrame = { transformSchema(dataset.schema, logging = true) val predUDF = udf((vector: Vector) => predict(vector)) val probUDF = udf((vector: Vector) => predictProbability(vector)) @@ -218,7 +219,7 @@ object GaussianMixtureModel extends MLReadable [GaussianMixtureModel] { /** Checked against metadata when loading model */ private val className = classOf [GaussianMixtureModel] .getName override def load(path: String): GaussianMixtureModel = { + override protected def loadImpl(path: String): GaussianMixtureModel = { val metadata = DefaultParamsReader.loadMetadata(path, sc, className) val dataPath = new Path(path, "data").toString @@ -336,7 +337,9 @@ class GaussianMixture @Since("2.0.0") ( private val numSamples = 5 @Since("2.0.0") override def fit(dataset: Dataset [_] ): GaussianMixtureModel = instrumented { instr => + override def fit(dataset: Dataset [_] ): GaussianMixtureModel = super.fit(dataset) + override protected def fitImpl( + dataset: Dataset [_] ): GaussianMixtureModel = instrumented { instr => transformSchema(dataset.schema, logging = true) val sc = dataset.sparkSession.sparkContext diff --git a/mllib/src/main/scala/org/apache/spark/ml/clustering/KMeans.scala b/mllib/src/main/scala/org/apache/spark/ml/clustering/KMeans.scala index 2eed84d51782a..1c8a17c04f99e 100644 — a/mllib/src/main/scala/org/apache/spark/ml/clustering/KMeans.scala +++ b/mllib/src/main/scala/org/apache/spark/ml/clustering/KMeans.scala @@ -124,7 +124,8 @@ class KMeansModel private [ml] ( def setPredictionCol(value: String): this.type = set(predictionCol, value) @Since("2.0.0") override def transform(dataset: Dataset [_] ): DataFrame = { + override def transform(dataset: Dataset [_] ): DataFrame = super.transform(dataset) + override protected def transformImpl(dataset: Dataset [_] ): DataFrame = { transformSchema(dataset.schema, logging = true) val predictUDF = udf((vector: Vector) => predict(vector)) @@ -238,7 +239,7 @@ object KMeansModel extends MLReadable [KMeansModel] { /** Checked against metadata when loading model */ private val className = classOf [KMeansModel] .getName override def load(path: String): KMeansModel = { + override protected def loadImpl(path: String): KMeansModel = { // Import implicits for Dataset Encoder val sparkSession = super.sparkSession import sparkSession.implicits._ @@ -321,7 +322,8 @@ class KMeans @Since("1.5.0") ( def setSeed(value: Long): this.type = set(seed, value) @Since("2.0.0") override def fit(dataset: Dataset [_] ): KMeansModel = instrumented { instr => + override def fit(dataset: Dataset [_] ): KMeansModel = super.fit(dataset) + override protected def fitImpl(dataset: Dataset [_] ): KMeansModel = instrumented { instr => transformSchema(dataset.schema, logging = true) val handlePersistence = dataset.storageLevel == StorageLevel.NONE diff --git a/mllib/src/main/scala/org/apache/spark/ml/clustering/LDA.scala b/mllib/src/main/scala/org/apache/spark/ml/clustering/LDA.scala index 84e73dc19a392..fde97d57fdb75 100644 — a/mllib/src/main/scala/org/apache/spark/ml/clustering/LDA.scala +++ b/mllib/src/main/scala/org/apache/spark/ml/clustering/LDA.scala @@ -455,7 +455,8 @@ abstract class LDAModel private [ml] ( This implementation may be changed in the future. */ @Since("2.0.0") override def transform(dataset: Dataset [_] ): DataFrame = { + override def transform(dataset: Dataset [_] ): DataFrame = super.transform(dataset) + override protected def transformImpl(dataset: Dataset [_] ): DataFrame = { if ($(topicDistributionCol).nonEmpty) { // TODO: Make the transformer natively in ml framework to avoid extra conversion. @@ -619,7 +620,7 @@ object LocalLDAModel extends MLReadable [LocalLDAModel] { private val className = classOf [LocalLDAModel] .getName override def load(path: String): LocalLDAModel = { + override protected def loadImpl(path: String): LocalLDAModel = { val metadata = DefaultParamsReader.loadMetadata(path, sc, className) val dataPath = new Path(path, "data").toString val data = sparkSession.read.parquet(dataPath) @@ -772,7 +773,7 @@ object DistributedLDAModel extends MLReadable [DistributedLDAModel] { private val className = classOf [DistributedLDAModel] .getName override def load(path: String): DistributedLDAModel = { + override protected def loadImpl(path: String): DistributedLDAModel = { val metadata = DefaultParamsReader.loadMetadata(path, sc, className) val modelPath = new Path(path, "oldModel").toString val oldModel = OldDistributedLDAModel.load(sc, modelPath) @@ -895,7 +896,8 @@ class LDA @Since("1.6.0") ( override def copy(extra: ParamMap): LDA = defaultCopy(extra) @Since("2.0.0") override def fit(dataset: Dataset [_] ): LDAModel = instrumented { instr => + override def fit(dataset: Dataset [_] ): LDAModel = super.fit(dataset) + override protected def fitImpl(dataset: Dataset [_] ): LDAModel = instrumented { instr => transformSchema(dataset.schema, logging = true) instr.logPipelineStage(this) @@ -952,7 +954,7 @@ object LDA extends MLReadable [LDA] { private val className = classOf [LDA] .getName override def load(path: String): LDA = { + override protected def loadImpl(path: String): LDA = { val metadata = DefaultParamsReader.loadMetadata(path, sc, className) val model = new LDA(metadata.uid) LDAParams.getAndSetParams(model, metadata) diff --git a/mllib/src/main/scala/org/apache/spark/ml/events.scala b/mllib/src/main/scala/org/apache/spark/ml/events.scala new file mode 100644 index 0000000000000..fe009394ca081 /dev/null +++ b/mllib/src/main/scala/org/apache/spark/ml/events.scala @@ -0,0 +1,109 @@ +/* + * Licensed to the Apache Software Foundation (ASF) under one or more + * contributor license agreements. See the NOTICE file distributed with + * this work for additional information regarding copyright ownership. + * The ASF licenses this file to You under the Apache License, Version 2.0 + * (the "License"); you may not use this file except in compliance with + * the License. You may obtain a copy of the License at + * + * http://www.apache.org/licenses/LICENSE-2.0 + * + * Unless required by applicable law or agreed to in writing, software + * distributed under the License is distributed on an "AS IS" BASIS, + * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. + * See the License for the specific language governing permissions and + * limitations under the License. + */ + +package org.apache.spark.ml + +import org.apache.spark.SparkContext +import org.apache.spark.annotation.Unstable +import org.apache.spark.ml.util. {MLReader, MLWriter} +import org.apache.spark.scheduler.SparkListenerEvent +import org.apache.spark.sql. {DataFrame, Dataset} + +/** + * Event emitted by ML operations. Events are either fired before and/or + * after each operation (the event should document this). + */ +@Unstable +sealed trait MLEvent extends SparkListenerEvent + +/** + * Event fired before `Transformer.transform`. + */ +@Unstable +case class TransformStart(transformer: Transformer, input: Dataset [_] ) extends MLEvent +/** + * Event fired after `Transformer.transform`. + */ +@Unstable +case class TransformEnd(transformer: Transformer, output: Dataset [_] ) extends MLEvent + +/** + * Event fired before `Estimator.fit`. + */ +@Unstable +case class FitStart[M <: Model [M] ](estimator: Estimator [M] , dataset: Dataset [_] ) extends MLEvent +/** + * Event fired after `Estimator.fit`. + */ +@Unstable +case class FitEnd[M <: Model [M] ](estimator: Estimator [M] , model: M) extends MLEvent + +/** + * Event fired before `MLReader.load`. + */ +@Unstable +case class LoadInstanceStart [T] (reader: MLReader [T] , path: String) extends MLEvent +/** + * Event fired after `MLReader.load`. + */ +@Unstable +case class LoadInstanceEnd [T] (reader: MLReader [T] , instance: T) extends MLEvent + +/** + * Event fired before `MLWriter.save`. + */ +@Unstable +case class SaveInstanceStart(writer: MLWriter, path: String) extends MLEvent +/** + * Event fired after `MLWriter.save`. + */ +@Unstable +case class SaveInstanceEnd(writer: MLWriter, path: String) extends MLEvent + + +private [ml] object MLEvents Unknown macro: {+ private def listenerBus = SparkContext.getOrCreate().listenerBus++ def withFitEvent[M <} diff --git a/mllib/src/main/scala/org/apache/spark/ml/feature/Binarizer.scala b/mllib/src/main/scala/org/apache/spark/ml/feature/Binarizer.scala index 2b0862c60fdf7..3a02b640e359a 100644 a/mllib/src/main/scala/org/apache/spark/ml/feature/Binarizer.scala +++ b/mllib/src/main/scala/org/apache/spark/ml/feature/Binarizer.scala @@ -70,7 +70,8 @@ final class Binarizer @Since("1.4.0") (@Since("1.4.0") override val uid: String) def setOutputCol(value: String): this.type = set(outputCol, value) @Since("2.0.0") override def transform(dataset: Dataset [_] ): DataFrame = { + override def transform(dataset: Dataset [_] ): DataFrame = super.transform(dataset) + override protected def transformImpl(dataset: Dataset [_] ): DataFrame = { val outputSchema = transformSchema(dataset.schema, logging = true) val schema = dataset.schema val inputType = schema($(inputCol)).dataType diff --git a/mllib/src/main/scala/org/apache/spark/ml/feature/BucketedRandomProjectionLSH.scala b/mllib/src/main/scala/org/apache/spark/ml/feature/BucketedRandomProjectionLSH.scala index 0554455a66d7f..f705418432a48 100644 a/mllib/src/main/scala/org/apache/spark/ml/feature/BucketedRandomProjectionLSH.scala +++ b/mllib/src/main/scala/org/apache/spark/ml/feature/BucketedRandomProjectionLSH.scala @@ -225,7 +225,7 @@ object BucketedRandomProjectionLSHModel extends MLReadable[BucketedRandomProject /** Checked against metadata when loading model */ private val className = classOf [BucketedRandomProjectionLSHModel] .getName override def load(path: String): BucketedRandomProjectionLSHModel = { + override protected def loadImpl(path: String): BucketedRandomProjectionLSHModel = { val metadata = DefaultParamsReader.loadMetadata(path, sc, className) val dataPath = new Path(path, "data").toString diff --git a/mllib/src/main/scala/org/apache/spark/ml/feature/Bucketizer.scala b/mllib/src/main/scala/org/apache/spark/ml/feature/Bucketizer.scala index 0b989b0d7d253..eaa9ae8d81c45 100644 — a/mllib/src/main/scala/org/apache/spark/ml/feature/Bucketizer.scala +++ b/mllib/src/main/scala/org/apache/spark/ml/feature/Bucketizer.scala @@ -143,7 +143,8 @@ final class Bucketizer @Since("1.4.0") (@Since("1.4.0") override val uid: String def setOutputCols(value: Array [String] ): this.type = set(outputCols, value) @Since("2.0.0") override def transform(dataset: Dataset [_] ): DataFrame = { + override def transform(dataset: Dataset [_] ): DataFrame = super.transform(dataset) + override protected def transformImpl(dataset: Dataset [_] ): DataFrame = { val transformedSchema = transformSchema(dataset.schema) val (inputColumns, outputColumns) = if (isSet(inputCols)) { diff --git a/mllib/src/main/scala/org/apache/spark/ml/feature/ChiSqSelector.scala b/mllib/src/main/scala/org/apache/spark/ml/feature/ChiSqSelector.scala index dbfb199ccd58f..ba8482d50a9cf 100644 — a/mllib/src/main/scala/org/apache/spark/ml/feature/ChiSqSelector.scala +++ b/mllib/src/main/scala/org/apache/spark/ml/feature/ChiSqSelector.scala @@ -197,7 +197,8 @@ final class ChiSqSelector @Since("1.6.0") (@Since("1.6.0") override val uid: Str def setLabelCol(value: String): this.type = set(labelCol, value) @Since("2.0.0") override def fit(dataset: Dataset [_] ): ChiSqSelectorModel = { + override def fit(dataset: Dataset [_] ): ChiSqSelectorModel = super.fit(dataset) + override protected def fitImpl(dataset: Dataset [_] ): ChiSqSelectorModel = { transformSchema(dataset.schema, logging = true) val input: RDD [OldLabeledPoint] = dataset.select(col($(labelCol)).cast(DoubleType), col($(featuresCol))).rdd.map { @@ -263,7 +264,8 @@ final class ChiSqSelectorModel private [ml] ( def setOutputCol(value: String): this.type = set(outputCol, value) @Since("2.0.0") override def transform(dataset: Dataset [_] ): DataFrame = { + override def transform(dataset: Dataset [_] ): DataFrame = super.transform(dataset) + override protected def transformImpl(dataset: Dataset [_] ): DataFrame = { val transformedSchema = transformSchema(dataset.schema, logging = true) val newField = transformedSchema.last @@ -327,7 +329,7 @@ object ChiSqSelectorModel extends MLReadable [ChiSqSelectorModel] { private val className = classOf [ChiSqSelectorModel] .getName override def load(path: String): ChiSqSelectorModel = { + override protected def loadImpl(path: String): ChiSqSelectorModel = { val metadata = DefaultParamsReader.loadMetadata(path, sc, className) val dataPath = new Path(path, "data").toString val data = sparkSession.read.parquet(dataPath).select("selectedFeatures").head() diff --git a/mllib/src/main/scala/org/apache/spark/ml/feature/CountVectorizer.scala b/mllib/src/main/scala/org/apache/spark/ml/feature/CountVectorizer.scala index dc8eb8261dbe2..a9ea509ada077 100644 a/mllib/src/main/scala/org/apache/spark/ml/feature/CountVectorizer.scala +++ b/mllib/src/main/scala/org/apache/spark/ml/feature/CountVectorizer.scala @@ -181,7 +181,8 @@ class CountVectorizer @Since("1.5.0") (@Since("1.5.0") override val uid: String) def setBinary(value: Boolean): this.type = set(binary, value) @Since("2.0.0") override def fit(dataset: Dataset [_] ): CountVectorizerModel = { + override def fit(dataset: Dataset [_] ): CountVectorizerModel = super.fit(dataset) + override protected def fitImpl(dataset: Dataset [_] ): CountVectorizerModel = { transformSchema(dataset.schema, logging = true) val vocSize = $(vocabSize) val input = dataset.select($(inputCol)).rdd.map(_.getAs[Seq [String] ](0)) @@ -291,7 +292,8 @@ class CountVectorizerModel( private var broadcastDict: Option[Broadcast[Map [String, Int] ]] = None @Since("2.0.0") override def transform(dataset: Dataset [_] ): DataFrame = { + override def transform(dataset: Dataset [_] ): DataFrame = super.transform(dataset) + override protected def transformImpl(dataset: Dataset [_] ): DataFrame = { transformSchema(dataset.schema, logging = true) if (broadcastDict.isEmpty) { val dict = vocabulary.zipWithIndex.toMap @@ -358,7 +360,7 @@ object CountVectorizerModel extends MLReadable [CountVectorizerModel] { private val className = classOf [CountVectorizerModel] .getName override def load(path: String): CountVectorizerModel = { + override protected def loadImpl(path: String): CountVectorizerModel = { val metadata = DefaultParamsReader.loadMetadata(path, sc, className) val dataPath = new Path(path, "data").toString val data = sparkSession.read.parquet(dataPath) diff --git a/mllib/src/main/scala/org/apache/spark/ml/feature/FeatureHasher.scala b/mllib/src/main/scala/org/apache/spark/ml/feature/FeatureHasher.scala index dc18e1d34880a..a58a1ff8e053c 100644 a/mllib/src/main/scala/org/apache/spark/ml/feature/FeatureHasher.scala +++ b/mllib/src/main/scala/org/apache/spark/ml/feature/FeatureHasher.scala @@ -140,7 +140,8 @@ class FeatureHasher(@Since("2.3.0") override val uid: String) extends Transforme def setCategoricalCols(value: Array [String] ): this.type = set(categoricalCols, value) @Since("2.3.0") override def transform(dataset: Dataset [_] ): DataFrame = { + override def transform(dataset: Dataset [_] ): DataFrame = super.transform(dataset) + override protected def transformImpl(dataset: Dataset [_] ): DataFrame = { val hashFunc: Any => Int = FeatureHasher.murmur3Hash val n = $(numFeatures) val localInputCols = $(inputCols) diff --git a/mllib/src/main/scala/org/apache/spark/ml/feature/HashingTF.scala b/mllib/src/main/scala/org/apache/spark/ml/feature/HashingTF.scala index dbda5b8d8fd4a..57b6bb1dbe432 100644 a/mllib/src/main/scala/org/apache/spark/ml/feature/HashingTF.scala +++ b/mllib/src/main/scala/org/apache/spark/ml/feature/HashingTF.scala @@ -91,7 +91,8 @@ class HashingTF @Since("1.4.0") (@Since("1.4.0") override val uid: String) def setBinary(value: Boolean): this.type = set(binary, value) @Since("2.0.0") override def transform(dataset: Dataset [_] ): DataFrame = { + override def transform(dataset: Dataset [_] ): DataFrame = super.transform(dataset) + override protected def transformImpl(dataset: Dataset [_] ): DataFrame = { val outputSchema = transformSchema(dataset.schema) val hashingTF = new feature.HashingTF($(numFeatures)).setBinary($(binary)) // TODO: Make the hashingTF.transform natively in ml framework to avoid extra conversion. diff --git a/mllib/src/main/scala/org/apache/spark/ml/feature/IDF.scala b/mllib/src/main/scala/org/apache/spark/ml/feature/IDF.scala index 58897cca4e5c6..9c91cc0417e48 100644 a/mllib/src/main/scala/org/apache/spark/ml/feature/IDF.scala +++ b/mllib/src/main/scala/org/apache/spark/ml/feature/IDF.scala @@ -84,7 +84,8 @@ final class IDF @Since("1.4.0") (@Since("1.4.0") override val uid: String) def setMinDocFreq(value: Int): this.type = set(minDocFreq, value) @Since("2.0.0") override def fit(dataset: Dataset [_] ): IDFModel = { + override def fit(dataset: Dataset [_] ): IDFModel = super.fit(dataset) + override protected def fitImpl(dataset: Dataset [_] ): IDFModel = { transformSchema(dataset.schema, logging = true) val input: RDD [OldVector] = dataset.select($(inputCol)).rdd.map { case Row(v: Vector) => OldVectors.fromML(v) @@ -129,7 +130,8 @@ class IDFModel private [ml] ( def setOutputCol(value: String): this.type = set(outputCol, value) @Since("2.0.0") override def transform(dataset: Dataset [_] ): DataFrame = { + override def transform(dataset: Dataset [_] ): DataFrame = super.transform(dataset) + override protected def transformImpl(dataset: Dataset [_] ): DataFrame = { transformSchema(dataset.schema, logging = true) // TODO: Make the idfModel.transform natively in ml framework to avoid extra conversion. val idf = udf { vec: Vector => idfModel.transform(OldVectors.fromML(vec)).asML } @@ -174,7 +176,7 @@ object IDFModel extends MLReadable [IDFModel] { private val className = classOf [IDFModel] .getName override def load(path: String): IDFModel = { + override protected def loadImpl(path: String): IDFModel = { val metadata = DefaultParamsReader.loadMetadata(path, sc, className) val dataPath = new Path(path, "data").toString val data = sparkSession.read.parquet(dataPath) diff --git a/mllib/src/main/scala/org/apache/spark/ml/feature/Imputer.scala b/mllib/src/main/scala/org/apache/spark/ml/feature/Imputer.scala index 1c074e204ad99..761947a7c394c 100644 a/mllib/src/main/scala/org/apache/spark/ml/feature/Imputer.scala +++ b/mllib/src/main/scala/org/apache/spark/ml/feature/Imputer.scala @@ -120,7 +120,10 @@ class Imputer @Since("2.2.0") (@Since("2.2.0") override val uid: String) setDefault(strategy -> Imputer.mean, missingValue -> Double.NaN) override def fit(dataset: Dataset [_] ): ImputerModel = { + // Explicitly call parent's load. Otherwise, MiMa complains. + override def fit(dataset: Dataset [_] ): ImputerModel = super.fit(dataset) + + override protected def fitImpl(dataset: Dataset [_] ): ImputerModel = { transformSchema(dataset.schema, logging = true) val spark = dataset.sparkSession @@ -211,7 +214,7 @@ class ImputerModel private [ml] ( /** @group setParam */ def setOutputCols(value: Array [String] ): this.type = set(outputCols, value) override def transform(dataset: Dataset [_] ): DataFrame = { + override protected def transformImpl(dataset: Dataset [_] ): DataFrame = { transformSchema(dataset.schema, logging = true) val surrogates = surrogateDF.select($(inputCols).map(col): _*).head().toSeq @@ -257,7 +260,7 @@ object ImputerModel extends MLReadable [ImputerModel] { private val className = classOf [ImputerModel] .getName override def load(path: String): ImputerModel = { + override protected def loadImpl(path: String): ImputerModel = { val metadata = DefaultParamsReader.loadMetadata(path, sc, className) val dataPath = new Path(path, "data").toString val surrogateDF = sqlContext.read.parquet(dataPath) diff --git a/mllib/src/main/scala/org/apache/spark/ml/feature/Interaction.scala b/mllib/src/main/scala/org/apache/spark/ml/feature/Interaction.scala index 611f1b691b782..319927e9dd228 100644 --- a/mllib/src/main/scala/org/apache/spark/ml/feature/Interaction.scala +++ b/mllib/src/main/scala/org/apache/spark/ml/feature/Interaction.scala @@ -67,7 +67,8 @@ class Interaction @Since("1.6.0") (@Since("1.6.0") override val uid: String) ext } @Since("2.0.0") override def transform(dataset: Dataset [_] ): DataFrame = { + override def transform(dataset: Dataset [_] ): DataFrame = super.transform(dataset) + override protected def transformImpl(dataset: Dataset [_] ): DataFrame = { transformSchema(dataset.schema, logging = true) val inputFeatures = $(inputCols).map(c => dataset.schema(c)) val featureEncoders = getFeatureEncoders(inputFeatures) diff --git a/mllib/src/main/scala/org/apache/spark/ml/feature/LSH.scala b/mllib/src/main/scala/org/apache/spark/ml/feature/LSH.scala index b20852383a6ff..b7cc016ebcaf1 100644 a/mllib/src/main/scala/org/apache/spark/ml/feature/LSH.scala +++ b/mllib/src/main/scala/org/apache/spark/ml/feature/LSH.scala @@ -95,7 +95,7 @@ private [ml] abstract class LSHModel[T <: LSHModel [T] ] */ protected [ml] def hashDistance(x: Seq [Vector] , y: Seq [Vector] ): Double override def transform(dataset: Dataset [_] ): DataFrame = { + override protected def transformImpl(dataset: Dataset [_] ): DataFrame = { transformSchema(dataset.schema, logging = true) val transformUDF = udf(hashFunction(_: Vector), DataTypes.createArrayType(new VectorUDT)) dataset.withColumn($(outputCol), transformUDF(dataset($(inputCol)))) @@ -323,7 +323,7 @@ private [ml] abstract class LSH[T <: LSHModel [T] ] */ protected [this] def createRawLSHModel(inputDim: Int): T override def fit(dataset: Dataset [_] ): T = { + override protected def fitImpl(dataset: Dataset [_] ): T = { transformSchema(dataset.schema, logging = true) val inputDim = dataset.select(col($(inputCol))).head().get(0).asInstanceOf [Vector] .size val model = createRawLSHModel(inputDim).setParent(this) diff --git a/mllib/src/main/scala/org/apache/spark/ml/feature/MaxAbsScaler.scala b/mllib/src/main/scala/org/apache/spark/ml/feature/MaxAbsScaler.scala index 90eceb0d61b40..295d3d0ccab3d 100644 a/mllib/src/main/scala/org/apache/spark/ml/feature/MaxAbsScaler.scala +++ b/mllib/src/main/scala/org/apache/spark/ml/feature/MaxAbsScaler.scala @@ -68,7 +68,8 @@ class MaxAbsScaler @Since("2.0.0") (@Since("2.0.0") override val uid: String) def setOutputCol(value: String): this.type = set(outputCol, value) @Since("2.0.0") override def fit(dataset: Dataset [_] ): MaxAbsScalerModel = { + override def fit(dataset: Dataset [_] ): MaxAbsScalerModel = super.fit(dataset) + override protected def fitImpl(dataset: Dataset [_] ): MaxAbsScalerModel = { transformSchema(dataset.schema, logging = true) val input: RDD [OldVector] = dataset.select($(inputCol)).rdd.map { case Row(v: Vector) => OldVectors.fromML(v) @@ -119,7 +120,8 @@ class MaxAbsScalerModel private [ml] ( def setOutputCol(value: String): this.type = set(outputCol, value) @Since("2.0.0") override def transform(dataset: Dataset [_] ): DataFrame = { + override def transform(dataset: Dataset [_] ): DataFrame = super.transform(dataset) + override protected def transformImpl(dataset: Dataset [_] ): DataFrame = { transformSchema(dataset.schema, logging = true) // TODO: this looks hack, we may have to handle sparse and dense vectors separately. val maxAbsUnzero = Vectors.dense(maxAbs.toArray.map(x => if (x == 0) 1 else x)) @@ -165,7 +167,7 @@ object MaxAbsScalerModel extends MLReadable [MaxAbsScalerModel] { private val className = classOf [MaxAbsScalerModel] .getName override def load(path: String): MaxAbsScalerModel = { + override protected def loadImpl(path: String): MaxAbsScalerModel = { val metadata = DefaultParamsReader.loadMetadata(path, sc, className) val dataPath = new Path(path, "data").toString val Row(maxAbs: Vector) = sparkSession.read.parquet(dataPath) diff --git a/mllib/src/main/scala/org/apache/spark/ml/feature/MinHashLSH.scala b/mllib/src/main/scala/org/apache/spark/ml/feature/MinHashLSH.scala index 21cde66d8db6b..168accb1a1722 100644 a/mllib/src/main/scala/org/apache/spark/ml/feature/MinHashLSH.scala +++ b/mllib/src/main/scala/org/apache/spark/ml/feature/MinHashLSH.scala @@ -194,7 +194,7 @@ object MinHashLSHModel extends MLReadable [MinHashLSHModel] { /** Checked against metadata when loading model */ private val className = classOf [MinHashLSHModel] .getName override def load(path: String): MinHashLSHModel = { + override protected def loadImpl(path: String): MinHashLSHModel = { val metadata = DefaultParamsReader.loadMetadata(path, sc, className) val dataPath = new Path(path, "data").toString diff --git a/mllib/src/main/scala/org/apache/spark/ml/feature/MinMaxScaler.scala b/mllib/src/main/scala/org/apache/spark/ml/feature/MinMaxScaler.scala index 2e0ae4af66f06..d76fc5ec05c52 100644 — a/mllib/src/main/scala/org/apache/spark/ml/feature/MinMaxScaler.scala +++ b/mllib/src/main/scala/org/apache/spark/ml/feature/MinMaxScaler.scala @@ -115,7 +115,8 @@ class MinMaxScaler @Since("1.5.0") (@Since("1.5.0") override val uid: String) def setMax(value: Double): this.type = set(max, value) @Since("2.0.0") override def fit(dataset: Dataset [_] ): MinMaxScalerModel = { + override def fit(dataset: Dataset [_] ): MinMaxScalerModel = super.fit(dataset) + override protected def fitImpl(dataset: Dataset [_] ): MinMaxScalerModel = { transformSchema(dataset.schema, logging = true) val input: RDD [OldVector] = dataset.select($(inputCol)).rdd.map { case Row(v: Vector) => OldVectors.fromML(v) @@ -174,7 +175,8 @@ class MinMaxScalerModel private [ml] ( def setMax(value: Double): this.type = set(max, value) @Since("2.0.0") override def transform(dataset: Dataset [_] ): DataFrame = { + override def transform(dataset: Dataset [_] ): DataFrame = super.transform(dataset) + override protected def transformImpl(dataset: Dataset [_] ): DataFrame = { transformSchema(dataset.schema, logging = true) val originalRange = (originalMax.asBreeze - originalMin.asBreeze).toArray val minArray = originalMin.toArray @@ -234,7 +236,7 @@ object MinMaxScalerModel extends MLReadable [MinMaxScalerModel] { private val className = classOf [MinMaxScalerModel] .getName override def load(path: String): MinMaxScalerModel = { + override protected def loadImpl(path: String): MinMaxScalerModel = { val metadata = DefaultParamsReader.loadMetadata(path, sc, className) val dataPath = new Path(path, "data").toString val data = sparkSession.read.parquet(dataPath) diff --git a/mllib/src/main/scala/org/apache/spark/ml/feature/OneHotEncoder.scala b/mllib/src/main/scala/org/apache/spark/ml/feature/OneHotEncoder.scala index ec9792cbbda8f..4e4a259c95cce 100644 --- a/mllib/src/main/scala/org/apache/spark/ml/feature/OneHotEncoder.scala +++ b/mllib/src/main/scala/org/apache/spark/ml/feature/OneHotEncoder.scala @@ -147,7 +147,8 @@ class OneHotEncoder @Since("3.0.0") (@Since("3.0.0") override val uid: String) } @Since("3.0.0") override def fit(dataset: Dataset [_] ): OneHotEncoderModel = { + override def fit(dataset: Dataset [_] ): OneHotEncoderModel = super.fit(dataset) + override protected def fitImpl(dataset: Dataset [_] ): OneHotEncoderModel = { transformSchema(dataset.schema) // Compute the plain number of categories without `handleInvalid` and @@ -324,7 +325,8 @@ class OneHotEncoderModel private[ml] ( } @Since("3.0.0") override def transform(dataset: Dataset [_] ): DataFrame = { + override def transform(dataset: Dataset [_] ): DataFrame = super.transform(dataset) + override protected def transformImpl(dataset: Dataset [_] ): DataFrame = { val transformedSchema = transformSchema(dataset.schema, logging = true) val keepInvalid = $(handleInvalid) == OneHotEncoder.KEEP_INVALID @@ -378,7 +380,7 @@ object OneHotEncoderModel extends MLReadable [OneHotEncoderModel] { private val className = classOf [OneHotEncoderModel] .getName override def load(path: String): OneHotEncoderModel = { + override protected def loadImpl(path: String): OneHotEncoderModel = { val metadata = DefaultParamsReader.loadMetadata(path, sc, className) val dataPath = new Path(path, "data").toString val data = sparkSession.read.parquet(dataPath) diff --git a/mllib/src/main/scala/org/apache/spark/ml/feature/PCA.scala b/mllib/src/main/scala/org/apache/spark/ml/feature/PCA.scala index 8172491a517d1..0a79b49b984c3 100644 a/mllib/src/main/scala/org/apache/spark/ml/feature/PCA.scala +++ b/mllib/src/main/scala/org/apache/spark/ml/feature/PCA.scala @@ -90,7 +90,8 @@ class PCA @Since("1.5.0") ( Computes a [ [PCAModel] ] that contains the principal components of the input vectors. */ @Since("2.0.0") override def fit(dataset: Dataset [_] ): PCAModel = { + override def fit(dataset: Dataset [_] ): PCAModel = super.fit(dataset) + override protected def fitImpl(dataset: Dataset [_] ): PCAModel = { transformSchema(dataset.schema, logging = true) val input: RDD [OldVector] = dataset.select($(inputCol)).rdd.map { case Row(v: Vector) => OldVectors.fromML(v) @@ -147,7 +148,8 @@ class PCAModel private [ml] ( to `PCA.fit()`. */ @Since("2.0.0") override def transform(dataset: Dataset [_] ): DataFrame = { + override def transform(dataset: Dataset [_] ): DataFrame = super.transform(dataset) + override protected def transformImpl(dataset: Dataset [_] ): DataFrame = { transformSchema(dataset.schema, logging = true) val pcaModel = new feature.PCAModel($(k), OldMatrices.fromML(pc).asInstanceOf [OldDenseMatrix] , @@ -203,7 +205,7 @@ object PCAModel extends MLReadable [PCAModel] { @param path path to serialized model data @return a [ [PCAModel] ] */ override def load(path: String): PCAModel = { + override protected def loadImpl(path: String): PCAModel = { val metadata = DefaultParamsReader.loadMetadata(path, sc, className) val dataPath = new Path(path, "data").toString diff --git a/mllib/src/main/scala/org/apache/spark/ml/feature/QuantileDiscretizer.scala b/mllib/src/main/scala/org/apache/spark/ml/feature/QuantileDiscretizer.scala index 5bfaa3b7f3f52..0f29ae9687c02 100644 --- a/mllib/src/main/scala/org/apache/spark/ml/feature/QuantileDiscretizer.scala +++ b/mllib/src/main/scala/org/apache/spark/ml/feature/QuantileDiscretizer.scala @@ -199,7 +199,8 @@ final class QuantileDiscretizer @Since("1.6.0") (@Since("1.6.0") override val ui } @Since("2.0.0") override def fit(dataset: Dataset [_] ): Bucketizer = { + override def fit(dataset: Dataset [_] ): Bucketizer = super.fit(dataset) + override protected def fitImpl(dataset: Dataset [_] ): Bucketizer = { transformSchema(dataset.schema, logging = true) val bucketizer = new Bucketizer(uid).setHandleInvalid($(handleInvalid)) if (isSet(inputCols)) { diff --git a/mllib/src/main/scala/org/apache/spark/ml/feature/RFormula.scala b/mllib/src/main/scala/org/apache/spark/ml/feature/RFormula.scala index d7eb13772aa64..f5132f09f95f4 100644 --- a/mllib/src/main/scala/org/apache/spark/ml/feature/RFormula.scala +++ b/mllib/src/main/scala/org/apache/spark/ml/feature/RFormula.scala @@ -193,7 +193,8 @@ class RFormula @Since("1.5.0") (@Since("1.5.0") override val uid: String) } @Since("2.0.0") override def fit(dataset: Dataset [_] ): RFormulaModel = { + override def fit(dataset: Dataset [_] ): RFormulaModel = super.fit(dataset) + override protected def fitImpl(dataset: Dataset [_] ): RFormulaModel = { transformSchema(dataset.schema, logging = true) require(isDefined(formula), "Formula must be defined first.") val parsedFormula = RFormulaParser.parse($(formula)) @@ -338,7 +339,8 @@ class RFormulaModel private [feature] ( extends Model [RFormulaModel] with RFormulaBase with MLWritable { @Since("2.0.0") override def transform(dataset: Dataset [_] ): DataFrame = { + override def transform(dataset: Dataset [_] ): DataFrame = super.transform(dataset) + override protected def transformImpl(dataset: Dataset [_] ): DataFrame = { checkCanTransform(dataset.schema) transformLabel(pipelineModel.transform(dataset)) } @@ -431,7 +433,7 @@ object RFormulaModel extends MLReadable [RFormulaModel] { /** Checked against metadata when loading model */ private val className = classOf [RFormulaModel] .getName override def load(path: String): RFormulaModel = { + override protected def loadImpl(path: String): RFormulaModel = { val metadata = DefaultParamsReader.loadMetadata(path, sc, className) val dataPath = new Path(path, "data").toString @@ -462,7 +464,7 @@ private class ColumnPruner(override val uid: String, val columnsToPrune: Set[Str def this(columnsToPrune: Set [String] ) = this(Identifiable.randomUID("columnPruner"), columnsToPrune) override def transform(dataset: Dataset [_] ): DataFrame = { + override protected def transformImpl(dataset: Dataset [_] ): DataFrame = { val columnsToKeep = dataset.columns.filter(!columnsToPrune.contains(_)) dataset.select(columnsToKeep.map(dataset.col): _*) } @@ -502,7 +504,7 @@ private object ColumnPruner extends MLReadable [ColumnPruner] { /** Checked against metadata when loading model */ private val className = classOf [ColumnPruner] .getName override def load(path: String): ColumnPruner = { + override protected def loadImpl(path: String): ColumnPruner = { val metadata = DefaultParamsReader.loadMetadata(path, sc, className) val dataPath = new Path(path, "data").toString @@ -535,7 +537,7 @@ private class VectorAttributeRewriter( def this(vectorCol: String, prefixesToRewrite: Map [String, String] ) = this(Identifiable.randomUID("vectorAttrRewriter"), vectorCol, prefixesToRewrite) override def transform(dataset: Dataset [_] ): DataFrame = { + override protected def transformImpl(dataset: Dataset [_] ): DataFrame = { val metadata = { val group = AttributeGroup.fromStructField(dataset.schema(vectorCol)) val attrs = group.attributes.get.map { attr => @@ -593,7 +595,7 @@ private object VectorAttributeRewriter extends MLReadable[VectorAttributeRewrite /** Checked against metadata when loading model */ private val className = classOf [VectorAttributeRewriter] .getName override def load(path: String): VectorAttributeRewriter = { + override protected def loadImpl(path: String): VectorAttributeRewriter = { val metadata = DefaultParamsReader.loadMetadata(path, sc, className) val dataPath = new Path(path, "data").toString diff --git a/mllib/src/main/scala/org/apache/spark/ml/feature/SQLTransformer.scala b/mllib/src/main/scala/org/apache/spark/ml/feature/SQLTransformer.scala index 0fb1d8c5dc579..d453ab3723c0c 100644 — a/mllib/src/main/scala/org/apache/spark/ml/feature/SQLTransformer.scala +++ b/mllib/src/main/scala/org/apache/spark/ml/feature/SQLTransformer.scala @@ -64,7 +64,8 @@ class SQLTransformer @Since("1.6.0") (@Since("1.6.0") override val uid: String) private val tableIdentifier: String = "_ THIS _" @Since("2.0.0") override def transform(dataset: Dataset [_] ): DataFrame = { + override def transform(dataset: Dataset [_] ): DataFrame = super.transform(dataset) + override protected def transformImpl(dataset: Dataset [_] ): DataFrame = { transformSchema(dataset.schema, logging = true) val tableName = Identifiable.randomUID(uid) dataset.createOrReplaceTempView(tableName) diff --git a/mllib/src/main/scala/org/apache/spark/ml/feature/StandardScaler.scala b/mllib/src/main/scala/org/apache/spark/ml/feature/StandardScaler.scala index 91b0707dec3f3..c96726faab4f5 100644 a/mllib/src/main/scala/org/apache/spark/ml/feature/StandardScaler.scala +++ b/mllib/src/main/scala/org/apache/spark/ml/feature/StandardScaler.scala @@ -108,7 +108,8 @@ class StandardScaler @Since("1.4.0") ( def setWithStd(value: Boolean): this.type = set(withStd, value) @Since("2.0.0") override def fit(dataset: Dataset [_] ): StandardScalerModel = { + override def fit(dataset: Dataset [_] ): StandardScalerModel = super.fit(dataset) + override protected def fitImpl(dataset: Dataset [_] ): StandardScalerModel = { transformSchema(dataset.schema, logging = true) val input: RDD [OldVector] = dataset.select($(inputCol)).rdd.map { case Row(v: Vector) => OldVectors.fromML(v) @@ -158,7 +159,8 @@ class StandardScalerModel private [ml] ( def setOutputCol(value: String): this.type = set(outputCol, value) @Since("2.0.0") override def transform(dataset: Dataset [_] ): DataFrame = { + override def transform(dataset: Dataset [_] ): DataFrame = super.transform(dataset) + override protected def transformImpl(dataset: Dataset [_] ): DataFrame = { transformSchema(dataset.schema, logging = true) val scaler = new feature.StandardScalerModel(std, mean, $(withStd), $(withMean)) @@ -204,7 +206,7 @@ object StandardScalerModel extends MLReadable [StandardScalerModel] { private val className = classOf [StandardScalerModel] .getName override def load(path: String): StandardScalerModel = { + override protected def loadImpl(path: String): StandardScalerModel = { val metadata = DefaultParamsReader.loadMetadata(path, sc, className) val dataPath = new Path(path, "data").toString val data = sparkSession.read.parquet(dataPath) diff --git a/mllib/src/main/scala/org/apache/spark/ml/feature/StopWordsRemover.scala b/mllib/src/main/scala/org/apache/spark/ml/feature/StopWordsRemover.scala index 6669d402cd996..8110cccf27167 100755 a/mllib/src/main/scala/org/apache/spark/ml/feature/StopWordsRemover.scala +++ b/mllib/src/main/scala/org/apache/spark/ml/feature/StopWordsRemover.scala @@ -109,7 +109,8 @@ class StopWordsRemover @Since("1.5.0") (@Since("1.5.0") override val uid: String caseSensitive -> false, locale -> Locale.getDefault.toString) @Since("2.0.0") override def transform(dataset: Dataset [_] ): DataFrame = { + override def transform(dataset: Dataset [_] ): DataFrame = super.transform(dataset) + override protected def transformImpl(dataset: Dataset [_] ): DataFrame = { val outputSchema = transformSchema(dataset.schema) val t = if ($(caseSensitive)) { val stopWordsSet = $(stopWords).toSet diff --git a/mllib/src/main/scala/org/apache/spark/ml/feature/StringIndexer.scala b/mllib/src/main/scala/org/apache/spark/ml/feature/StringIndexer.scala index a833d8b270cf1..74843bac1ea82 100644 a/mllib/src/main/scala/org/apache/spark/ml/feature/StringIndexer.scala +++ b/mllib/src/main/scala/org/apache/spark/ml/feature/StringIndexer.scala @@ -131,7 +131,8 @@ class StringIndexer @Since("1.4.0") ( def setOutputCol(value: String): this.type = set(outputCol, value) @Since("2.0.0") override def fit(dataset: Dataset [_] ): StringIndexerModel = { + override def fit(dataset: Dataset [_] ): StringIndexerModel = super.fit(dataset) + override protected def fitImpl(dataset: Dataset [_] ): StringIndexerModel = { transformSchema(dataset.schema, logging = true) val values = dataset.na.drop(Array($(inputCol))) .select(col($(inputCol)).cast(StringType)) @@ -218,7 +219,8 @@ class StringIndexerModel ( def setOutputCol(value: String): this.type = set(outputCol, value) @Since("2.0.0") override def transform(dataset: Dataset [_] ): DataFrame = { + override def transform(dataset: Dataset [_] ): DataFrame = super.transform(dataset) + override protected def transformImpl(dataset: Dataset [_] ): DataFrame = { if (!dataset.schema.fieldNames.contains($(inputCol))) { logInfo(s"Input column ${$(inputCol)} does not exist during transformation. " + "Skip StringIndexerModel.") @@ -307,7 +309,7 @@ object StringIndexerModel extends MLReadable [StringIndexerModel] { private val className = classOf [StringIndexerModel] .getName override def load(path: String): StringIndexerModel = { + override protected def loadImpl(path: String): StringIndexerModel = { val metadata = DefaultParamsReader.loadMetadata(path, sc, className) val dataPath = new Path(path, "data").toString val data = sparkSession.read.parquet(dataPath) @@ -386,7 +388,8 @@ class IndexToString @Since("2.2.0") (@Since("1.5.0") override val uid: String) } @Since("2.0.0") override def transform(dataset: Dataset [_] ): DataFrame = { + override def transform(dataset: Dataset [_] ): DataFrame = super.transform(dataset) + override protected def transformImpl(dataset: Dataset [_] ): DataFrame = { transformSchema(dataset.schema, logging = true) val inputColSchema = dataset.schema($(inputCol)) // If the labels array is empty use column metadata diff --git a/mllib/src/main/scala/org/apache/spark/ml/feature/VectorAssembler.scala b/mllib/src/main/scala/org/apache/spark/ml/feature/VectorAssembler.scala index 57e23d5072b88..6add5f8d8c4e6 100644 a/mllib/src/main/scala/org/apache/spark/ml/feature/VectorAssembler.scala +++ b/mllib/src/main/scala/org/apache/spark/ml/feature/VectorAssembler.scala @@ -82,7 +82,8 @@ class VectorAssembler @Since("1.4.0") (@Since("1.4.0") override val uid: String) setDefault(handleInvalid, VectorAssembler.ERROR_INVALID) @Since("2.0.0") override def transform(dataset: Dataset [_] ): DataFrame = { + override def transform(dataset: Dataset [_] ): DataFrame = super.transform(dataset) + override protected def transformImpl(dataset: Dataset [_] ): DataFrame = { transformSchema(dataset.schema, logging = true) // Schema transformation. val schema = dataset.schema diff --git a/mllib/src/main/scala/org/apache/spark/ml/feature/VectorIndexer.scala b/mllib/src/main/scala/org/apache/spark/ml/feature/VectorIndexer.scala index 0e7396a621dbd..fd6e79c4e21fb 100644 a/mllib/src/main/scala/org/apache/spark/ml/feature/VectorIndexer.scala +++ b/mllib/src/main/scala/org/apache/spark/ml/feature/VectorIndexer.scala @@ -140,7 +140,8 @@ class VectorIndexer @Since("1.4.0") ( def setHandleInvalid(value: String): this.type = set(handleInvalid, value) @Since("2.0.0") override def fit(dataset: Dataset [_] ): VectorIndexerModel = { + override def fit(dataset: Dataset [_] ): VectorIndexerModel = super.fit(dataset) + override protected def fitImpl(dataset: Dataset [_] ): VectorIndexerModel = { transformSchema(dataset.schema, logging = true) val firstRow = dataset.select($(inputCol)).take(1) require(firstRow.length == 1, s"VectorIndexer cannot be fit on an empty dataset.") @@ -425,7 +426,8 @@ class VectorIndexerModel private [ml] ( def setOutputCol(value: String): this.type = set(outputCol, value) @Since("2.0.0") override def transform(dataset: Dataset [_] ): DataFrame = { + override def transform(dataset: Dataset [_] ): DataFrame = super.transform(dataset) + override protected def transformImpl(dataset: Dataset [_] ): DataFrame = { transformSchema(dataset.schema, logging = true) val newField = prepOutputField(dataset.schema) val transformUDF = udf { (vector: Vector) => transformFunc(vector) } @@ -528,7 +530,7 @@ object VectorIndexerModel extends MLReadable [VectorIndexerModel] { private val className = classOf [VectorIndexerModel] .getName override def load(path: String): VectorIndexerModel = { + override protected def loadImpl(path: String): VectorIndexerModel = { val metadata = DefaultParamsReader.loadMetadata(path, sc, className) val dataPath = new Path(path, "data").toString val data = sparkSession.read.parquet(dataPath) diff --git a/mllib/src/main/scala/org/apache/spark/ml/feature/VectorSizeHint.scala b/mllib/src/main/scala/org/apache/spark/ml/feature/VectorSizeHint.scala index f5947d61fe349..854fd1b4d3776 100644 a/mllib/src/main/scala/org/apache/spark/ml/feature/VectorSizeHint.scala +++ b/mllib/src/main/scala/org/apache/spark/ml/feature/VectorSizeHint.scala @@ -96,7 +96,8 @@ class VectorSizeHint @Since("2.3.0") (@Since("2.3.0") override val uid: String) setDefault(handleInvalid, VectorSizeHint.ERROR_INVALID) @Since("2.3.0") override def transform(dataset: Dataset [_] ): DataFrame = { + override def transform(dataset: Dataset [_] ): DataFrame = super.transform(dataset) + override protected def transformImpl(dataset: Dataset [_] ): DataFrame = { val localInputCol = getInputCol val localSize = getSize val localHandleInvalid = getHandleInvalid diff --git a/mllib/src/main/scala/org/apache/spark/ml/feature/VectorSlicer.scala b/mllib/src/main/scala/org/apache/spark/ml/feature/VectorSlicer.scala index e3e462d07e10c..cd1d49c1a2cb0 100644 a/mllib/src/main/scala/org/apache/spark/ml/feature/VectorSlicer.scala +++ b/mllib/src/main/scala/org/apache/spark/ml/feature/VectorSlicer.scala @@ -98,7 +98,8 @@ final class VectorSlicer @Since("1.5.0") (@Since("1.5.0") override val uid: Stri def setOutputCol(value: String): this.type = set(outputCol, value) @Since("2.0.0") override def transform(dataset: Dataset [_] ): DataFrame = { + override def transform(dataset: Dataset [_] ): DataFrame = super.transform(dataset) + override protected def transformImpl(dataset: Dataset [_] ): DataFrame = { // Validity checks transformSchema(dataset.schema) val inputAttr = AttributeGroup.fromStructField(dataset.schema($(inputCol))) diff --git a/mllib/src/main/scala/org/apache/spark/ml/feature/Word2Vec.scala b/mllib/src/main/scala/org/apache/spark/ml/feature/Word2Vec.scala index fc9996d69ba72..31e5b00765c68 100644 a/mllib/src/main/scala/org/apache/spark/ml/feature/Word2Vec.scala +++ b/mllib/src/main/scala/org/apache/spark/ml/feature/Word2Vec.scala @@ -171,7 +171,8 @@ final class Word2Vec @Since("1.4.0") ( def setMaxSentenceLength(value: Int): this.type = set(maxSentenceLength, value) @Since("2.0.0") override def fit(dataset: Dataset [_] ): Word2VecModel = { + override def fit(dataset: Dataset [_] ): Word2VecModel = super.fit(dataset) + override protected def fitImpl(dataset: Dataset [_] ): Word2VecModel = { transformSchema(dataset.schema, logging = true) val input = dataset.select($(inputCol)).rdd.map(_.getAs[Seq [String] ](0)) val wordVectors = new feature.Word2Vec() @@ -286,7 +287,8 @@ class Word2VecModel private [ml] ( is performed by averaging all word vectors it contains. */ @Since("2.0.0") override def transform(dataset: Dataset [_] ): DataFrame = { + override def transform(dataset: Dataset [_] ): DataFrame = super.transform(dataset) + override protected def transformImpl(dataset: Dataset [_] ): DataFrame = { transformSchema(dataset.schema, logging = true) val vectors = wordVectors.getVectors .mapValues(vv => Vectors.dense(vv.map(_.toDouble))) @@ -385,7 +387,7 @@ object Word2VecModel extends MLReadable [Word2VecModel] { private val className = classOf [Word2VecModel] .getName override def load(path: String): Word2VecModel = { + override protected def loadImpl(path: String): Word2VecModel = { val spark = sparkSession import spark.implicits._ diff --git a/mllib/src/main/scala/org/apache/spark/ml/fpm/FPGrowth.scala b/mllib/src/main/scala/org/apache/spark/ml/fpm/FPGrowth.scala index 7322815c12ab8..d2ca4bc53957f 100644 — a/mllib/src/main/scala/org/apache/spark/ml/fpm/FPGrowth.scala +++ b/mllib/src/main/scala/org/apache/spark/ml/fpm/FPGrowth.scala @@ -157,7 +157,8 @@ class FPGrowth @Since("2.2.0") ( def setPredictionCol(value: String): this.type = set(predictionCol, value) @Since("2.2.0") override def fit(dataset: Dataset [_] ): FPGrowthModel = { + override def fit(dataset: Dataset [_] ): FPGrowthModel = super.fit(dataset) + override protected def fitImpl(dataset: Dataset [_] ): FPGrowthModel = { transformSchema(dataset.schema, logging = true) genericFit(dataset) } @@ -277,7 +278,8 @@ class FPGrowthModel private [ml] ( efficiency. This may bring pressure to driver memory for large set of association rules. */ @Since("2.2.0") override def transform(dataset: Dataset [_] ): DataFrame = { + override def transform(dataset: Dataset [_] ): DataFrame = super.transform(dataset) + override protected def transformImpl(dataset: Dataset [_] ): DataFrame = { transformSchema(dataset.schema, logging = true) genericTransform(dataset) } @@ -342,7 +344,7 @@ object FPGrowthModel extends MLReadable [FPGrowthModel] { /** Checked against metadata when loading model */ private val className = classOf [FPGrowthModel] .getName override def load(path: String): FPGrowthModel = { + override protected def loadImpl(path: String): FPGrowthModel = { implicit val format = DefaultFormats val metadata = DefaultParamsReader.loadMetadata(path, sc, className) val (major, minor) = VersionUtils.majorMinorVersion(metadata.sparkVersion) diff --git a/mllib/src/main/scala/org/apache/spark/ml/r/AFTSurvivalRegressionWrapper.scala b/mllib/src/main/scala/org/apache/spark/ml/r/AFTSurvivalRegressionWrapper.scala index 1b5f77a9ae897..d45a5fa14df90 100644 a/mllib/src/main/scala/org/apache/spark/ml/r/AFTSurvivalRegressionWrapper.scala +++ b/mllib/src/main/scala/org/apache/spark/ml/r/AFTSurvivalRegressionWrapper.scala @@ -136,7 +136,7 @@ private [r] object AFTSurvivalRegressionWrapper extends MLReadable[AFTSurvivalReg class AFTSurvivalRegressionWrapperReader extends MLReader [AFTSurvivalRegressionWrapper] { override def load(path: String): AFTSurvivalRegressionWrapper = { + override protected def loadImpl(path: String): AFTSurvivalRegressionWrapper = { implicit val format = DefaultFormats val rMetadataPath = new Path(path, "rMetadata").toString val pipelinePath = new Path(path, "pipeline").toString diff --git a/mllib/src/main/scala/org/apache/spark/ml/r/ALSWrapper.scala b/mllib/src/main/scala/org/apache/spark/ml/r/ALSWrapper.scala index ad13cced4667b..8d12d80ab4734 100644 a/mllib/src/main/scala/org/apache/spark/ml/r/ALSWrapper.scala +++ b/mllib/src/main/scala/org/apache/spark/ml/r/ALSWrapper.scala @@ -102,7 +102,7 @@ private [r] object ALSWrapper extends MLReadable [ALSWrapper] { class ALSWrapperReader extends MLReader [ALSWrapper] { override def load(path: String): ALSWrapper = { + override protected def loadImpl(path: String): ALSWrapper = { implicit val format = DefaultFormats val rMetadataPath = new Path(path, "rMetadata").toString val modelPath = new Path(path, "model").toString diff --git a/mllib/src/main/scala/org/apache/spark/ml/r/BisectingKMeansWrapper.scala b/mllib/src/main/scala/org/apache/spark/ml/r/BisectingKMeansWrapper.scala index 71712c1c5eec5..8478c7b6e8c77 100644 a/mllib/src/main/scala/org/apache/spark/ml/r/BisectingKMeansWrapper.scala +++ b/mllib/src/main/scala/org/apache/spark/ml/r/BisectingKMeansWrapper.scala @@ -126,7 +126,7 @@ private [r] object BisectingKMeansWrapper extends MLReadable[BisectingKMeansWrapp class BisectingKMeansWrapperReader extends MLReader [BisectingKMeansWrapper] { override def load(path: String): BisectingKMeansWrapper = { + override protected def loadImpl(path: String): BisectingKMeansWrapper = { implicit val format = DefaultFormats val rMetadataPath = new Path(path, "rMetadata").toString val pipelinePath = new Path(path, "pipeline").toString diff --git a/mllib/src/main/scala/org/apache/spark/ml/r/DecisionTreeClassificationWrapper.scala b/mllib/src/main/scala/org/apache/spark/ml/r/DecisionTreeClassificationWrapper.scala index a90cae5869b2a..ad9476c1c000c 100644 a/mllib/src/main/scala/org/apache/spark/ml/r/DecisionTreeClassificationWrapper.scala +++ b/mllib/src/main/scala/org/apache/spark/ml/r/DecisionTreeClassificationWrapper.scala @@ -137,7 +137,7 @@ private [r] object DecisionTreeClassifierWrapper extends MLReadable[DecisionTreeC class DecisionTreeClassifierWrapperReader extends MLReader [DecisionTreeClassifierWrapper] { override def load(path: String): DecisionTreeClassifierWrapper = { + override protected def loadImpl(path: String): DecisionTreeClassifierWrapper = { implicit val format = DefaultFormats val rMetadataPath = new Path(path, "rMetadata").toString val pipelinePath = new Path(path, "pipeline").toString diff --git a/mllib/src/main/scala/org/apache/spark/ml/r/DecisionTreeRegressionWrapper.scala b/mllib/src/main/scala/org/apache/spark/ml/r/DecisionTreeRegressionWrapper.scala index de712d67e6df5..efe7884d5a170 100644 a/mllib/src/main/scala/org/apache/spark/ml/r/DecisionTreeRegressionWrapper.scala +++ b/mllib/src/main/scala/org/apache/spark/ml/r/DecisionTreeRegressionWrapper.scala @@ -120,7 +120,7 @@ private [r] object DecisionTreeRegressorWrapper extends MLReadable[DecisionTreeRe class DecisionTreeRegressorWrapperReader extends MLReader [DecisionTreeRegressorWrapper] { override def load(path: String): DecisionTreeRegressorWrapper = { + override protected def loadImpl(path: String): DecisionTreeRegressorWrapper = { implicit val format = DefaultFormats val rMetadataPath = new Path(path, "rMetadata").toString val pipelinePath = new Path(path, "pipeline").toString diff --git a/mllib/src/main/scala/org/apache/spark/ml/r/FPGrowthWrapper.scala b/mllib/src/main/scala/org/apache/spark/ml/r/FPGrowthWrapper.scala index b8151d8d90702..27a859678372f 100644 a/mllib/src/main/scala/org/apache/spark/ml/r/FPGrowthWrapper.scala +++ b/mllib/src/main/scala/org/apache/spark/ml/r/FPGrowthWrapper.scala @@ -61,7 +61,7 @@ private [r] object FPGrowthWrapper extends MLReadable [FPGrowthWrapper] { override def read: MLReader [FPGrowthWrapper] = new FPGrowthWrapperReader class FPGrowthWrapperReader extends MLReader [FPGrowthWrapper] { override def load(path: String): FPGrowthWrapper = { + override protected def loadImpl(path: String): FPGrowthWrapper = { val modelPath = new Path(path, "model").toString val fPGrowthModel = FPGrowthModel.load(modelPath) diff --git a/mllib/src/main/scala/org/apache/spark/ml/r/GBTClassificationWrapper.scala b/mllib/src/main/scala/org/apache/spark/ml/r/GBTClassificationWrapper.scala index ecaeec5a7791a..ff55d32019030 100644 — a/mllib/src/main/scala/org/apache/spark/ml/r/GBTClassificationWrapper.scala +++ b/mllib/src/main/scala/org/apache/spark/ml/r/GBTClassificationWrapper.scala @@ -144,7 +144,7 @@ private [r] object GBTClassifierWrapper extends MLReadable [GBTClassifierWrapper] class GBTClassifierWrapperReader extends MLReader [GBTClassifierWrapper] { override def load(path: String): GBTClassifierWrapper = { + override protected def loadImpl(path: String): GBTClassifierWrapper = { implicit val format = DefaultFormats val rMetadataPath = new Path(path, "rMetadata").toString val pipelinePath = new Path(path, "pipeline").toString diff --git a/mllib/src/main/scala/org/apache/spark/ml/r/GBTRegressionWrapper.scala b/mllib/src/main/scala/org/apache/spark/ml/r/GBTRegressionWrapper.scala index b568d7859221f..fef2c5755e8f9 100644 a/mllib/src/main/scala/org/apache/spark/ml/r/GBTRegressionWrapper.scala +++ b/mllib/src/main/scala/org/apache/spark/ml/r/GBTRegressionWrapper.scala @@ -128,7 +128,7 @@ private [r] object GBTRegressorWrapper extends MLReadable [GBTRegressorWrapper] { class GBTRegressorWrapperReader extends MLReader [GBTRegressorWrapper] { override def load(path: String): GBTRegressorWrapper = { + override protected def loadImpl(path: String): GBTRegressorWrapper = { implicit val format = DefaultFormats val rMetadataPath = new Path(path, "rMetadata").toString val pipelinePath = new Path(path, "pipeline").toString diff --git a/mllib/src/main/scala/org/apache/spark/ml/r/GaussianMixtureWrapper.scala b/mllib/src/main/scala/org/apache/spark/ml/r/GaussianMixtureWrapper.scala index 9a98a8b18b141..656a0062cd14f 100644 a/mllib/src/main/scala/org/apache/spark/ml/r/GaussianMixtureWrapper.scala +++ b/mllib/src/main/scala/org/apache/spark/ml/r/GaussianMixtureWrapper.scala @@ -120,7 +120,7 @@ private [r] object GaussianMixtureWrapper extends MLReadable[GaussianMixtureWrapp class GaussianMixtureWrapperReader extends MLReader [GaussianMixtureWrapper] { override def load(path: String): GaussianMixtureWrapper = { + override protected def loadImpl(path: String): GaussianMixtureWrapper = { implicit val format = DefaultFormats val rMetadataPath = new Path(path, "rMetadata").toString val pipelinePath = new Path(path, "pipeline").toString diff --git a/mllib/src/main/scala/org/apache/spark/ml/r/GeneralizedLinearRegressionWrapper.scala b/mllib/src/main/scala/org/apache/spark/ml/r/GeneralizedLinearRegressionWrapper.scala index 64575b0cb0cb5..c974519211288 100644 a/mllib/src/main/scala/org/apache/spark/ml/r/GeneralizedLinearRegressionWrapper.scala +++ b/mllib/src/main/scala/org/apache/spark/ml/r/GeneralizedLinearRegressionWrapper.scala @@ -179,7 +179,7 @@ private [r] object GeneralizedLinearRegressionWrapper class GeneralizedLinearRegressionWrapperReader extends MLReader [GeneralizedLinearRegressionWrapper] { override def load(path: String): GeneralizedLinearRegressionWrapper = { + override protected def loadImpl(path: String): GeneralizedLinearRegressionWrapper = { implicit val format = DefaultFormats val rMetadataPath = new Path(path, "rMetadata").toString val pipelinePath = new Path(path, "pipeline").toString diff --git a/mllib/src/main/scala/org/apache/spark/ml/r/IsotonicRegressionWrapper.scala b/mllib/src/main/scala/org/apache/spark/ml/r/IsotonicRegressionWrapper.scala index d31ebb46afb97..dc1f3e62056f6 100644 a/mllib/src/main/scala/org/apache/spark/ml/r/IsotonicRegressionWrapper.scala +++ b/mllib/src/main/scala/org/apache/spark/ml/r/IsotonicRegressionWrapper.scala @@ -106,7 +106,7 @@ private [r] object IsotonicRegressionWrapper class IsotonicRegressionWrapperReader extends MLReader [IsotonicRegressionWrapper] { override def load(path: String): IsotonicRegressionWrapper = { + override protected def loadImpl(path: String): IsotonicRegressionWrapper = { implicit val format = DefaultFormats val rMetadataPath = new Path(path, "rMetadata").toString val pipelinePath = new Path(path, "pipeline").toString diff --git a/mllib/src/main/scala/org/apache/spark/ml/r/KMeansWrapper.scala b/mllib/src/main/scala/org/apache/spark/ml/r/KMeansWrapper.scala index 8d596863b459e..2b239d7a786ce 100644 a/mllib/src/main/scala/org/apache/spark/ml/r/KMeansWrapper.scala +++ b/mllib/src/main/scala/org/apache/spark/ml/r/KMeansWrapper.scala @@ -129,7 +129,7 @@ private [r] object KMeansWrapper extends MLReadable [KMeansWrapper] { class KMeansWrapperReader extends MLReader [KMeansWrapper] { override def load(path: String): KMeansWrapper = { + override protected def loadImpl(path: String): KMeansWrapper = { implicit val format = DefaultFormats val rMetadataPath = new Path(path, "rMetadata").toString val pipelinePath = new Path(path, "pipeline").toString diff --git a/mllib/src/main/scala/org/apache/spark/ml/r/LDAWrapper.scala b/mllib/src/main/scala/org/apache/spark/ml/r/LDAWrapper.scala index e096bf1f29f3e..210baec3cb33c 100644 a/mllib/src/main/scala/org/apache/spark/ml/r/LDAWrapper.scala +++ b/mllib/src/main/scala/org/apache/spark/ml/r/LDAWrapper.scala @@ -206,7 +206,7 @@ private [r] object LDAWrapper extends MLReadable [LDAWrapper] { class LDAWrapperReader extends MLReader [LDAWrapper] { override def load(path: String): LDAWrapper = { + override protected def loadImpl(path: String): LDAWrapper = { implicit val format = DefaultFormats val rMetadataPath = new Path(path, "rMetadata").toString val pipelinePath = new Path(path, "pipeline").toString diff --git a/mllib/src/main/scala/org/apache/spark/ml/r/LinearSVCWrapper.scala b/mllib/src/main/scala/org/apache/spark/ml/r/LinearSVCWrapper.scala index 7a22a71c3a819..7ec2717f515de 100644 a/mllib/src/main/scala/org/apache/spark/ml/r/LinearSVCWrapper.scala +++ b/mllib/src/main/scala/org/apache/spark/ml/r/LinearSVCWrapper.scala @@ -144,7 +144,7 @@ private [r] object LinearSVCWrapper class LinearSVCWrapperReader extends MLReader [LinearSVCWrapper] { override def load(path: String): LinearSVCWrapper = { + override protected def loadImpl(path: String): LinearSVCWrapper = { implicit val format = DefaultFormats val rMetadataPath = new Path(path, "rMetadata").toString val pipelinePath = new Path(path, "pipeline").toString diff --git a/mllib/src/main/scala/org/apache/spark/ml/r/LogisticRegressionWrapper.scala b/mllib/src/main/scala/org/apache/spark/ml/r/LogisticRegressionWrapper.scala index 18acf7d21656f..a7dfcb3953e19 100644 a/mllib/src/main/scala/org/apache/spark/ml/r/LogisticRegressionWrapper.scala +++ b/mllib/src/main/scala/org/apache/spark/ml/r/LogisticRegressionWrapper.scala @@ -199,7 +199,7 @@ private [r] object LogisticRegressionWrapper class LogisticRegressionWrapperReader extends MLReader [LogisticRegressionWrapper] { override def load(path: String): LogisticRegressionWrapper = { + override protected def loadImpl(path: String): LogisticRegressionWrapper = { implicit val format = DefaultFormats val rMetadataPath = new Path(path, "rMetadata").toString val pipelinePath = new Path(path, "pipeline").toString diff --git a/mllib/src/main/scala/org/apache/spark/ml/r/MultilayerPerceptronClassifierWrapper.scala b/mllib/src/main/scala/org/apache/spark/ml/r/MultilayerPerceptronClassifierWrapper.scala index 62f642142701b..6ac25957b9c81 100644 a/mllib/src/main/scala/org/apache/spark/ml/r/MultilayerPerceptronClassifierWrapper.scala +++ b/mllib/src/main/scala/org/apache/spark/ml/r/MultilayerPerceptronClassifierWrapper.scala @@ -124,7 +124,7 @@ private [r] object MultilayerPerceptronClassifierWrapper class MultilayerPerceptronClassifierWrapperReader extends MLReader [MultilayerPerceptronClassifierWrapper] { override def load(path: String): MultilayerPerceptronClassifierWrapper = { + override protected def loadImpl(path: String): MultilayerPerceptronClassifierWrapper = { implicit val format = DefaultFormats val pipelinePath = new Path(path, "pipeline").toString diff --git a/mllib/src/main/scala/org/apache/spark/ml/r/NaiveBayesWrapper.scala b/mllib/src/main/scala/org/apache/spark/ml/r/NaiveBayesWrapper.scala index fbf9f462ff5f6..e84b1fc297e5e 100644 — a/mllib/src/main/scala/org/apache/spark/ml/r/NaiveBayesWrapper.scala +++ b/mllib/src/main/scala/org/apache/spark/ml/r/NaiveBayesWrapper.scala @@ -109,7 +109,7 @@ private [r] object NaiveBayesWrapper extends MLReadable [NaiveBayesWrapper] { class NaiveBayesWrapperReader extends MLReader [NaiveBayesWrapper] { override def load(path: String): NaiveBayesWrapper = { + override protected def loadImpl(path: String): NaiveBayesWrapper = { implicit val format = DefaultFormats val rMetadataPath = new Path(path, "rMetadata").toString val pipelinePath = new Path(path, "pipeline").toString diff --git a/mllib/src/main/scala/org/apache/spark/ml/r/RWrappers.scala b/mllib/src/main/scala/org/apache/spark/ml/r/RWrappers.scala index ba6445a730306..7dd93f1420f6f 100644 a/mllib/src/main/scala/org/apache/spark/ml/r/RWrappers.scala +++ b/mllib/src/main/scala/org/apache/spark/ml/r/RWrappers.scala @@ -30,7 +30,7 @@ import org.apache.spark.ml.util.MLReader */ private [r] object RWrappers extends MLReader [Object] { override def load(path: String): Object = { + override protected def loadImpl(path: String): Object = { implicit val format = DefaultFormats val rMetadataPath = new Path(path, "rMetadata").toString val rMetadataStr = sc.textFile(rMetadataPath, 1).first() diff --git a/mllib/src/main/scala/org/apache/spark/ml/r/RandomForestClassificationWrapper.scala b/mllib/src/main/scala/org/apache/spark/ml/r/RandomForestClassificationWrapper.scala index 132345fb9a6d9..c905319ba0ec2 100644 a/mllib/src/main/scala/org/apache/spark/ml/r/RandomForestClassificationWrapper.scala +++ b/mllib/src/main/scala/org/apache/spark/ml/r/RandomForestClassificationWrapper.scala @@ -145,7 +145,7 @@ private [r] object RandomForestClassifierWrapper extends MLReadable[RandomForestC class RandomForestClassifierWrapperReader extends MLReader [RandomForestClassifierWrapper] { override def load(path: String): RandomForestClassifierWrapper = { + override protected def loadImpl(path: String): RandomForestClassifierWrapper = { implicit val format = DefaultFormats val rMetadataPath = new Path(path, "rMetadata").toString val pipelinePath = new Path(path, "pipeline").toString diff --git a/mllib/src/main/scala/org/apache/spark/ml/r/RandomForestRegressionWrapper.scala b/mllib/src/main/scala/org/apache/spark/ml/r/RandomForestRegressionWrapper.scala index 038bd79c7022b..1f432da570560 100644 a/mllib/src/main/scala/org/apache/spark/ml/r/RandomForestRegressionWrapper.scala +++ b/mllib/src/main/scala/org/apache/spark/ml/r/RandomForestRegressionWrapper.scala @@ -128,7 +128,7 @@ private [r] object RandomForestRegressorWrapper extends MLReadable[RandomForestRe class RandomForestRegressorWrapperReader extends MLReader [RandomForestRegressorWrapper] { override def load(path: String): RandomForestRegressorWrapper = { + override protected def loadImpl(path: String): RandomForestRegressorWrapper = { implicit val format = DefaultFormats val rMetadataPath = new Path(path, "rMetadata").toString val pipelinePath = new Path(path, "pipeline").toString diff --git a/mllib/src/main/scala/org/apache/spark/ml/recommendation/ALS.scala b/mllib/src/main/scala/org/apache/spark/ml/recommendation/ALS.scala index 50ef4330ddc80..fbcf39dcbe3ba 100644 --- a/mllib/src/main/scala/org/apache/spark/ml/recommendation/ALS.scala +++ b/mllib/src/main/scala/org/apache/spark/ml/recommendation/ALS.scala @@ -303,7 +303,8 @@ class ALSModel private[ml] ( } @Since("2.0.0") override def transform(dataset: Dataset [_] ): DataFrame = { + override def transform(dataset: Dataset [_] ): DataFrame = super.transform(dataset) + override protected def transformImpl(dataset: Dataset [_] ): DataFrame = { transformSchema(dataset.schema) // create a new column named map(predictionCol) by running the predict UDF. val predictions = dataset @@ -519,7 +520,7 @@ object ALSModel extends MLReadable [ALSModel] { /** Checked against metadata when loading model */ private val className = classOf [ALSModel] .getName override def load(path: String): ALSModel = { + override protected def loadImpl(path: String): ALSModel = { val metadata = DefaultParamsReader.loadMetadata(path, sc, className) implicit val format = DefaultFormats val rank = (metadata.metadata \ "rank").extract[Int] @@ -655,7 +656,8 @@ class ALS(@Since("1.4.0") override val uid: String) extends Estimator[ALSModel] } @Since("2.0.0") override def fit(dataset: Dataset [_] ): ALSModel = instrumented { instr => + override def fit(dataset: Dataset [_] ): ALSModel = super.fit(dataset) + override protected def fitImpl(dataset: Dataset [_] ): ALSModel = instrumented { instr => transformSchema(dataset.schema) import dataset.sparkSession.implicits._ diff --git a/mllib/src/main/scala/org/apache/spark/ml/regression/AFTSurvivalRegression.scala b/mllib/src/main/scala/org/apache/spark/ml/regression/AFTSurvivalRegression.scala index 8d6e36697d2cc..ebda26e8ffc8e 100644 --- a/mllib/src/main/scala/org/apache/spark/ml/regression/AFTSurvivalRegression.scala +++ b/mllib/src/main/scala/org/apache/spark/ml/regression/AFTSurvivalRegression.scala @@ -211,7 +211,9 @@ class AFTSurvivalRegression @Since("1.6.0") (@Since("1.6.0") override val uid: S } @Since("2.0.0") override def fit(dataset: Dataset [_] ): AFTSurvivalRegressionModel = instrumented { instr => + override def fit(dataset: Dataset [_] ): AFTSurvivalRegressionModel = super.fit(dataset) + override protected def fitImpl( + dataset: Dataset [_] ): AFTSurvivalRegressionModel = instrumented { instr => transformSchema(dataset.schema, logging = true) val instances = extractAFTPoints(dataset) val handlePersistence = dataset.storageLevel == StorageLevel.NONE @@ -353,7 +355,8 @@ class AFTSurvivalRegressionModel private[ml] ( } @Since("2.0.0") override def transform(dataset: Dataset [_] ): DataFrame = { + override def transform(dataset: Dataset [_] ): DataFrame = super.transform(dataset) + override protected def transformImpl(dataset: Dataset [_] ): DataFrame = { transformSchema(dataset.schema, logging = true) val predictUDF = udf { features: Vector => predict(features) } val predictQuantilesUDF = udf { features: Vector => predictQuantiles(features)} @@ -412,7 +415,7 @@ object AFTSurvivalRegressionModel extends MLReadable [AFTSurvivalRegressionModel] /** Checked against metadata when loading model */ private val className = classOf [AFTSurvivalRegressionModel] .getName override def load(path: String): AFTSurvivalRegressionModel = { + override protected def loadImpl(path: String): AFTSurvivalRegressionModel = { val metadata = DefaultParamsReader.loadMetadata(path, sc, className) val dataPath = new Path(path, "data").toString diff --git a/mllib/src/main/scala/org/apache/spark/ml/regression/DecisionTreeRegressor.scala b/mllib/src/main/scala/org/apache/spark/ml/regression/DecisionTreeRegressor.scala index faadc4d7b4ccc..155c979e28250 100644 — a/mllib/src/main/scala/org/apache/spark/ml/regression/DecisionTreeRegressor.scala +++ b/mllib/src/main/scala/org/apache/spark/ml/regression/DecisionTreeRegressor.scala @@ -22,7 +22,7 @@ import org.json4s. {DefaultFormats, JObject} import org.json4s.JsonDSL._ import org.apache.spark.annotation.Since -import org.apache.spark.ml. {PredictionModel, Predictor} +import org.apache.spark.ml. {MLEvents, PredictionModel, Predictor} import org.apache.spark.ml.feature.LabeledPoint import org.apache.spark.ml.linalg.Vector import org.apache.spark.ml.param.ParamMap @@ -188,7 +188,8 @@ class DecisionTreeRegressionModel private [ml] ( } @Since("2.0.0") override def transform(dataset: Dataset [_] ): DataFrame = { + override def transform( + dataset: Dataset [_] ): DataFrame = MLEvents.withTransformEvent(this, dataset) { transformSchema(dataset.schema, logging = true) transformImpl(dataset) } @@ -275,7 +276,7 @@ object DecisionTreeRegressionModel extends MLReadable[DecisionTreeRegressionMode /** Checked against metadata when loading model */ private val className = classOf [DecisionTreeRegressionModel] .getName override def load(path: String): DecisionTreeRegressionModel = { + override protected def loadImpl(path: String): DecisionTreeRegressionModel = { implicit val format = DefaultFormats val metadata = DefaultParamsReader.loadMetadata(path, sc, className) val numFeatures = (metadata.metadata \ "numFeatures").extract [Int] diff --git a/mllib/src/main/scala/org/apache/spark/ml/regression/GBTRegressor.scala b/mllib/src/main/scala/org/apache/spark/ml/regression/GBTRegressor.scala index 9a5b7d59e9aef..befef2737b9bf 100644 a/mllib/src/main/scala/org/apache/spark/ml/regression/GBTRegressor.scala +++ b/mllib/src/main/scala/org/apache/spark/ml/regression/GBTRegressor.scala @@ -337,7 +337,7 @@ object GBTRegressionModel extends MLReadable [GBTRegressionModel] { private val className = classOf [GBTRegressionModel] .getName private val treeClassName = classOf [DecisionTreeRegressionModel] .getName override def load(path: String): GBTRegressionModel = { + override protected def loadImpl(path: String): GBTRegressionModel = { implicit val format = DefaultFormats val (metadata: Metadata, treesData: Array [(Metadata, Node)] , treeWeights: Array [Double] ) = EnsembleModelReadWrite.loadImpl(path, sparkSession, className, treeClassName) diff --git a/mllib/src/main/scala/org/apache/spark/ml/regression/GeneralizedLinearRegression.scala b/mllib/src/main/scala/org/apache/spark/ml/regression/GeneralizedLinearRegression.scala index abb60ea205751..648167fe3e012 100644 a/mllib/src/main/scala/org/apache/spark/ml/regression/GeneralizedLinearRegression.scala +++ b/mllib/src/main/scala/org/apache/spark/ml/regression/GeneralizedLinearRegression.scala @@ -26,7 +26,7 @@ import org.apache.hadoop.fs.Path import org.apache.spark.SparkException import org.apache.spark.annotation. {Experimental, Since} import org.apache.spark.internal.Logging -import org.apache.spark.ml.PredictorParams +import org.apache.spark.ml. {MLEvents, PredictorParams} import org.apache.spark.ml.attribute.AttributeGroup import org.apache.spark.ml.feature. {Instance, OffsetInstance} import org.apache.spark.ml.linalg. {BLAS, Vector, Vectors} @@ -1034,7 +1034,8 @@ class GeneralizedLinearRegressionModel private [ml] ( BLAS.dot(features, coefficients) + intercept + offset } override def transform(dataset: Dataset [_] ): DataFrame = { + override def transform( + dataset: Dataset [_] ): DataFrame = MLEvents.withTransformEvent(this, dataset) { transformSchema(dataset.schema) transformImpl(dataset) } @@ -1140,7 +1141,7 @@ object GeneralizedLinearRegressionModel extends MLReadable[GeneralizedLinearRegr /** Checked against metadata when loading model */ private val className = classOf [GeneralizedLinearRegressionModel] .getName override def load(path: String): GeneralizedLinearRegressionModel = { + override protected def loadImpl(path: String): GeneralizedLinearRegressionModel = { val metadata = DefaultParamsReader.loadMetadata(path, sc, className) val dataPath = new Path(path, "data").toString diff --git a/mllib/src/main/scala/org/apache/spark/ml/regression/IsotonicRegression.scala b/mllib/src/main/scala/org/apache/spark/ml/regression/IsotonicRegression.scala index 8b9233dcdc4d1..422eaf8d4b9b3 100644 — a/mllib/src/main/scala/org/apache/spark/ml/regression/IsotonicRegression.scala +++ b/mllib/src/main/scala/org/apache/spark/ml/regression/IsotonicRegression.scala @@ -162,7 +162,9 @@ class IsotonicRegression @Since("1.5.0") (@Since("1.5.0") override val uid: Stri override def copy(extra: ParamMap): IsotonicRegression = defaultCopy(extra) @Since("2.0.0") override def fit(dataset: Dataset [_] ): IsotonicRegressionModel = instrumented { instr => + override def fit(dataset: Dataset [_] ): IsotonicRegressionModel = super.fit(dataset) + override protected def fitImpl( + dataset: Dataset [_] ): IsotonicRegressionModel = instrumented { instr => transformSchema(dataset.schema, logging = true) // Extract columns from data. If dataset is persisted, do not persist oldDataset. val instances = extractWeightedLabeledPoints(dataset) @@ -239,7 +241,8 @@ class IsotonicRegressionModel private[ml] ( } @Since("2.0.0") override def transform(dataset: Dataset [_] ): DataFrame = { + override def transform(dataset: Dataset [_] ): DataFrame = super.transform(dataset) + override protected def transformImpl(dataset: Dataset [_] ): DataFrame = { transformSchema(dataset.schema, logging = true) val predict = dataset.schema($(featuresCol)).dataType match { case DoubleType => @@ -296,7 +299,7 @@ object IsotonicRegressionModel extends MLReadable [IsotonicRegressionModel] { /** Checked against metadata when loading model */ private val className = classOf [IsotonicRegressionModel] .getName override def load(path: String): IsotonicRegressionModel = { + override protected def loadImpl(path: String): IsotonicRegressionModel = { val metadata = DefaultParamsReader.loadMetadata(path, sc, className) val dataPath = new Path(path, "data").toString diff --git a/mllib/src/main/scala/org/apache/spark/ml/regression/LinearRegression.scala b/mllib/src/main/scala/org/apache/spark/ml/regression/LinearRegression.scala index ce6c12cc368dd..395ebd60c1728 100644 — a/mllib/src/main/scala/org/apache/spark/ml/regression/LinearRegression.scala +++ b/mllib/src/main/scala/org/apache/spark/ml/regression/LinearRegression.scala @@ -782,7 +782,7 @@ object LinearRegressionModel extends MLReadable [LinearRegressionModel] { /** Checked against metadata when loading model */ private val className = classOf [LinearRegressionModel] .getName override def load(path: String): LinearRegressionModel = { + override protected def loadImpl(path: String): LinearRegressionModel = { val metadata = DefaultParamsReader.loadMetadata(path, sc, className) val dataPath = new Path(path, "data").toString diff --git a/mllib/src/main/scala/org/apache/spark/ml/regression/RandomForestRegressor.scala b/mllib/src/main/scala/org/apache/spark/ml/regression/RandomForestRegressor.scala index afa9a646412b3..d1132f09d1975 100644 — a/mllib/src/main/scala/org/apache/spark/ml/regression/RandomForestRegressor.scala +++ b/mllib/src/main/scala/org/apache/spark/ml/regression/RandomForestRegressor.scala @@ -268,7 +268,7 @@ object RandomForestRegressionModel extends MLReadable[RandomForestRegressionMode private val className = classOf [RandomForestRegressionModel] .getName private val treeClassName = classOf [DecisionTreeRegressionModel] .getName override def load(path: String): RandomForestRegressionModel = { + override protected def loadImpl(path: String): RandomForestRegressionModel = { implicit val format = DefaultFormats val (metadata: Metadata, treesData: Array [(Metadata, Node)] , treeWeights: Array [Double] ) = EnsembleModelReadWrite.loadImpl(path, sparkSession, className, treeClassName) diff --git a/mllib/src/main/scala/org/apache/spark/ml/tuning/CrossValidator.scala b/mllib/src/main/scala/org/apache/spark/ml/tuning/CrossValidator.scala index e60a14f976a5c..dd5124a9fd584 100644 a/mllib/src/main/scala/org/apache/spark/ml/tuning/CrossValidator.scala +++ b/mllib/src/main/scala/org/apache/spark/ml/tuning/CrossValidator.scala @@ -119,7 +119,8 @@ class CrossValidator @Since("1.2.0") (@Since("1.4.0") override val uid: String) def setCollectSubModels(value: Boolean): this.type = set(collectSubModels, value) @Since("2.0.0") override def fit(dataset: Dataset [_] ): CrossValidatorModel = instrumented { instr => + override def fit(dataset: Dataset [_] ): CrossValidatorModel = super.fit(dataset) + override protected def fitImpl(dataset: Dataset [_] ): CrossValidatorModel = instrumented { instr => val schema = dataset.schema transformSchema(schema, logging = true) val sparkSession = dataset.sparkSession @@ -226,7 +227,7 @@ object CrossValidator extends MLReadable [CrossValidator] { /** Checked against metadata when loading model */ private val className = classOf [CrossValidator] .getName override def load(path: String): CrossValidator = { + override protected def loadImpl(path: String): CrossValidator = { implicit val format = DefaultFormats val (metadata, estimator, evaluator, estimatorParamMaps) = @@ -299,7 +300,8 @@ class CrossValidatorModel private [ml] ( def hasSubModels: Boolean = _subModels.isDefined @Since("2.0.0") override def transform(dataset: Dataset [_] ): DataFrame = { + override def transform(dataset: Dataset [_] ): DataFrame = super.transform(dataset) + override protected def transformImpl(dataset: Dataset [_] ): DataFrame = { transformSchema(dataset.schema, logging = true) bestModel.transform(dataset) } @@ -392,7 +394,10 @@ object CrossValidatorModel extends MLReadable [CrossValidatorModel] { /** Checked against metadata when loading model */ private val className = classOf [CrossValidatorModel] .getName - override def load(path: String): CrossValidatorModel = { + // Explicitly call parent's load. Otherwise, MiMa complains. + override def load(path: String): CrossValidatorModel = super.load(path) + + override protected def loadImpl(path: String): CrossValidatorModel = { implicit val format = DefaultFormats val (metadata, estimator, evaluator, estimatorParamMaps) = diff --git a/mllib/src/main/scala/org/apache/spark/ml/tuning/TrainValidationSplit.scala b/mllib/src/main/scala/org/apache/spark/ml/tuning/TrainValidationSplit.scala index 8b251197afbef..7fc662de85a77 100644 — a/mllib/src/main/scala/org/apache/spark/ml/tuning/TrainValidationSplit.scala +++ b/mllib/src/main/scala/org/apache/spark/ml/tuning/TrainValidationSplit.scala @@ -118,7 +118,9 @@ class TrainValidationSplit @Since("1.5.0") (@Since("1.5.0") override val uid: St def setCollectSubModels(value: Boolean): this.type = set(collectSubModels, value) @Since("2.0.0") - override def fit(dataset: Dataset [_] ): TrainValidationSplitModel = instrumented { instr => + override def fit(dataset: Dataset [_] ): TrainValidationSplitModel = super.fit(dataset) + override protected def fitImpl( + dataset: Dataset [_] ): TrainValidationSplitModel = instrumented { instr => val schema = dataset.schema transformSchema(schema, logging = true) val est = $(estimator) @@ -220,7 +222,7 @@ object TrainValidationSplit extends MLReadable [TrainValidationSplit] { /** Checked against metadata when loading model */ private val className = classOf [TrainValidationSplit] .getName - override def load(path: String): TrainValidationSplit = { + override protected def loadImpl(path: String): TrainValidationSplit = { implicit val format = DefaultFormats val (metadata, estimator, evaluator, estimatorParamMaps) = @@ -290,7 +292,8 @@ class TrainValidationSplitModel private [ml] ( def hasSubModels: Boolean = _subModels.isDefined @Since("2.0.0") - override def transform(dataset: Dataset [_] ): DataFrame = { + override def transform(dataset: Dataset [_] ): DataFrame = super.transform(dataset) + override protected def transformImpl(dataset: Dataset [_] ): DataFrame = { transformSchema(dataset.schema, logging = true) bestModel.transform(dataset) } @@ -380,7 +383,10 @@ object TrainValidationSplitModel extends MLReadable [TrainValidationSplitModel] { /** Checked against metadata when loading model */ private val className = classOf [TrainValidationSplitModel] .getName override def load(path: String): TrainValidationSplitModel = { + // Explicitly call parent's load. Otherwise, MiMa complains. + override def load(path: String): TrainValidationSplitModel = super.load(path) + + override protected def loadImpl(path: String): TrainValidationSplitModel = { implicit val format = DefaultFormats val (metadata, estimator, evaluator, estimatorParamMaps) = diff --git a/mllib/src/main/scala/org/apache/spark/ml/util/ReadWrite.scala b/mllib/src/main/scala/org/apache/spark/ml/util/ReadWrite.scala index fbc7be25a5640..0a45fa8e267ed 100644 — a/mllib/src/main/scala/org/apache/spark/ml/util/ReadWrite.scala +++ b/mllib/src/main/scala/org/apache/spark/ml/util/ReadWrite.scala @@ -163,7 +163,7 @@ abstract class MLWriter extends BaseReadWrite with Logging { */ @Since("1.6.0") @throws [IOException] ("If the input path already exists but overwrite is not enabled.") def save(path: String): Unit = { + def save(path: String): Unit = MLEvents.withSaveInstanceEvent(this, path) { new FileSystemOverwrite().handleOverwrite(path, shouldOverwrite, sc) saveImpl(path) } @@ -329,7 +329,19 @@ abstract class MLReader [T] extends BaseReadWrite { Loads the ML component from the input path. */ @Since("1.6.0") def load(path: String): T + def load(path: String): T = MLEvents.withLoadInstanceEvent(this, path) { + loadImpl(path) + } + + /** + * `load()` handles events and then calls this method. Subclasses should override this + * method to implement the actual loading of the instance. + */ + @Since("3.0.0") + protected def loadImpl(path: String): T = { + // Keep this default body for backward compatibility. + throw new UnsupportedOperationException("loadImpl is not implemented.") + } // override for Java compatibility override def session(sparkSession: SparkSession): this.type = super.session(sparkSession) @@ -467,7 +479,7 @@ private [ml] object DefaultParamsWriter { */ private [ml] class DefaultParamsReader [T] extends MLReader [T] { override def load(path: String): T = { + override protected def loadImpl(path: String): T = { val metadata = DefaultParamsReader.loadMetadata(path, sc) val cls = Utils.classForName(metadata.className) val instance = diff --git a/mllib/src/test/scala/org/apache/spark/ml/MLEventsSuite.scala b/mllib/src/test/scala/org/apache/spark/ml/MLEventsSuite.scala new file mode 100644 index 0000000000000..e63eef870d985 /dev/null +++ b/mllib/src/test/scala/org/apache/spark/ml/MLEventsSuite.scala @@ -0,0 +1,183 @@ +/* + * Licensed to the Apache Software Foundation (ASF) under one or more + * contributor license agreements. See the NOTICE file distributed with + * this work for additional information regarding copyright ownership. + * The ASF licenses this file to You under the Apache License, Version 2.0 + * (the "License"); you may not use this file except in compliance with + * the License. You may obtain a copy of the License at + * + * http://www.apache.org/licenses/LICENSE-2.0 + * + * Unless required by applicable law or agreed to in writing, software + * distributed under the License is distributed on an "AS IS" BASIS, + * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. + * See the License for the specific language governing permissions and + * limitations under the License. + */ + +package org.apache.spark.ml + +import scala.collection.mutable +import scala.concurrent.duration._ +import scala.language.postfixOps + +import org.apache.hadoop.fs.Path +import org.mockito.Matchers. {any, eq => meq} +import org.mockito.Mockito.when +import org.scalatest.BeforeAndAfterEach +import org.scalatest.concurrent.Eventually +import org.scalatest.mockito.MockitoSugar.mock + +import org.apache.spark.SparkFunSuite +import org.apache.spark.ml.param.ParamMap +import org.apache.spark.mllib.util.MLlibTestSparkContext +import org.apache.spark.scheduler. {SparkListener, SparkListenerEvent} +import org.apache.spark.sql._ + + +class MLEventsSuite + extends SparkFunSuite + with BeforeAndAfterEach + with MLlibTestSparkContext + with Eventually { + + private val dirName: String = "pipeline" + private val events = mutable.ArrayBuffer.empty [MLEvent] + private val listener: SparkListener = new SparkListener Unknown macro: {+ override def onOtherEvent(event} + + override def beforeAll(): Unit = { + super.beforeAll() + spark.sparkContext.addSparkListener(listener) + } + + override def afterEach(): Unit = Unknown macro: {+ try { + events.clear() + } finally { + super.afterEach() + }+ } + + override def afterAll(): Unit = { + try Unknown macro: {+ if (spark != null) { + spark.sparkContext.removeSparkListener(listener) + }+ } finally { + super.afterAll() + } + } + + abstract class MyModel extends Model [MyModel] + + test("pipeline fit events") Unknown macro: {+ val estimator0 = mock[Estimator[MyModel]]+ val model0 = mock[MyModel]+ val transformer1 = mock[Transformer]+ val estimator2 = mock[Estimator[MyModel]]+ val model2 = mock[MyModel]+ val transformer3 = mock[Transformer]++ when(estimator0.copy(any[ParamMap])).thenReturn(estimator0)+ when(model0.copy(any[ParamMap])).thenReturn(model0)+ when(transformer1.copy(any[ParamMap])).thenReturn(transformer1)+ when(estimator2.copy(any[ParamMap])).thenReturn(estimator2)+ when(model2.copy(any[ParamMap])).thenReturn(model2)+ when(transformer3.copy(any[ParamMap])).thenReturn(transformer3)++ val dataset0 = mock[DataFrame]+ val dataset1 = mock[DataFrame]+ val dataset2 = mock[DataFrame]+ val dataset3 = mock[DataFrame]+ val dataset4 = mock[DataFrame]++ when(dataset0.toDF).thenReturn(dataset0)+ when(dataset1.toDF).thenReturn(dataset1)+ when(dataset2.toDF).thenReturn(dataset2)+ when(dataset3.toDF).thenReturn(dataset3)+ when(dataset4.toDF).thenReturn(dataset4)++ when(estimator0.fit(meq(dataset0))).thenReturn(model0)+ when(model0.transform(meq(dataset0))).thenReturn(dataset1)+ when(model0.parent).thenReturn(estimator0)+ when(transformer1.transform(meq(dataset1))).thenReturn(dataset2)+ when(estimator2.fit(meq(dataset2))).thenReturn(model2)+ when(model2.transform(meq(dataset2))).thenReturn(dataset3)+ when(model2.parent).thenReturn(estimator2)+ when(transformer3.transform(meq(dataset3))).thenReturn(dataset4)++ val pipeline = new Pipeline()+ .setStages(Array(estimator0, transformer1, estimator2, transformer3))+ val pipelineModel = pipeline.fit(dataset0)++ val expected =+ FitStart(pipeline, dataset0) } + + test("pipeline read/write events") { + withTempDir Unknown macro: { dir =>+ val path = new Path(dir.getCanonicalPath, dirName).toUri.toString+ val writableStage = new WritableStage("writableStage")+ val newPipeline = new Pipeline().setStages(Array(writableStage))+ val pipelineWriter = newPipeline.write+ pipelineWriter.save(path)++ val expected =+ SaveInstanceStart(pipelineWriter, path) } + } +} ---------------------------------------------------------------- This is an automated message from the Apache Git Service. To respond to the message, please log on GitHub and use the URL above to go to the specific comment. For queries about this service, please contact Infrastructure at: users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [12/Dec/18 07:03](https://issues.apache.org/jira/browse/SPARK-23674?focusedCommentId=16718527&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16718527)
HyukjinKwon opened a new pull request #23263: [~~SPARK-23674~~](https://issues.apache.org/jira/browse/SPARK-23674 "Add Spark ML Listener for Tracking ML Pipeline Status")[ML] Adds Spark ML Events
URL: <https://github.com/apache/spark/pull/23263>
  1.     1. What changes were proposed in this pull request?

This PR proposes to add ML events so that other developers can track and add some actions for them.
  1.     1. Introduction

ML events (like SQL events) can be quite useful when people want to track and make some actions for corresponding ML operations. For instance, I have been working on integrating
Apache Spark with [Apache Atlas](<https://atlas.apache.org/QuickStart.html>). With some custom changes with this PR, I can visualise ML pipeline as below:
![spark_ml_streaming_lineage](<https://user-images.githubusercontent.com/6477701/49682779-394bca80-faf5-11e8-85b8-5fae28b784b3.png>)
Another good thing that might have to be considered is, that we can interact this with other SQL/Streaming events. For instance, where the input `Dataset` is originated. For instance, with current Apache Spark, I can visualise SQL operations as below:
![screen shot 2018-12-10 at 9 41 36 am](<https://user-images.githubusercontent.com/6477701/49706269-d9bdfe00-fc5f-11e8-943a-3309d1856ba5.png>)
I think we can combine those existing lineages together to easily understand where the data comes and goes. Currently, ML side is a hole so the lineages can't be connected for the current Apache Spark ..
To add up, I think it's not to mention how useful it is to track the SQL/Streaming operations. Likewise, I would like to propose ML events as well (as lowest stability `@Unstable` APIs for now - no guarantee about stability).
  1.     1. Implementation Details

  1.     1.       1. Sends event (but not expose ML specific listener)

* **`mllib/src/main/scala/org/apache/spark/ml/events.scala`** *
```scala
@Unstable
case class ...StartEvent(caller, input)
@Unstable
case class ...EndEvent(caller, output)
object MLEvents {
// Wrappers to send events:
// def with...Event(body) =
{ // body() // SparkContext.getOrCreate().listenerBus.post(event) // }
}
```
This way mimics both:
* **1. Catalog events (see `org/apache/spark/sql/catalyst/catalog/events.scala`)** *
  * This allows a Catalog specific listener to be added `ExternalCatalogEventListener`

  * It's implemented in a way of wrapping whole `ExternalCatalog` named `ExternalCatalogWithListener`
which delegates the operations to `ExternalCatalog`

This is not quite possible in this case because most of instances (like `Pipeline`) will be directly created in most of cases. We might be able to do that via extending `ListenerBus` for all possible instances but IMHO it's too invasive. Also, exposing another ML specific listener sounds a bit too much at this stage. Therefore, I simply borrowed file name and structures here
* **2. SQL execution events (see `org/apache/spark/sql/execution/SQLExecution.scala`)** *
  * Add an object that wraps a body to send events

Current apporach is rather close to this. It has a `with...` wrapper to send events. I borrowed this approach to be consistent.
  1.     1.       1. Add `...Impl` methods to wrap each to send events

* **`mllib/src/main/scala/org/apache/spark/ml/util/ReadWrite.scala`** *
```diff
  * def save(...) = { saveImpl(...) }
+ def save(...) = MLEvents.withSaveInstanceEvent { saveImpl(...) }
def saveImpl(...): Unit = ...
```

Note that `saveImpl` was already implemented unlike other instances below.
```diff
  * def load(...): T
+ def load(...): T = MLEvents.withLoadInstanceEvent { loadImple(...) }
+ def loadImpl(...): T
```

* **`mllib/src/main/scala/org/apache/spark/ml/Estimator.scala`** *
```diff
  * def fit(...): Model
+ def fit(...): Model = MLEvents.withFitEvent { fitImpl(...) }
+ def fitImpl(...): Model
```

* **`mllib/src/main/scala/org/apache/spark/ml/Transformer.scala`** *
```diff
  * def transform(...): DataFrame
+ def transform(...): DataFrame = MLEvents.withTransformEvent { transformImpl(...) }
+ def transformImpl(...): DataFrame
```

This approach follows the existing way as below in ML:
* **1. `transform` and `transformImpl`** *
<https://github.com/apache/spark/blob/9b1f6c8bab5401258c653d4e2efb50e97c6d282f/mllib/src/main/scala/org/apache/spark/ml/Predictor.scala#L202-L213>
<https://github.com/apache/spark/blob/9b1f6c8bab5401258c653d4e2efb50e97c6d282f/mllib/src/main/scala/org/apache/spark/ml/regression/DecisionTreeRegressor.scala#L191-L196>
<https://github.com/apache/spark/blob/9b1f6c8bab5401258c653d4e2efb50e97c6d282f/mllib/src/main/scala/org/apache/spark/ml/regression/GeneralizedLinearRegression.scala#L1037-L1042>
* **2. `save` and `saveImpl`** *
<https://github.com/apache/spark/blob/9b1f6c8bab5401258c653d4e2efb50e97c6d282f/mllib/src/main/scala/org/apache/spark/ml/util/ReadWrite.scala#L166-L176>
Inherited ones are intentionally omitted here for simplicity. They are inherited and implemented at multiple places.
  1.     1. Usage

It needs a custom implementation for a query listener. For instance,
with the custom listener below:
```scala
class CustomMLListener extends SparkListener
def onOtherEvents(e) = e match
{ case e: MLEvent => // do something case _ => // pass }
}
```
There are two (existing) ways to use this.
```scala
spark.sparkContext.addSparkListener(new CustomMLListener)
```
```bash
spark-submit ...\
--conf spark.extraListeners=CustomMLListener\
...
```
It's also similar with other existing implementation in SQL side.
  1.     1. Target users

1. I think someone in general would likely utilise this feature like other event listeners. At least, I can see some interests going on outside.
  * SQL Listener
  * <https://stackoverflow.com/questions/46409339/spark-listener-to-an-sql-query>
  * <http://apache-spark-user-list.1001560.n3.nabble.com/spark-sql-Custom-Query-Execution-listener-via-conf-properties-td30979.html>

  * Streaming Query Listener
  * <https://jhui.github.io/2017/01/15/Apache-Spark-Streaming/>
  * <http://apache-spark-developers-list.1001551.n3.nabble.com/Structured-Streaming-with-Watermark-td25413.html#a25416>

2. Someone would likely run this via Atlas. The plugin mirror intentionally is exposed at [spark-atlas-connector](<https://github.com/hortonworks-spark/spark-atlas-connector>) so that anyone could do something about lineage and governance in Atlas, yes, as you said. Yes, I'm trying to show integrated lineages in Apache Spark but this is a missing hole. There had to be this change for it.
  1.     1. Backward Compatibility

_This keeps both source and binary backward compatibility_. I was thinking enforcing `...Impl` by leaving it abstract methods to force to implement but just decided to leave a body that throws `UnsupportedOperationException` so that we can keep full source and binary compatibilities.
  * For user-faced API perspective, _there's no difference_. `...Impl` methods are protected and not visible to end users.

  * For developer API perspective, if some developers want to `...` methods instead of `...Impl`, that's still fine. It only does not handle events. If developers want to handle events from their custom implementation, they should implement `...Impl`. Of course, it is encouraged to implement `...Impl`

For instance,
```scala
class Pipeline extends Estimator[PipelineModel] {
def fit(dataset: Dataset[_]): PipelineModel =
{ ... }
}
```
still works fine without any behaviour changes.
If developers want their pipeline to emit events, they should change:
```diff
class Pipeline extends Estimator[PipelineModel] {
  * def fit(dataset: Dataset[_]): PipelineModel =
Unknown macro: { + def fitImpl(dataset}
```

_^ this is only API change this PR causes._
  1.     1. How was this patch tested?

Manually tested and unit tests were added.
----------------------------------------------------------------
This is an automated message from the Apache Git Service.
To respond to the message, please log on GitHub and use the
URL above to go to the specific comment.
For queries about this service, please contact Infrastructure at:
users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [12/Dec/18 07:03](https://issues.apache.org/jira/browse/SPARK-23674?focusedCommentId=16718527&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16718527) HyukjinKwon opened a new pull request #23263: SPARK-23674 [ML] Adds Spark ML Events URL: https://github.com/apache/spark/pull/23263 What changes were proposed in this pull request? This PR proposes to add ML events so that other developers can track and add some actions for them. Introduction ML events (like SQL events) can be quite useful when people want to track and make some actions for corresponding ML operations. For instance, I have been working on integrating Apache Spark with [Apache Atlas] ( https://atlas.apache.org/QuickStart.html ). With some custom changes with this PR, I can visualise ML pipeline as below: ! [spark_ml_streaming_lineage] ( https://user-images.githubusercontent.com/6477701/49682779-394bca80-faf5-11e8-85b8-5fae28b784b3.png ) Another good thing that might have to be considered is, that we can interact this with other SQL/Streaming events. For instance, where the input `Dataset` is originated. For instance, with current Apache Spark, I can visualise SQL operations as below: ! [screen shot 2018-12-10 at 9 41 36 am] ( https://user-images.githubusercontent.com/6477701/49706269-d9bdfe00-fc5f-11e8-943a-3309d1856ba5.png ) I think we can combine those existing lineages together to easily understand where the data comes and goes. Currently, ML side is a hole so the lineages can't be connected for the current Apache Spark .. To add up, I think it's not to mention how useful it is to track the SQL/Streaming operations. Likewise, I would like to propose ML events as well (as lowest stability `@Unstable` APIs for now - no guarantee about stability). Implementation Details Sends event (but not expose ML specific listener) * `mllib/src/main/scala/org/apache/spark/ml/events.scala` * ```scala @Unstable case class ...StartEvent(caller, input) @Unstable case class ...EndEvent(caller, output) object MLEvents { // Wrappers to send events: // def with...Event(body) = { // body() // SparkContext.getOrCreate().listenerBus.post(event) // } } ``` This way mimics both: * 1. Catalog events (see `org/apache/spark/sql/catalyst/catalog/events.scala`) * This allows a Catalog specific listener to be added `ExternalCatalogEventListener` It's implemented in a way of wrapping whole `ExternalCatalog` named `ExternalCatalogWithListener` which delegates the operations to `ExternalCatalog` This is not quite possible in this case because most of instances (like `Pipeline`) will be directly created in most of cases. We might be able to do that via extending `ListenerBus` for all possible instances but IMHO it's too invasive. Also, exposing another ML specific listener sounds a bit too much at this stage. Therefore, I simply borrowed file name and structures here * 2. SQL execution events (see `org/apache/spark/sql/execution/SQLExecution.scala`) * Add an object that wraps a body to send events Current apporach is rather close to this. It has a `with...` wrapper to send events. I borrowed this approach to be consistent. Add `...Impl` methods to wrap each to send events * `mllib/src/main/scala/org/apache/spark/ml/util/ReadWrite.scala` * ```diff def save(...) = { saveImpl(...) } + def save(...) = MLEvents.withSaveInstanceEvent { saveImpl(...) } def saveImpl(...): Unit = ... ``` Note that `saveImpl` was already implemented unlike other instances below. ```diff def load(...): T + def load(...): T = MLEvents.withLoadInstanceEvent { loadImple(...) } + def loadImpl(...): T ``` * `mllib/src/main/scala/org/apache/spark/ml/Estimator.scala` * ```diff def fit(...): Model + def fit(...): Model = MLEvents.withFitEvent { fitImpl(...) } + def fitImpl(...): Model ``` * `mllib/src/main/scala/org/apache/spark/ml/Transformer.scala` * ```diff def transform(...): DataFrame + def transform(...): DataFrame = MLEvents.withTransformEvent { transformImpl(...) } + def transformImpl(...): DataFrame ``` This approach follows the existing way as below in ML: * 1. `transform` and `transformImpl` * https://github.com/apache/spark/blob/9b1f6c8bab5401258c653d4e2efb50e97c6d282f/mllib/src/main/scala/org/apache/spark/ml/Predictor.scala#L202-L213 https://github.com/apache/spark/blob/9b1f6c8bab5401258c653d4e2efb50e97c6d282f/mllib/src/main/scala/org/apache/spark/ml/regression/DecisionTreeRegressor.scala#L191-L196 https://github.com/apache/spark/blob/9b1f6c8bab5401258c653d4e2efb50e97c6d282f/mllib/src/main/scala/org/apache/spark/ml/regression/GeneralizedLinearRegression.scala#L1037-L1042 * 2. `save` and `saveImpl` * https://github.com/apache/spark/blob/9b1f6c8bab5401258c653d4e2efb50e97c6d282f/mllib/src/main/scala/org/apache/spark/ml/util/ReadWrite.scala#L166-L176 Inherited ones are intentionally omitted here for simplicity. They are inherited and implemented at multiple places. Usage It needs a custom implementation for a query listener. For instance, with the custom listener below: ```scala class CustomMLListener extends SparkListener def onOtherEvents(e) = e match { case e: MLEvent => // do something case _ => // pass } } ``` There are two (existing) ways to use this. ```scala spark.sparkContext.addSparkListener(new CustomMLListener) ``` ```bash spark-submit ...\ --conf spark.extraListeners=CustomMLListener\ ... ``` It's also similar with other existing implementation in SQL side. Target users 1. I think someone in general would likely utilise this feature like other event listeners. At least, I can see some interests going on outside. SQL Listener https://stackoverflow.com/questions/46409339/spark-listener-to-an-sql-query http://apache-spark-user-list.1001560.n3.nabble.com/spark-sql-Custom-Query-Execution-listener-via-conf-properties-td30979.html Streaming Query Listener https://jhui.github.io/2017/01/15/Apache-Spark-Streaming/ http://apache-spark-developers-list.1001551.n3.nabble.com/Structured-Streaming-with-Watermark-td25413.html#a25416 2. Someone would likely run this via Atlas. The plugin mirror intentionally is exposed at [spark-atlas-connector] ( https://github.com/hortonworks-spark/spark-atlas-connector ) so that anyone could do something about lineage and governance in Atlas, yes, as you said. Yes, I'm trying to show integrated lineages in Apache Spark but this is a missing hole. There had to be this change for it. Backward Compatibility This keeps both source and binary backward compatibility . I was thinking enforcing `...Impl` by leaving it abstract methods to force to implement but just decided to leave a body that throws `UnsupportedOperationException` so that we can keep full source and binary compatibilities. For user-faced API perspective, there's no difference . `...Impl` methods are protected and not visible to end users. For developer API perspective, if some developers want to `...` methods instead of `...Impl`, that's still fine. It only does not handle events. If developers want to handle events from their custom implementation, they should implement `...Impl`. Of course, it is encouraged to implement `...Impl` For instance, ```scala class Pipeline extends Estimator [PipelineModel] { def fit(dataset: Dataset [_] ): PipelineModel = { ... } } ``` still works fine without any behaviour changes. If developers want their pipeline to emit events, they should change: ```diff class Pipeline extends Estimator [PipelineModel] { def fit(dataset: Dataset [_] ): PipelineModel = Unknown macro: { + def fitImpl(dataset} ``` ^ this is only API change this PR causes. How was this patch tested? Manually tested and unit tests were added. ---------------------------------------------------------------- This is an automated message from the Apache Git Service. To respond to the message, please log on GitHub and use the URL above to go to the specific comment. For queries about this service, please contact Infrastructure at: users@infra.apache.org
[![gurwls223](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Hyukjin Kwon](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=gurwls223) added a comment - [25/Jan/19 02:12](https://issues.apache.org/jira/browse/SPARK-23674?focusedCommentId=16751809&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16751809) - edited
Issue resolved by pull request 23263
<https://github.com/apache/spark/pull/23263>
[![gurwls223](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Hyukjin Kwon](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=gurwls223) added a comment - [25/Jan/19 02:12](https://issues.apache.org/jira/browse/SPARK-23674?focusedCommentId=16751809&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16751809) - edited Issue resolved by pull request 23263 https://github.com/apache/spark/pull/23263
#### People

Assignee:
     ![gurwls223](https://issues.apache.org/jira/secure/useravatar?size=small&avatarId=10452) Hyukjin Kwon

Reporter:
     ![merlin](https://issues.apache.org/jira/secure/useravatar?size=small&avatarId=10452) Mingjie Tang

Votes:
     0 Vote for this issue

Watchers:
     6 Start watching this issue
#### Dates

Created:
     13/Mar/18 21:12

Updated:
     15/Feb/26 20:10

Resolved:
     25/Jan/19 02:12
  * Atlassian Jira [Project Management Software](https://www.atlassian.com/software/jira)
  * [About Jira](https://issues.apache.org/jira/secure/AboutPage.jspa/secure/AboutPage.jspa)
  * [Report a problem](https://issues.apache.org/jira/secure/CreateIssue!default.jspa)

Powered by a free Atlassian [Jira](http://www.atlassian.com/software/jira) open source license for Apache Software Foundation. Try Jira - [bug tracking software](http://www.atlassian.com/software/jira) for _your_ team.
[Atlassian](http://www.atlassian.com/)
[](javascript:;)[](javascript:;)

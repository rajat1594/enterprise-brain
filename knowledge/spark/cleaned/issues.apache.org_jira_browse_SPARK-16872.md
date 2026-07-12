[Log in](https://issues.apache.org/jira/login.jsp?os_destination=%2Fbrowse%2FSPARK-16872)[Skip to main content](https://issues.apache.org/jira/browse/SPARK-16872#main)[Skip to sidebar](https://issues.apache.org/jira/browse/SPARK-16872#sidebar)
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
  * [Log In](https://issues.apache.org/jira/login.jsp?os_destination=%2Fbrowse%2FSPARK-16872)

Public signup for this instance is **disabled**. Go to our [Self serve sign up page](https://selfserve.apache.org/jira-account.html) to request an account. Report potential security issues [privately](https://apache.org/security/#reporting-a-vulnerability)
[![Spark](https://issues.apache.org/jira/secure/projectavatar?pid=12315420&avatarId=27346)![Project Type: software](https://issues.apache.org/jira/browse/SPARK-16872)](https://issues.apache.org/jira/projects/SPARK/summary "Spark")
#
[Spark](https://issues.apache.org/jira/projects/SPARK/summary "Spark")
  * [Issues](https://issues.apache.org/jira/projects/SPARK/issues)
  * [Reports](https://issues.apache.org/jira/projects/SPARK?selectedItem=com.atlassian.jira.jira-projects-plugin:report-page)
  * [Components](https://issues.apache.org/jira/projects/SPARK?selectedItem=com.atlassian.jira.jira-projects-plugin:components-page)
  * [Roadmap](https://issues.apache.org/jira/projects/SPARK?selectedItem=biz.everit.jira.epic-roadmap:erfj-sidebar-roadmap)

![Uploaded image for project: 'Spark'](https://issues.apache.org/jira/secure/projectavatar?pid=12315420&avatarId=27346)
  1. [Spark](https://issues.apache.org/jira/browse/SPARK)
  2. [SPARK-16872](https://issues.apache.org/jira/browse/SPARK-16872)

# Impl Gaussian Naive Bayes Classifier
[Log In](https://issues.apache.org/jira/login.jsp?os_destination=%2Fbrowse%2FSPARK-16872 "Log In")
[ Export](https://issues.apache.org/jira/browse/SPARK-16872)
[XML](https://issues.apache.org/jira/si/jira.issueviews:issue-xml/SPARK-16872/SPARK-16872.xml)[Word](https://issues.apache.org/jira/si/jira.issueviews:issue-word/SPARK-16872/SPARK-16872.doc)[Printable](https://issues.apache.org/jira/si/jira.issueviews:issue-html/SPARK-16872/SPARK-16872.html)[JSON](https://issues.apache.org/jira/si/com.atlassian.jira.plugins.jira-importers-plugin:issue-json/SPARK-16872/SPARK-16872.json)

#### Details
  * ** Type: ** ![](https://issues.apache.org/jira/secure/viewavatar?size=xsmall&avatarId=21141&avatarType=issuetype) New Feature
  * **Status:** Closed
  * ** Priority: ** ![](https://issues.apache.org/jira/images/icons/priorities/major.svg) Major
  * **Resolution:** Fixed
  * ** Affects Version/s: ** None
  * ** Fix Version/s:  ** [3.0.0](https://issues.apache.org/jira/issues/?jql=project+%3D+SPARK+AND+fixVersion+%3D+3.0.0 "3.0.0 ")
  * ** Component/s: ** [ML](https://issues.apache.org/jira/issues/?jql=project+%3D+SPARK+AND+component+%3D+ML "ML Features under the spark.ml package"), [PySpark](https://issues.apache.org/jira/issues/?jql=project+%3D+SPARK+AND+component+%3D+PySpark "PySpark Spark Python API")
  * ** Labels: **
None

#### Description
I implemented Gaussian NB according to scikit-learn's `GaussianNB`.
In GaussianNB model, the `theta` matrix is used to store means and there is a extra `sigma` matrix storing the variance of each feature.
GaussianNB in spark

```
scala> import org.apache.spark.ml.classification.GaussianNaiveBayes
import org.apache.spark.ml.classification.GaussianNaiveBayes

scala> val path = "/Users/zrf/.dev/spark-2.1.0-bin-hadoop2.7/data/mllib/sample_multiclass_classification_data.txt"
path: String = /Users/zrf/.dev/spark-2.1.0-bin-hadoop2.7/data/mllib/sample_multiclass_classification_data.txt

scala> val data = spark.read.format("libsvm").load(path).persist()
data: org.apache.spark.sql.Dataset[org.apache.spark.sql.Row] = [label: double, features: vector]

scala> val gnb = new GaussianNaiveBayes()
gnb: org.apache.spark.ml.classification.GaussianNaiveBayes = gnb_54c50467306c

scala> val model = gnb.fit(data)
17/01/03 14:25:48 INFO Instrumentation: GaussianNaiveBayes-gnb_54c50467306c-720112035-1: training: numPartitions=1 storageLevel=StorageLevel(1 replicas)
17/01/03 14:25:48 INFO Instrumentation: GaussianNaiveBayes-gnb_54c50467306c-720112035-1: {}
17/01/03 14:25:49 INFO Instrumentation: GaussianNaiveBayes-gnb_54c50467306c-720112035-1: {"numFeatures":4}
17/01/03 14:25:49 INFO Instrumentation: GaussianNaiveBayes-gnb_54c50467306c-720112035-1: {"numClasses":3}
17/01/03 14:25:49 INFO Instrumentation: GaussianNaiveBayes-gnb_54c50467306c-720112035-1: training finished
model: org.apache.spark.ml.classification.GaussianNaiveBayesModel = GaussianNaiveBayesModel (uid=gnb_54c50467306c) with 3 classes

scala> model.pi
res0: org.apache.spark.ml.linalg.Vector = [-1.0986122886681098,-1.0986122886681098,-1.0986122886681098]

scala> model.pi.toArray.map(math.exp)
res1: Array[Double] = Array(0.3333333333333333, 0.3333333333333333, 0.3333333333333333)

scala> model.theta
res2: org.apache.spark.ml.linalg.Matrix =
0.2711110067018001   -0.18833335400000006  0.5430507200000001   0.605000046
-0.6077777799999998  0.181666672           -0.8427117400000006  -0.8800001399999998
-0.0911111425964     -0.3583333580000001   0.105084738          0.021666701507102017

scala> model.sigma
res3: org.apache.spark.ml.linalg.Matrix =
0.1223012510889361   0.07078051983960698  0.03430000595243976   0.051336071297393815
0.03758145300924998  0.09880280046403413  0.003390296940069426  0.007822241779598893
0.08058763609659315  0.06701386661293329  0.024866409227781675  0.02661391644759426

scala> model.transform(data).select("probability").take(10)
[rdd_68_0]
res4: Array[org.apache.spark.sql.Row] = Array([[1.0627410543476422E-21,0.9999999999999938,6.2765233965353945E-15]], [[7.254521422345374E-26,1.0,1.3849442153180895E-18]], [[1.9629244119173135E-24,0.9999999999999998,1.9424765181237926E-16]], [[6.061218297948492E-22,0.9999999999999902,9.853216073401884E-15]], [[0.9972225671942837,8.844241161578932E-165,0.002777432805716399]], [[5.361683970373604E-26,1.0,2.3004604508982183E-18]], [[0.01062850630038623,3.3102617689978775E-100,0.9893714936996136]], [[1.9297314618271785E-4,2.124922209137708E-71,0.9998070268538172]], [[3.118816393732361E-27,1.0,6.5310299615983584E-21]], [[0.9999926009854522,8.734773657627494E-206,7.399014547943611E-6]])

scala> model.transform(data).select("prediction").take(10)
[rdd_68_0]
res5: Array[org.apache.spark.sql.Row] = Array([1.0], [1.0], [1.0], [1.0], [0.0], [1.0], [2.0], [2.0], [1.0], [0.0])

```

GaussianNB in scikit-learn

```
import numpy as np
from sklearn.naive_bayes import GaussianNB
from sklearn.datasets import load_svmlight_file

path = '/Users/zrf/.dev/spark-2.1.0-bin-hadoop2.7/data/mllib/sample_multiclass_classification_data.txt'
X, y = load_svmlight_file(path)
X = X.toarray()

clf = GaussianNB()

clf.fit(X, y)

>>> clf.class_prior_
array([ 0.33333333,  0.33333333,  0.33333333])

>>> clf.theta_
array([[ 0.27111101, -0.18833335,  0.54305072,  0.60500005],
       [-0.60777778,  0.18166667, -0.84271174, -0.88000014],
       [-0.09111114, -0.35833336,  0.10508474,  0.0216667 ]])

>>> clf.sigma_
array([[ 0.12230125,  0.07078052,  0.03430001,  0.05133607],
       [ 0.03758145,  0.0988028 ,  0.0033903 ,  0.00782224],
       [ 0.08058764,  0.06701387,  0.02486641,  0.02661392]])

>>> clf.predict_proba(X)[:10]
array([[  1.06274105e-021,   1.00000000e+000,   6.27652340e-015],
       [  7.25452142e-026,   1.00000000e+000,   1.38494422e-018],
       [  1.96292441e-024,   1.00000000e+000,   1.94247652e-016],
       [  6.06121830e-022,   1.00000000e+000,   9.85321607e-015],
       [  9.97222567e-001,   8.84424116e-165,   2.77743281e-003],
       [  5.36168397e-026,   1.00000000e+000,   2.30046045e-018],
       [  1.06285063e-002,   3.31026177e-100,   9.89371494e-001],
       [  1.92973146e-004,   2.12492221e-071,   9.99807027e-001],
       [  3.11881639e-027,   1.00000000e+000,   6.53102996e-021],
       [  9.99992601e-001,   8.73477366e-206,   7.39901455e-006]])

>>> clf.predict(X)[:10]
array([ 1.,  1.,  1.,  1.,  0.,  1.,  2.,  2.,  1.,  0.])

```

#### Attachments
#### Issue Links

relates to

![New Feature - A new feature of the product, which has yet to be developed.](https://issues.apache.org/jira/secure/viewavatar?size=xsmall&avatarId=21141&avatarType=issuetype) [SPARK-14077](https://issues.apache.org/jira/browse/SPARK-14077) Support weighted instances in naive Bayes
  * ![Major - Major loss of function.](https://issues.apache.org/jira/images/icons/priorities/major.svg)
  * Closed

links to

![Pull request #15324](https://assets-cdn.github.com/favicon.ico) [[Github] Pull Request #15324 (zhengruifeng)](https://github.com/apache/spark/pull/15324)
![Pull request #18589](https://assets-cdn.github.com/favicon.ico) [[Github] Pull Request #18589 (zhengruifeng)](https://github.com/apache/spark/pull/18589)
![Web Link](https://github.com/favicon.ico) [GitHub Pull Request #26413](https://github.com/apache/spark/pull/26413)
#### Activity
  * [All](https://issues.apache.org/jira/browse/SPARK-16872?page=com.atlassian.jira.plugin.system.issuetabpanels:all-tabpanel)
  * Comments
  * [Work Log](https://issues.apache.org/jira/browse/SPARK-16872?page=com.atlassian.jira.plugin.system.issuetabpanels:worklog-tabpanel)
  * [History](https://issues.apache.org/jira/browse/SPARK-16872?page=com.atlassian.jira.plugin.system.issuetabpanels:changehistory-tabpanel)
  * [Activity](https://issues.apache.org/jira/browse/SPARK-16872?page=com.atlassian.streams.streams-jira-plugin:activity-stream-issue-tab)
  * [Transitions](https://issues.apache.org/jira/browse/SPARK-16872?page=com.googlecode.jira-suite-utilities:transitions-summary-tabpanel)

[ Ascending order - Click to sort in descending order ](https://issues.apache.org/jira/browse/SPARK-16872?actionOrder=desc "Ascending order - Click to sort in descending order")
[![podongfeng](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Ruifeng Zheng](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=podongfeng) added a comment - [03/Aug/16 08:32](https://issues.apache.org/jira/browse/SPARK-16872?focusedCommentId=15405570&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15405570)
cc [yanboliang](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=yanboliang) [josephkb](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=josephkb) [mengxr](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=mengxr)
[![podongfeng](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Ruifeng Zheng](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=podongfeng) added a comment - [03/Aug/16 08:32](https://issues.apache.org/jira/browse/SPARK-16872?focusedCommentId=15405570&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15405570) cc yanboliang josephkb mengxr
[![mlnick](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Nicholas Pentreath](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=mlnick) added a comment - [05/Aug/16 06:40](https://issues.apache.org/jira/browse/SPARK-16872?focusedCommentId=15408986&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15408986)
I think this would be good to add - though we would only add it to `ml` package API given `mllib` is maintenance mode. Are you working on a PR?
[![mlnick](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Nicholas Pentreath](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=mlnick) added a comment - [05/Aug/16 06:40](https://issues.apache.org/jira/browse/SPARK-16872?focusedCommentId=15408986&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15408986) I think this would be good to add - though we would only add it to ml package API given mllib is maintenance mode. Are you working on a PR?
[![yanboliang](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Yanbo Liang](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=yanboliang) added a comment - [05/Aug/16 07:19](https://issues.apache.org/jira/browse/SPARK-16872?focusedCommentId=15409047&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15409047)
+1 [mlnick](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=mlnick)
But currently `ml.NaiveBayes` is only a wrapper of `mllib.NaiveBayes` and the actual fit process is still in `mllib`. Should we move the code of fit to `ml` and let `mllib` call `ml` firstly? Then it will be simple to add new features to it. Actually `mllib.LogisticRegressionWithLBFGS` has already done similar conversion. Thanks!
[![yanboliang](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Yanbo Liang](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=yanboliang) added a comment - [05/Aug/16 07:19](https://issues.apache.org/jira/browse/SPARK-16872?focusedCommentId=15409047&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15409047) +1 mlnick But currently ml.NaiveBayes is only a wrapper of mllib.NaiveBayes and the actual fit process is still in mllib . Should we move the code of fit to ml and let mllib call ml firstly? Then it will be simple to add new features to it. Actually mllib.LogisticRegressionWithLBFGS has already done similar conversion. Thanks!
[![podongfeng](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Ruifeng Zheng](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=podongfeng) added a comment - [05/Aug/16 07:20](https://issues.apache.org/jira/browse/SPARK-16872?focusedCommentId=15409048&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15409048)
I am working on it. When finished, I will make a PR.
[![podongfeng](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Ruifeng Zheng](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=podongfeng) added a comment - [05/Aug/16 07:20](https://issues.apache.org/jira/browse/SPARK-16872?focusedCommentId=15409048&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15409048) I am working on it. When finished, I will make a PR.
[![yanboliang](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Yanbo Liang](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=yanboliang) added a comment - [05/Aug/16 07:38](https://issues.apache.org/jira/browse/SPARK-16872?focusedCommentId=15409071&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15409071)
[podongfeng](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=podongfeng) This task can be worked together with [~~SPARK-14077~~](https://issues.apache.org/jira/browse/SPARK-14077 "Support weighted instances in naive Bayes"). Let's separate the task into the following steps:
  * Move the `NaiveBayes` implementation from `mllib` to `ml` and make `mllib` as a wrapper to call `ml`.
  * Support weighted instances (Only for `ml`).
  * Support GaussianNB (Only for `ml`).

[mlnick](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=mlnick) [josephkb](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=josephkb) [mengxr](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=mengxr) What about your opinion?
[![yanboliang](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Yanbo Liang](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=yanboliang) added a comment - [05/Aug/16 07:38](https://issues.apache.org/jira/browse/SPARK-16872?focusedCommentId=15409071&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15409071) podongfeng This task can be worked together with SPARK-14077 . Let's separate the task into the following steps: Move the NaiveBayes implementation from mllib to ml and make mllib as a wrapper to call ml . Support weighted instances (Only for ml ). Support GaussianNB (Only for ml ). mlnick josephkb mengxr What about your opinion?
[![mlnick](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Nicholas Pentreath](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=mlnick) added a comment - [05/Aug/16 07:51](https://issues.apache.org/jira/browse/SPARK-16872?focusedCommentId=15409086&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15409086)
Sounds good to me
[![mlnick](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Nicholas Pentreath](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=mlnick) added a comment - [05/Aug/16 07:51](https://issues.apache.org/jira/browse/SPARK-16872?focusedCommentId=15409086&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15409086) Sounds good to me
[![apachespark](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Apache Spark](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=apachespark) added a comment - [02/Oct/16 02:40](https://issues.apache.org/jira/browse/SPARK-16872?focusedCommentId=15539581&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15539581)
User 'zhengruifeng' has created a pull request for this issue:
<https://github.com/apache/spark/pull/15324>
[![apachespark](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Apache Spark](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=apachespark) added a comment - [02/Oct/16 02:40](https://issues.apache.org/jira/browse/SPARK-16872?focusedCommentId=15539581&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15539581) User 'zhengruifeng' has created a pull request for this issue: https://github.com/apache/spark/pull/15324
[![apachespark](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Apache Spark](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=apachespark) added a comment - [10/Jul/17 11:36](https://issues.apache.org/jira/browse/SPARK-16872?focusedCommentId=16080200&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16080200)
User 'zhengruifeng' has created a pull request for this issue:
<https://github.com/apache/spark/pull/18589>
[![apachespark](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Apache Spark](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=apachespark) added a comment - [10/Jul/17 11:36](https://issues.apache.org/jira/browse/SPARK-16872?focusedCommentId=16080200&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16080200) User 'zhengruifeng' has created a pull request for this issue: https://github.com/apache/spark/pull/18589
[![podongfeng](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Ruifeng Zheng](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=podongfeng) added a comment - [20/Mar/18 10:57](https://issues.apache.org/jira/browse/SPARK-16872?focusedCommentId=16406128&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16406128)
I think both 1) a new GNB estimator and 2) current NB includes Gaussian are OK.
[mlnick](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=mlnick) [josephkb](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=josephkb) [yanboliang](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=yanboliang) What are your thoughts?
It has been a long time since my first PR, and I really hope to finish it in following months. Could you help shepherding this ?
[![podongfeng](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Ruifeng Zheng](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=podongfeng) added a comment - [20/Mar/18 10:57](https://issues.apache.org/jira/browse/SPARK-16872?focusedCommentId=16406128&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16406128) I think both 1) a new GNB estimator and 2) current NB includes Gaussian are OK. mlnick josephkb yanboliang What are your thoughts? It has been a long time since my first PR, and I really hope to finish it in following months. Could you help shepherding this ?
[![podongfeng](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Ruifeng Zheng](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=podongfeng) added a comment - [18/Nov/19 02:09](https://issues.apache.org/jira/browse/SPARK-16872?focusedCommentId=16976231&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16976231)
Issue resolved by pull request 26413
<https://github.com/apache/spark/pull/26413>
[![podongfeng](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Ruifeng Zheng](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=podongfeng) added a comment - [18/Nov/19 02:09](https://issues.apache.org/jira/browse/SPARK-16872?focusedCommentId=16976231&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16976231) Issue resolved by pull request 26413 https://github.com/apache/spark/pull/26413
#### People

Assignee:
     ![podongfeng](https://issues.apache.org/jira/secure/useravatar?size=small&avatarId=10452) Ruifeng Zheng

Reporter:
     ![podongfeng](https://issues.apache.org/jira/secure/useravatar?size=small&avatarId=10452) Ruifeng Zheng

Shepherd:
     ![Yanbo Liang](https://issues.apache.org/jira/secure/useravatar?avatarId=10452) Yanbo Liang

Votes:
     0 Vote for this issue

Watchers:
     5 Start watching this issue
#### Dates

Created:
     03/Aug/16 08:30

Updated:
     15/Feb/26 20:10

Resolved:
     18/Nov/19 02:09
  * Atlassian Jira [Project Management Software](https://www.atlassian.com/software/jira)
  * [About Jira](https://issues.apache.org/jira/secure/AboutPage.jspa/secure/AboutPage.jspa)
  * [Report a problem](https://issues.apache.org/jira/secure/CreateIssue!default.jspa)

Powered by a free Atlassian [Jira](http://www.atlassian.com/software/jira) open source license for Apache Software Foundation. Try Jira - [bug tracking software](http://www.atlassian.com/software/jira) for _your_ team.
[Atlassian](http://www.atlassian.com/)
[](javascript:;)[](javascript:;)

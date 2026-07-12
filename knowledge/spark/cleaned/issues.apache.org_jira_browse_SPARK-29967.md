[Log in](https://issues.apache.org/jira/login.jsp?os_destination=%2Fbrowse%2FSPARK-29967)[Skip to main content](https://issues.apache.org/jira/browse/SPARK-29967#main)[Skip to sidebar](https://issues.apache.org/jira/browse/SPARK-29967#sidebar)
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
  * [Log In](https://issues.apache.org/jira/login.jsp?os_destination=%2Fbrowse%2FSPARK-29967)

Public signup for this instance is **disabled**. Go to our [Self serve sign up page](https://selfserve.apache.org/jira-account.html) to request an account. Report potential security issues [privately](https://apache.org/security/#reporting-a-vulnerability)
[![Spark](https://issues.apache.org/jira/secure/projectavatar?pid=12315420&avatarId=27346)![Project Type: software](https://issues.apache.org/jira/browse/SPARK-29967)](https://issues.apache.org/jira/projects/SPARK/summary "Spark")
#
[Spark](https://issues.apache.org/jira/projects/SPARK/summary "Spark")
  * [Issues](https://issues.apache.org/jira/projects/SPARK/issues)
  * [Reports](https://issues.apache.org/jira/projects/SPARK?selectedItem=com.atlassian.jira.jira-projects-plugin:report-page)
  * [Components](https://issues.apache.org/jira/projects/SPARK?selectedItem=com.atlassian.jira.jira-projects-plugin:components-page)
  * [Roadmap](https://issues.apache.org/jira/projects/SPARK?selectedItem=biz.everit.jira.epic-roadmap:erfj-sidebar-roadmap)

![Uploaded image for project: 'Spark'](https://issues.apache.org/jira/secure/projectavatar?pid=12315420&avatarId=27346)
  1. [Spark](https://issues.apache.org/jira/browse/SPARK)
  2. [SPARK-29967](https://issues.apache.org/jira/browse/SPARK-29967)

# KMeans support instance weighting
[Log In](https://issues.apache.org/jira/login.jsp?os_destination=%2Fbrowse%2FSPARK-29967 "Log In")
[ Export](https://issues.apache.org/jira/browse/SPARK-29967)
[XML](https://issues.apache.org/jira/si/jira.issueviews:issue-xml/SPARK-29967/SPARK-29967.xml)[Word](https://issues.apache.org/jira/si/jira.issueviews:issue-word/SPARK-29967/SPARK-29967.doc)[Printable](https://issues.apache.org/jira/si/jira.issueviews:issue-html/SPARK-29967/SPARK-29967.html)[JSON](https://issues.apache.org/jira/si/com.atlassian.jira.plugins.jira-importers-plugin:issue-json/SPARK-29967/SPARK-29967.json)

#### Details
  * ** Type: ** ![](https://issues.apache.org/jira/secure/viewavatar?size=xsmall&avatarId=21140&avatarType=issuetype) Improvement
  * **Status:** Closed
  * ** Priority: ** ![](https://issues.apache.org/jira/images/icons/priorities/major.svg) Major
  * **Resolution:** Fixed
  * ** Affects Version/s: ** 3.0.0
  * ** Fix Version/s:  ** [3.0.0](https://issues.apache.org/jira/issues/?jql=project+%3D+SPARK+AND+fixVersion+%3D+3.0.0 "3.0.0 ")
  * ** Component/s: ** [ML](https://issues.apache.org/jira/issues/?jql=project+%3D+SPARK+AND+component+%3D+ML "ML Features under the spark.ml package"), [PySpark](https://issues.apache.org/jira/issues/?jql=project+%3D+SPARK+AND+component+%3D+PySpark "PySpark Spark Python API")
  * ** Labels: **
None

#### Description
Since <https://issues.apache.org/jira/browse/SPARK-9610>, we start to support instance weighting in ML.
However, Clustering and other impl in features still do not support instance weighting.
I think we need to start support weighting in KMeans, like what scikit-learn does.
It will contains three parts:
1, move the impl from .mllib to .ml
2, make .mllib.KMeans as a wrapper of .ml.KMeans
3, support instance weighting in the .ml.KMeans
#### Attachments
#### Issue Links

relates to

![Umbrella - An overarching type made of sub-tasks](https://issues.apache.org/jira/secure/viewavatar?size=xsmall&avatarId=21130&avatarType=issuetype) [SPARK-9610](https://issues.apache.org/jira/browse/SPARK-9610) Class and instance weighting for ML
  * ![Major - Major loss of function.](https://issues.apache.org/jira/images/icons/priorities/major.svg)
  * Resolved

links to

![Web Link](https://github.com/favicon.ico) [GitHub Pull Request #26739](https://github.com/apache/spark/pull/26739)
![Web Link](https://github.com/favicon.ico) [GitHub Pull Request #27014](https://github.com/apache/spark/pull/27014)
#### Activity
  * [All](https://issues.apache.org/jira/browse/SPARK-29967?page=com.atlassian.jira.plugin.system.issuetabpanels:all-tabpanel)
  * Comments
  * [Work Log](https://issues.apache.org/jira/browse/SPARK-29967?page=com.atlassian.jira.plugin.system.issuetabpanels:worklog-tabpanel)
  * [History](https://issues.apache.org/jira/browse/SPARK-29967?page=com.atlassian.jira.plugin.system.issuetabpanels:changehistory-tabpanel)
  * [Activity](https://issues.apache.org/jira/browse/SPARK-29967?page=com.atlassian.streams.streams-jira-plugin:activity-stream-issue-tab)
  * [Transitions](https://issues.apache.org/jira/browse/SPARK-29967?page=com.googlecode.jira-suite-utilities:transitions-summary-tabpanel)

[ Ascending order - Click to sort in descending order ](https://issues.apache.org/jira/browse/SPARK-29967?actionOrder=desc "Ascending order - Click to sort in descending order")
[![podongfeng](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Ruifeng Zheng](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=podongfeng) added a comment - [21/Nov/19 01:52](https://issues.apache.org/jira/browse/SPARK-29967?focusedCommentId=16978897&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16978897)
[srowen](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=srowen) Hi, Owen how would you think of this ticket? If you feel OK, I guess we can working on making existing clustering algoritms support weight sample.
[![podongfeng](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Ruifeng Zheng](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=podongfeng) added a comment - [21/Nov/19 01:52](https://issues.apache.org/jira/browse/SPARK-29967?focusedCommentId=16978897&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16978897) srowen Hi, Owen how would you think of this ticket? If you feel OK, I guess we can working on making existing clustering algoritms support weight sample.
[![srowen](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Sean R. Owen](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=srowen) added a comment - [21/Nov/19 02:05](https://issues.apache.org/jira/browse/SPARK-29967?focusedCommentId=16978905&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16978905)
Is it necessary to move the implementation? not that this is a bad thing, but might be simpler to not move it if it's as easy.
[![srowen](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Sean R. Owen](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=srowen) added a comment - [21/Nov/19 02:05](https://issues.apache.org/jira/browse/SPARK-29967?focusedCommentId=16978905&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16978905) Is it necessary to move the implementation? not that this is a bad thing, but might be simpler to not move it if it's as easy.
[![podongfeng](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Ruifeng Zheng](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=podongfeng) added a comment - [21/Nov/19 03:25](https://issues.apache.org/jira/browse/SPARK-29967?focusedCommentId=16978942&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16978942)
[srowen](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=srowen) I suggested move the impl, since if I recall correctly, there seems some consensus on removing spark.mllib code in the future. I just find that in [GMM's emgration from mllib to ml|<https://github.com/apache/spark/pull/15413http://example.com>,|http://example.com],] [josephkb](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=josephkb) commented that 'As far as keeping the code around, I much prefer either the current approach (separate code) or having spark.mllib call into spark.ml. That will make it easier to deprecate and eventually remove spark.mllib code in 3.0.'
Are we still aim to emigrate the impls? If above tree parts is too large, what about spliting it into serveral sub-tasks?
[![podongfeng](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Ruifeng Zheng](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=podongfeng) added a comment - [21/Nov/19 03:25](https://issues.apache.org/jira/browse/SPARK-29967?focusedCommentId=16978942&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16978942) srowen I suggested move the impl, since if I recall correctly, there seems some consensus on removing spark.mllib code in the future. I just find that in [GMM's emgration from mllib to ml| https://github.com/apache/spark/pull/15413http://example.com ,|http://example.com],] josephkb commented that 'As far as keeping the code around, I much prefer either the current approach (separate code) or having spark.mllib call into spark.ml. That will make it easier to deprecate and eventually remove spark.mllib code in 3.0.' Are we still aim to emigrate the impls? If above tree parts is too large, what about spliting it into serveral sub-tasks?
[![srowen](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Sean R. Owen](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=srowen) added a comment - [21/Nov/19 03:49](https://issues.apache.org/jira/browse/SPARK-29967?focusedCommentId=16978952&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16978952)
Yes, I think that is a fine idea, but nothing has really been migrated. For consistency, might be fine to leave the core in .mllib and consider a mass migration later. (If it's not going to make the change unwieldy.) I kind of doubt it'll ever really be moved as there isn't a huge upside to breaking any code using .mllib
[![srowen](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Sean R. Owen](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=srowen) added a comment - [21/Nov/19 03:49](https://issues.apache.org/jira/browse/SPARK-29967?focusedCommentId=16978952&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16978952) Yes, I think that is a fine idea, but nothing has really been migrated. For consistency, might be fine to leave the core in .mllib and consider a mass migration later. (If it's not going to make the change unwieldy.) I kind of doubt it'll ever really be moved as there isn't a huge upside to breaking any code using .mllib
[![huaxingao](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Huaxin Gao](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=huaxingao) added a comment - [26/Nov/19 01:07](https://issues.apache.org/jira/browse/SPARK-29967?focusedCommentId=16982021&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16982021)
I will work on this.
[![huaxingao](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Huaxin Gao](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=huaxingao) added a comment - [26/Nov/19 01:07](https://issues.apache.org/jira/browse/SPARK-29967?focusedCommentId=16982021&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16982021) I will work on this.
[![srowen](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Sean R. Owen](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=srowen) added a comment - [10/Dec/19 15:33](https://issues.apache.org/jira/browse/SPARK-29967?focusedCommentId=16992658&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16992658)
Issue resolved by pull request 26739
<https://github.com/apache/spark/pull/26739>
[![srowen](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Sean R. Owen](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=srowen) added a comment - [10/Dec/19 15:33](https://issues.apache.org/jira/browse/SPARK-29967?focusedCommentId=16992658&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16992658) Issue resolved by pull request 26739 https://github.com/apache/spark/pull/26739
[![YuQiang Ye](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) YuQiang Ye](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=YuQiang+Ye) added a comment - [20/Aug/20 02:48](https://issues.apache.org/jira/browse/SPARK-29967?focusedCommentId=17180932&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-17180932)

```
  def run(data: RDD[Vector]): KMeansModel = {
-    run(data, None)
+    val instances: RDD[(Vector, Double)] = data.map {
+      case (point) => (point, 1.0)
+    }
+    runWithWeight(instances, None)
  }

```

Hi, I was testing KMeans performance from Spark 2.4 to Spark 3.0. The perf becomes quite worse than Spark 2.4. Will above code in this PR cause the instances' storage level always be NONE and in runWithWeight, the instances will be cached again
[srowen](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=srowen)[huaxingao](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=huaxingao)
[![YuQiang Ye](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) YuQiang Ye](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=YuQiang+Ye) added a comment - [20/Aug/20 02:48](https://issues.apache.org/jira/browse/SPARK-29967?focusedCommentId=17180932&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-17180932) def run(data: RDD[Vector]): KMeansModel = { - run(data, None) + val instances: RDD[(Vector, Double )] = data.map { + case (point) => (point, 1.0) + } + runWithWeight(instances, None) } Hi, I was testing KMeans performance from Spark 2.4 to Spark 3.0. The perf becomes quite worse than Spark 2.4. Will above code in this PR cause the instances' storage level always be NONE and in runWithWeight, the instances will be cached again srowen huaxingao
[![srowen](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Sean R. Owen](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=srowen) added a comment - [20/Aug/20 02:56](https://issues.apache.org/jira/browse/SPARK-29967?focusedCommentId=17180936&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-17180936)
No, why? I don't understand any of that.
[![srowen](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Sean R. Owen](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=srowen) added a comment - [20/Aug/20 02:56](https://issues.apache.org/jira/browse/SPARK-29967?focusedCommentId=17180936&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-17180936) No, why? I don't understand any of that.
[![podongfeng](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Ruifeng Zheng](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=podongfeng) added a comment - [20/Aug/20 03:01](https://issues.apache.org/jira/browse/SPARK-29967?focusedCommentId=17180937&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-17180937)
[YuQiang Ye](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=YuQiang+Ye) can you provide more details (dataset/params/env) for reproduction?
[![podongfeng](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Ruifeng Zheng](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=podongfeng) added a comment - [20/Aug/20 03:01](https://issues.apache.org/jira/browse/SPARK-29967?focusedCommentId=17180937&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-17180937) YuQiang Ye can you provide more details (dataset/params/env) for reproduction?
[![YuQiang Ye](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) YuQiang Ye](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=YuQiang+Ye) added a comment - [20/Aug/20 05:46](https://issues.apache.org/jira/browse/SPARK-29967?focusedCommentId=17180970&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-17180970)

```
scala> import org.apache.spark.mllib.linalg.{DenseVector, SparseVector, Vector, Vectors}
import org.apache.spark.mllib.linalg.{DenseVector, SparseVector, Vector, Vectors}

scala> import org.apache.spark.storage.StorageLevel
import org.apache.spark.storage.StorageLevel

scala>

scala> val data = sc.parallelize(Seq(
     |             Vectors.dense(1.0, 2.0, 6.0),
     |             Vectors.dense(1.0, 3.0, 0.0),
     |             Vectors.dense(1.0, 4.0, 6.0)
     |     ))
data: org.apache.spark.rdd.RDD[org.apache.spark.mllib.linalg.Vector] = ParallelCollectionRDD[0] at parallelize at <console>:26

scala>

scala> data.persist(StorageLevel.OFF_HEAP)
res0: data.type = ParallelCollectionRDD[0] at parallelize at <console>:26

scala> data.getStorageLevel
res1: org.apache.spark.storage.StorageLevel = StorageLevel(disk, memory, offheap, 1 replicas)

scala>

scala> val instances = data.map(point => (point, 1.0))
instances: org.apache.spark.rdd.RDD[(org.apache.spark.mllib.linalg.Vector, Double)] = MapPartitionsRDD[1] at map at <console>:27

scala>

scala> // in runWithWeight

scala> instances.getStorageLevel
res2: org.apache.spark.storage.StorageLevel = StorageLevel(1 replicas)

scala> if (instances.getStorageLevel == StorageLevel.NONE) {
     |     // zippedData.persist(StorageLevel.MEMORY_AND_DISK)
     |       print("Data is NONE")
     | }
Data is NONE
scala>

I was persiting the training data on OFF_HEAP, but after convert the data with weight to instances. instances.getStorageLevel will be NONE and persist to MEMORY_AND_DISK. I was expected to persist all the data to OFF_HEAP.

```

[![YuQiang Ye](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) YuQiang Ye](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=YuQiang+Ye) added a comment - [20/Aug/20 05:46](https://issues.apache.org/jira/browse/SPARK-29967?focusedCommentId=17180970&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-17180970) scala> import org.apache.spark.mllib.linalg.{DenseVector, SparseVector, Vector, Vectors} import org.apache.spark.mllib.linalg.{DenseVector, SparseVector, Vector, Vectors} scala> import org.apache.spark.storage.StorageLevel import org.apache.spark.storage.StorageLevel scala> scala> val data = sc.parallelize(Seq( | Vectors.dense(1.0, 2.0, 6.0), | Vectors.dense(1.0, 3.0, 0.0), | Vectors.dense(1.0, 4.0, 6.0) | )) data: org.apache.spark.rdd.RDD[org.apache.spark.mllib.linalg.Vector] = ParallelCollectionRDD[0] at parallelize at <console>:26 scala> scala> data.persist(StorageLevel.OFF_HEAP) res0: data.type = ParallelCollectionRDD[0] at parallelize at <console>:26 scala> data.getStorageLevel res1: org.apache.spark.storage.StorageLevel = StorageLevel(disk, memory, offheap, 1 replicas) scala> scala> val instances = data.map(point => (point, 1.0)) instances: org.apache.spark.rdd.RDD[(org.apache.spark.mllib.linalg.Vector, Double )] = MapPartitionsRDD[1] at map at <console>:27 scala> scala> // in runWithWeight scala> instances.getStorageLevel res2: org.apache.spark.storage.StorageLevel = StorageLevel(1 replicas) scala> if (instances.getStorageLevel == StorageLevel.NONE) { | // zippedData.persist(StorageLevel.MEMORY_AND_DISK) | print( "Data is NONE" ) | } Data is NONE scala> I was persiting the training data on OFF_HEAP, but after convert the data with weight to instances. instances.getStorageLevel will be NONE and persist to MEMORY_AND_DISK. I was expected to persist all the data to OFF_HEAP.
[![podongfeng](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Ruifeng Zheng](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=podongfeng) added a comment - [21/Aug/20 03:34](https://issues.apache.org/jira/browse/SPARK-29967?focusedCommentId=17181558&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-17181558)
[YuQiang Ye](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=YuQiang+Ye) I open ticket [~~SPARK-32676~~](https://issues.apache.org/jira/browse/SPARK-32676 "Fix double caching in KMeans/BiKMeans") for this issue, and send a pr <https://github.com/apache/spark/pull/29501>
[![podongfeng](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Ruifeng Zheng](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=podongfeng) added a comment - [21/Aug/20 03:34](https://issues.apache.org/jira/browse/SPARK-29967?focusedCommentId=17181558&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-17181558) YuQiang Ye I open ticket SPARK-32676 for this issue, and send a pr https://github.com/apache/spark/pull/29501
#### People

Assignee:
     ![huaxingao](https://issues.apache.org/jira/secure/useravatar?size=small&avatarId=10452) Huaxin Gao

Reporter:
     ![podongfeng](https://issues.apache.org/jira/secure/useravatar?size=small&avatarId=10452) Ruifeng Zheng

Shepherd:
     ![Ruifeng Zheng](https://issues.apache.org/jira/secure/useravatar?avatarId=10452) Ruifeng Zheng

Votes:
     0 Vote for this issue

Watchers:
     3 Start watching this issue
#### Dates

Created:
     20/Nov/19 01:34

Updated:
     15/Feb/26 20:00

Resolved:
     10/Dec/19 15:33
  * Atlassian Jira [Project Management Software](https://www.atlassian.com/software/jira)
  * [About Jira](https://issues.apache.org/jira/secure/AboutPage.jspa/secure/AboutPage.jspa)
  * [Report a problem](https://issues.apache.org/jira/secure/CreateIssue!default.jspa)

Powered by a free Atlassian [Jira](http://www.atlassian.com/software/jira) open source license for Apache Software Foundation. Try Jira - [bug tracking software](http://www.atlassian.com/software/jira) for _your_ team.
[Atlassian](http://www.atlassian.com/)
[](javascript:;)[](javascript:;)

[Log in](https://issues.apache.org/jira/login.jsp?os_destination=%2Fbrowse%2FSPARK-2546)[Skip to main content](https://issues.apache.org/jira/browse/SPARK-2546#main)[Skip to sidebar](https://issues.apache.org/jira/browse/SPARK-2546#sidebar)
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
  * [Log In](https://issues.apache.org/jira/login.jsp?os_destination=%2Fbrowse%2FSPARK-2546)

Public signup for this instance is **disabled**. Go to our [Self serve sign up page](https://selfserve.apache.org/jira-account.html) to request an account. Report potential security issues [privately](https://apache.org/security/#reporting-a-vulnerability)
[![Spark](https://issues.apache.org/jira/secure/projectavatar?pid=12315420&avatarId=27346)![Project Type: software](https://issues.apache.org/jira/browse/SPARK-2546)](https://issues.apache.org/jira/projects/SPARK/summary "Spark")
#
[Spark](https://issues.apache.org/jira/projects/SPARK/summary "Spark")
  * [Issues](https://issues.apache.org/jira/projects/SPARK/issues)
  * [Reports](https://issues.apache.org/jira/projects/SPARK?selectedItem=com.atlassian.jira.jira-projects-plugin:report-page)
  * [Components](https://issues.apache.org/jira/projects/SPARK?selectedItem=com.atlassian.jira.jira-projects-plugin:components-page)
  * [Roadmap](https://issues.apache.org/jira/projects/SPARK?selectedItem=biz.everit.jira.epic-roadmap:erfj-sidebar-roadmap)

![Uploaded image for project: 'Spark'](https://issues.apache.org/jira/secure/projectavatar?pid=12315420&avatarId=27346)
  1. [Spark](https://issues.apache.org/jira/browse/SPARK)
  2. [SPARK-2546](https://issues.apache.org/jira/browse/SPARK-2546)

# Configuration object thread safety issue
[Log In](https://issues.apache.org/jira/login.jsp?os_destination=%2Fbrowse%2FSPARK-2546 "Log In")
[ Export](https://issues.apache.org/jira/browse/SPARK-2546)
[XML](https://issues.apache.org/jira/si/jira.issueviews:issue-xml/SPARK-2546/SPARK-2546.xml)[Word](https://issues.apache.org/jira/si/jira.issueviews:issue-word/SPARK-2546/SPARK-2546.doc)[Printable](https://issues.apache.org/jira/si/jira.issueviews:issue-html/SPARK-2546/SPARK-2546.html)[JSON](https://issues.apache.org/jira/si/com.atlassian.jira.plugins.jira-importers-plugin:issue-json/SPARK-2546/SPARK-2546.json)

#### Details
  * ** Type: ** ![](https://issues.apache.org/jira/secure/viewavatar?size=xsmall&avatarId=21133&avatarType=issuetype) Bug
  * **Status:** Resolved
  * ** Priority: ** ![](https://issues.apache.org/jira/images/icons/priorities/critical.svg) Critical
  * **Resolution:** Fixed
  * ** Affects Version/s: ** 0.9.1, 1.0.2, 1.1.0, 1.2.0
  * ** Fix Version/s:  ** [1.0.3](https://issues.apache.org/jira/issues/?jql=project+%3D+SPARK+AND+fixVersion+%3D+1.0.3 "1.0.3 "), [1.1.1](https://issues.apache.org/jira/issues/?jql=project+%3D+SPARK+AND+fixVersion+%3D+1.1.1 "1.1.1 "), [1.2.0](https://issues.apache.org/jira/issues/?jql=project+%3D+SPARK+AND+fixVersion+%3D+1.2.0 "1.2.0 ")
  * ** Component/s: ** [Spark Core](https://issues.apache.org/jira/issues/?jql=project+%3D+SPARK+AND+component+%3D+%22Spark+Core%22 "Spark Core ")
  * ** Labels: **
None

  * ** Target Version/s: **
[1.2.0](https://issues.apache.org/jira/issues/?jql=project%3D%22SPARK%22%20AND%20%22Target+Version%2Fs%22%3D%221.2.0%22%20ORDER%20BY%20priority%20ASC "1.2.0")

#### Description
// observed in 0.9.1 but expected to exist in 1.0.1 as well
This ticket is copy-pasted from a thread on the dev@ list:
> We discovered a very interesting bug in Spark at work last week in Spark 0.9.1 — that the way Spark uses the Hadoop Configuration object is prone to thread safety issues. I believe it still applies in Spark 1.0.1 as well. Let me explain:
> Observations
>   * Was running a relatively simple job (read from Avro files, do a map, do another map, write back to Avro files)
>   * 412 of 413 tasks completed, but the last task was hung in RUNNING state
>   * The 412 successful tasks completed in median time 3.4s
>   * The last hung task didn't finish even in 20 hours
>   * The executor with the hung task was responsible for 100% of one core of CPU usage
>   * Jstack of the executor attached (relevant thread pasted below)
>

> Diagnosis
> After doing some code spelunking, we determined the issue was concurrent use of a Configuration object for each task on an executor. In Hadoop each task runs in its own JVM, but in Spark multiple tasks can run in the same JVM, so the single-threaded access assumptions of the Configuration object no longer hold in Spark.
> The specific issue is that the AvroRecordReader actually _modifies_ the JobConf it's given when it's instantiated! It adds a key for the RPC protocol engine in the process of connecting to the Hadoop FileSystem. When many tasks start at the same time (like at the start of a job), many tasks are adding this configuration item to the one Configuration object at once. Internally Configuration uses a java.lang.HashMap, which isn't threadsafe… The below post is an excellent explanation of what happens in the situation where multiple threads insert into a HashMap at the same time.
> <http://mailinator.blogspot.com/2009/06/beautiful-race-condition.html>
> The gist is that you have a thread following a cycle of linked list nodes indefinitely. This exactly matches our observations of the 100% CPU core and also the final location in the stack trace.
> So it seems the way Spark shares a Configuration object between task threads in an executor is incorrect. We need some way to prevent concurrent access to a single Configuration object.
> Proposed fix
> We can clone the JobConf object in HadoopRDD.getJobConf() so each task gets its own JobConf object (and thus Configuration object). The optimization of broadcasting the Configuration object across the cluster can remain, but on the other side I think it needs to be cloned for each task to allow for concurrent access. I'm not sure the performance implications, but the comments suggest that the Configuration object is ~10KB so I would expect a clone on the object to be relatively speedy.
> Has this been observed before? Does my suggested fix make sense? I'd be happy to file a Jira ticket and continue discussion there for the right way to fix.
> Thanks!
>  Andrew
> P.S. For others seeing this issue, our temporary workaround is to enable spark.speculation, which retries failed (or hung) tasks on other machines.
>
```
"Executor task launch worker-6" daemon prio=10 tid=0x00007f91f01fe000 nid=0x54b1 runnable [0x00007f92d74f1000]
   java.lang.Thread.State: RUNNABLE
    at java.util.HashMap.transfer(HashMap.java:601)
    at java.util.HashMap.resize(HashMap.java:581)
    at java.util.HashMap.addEntry(HashMap.java:879)
    at java.util.HashMap.put(HashMap.java:505)
    at org.apache.hadoop.conf.Configuration.set(Configuration.java:803)
    at org.apache.hadoop.conf.Configuration.set(Configuration.java:783)
    at org.apache.hadoop.conf.Configuration.setClass(Configuration.java:1662)
    at org.apache.hadoop.ipc.RPC.setProtocolEngine(RPC.java:193)
    at org.apache.hadoop.hdfs.NameNodeProxies.createNNProxyWithClientProtocol(NameNodeProxies.java:343)
    at org.apache.hadoop.hdfs.NameNodeProxies.createNonHAProxy(NameNodeProxies.java:168)
    at org.apache.hadoop.hdfs.NameNodeProxies.createProxy(NameNodeProxies.java:129)
    at org.apache.hadoop.hdfs.DFSClient.<init>(DFSClient.java:436)
    at org.apache.hadoop.hdfs.DFSClient.<init>(DFSClient.java:403)
    at org.apache.hadoop.hdfs.DistributedFileSystem.initialize(DistributedFileSystem.java:125)
    at org.apache.hadoop.fs.FileSystem.createFileSystem(FileSystem.java:2262)
    at org.apache.hadoop.fs.FileSystem.access$200(FileSystem.java:86)
    at org.apache.hadoop.fs.FileSystem$Cache.getInternal(FileSystem.java:2296)
    at org.apache.hadoop.fs.FileSystem$Cache.get(FileSystem.java:2278)
    at org.apache.hadoop.fs.FileSystem.get(FileSystem.java:316)
    at org.apache.hadoop.fs.Path.getFileSystem(Path.java:194)
    at org.apache.avro.mapred.FsInput.<init>(FsInput.java:37)
    at org.apache.avro.mapred.AvroRecordReader.<init>(AvroRecordReader.java:43)
    at org.apache.avro.mapred.AvroInputFormat.getRecordReader(AvroInputFormat.java:52)
    at org.apache.spark.rdd.HadoopRDD$$anon$1.<init>(HadoopRDD.scala:156)
    at org.apache.spark.rdd.HadoopRDD.compute(HadoopRDD.scala:149)
    at org.apache.spark.rdd.HadoopRDD.compute(HadoopRDD.scala:64)
    at org.apache.spark.rdd.RDD.computeOrReadCheckpoint(RDD.scala:241)
    at org.apache.spark.rdd.RDD.iterator(RDD.scala:232)
    at org.apache.spark.rdd.MappedRDD.compute(MappedRDD.scala:31)
    at org.apache.spark.rdd.RDD.computeOrReadCheckpoint(RDD.scala:241)
    at org.apache.spark.rdd.RDD.iterator(RDD.scala:232)
    at org.apache.spark.rdd.MappedRDD.compute(MappedRDD.scala:31)
    at org.apache.spark.rdd.RDD.computeOrReadCheckpoint(RDD.scala:241)
    at org.apache.spark.rdd.RDD.iterator(RDD.scala:232)
    at org.apache.spark.scheduler.ResultTask.runTask(ResultTask.scala:109)
    at org.apache.spark.scheduler.Task.run(Task.scala:53)
    at org.apache.spark.executor.Executor$TaskRunner$$anonfun$run$1.apply$mcV$sp(Executor.scala:211)
    at org.apache.spark.deploy.SparkHadoopUtil$$anon$1.run(SparkHadoopUtil.scala:42)
    at org.apache.spark.deploy.SparkHadoopUtil$$anon$1.run(SparkHadoopUtil.scala:41)
    at java.security.AccessController.doPrivileged(Native Method)
    at javax.security.auth.Subject.doAs(Subject.java:415)
    at org.apache.hadoop.security.UserGroupInformation.doAs(UserGroupInformation.java:1408)
    at org.apache.spark.deploy.SparkHadoopUtil.runAsUser(SparkHadoopUtil.scala:41)
    at org.apache.spark.executor.Executor$TaskRunner.run(Executor.scala:176)
    at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1145)
    at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:615)
    at java.lang.Thread.run(Thread.java:745)

```

#### Attachments
#### Issue Links

is related to

![Improvement - An improvement or enhancement to an existing feature or task.](https://issues.apache.org/jira/secure/viewavatar?size=xsmall&avatarId=21140&avatarType=issuetype) [SPARK-2585](https://issues.apache.org/jira/browse/SPARK-2585) Remove special handling of Hadoop JobConf
  * ![Critical - Crashes, loss of data, severe memory leak.](https://issues.apache.org/jira/images/icons/priorities/critical.svg)
  * Resolved

relates to

![Bug - A problem which impairs or prevents the functions of the product.](https://issues.apache.org/jira/secure/viewavatar?size=xsmall&avatarId=21133&avatarType=issuetype) [SPARK-10611](https://issues.apache.org/jira/browse/SPARK-10611) Configuration object thread safety issue in NewHadoopRDD
  * ![Critical - Crashes, loss of data, severe memory leak.](https://issues.apache.org/jira/images/icons/priorities/critical.svg)
  * Resolved

![Bug - A problem which impairs or prevents the functions of the product.](https://issues.apache.org/jira/secure/viewavatar?size=xsmall&avatarId=21133&avatarType=issuetype) [SPARK-1097](https://issues.apache.org/jira/browse/SPARK-1097) ConcurrentModificationException
  * ![Major - Major loss of function.](https://issues.apache.org/jira/images/icons/priorities/major.svg)
  * Resolved

![Bug - A problem which impairs or prevents the functions of the product.](https://issues.apache.org/jira/secure/viewavatar?size=xsmall&avatarId=21133&avatarType=issuetype) [HADOOP-11209](https://issues.apache.org/jira/browse/HADOOP-11209) Configuration#updatingResource/finalParameters are not thread-safe
  * ![Major - Major loss of function.](https://issues.apache.org/jira/images/icons/priorities/major.svg)
  * Closed

requires

![Improvement - An improvement or enhancement to an existing feature or task.](https://issues.apache.org/jira/secure/viewavatar?size=xsmall&avatarId=21140&avatarType=issuetype) [SPARK-2521](https://issues.apache.org/jira/browse/SPARK-2521) Broadcast RDD object once per TaskSet (instead of sending it for every task)
  * ![Major - Major loss of function.](https://issues.apache.org/jira/images/icons/priorities/major.svg)
  * Resolved

links to

![Pull request #2684](https://assets-cdn.github.com/favicon.ico) [[Github] Pull Request #2684 (JoshRosen)](https://github.com/apache/spark/pull/2684)
Show 1 more links (1 links to)
#### Activity
  * [All](https://issues.apache.org/jira/browse/SPARK-2546?page=com.atlassian.jira.plugin.system.issuetabpanels:all-tabpanel)
  * Comments
  * [Work Log](https://issues.apache.org/jira/browse/SPARK-2546?page=com.atlassian.jira.plugin.system.issuetabpanels:worklog-tabpanel)
  * [History](https://issues.apache.org/jira/browse/SPARK-2546?page=com.atlassian.jira.plugin.system.issuetabpanels:changehistory-tabpanel)
  * [Activity](https://issues.apache.org/jira/browse/SPARK-2546?page=com.atlassian.streams.streams-jira-plugin:activity-stream-issue-tab)
  * [Transitions](https://issues.apache.org/jira/browse/SPARK-2546?page=com.googlecode.jira-suite-utilities:transitions-summary-tabpanel)

[ Ascending order - Click to sort in descending order ](https://issues.apache.org/jira/browse/SPARK-2546?actionOrder=desc "Ascending order - Click to sort in descending order")
[![aash](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Andrew Ash](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=aash) added a comment - [17/Jul/14 06:19](https://issues.apache.org/jira/browse/SPARK-2546?focusedCommentId=14064625&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-14064625)
On the thread:
Me:
> Reynold's recent announcement of the broadcast RDD object patch may also have implications of the right path forward here. I'm not sure I fully understand the implications though: <https://github.com/apache/spark/pull/1452>
> "Once this is committed, we can also remove the JobConf broadcast in HadoopRDD."
[pwendell](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=pwendell):
> I think you are correct and a follow up to [~~SPARK-2521~~](https://issues.apache.org/jira/browse/SPARK-2521 "Broadcast RDD object once per TaskSet \(instead of sending it for every task\)") will end up
>  fixing this. The desing of [~~SPARK-2521~~](https://issues.apache.org/jira/browse/SPARK-2521 "Broadcast RDD object once per TaskSet \(instead of sending it for every task\)") automatically broadcasts RDD
>  data in tasks and the approach creates a new copy of the RDD and
>  associated data for each task. A natural follow-up to that patch is to
>  stop handling the jobConf separately (since we will now broadcast all
>  referents of the RDD itself) and just have it broadcasted with the
>  RDD. I'm not sure if Reynold plans to include this in [~~SPARK-2521~~](https://issues.apache.org/jira/browse/SPARK-2521 "Broadcast RDD object once per TaskSet \(instead of sending it for every task\)") or
>  afterwards, but it's likely we'd do that soon.
[![aash](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Andrew Ash](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=aash) added a comment - [17/Jul/14 06:19](https://issues.apache.org/jira/browse/SPARK-2546?focusedCommentId=14064625&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-14064625) On the thread: Me: Reynold's recent announcement of the broadcast RDD object patch may also have implications of the right path forward here. I'm not sure I fully understand the implications though: https://github.com/apache/spark/pull/1452 "Once this is committed, we can also remove the JobConf broadcast in HadoopRDD." pwendell : I think you are correct and a follow up to SPARK-2521 will end up fixing this. The desing of SPARK-2521 automatically broadcasts RDD data in tasks and the approach creates a new copy of the RDD and associated data for each task. A natural follow-up to that patch is to stop handling the jobConf separately (since we will now broadcast all referents of the RDD itself) and just have it broadcasted with the RDD. I'm not sure if Reynold plans to include this in SPARK-2521 or afterwards, but it's likely we'd do that soon.
[![pwendell](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Patrick Wendell](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=pwendell) added a comment - [31/Jul/14 05:48](https://issues.apache.org/jira/browse/SPARK-2546?focusedCommentId=14080531&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-14080531)
Ideally we should merge either this or [~~SPARK-2585~~](https://issues.apache.org/jira/browse/SPARK-2585 "Remove special handling of Hadoop JobConf") in the 1.1 release.
[![pwendell](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Patrick Wendell](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=pwendell) added a comment - [31/Jul/14 05:48](https://issues.apache.org/jira/browse/SPARK-2546?focusedCommentId=14080531&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-14080531) Ideally we should merge either this or SPARK-2585 in the 1.1 release.
[![joshrosen](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Josh Rosen](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=joshrosen) added a comment - [05/Aug/14 19:57](https://issues.apache.org/jira/browse/SPARK-2546?focusedCommentId=14086660&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-14086660)
Hi Andrew,
Do you have any way to reliably reproduce this issue? I'm considering implementing a clone()-based approach and I'd like to have a way to test whether I've fixed this bug.
[![joshrosen](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Josh Rosen](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=joshrosen) added a comment - [05/Aug/14 19:57](https://issues.apache.org/jira/browse/SPARK-2546?focusedCommentId=14086660&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-14086660) Hi Andrew, Do you have any way to reliably reproduce this issue? I'm considering implementing a clone()-based approach and I'd like to have a way to test whether I've fixed this bug.
[![ash211](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Andrew Ash](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=ash211) added a comment - [05/Aug/14 21:37](https://issues.apache.org/jira/browse/SPARK-2546?focusedCommentId=14086830&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-14086830)
I don't have a reliable repro that's in a unit test format. On my prod
cluster though it reproduces quite reliably! I'd suggest using the
AvroInputFormat on sizable files and a large number of partitions – I had
O(400) partitions and O(15GB) of data in that dataset.
Sidenote – the trouble with unit testing race conditions is that you have
to run them for a long time in an error-prone situation and hope that the
behavior is triggered. You could verify that the Configuration objects
each partition gets are equal() but not reference equal, but that's not
directly testing for the race condition.
[![ash211](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Andrew Ash](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=ash211) added a comment - [05/Aug/14 21:37](https://issues.apache.org/jira/browse/SPARK-2546?focusedCommentId=14086830&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-14086830) I don't have a reliable repro that's in a unit test format. On my prod cluster though it reproduces quite reliably! I'd suggest using the AvroInputFormat on sizable files and a large number of partitions – I had O(400) partitions and O(15GB) of data in that dataset. Sidenote – the trouble with unit testing race conditions is that you have to run them for a long time in an error-prone situation and hope that the behavior is triggered. You could verify that the Configuration objects each partition gets are equal() but not reference equal, but that's not directly testing for the race condition.
[![pwendell](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Patrick Wendell](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=pwendell) added a comment - [15/Aug/14 22:02](https://issues.apache.org/jira/browse/SPARK-2546?focusedCommentId=14099239&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-14099239)
Hey Andrew I think due to us cutting [~~SPARK-2585~~](https://issues.apache.org/jira/browse/SPARK-2585 "Remove special handling of Hadoop JobConf") from this release it will remain broken in Spark 1.1. We could look into a solution based on clone()'ing the conf for future patch releases in the 1.1 branch.
[![pwendell](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Patrick Wendell](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=pwendell) added a comment - [15/Aug/14 22:02](https://issues.apache.org/jira/browse/SPARK-2546?focusedCommentId=14099239&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-14099239) Hey Andrew I think due to us cutting SPARK-2585 from this release it will remain broken in Spark 1.1. We could look into a solution based on clone()'ing the conf for future patch releases in the 1.1 branch.
[![ash211](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Andrew Ash](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=ash211) added a comment - [15/Aug/14 22:11](https://issues.apache.org/jira/browse/SPARK-2546?focusedCommentId=14099251&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-14099251)
Ok I'll stay on the lookout for this bug and ping here again if we observe
this. Luckily we haven't seen this particular issue since, but that's
mostly been because other things are causing problems.
We have a few bugs now that are nondeterministically broken in Spark and
cause jobs to fail/hang, but if we retry the job several times (and
spark.speculation helps somewhat) we can usually eventually get a job to
complete. I can share that list if you're interested of what's highest on
our minds right now.
On Fri, Aug 15, 2014 at 6:03 PM, Patrick Wendell (JIRA) <jira@apache.org>
[![ash211](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Andrew Ash](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=ash211) added a comment - [15/Aug/14 22:11](https://issues.apache.org/jira/browse/SPARK-2546?focusedCommentId=14099251&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-14099251) Ok I'll stay on the lookout for this bug and ping here again if we observe this. Luckily we haven't seen this particular issue since, but that's mostly been because other things are causing problems. We have a few bugs now that are nondeterministically broken in Spark and cause jobs to fail/hang, but if we retry the job several times (and spark.speculation helps somewhat) we can usually eventually get a job to complete. I can share that list if you're interested of what's highest on our minds right now. On Fri, Aug 15, 2014 at 6:03 PM, Patrick Wendell (JIRA) <jira@apache.org>
[![aash](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Andrew Ash](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=aash) added a comment - [25/Sep/14 20:18](https://issues.apache.org/jira/browse/SPARK-2546?focusedCommentId=14148244&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-14148244)
Another proposed fix: extend JobConf as a shim and replace the Hadoop one with one that's threadsafe
[![aash](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Andrew Ash](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=aash) added a comment - [25/Sep/14 20:18](https://issues.apache.org/jira/browse/SPARK-2546?focusedCommentId=14148244&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-14148244) Another proposed fix: extend JobConf as a shim and replace the Hadoop one with one that's threadsafe
[![joshrosen](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Josh Rosen](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=joshrosen) added a comment - [26/Sep/14 02:36](https://issues.apache.org/jira/browse/SPARK-2546?focusedCommentId=14148645&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-14148645)
JobConf has a _ton_ of methods and it's not clear whether we can get away with synchronizing only some of them.
I'm going to look into using Scala macro annotations (<http://docs.scala-lang.org/overviews/macros/annotations.html>) to create a `@synchronizeAll` macro for adding synchronization to all methods of a class.
[![joshrosen](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Josh Rosen](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=joshrosen) added a comment - [26/Sep/14 02:36](https://issues.apache.org/jira/browse/SPARK-2546?focusedCommentId=14148645&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-14148645) JobConf has a ton of methods and it's not clear whether we can get away with synchronizing only some of them. I'm going to look into using Scala macro annotations ( http://docs.scala-lang.org/overviews/macros/annotations.html ) to create a @synchronizeAll macro for adding synchronization to all methods of a class.
[![joshrosen](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Josh Rosen](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=joshrosen) added a comment - [26/Sep/14 02:56](https://issues.apache.org/jira/browse/SPARK-2546?focusedCommentId=14148657&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-14148657)
A synchronization wrapper (whether written by hand or generated using macros) might introduce an unwanted runtime dependency on the exact compile-time version of Hadoop that we used. For example, say we compile against Hadoop 1.x and run on Hadoop 1.y (where y > x) and the runtime version of JobConf contains methods that were not present in the version that we wrapped at compile-time. What happens in this case?
Before we explore this option, I should probably re-visit [~~SPARK-2585~~](https://issues.apache.org/jira/browse/SPARK-2585 "Remove special handling of Hadoop JobConf") to see if I can understand why the patch seemed to introduce a performance regression, since that approach is Hadoop version agnostic.
[![joshrosen](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Josh Rosen](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=joshrosen) added a comment - [26/Sep/14 02:56](https://issues.apache.org/jira/browse/SPARK-2546?focusedCommentId=14148657&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-14148657) A synchronization wrapper (whether written by hand or generated using macros) might introduce an unwanted runtime dependency on the exact compile-time version of Hadoop that we used. For example, say we compile against Hadoop 1.x and run on Hadoop 1.y (where y > x) and the runtime version of JobConf contains methods that were not present in the version that we wrapped at compile-time. What happens in this case? Before we explore this option, I should probably re-visit SPARK-2585 to see if I can understand why the patch seemed to introduce a performance regression, since that approach is Hadoop version agnostic.
[![joshrosen](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Josh Rosen](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=joshrosen) added a comment - [06/Oct/14 19:28](https://issues.apache.org/jira/browse/SPARK-2546?focusedCommentId=14160790&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-14160790)
I've decided to go with the cloning approach, since this seems simplest and safest.
It looks like SparkContext has a public `hadoopConfiguration` `val` that holds a re-used Configuration object. It looks like this may have been purposely exposed to allow users to set Hadoop configuration properties (see how it's mentioned in docs/storage-openstack-swift.md; the Spark EC2 instructions also mention using this attribute to set S3 credentials). This object is used as the default Hadoop configuration in the `newAPIHadoopRDD` and `saveAsHadoop*` methods; it's also read in many other places inside of Spark.
While [~~SPARK-2585~~](https://issues.apache.org/jira/browse/SPARK-2585 "Remove special handling of Hadoop JobConf") addressed sharing of the Configuration objects in executors, it seems that we still might face races in the driver if multiple threads are sharing a SparkContext and one thread mutates the shared configuration while another thread submits a job that reads it.
This seems like a tricky problem to fix. I don't think that we can change `SparkContext.hadoopConfiguration` to return a copy of the configuration object, since it seems that the shared / mutating semantics are required by some existing code. At the same time, we can't simply clone the return value before using it in our internal driver-side code since a) we can't lock out writers/mutators while performing the clone() and b) the change in semantics might break existing user-code. Essentially, I don't think that there's anything that we can do that's guaranteed to be safe once a Configuration has been exposed to multiple threads; we need to perform the cloning before the object has been shared.
[![joshrosen](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Josh Rosen](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=joshrosen) added a comment - [06/Oct/14 19:28](https://issues.apache.org/jira/browse/SPARK-2546?focusedCommentId=14160790&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-14160790) I've decided to go with the cloning approach, since this seems simplest and safest. It looks like SparkContext has a public hadoopConfiguration val that holds a re-used Configuration object. It looks like this may have been purposely exposed to allow users to set Hadoop configuration properties (see how it's mentioned in docs/storage-openstack-swift.md; the Spark EC2 instructions also mention using this attribute to set S3 credentials). This object is used as the default Hadoop configuration in the newAPIHadoopRDD and saveAsHadoop* methods; it's also read in many other places inside of Spark. While SPARK-2585 addressed sharing of the Configuration objects in executors, it seems that we still might face races in the driver if multiple threads are sharing a SparkContext and one thread mutates the shared configuration while another thread submits a job that reads it. This seems like a tricky problem to fix. I don't think that we can change SparkContext.hadoopConfiguration to return a copy of the configuration object, since it seems that the shared / mutating semantics are required by some existing code. At the same time, we can't simply clone the return value before using it in our internal driver-side code since a) we can't lock out writers/mutators while performing the clone() and b) the change in semantics might break existing user-code. Essentially, I don't think that there's anything that we can do that's guaranteed to be safe once a Configuration has been exposed to multiple threads; we need to perform the cloning before the object has been shared.
[![joshrosen](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Josh Rosen](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=joshrosen) added a comment - [06/Oct/14 20:00](https://issues.apache.org/jira/browse/SPARK-2546?focusedCommentId=14160842&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-14160842)
Here are a few "in the wild" examples of how `sc.hadoopConfiguration` is currently used, to give a sense of the impact of any changes that we might make here.
[Setting elasticserach configuration properties](https://github.com/barnybug/spark-elasticsearch-blogpost/blob/master/Main.scala#L23):

```
sc.hadoopConfiguration.set("es.resource", "syslog/entry")
output.saveAsHadoopFile[ESOutputFormat]("-")

```

[Setting S3 credentials](http://stackoverflow.com/a/26156429/590203):

```
val conf = new SparkConf().setAppName("Simple Application").setMaster("local")
val sc = new SparkContext(conf)
val hadoopConf=sc.hadoopConfiguration;
hadoopConf.set("fs.s3.impl", "org.apache.hadoop.fs.s3native.NativeS3FileSystem")
hadoopConf.set("fs.s3.awsAccessKeyId",myAccessKey)
hadoopConf.set("fs.s3.awsSecretAccessKey",mySecretKey)

```

There's a lot more examples here: [https://github.com/search?utf8=%E2%9C%93&q=%22sc.hadoopconfiguration%22&type=Code&ref=searchresults](https://github.com/search?utf8=%E2%9C%93&q=%22sc.hadoopconfiguration%22&type=Code&ref=searchresults)
The most common use-case seems to be setting S3 credentials. One option would be to slowly deprecate the existing `hadoopConfiguration` field in favor of methods for setting S3 credentials. Currently, you can set these options in SparkConf before creating the SparkContext; unfortunately, this isn't an option for users that want to set configurations after starting SparkContext (e.g. IPython notebook users). I suppose that these users could work with a clone of the configuration object and manually pass that object into Spark methods.
If we did add a SparkContext-wide setting for changing Hadoop configurations, then in multi-user shared-SparkContext environments we run the risk of users overwriting each others' S3 credentials.
[![joshrosen](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Josh Rosen](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=joshrosen) added a comment - [06/Oct/14 20:00](https://issues.apache.org/jira/browse/SPARK-2546?focusedCommentId=14160842&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-14160842) Here are a few "in the wild" examples of how sc.hadoopConfiguration is currently used, to give a sense of the impact of any changes that we might make here. Setting elasticserach configuration properties : sc.hadoopConfiguration.set( "es.resource" , "syslog/entry" ) output.saveAsHadoopFile[ESOutputFormat]( "-" ) Setting S3 credentials : val conf = new SparkConf().setAppName( "Simple Application" ).setMaster( "local" ) val sc = new SparkContext(conf) val hadoopConf=sc.hadoopConfiguration; hadoopConf.set( "fs.s3.impl" , "org.apache.hadoop.fs.s3native.NativeS3FileSystem" ) hadoopConf.set( "fs.s3.awsAccessKeyId" ,myAccessKey) hadoopConf.set( "fs.s3.awsSecretAccessKey" ,mySecretKey) There's a lot more examples here: https://github.com/search?utf8=%E2%9C%93&q=%22sc.hadoopconfiguration%22&type=Code&ref=searchresults The most common use-case seems to be setting S3 credentials. One option would be to slowly deprecate the existing hadoopConfiguration field in favor of methods for setting S3 credentials. Currently, you can set these options in SparkConf before creating the SparkContext; unfortunately, this isn't an option for users that want to set configurations after starting SparkContext (e.g. IPython notebook users). I suppose that these users could work with a clone of the configuration object and manually pass that object into Spark methods. If we did add a SparkContext-wide setting for changing Hadoop configurations, then in multi-user shared-SparkContext environments we run the risk of users overwriting each others' S3 credentials.
[![joshrosen](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Josh Rosen](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=joshrosen) added a comment - [06/Oct/14 20:33](https://issues.apache.org/jira/browse/SPARK-2546?focusedCommentId=14160892&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-14160892)
For now, let's ignore the design issue of whether the current API is confusing in multi-user shared-SparkContext environments. If we want to keep the current API without any driver-side thread-safety issues, is there anything that we can do?
Maybe we can add a very limited amount of synchronization to Configuration. [Looking at a recent version of Configuration.java](https://github.com/apache/hadoop/blob/d989ac04449dc33da5e2c32a7f24d59cc92de536/hadoop-common-project/hadoop-common/src/main/java/org/apache/hadoop/conf/Configuration.java#L666), it seems that the private `updatingResource` HashMap and `finalParameters` HashSet fields the only non-thread-safe collections in Configuration (Java's `Properties` class is thread-safe).
My hunch is that the `updatingResource` HashMap was the map referred to by the stacktrace posted in this issue. We might be able to use reflection to find this field and inject a synchronized HashMap instead.
[![joshrosen](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Josh Rosen](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=joshrosen) added a comment - [06/Oct/14 20:33](https://issues.apache.org/jira/browse/SPARK-2546?focusedCommentId=14160892&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-14160892) For now, let's ignore the design issue of whether the current API is confusing in multi-user shared-SparkContext environments. If we want to keep the current API without any driver-side thread-safety issues, is there anything that we can do? Maybe we can add a very limited amount of synchronization to Configuration. Looking at a recent version of Configuration.java , it seems that the private updatingResource HashMap and finalParameters HashSet fields the only non-thread-safe collections in Configuration (Java's Properties class is thread-safe). My hunch is that the updatingResource HashMap was the map referred to by the stacktrace posted in this issue. We might be able to use reflection to find this field and inject a synchronized HashMap instead.
[![aash](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Andrew Ash](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=aash) added a comment - [06/Oct/14 21:41](https://issues.apache.org/jira/browse/SPARK-2546?focusedCommentId=14161013&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-14161013)
Excellent research Josh!
I agree that we should pass for now on the driver-side thread-safety issues. All the issues I've encountered so far have been in multiple accesses on the executor side, which the cloning on access approach seems to take care of.
[![aash](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Andrew Ash](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=aash) added a comment - [06/Oct/14 21:41](https://issues.apache.org/jira/browse/SPARK-2546?focusedCommentId=14161013&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-14161013) Excellent research Josh! I agree that we should pass for now on the driver-side thread-safety issues. All the issues I've encountered so far have been in multiple accesses on the executor side, which the cloning on access approach seems to take care of.
[![apachespark](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Apache Spark](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=apachespark) added a comment - [06/Oct/14 23:35](https://issues.apache.org/jira/browse/SPARK-2546?focusedCommentId=14161214&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-14161214)
User 'JoshRosen' has created a pull request for this issue:
<https://github.com/apache/spark/pull/2684>
[![apachespark](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Apache Spark](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=apachespark) added a comment - [06/Oct/14 23:35](https://issues.apache.org/jira/browse/SPARK-2546?focusedCommentId=14161214&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-14161214) User 'JoshRosen' has created a pull request for this issue: https://github.com/apache/spark/pull/2684
[![aash](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Andrew Ash](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=aash) added a comment - [17/Oct/14 21:59](https://issues.apache.org/jira/browse/SPARK-2546?focusedCommentId=14175608&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-14175608)
We tested Josh's patch, confirming the fix and measuring the perf regression at ~8%
[![aash](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Andrew Ash](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=aash) added a comment - [17/Oct/14 21:59](https://issues.apache.org/jira/browse/SPARK-2546?focusedCommentId=14175608&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-14175608) We tested Josh's patch, confirming the fix and measuring the perf regression at ~8%
[![joshrosen](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Josh Rosen](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=joshrosen) added a comment - [19/Oct/14 07:40](https://issues.apache.org/jira/browse/SPARK-2546?focusedCommentId=14176243&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-14176243)
Issue resolved by pull request 2684
<https://github.com/apache/spark/pull/2684>
[![joshrosen](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Josh Rosen](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=joshrosen) added a comment - [19/Oct/14 07:40](https://issues.apache.org/jira/browse/SPARK-2546?focusedCommentId=14176243&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-14176243) Issue resolved by pull request 2684 https://github.com/apache/spark/pull/2684
[![joshrosen](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Josh Rosen](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=joshrosen) added a comment - [19/Oct/14 07:45](https://issues.apache.org/jira/browse/SPARK-2546?focusedCommentId=14176245&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-14176245)
I've fixed this in HadoopRDD and applied my fix to all branches. Note that the fix is currently guarded by a configuration option, `spark.hadoop.cloneConf`. This is in order to avoid unexpected performance regressions when users who were unaffected by this issue choose to upgrade to 1.1.1 or 1.0.3. We'll probably make cloning the default in 1.2.0 and may spend some more time trying to understand its performance implications.
Note that this does not address the potential for thread-safety issues due to Configuration-sharing on the driver. As described upthread, this is a much harder issue to fix. Since I'm not aware of any cases where this has caused issues on the driver, I'm inclined to wait things out and address that if it's discovered to be an issue.
I've opened [~~HADOOP-11209~~](https://issues.apache.org/jira/browse/HADOOP-11209 "Configuration#updatingResource/finalParameters are not thread-safe") to try to fix the Configuration thread-safety issues upstream, so hopefully this won't be a problem in the future.
[![joshrosen](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Josh Rosen](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=joshrosen) added a comment - [19/Oct/14 07:45](https://issues.apache.org/jira/browse/SPARK-2546?focusedCommentId=14176245&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-14176245) I've fixed this in HadoopRDD and applied my fix to all branches. Note that the fix is currently guarded by a configuration option, spark.hadoop.cloneConf . This is in order to avoid unexpected performance regressions when users who were unaffected by this issue choose to upgrade to 1.1.1 or 1.0.3. We'll probably make cloning the default in 1.2.0 and may spend some more time trying to understand its performance implications. Note that this does not address the potential for thread-safety issues due to Configuration-sharing on the driver. As described upthread, this is a much harder issue to fix. Since I'm not aware of any cases where this has caused issues on the driver, I'm inclined to wait things out and address that if it's discovered to be an issue. I've opened HADOOP-11209 to try to fix the Configuration thread-safety issues upstream, so hopefully this won't be a problem in the future.
[![ozawa](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Tsuyoshi Ozawa](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=ozawa) added a comment - [22/Jan/15 05:22](https://issues.apache.org/jira/browse/SPARK-2546?focusedCommentId=14286971&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-14286971)
Now [~~HADOOP-11209~~](https://issues.apache.org/jira/browse/HADOOP-11209 "Configuration#updatingResource/finalParameters are not thread-safe"), the problem reported by [joshrosen](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=joshrosen), is resolved by [varun_saxena](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=varun_saxena)'s contribution. Thanks for your reporting.
[![ozawa](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Tsuyoshi Ozawa](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=ozawa) added a comment - [22/Jan/15 05:22](https://issues.apache.org/jira/browse/SPARK-2546?focusedCommentId=14286971&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-14286971) Now HADOOP-11209 , the problem reported by joshrosen , is resolved by varun_saxena 's contribution. Thanks for your reporting.
[![ankurmitujjain](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Ankur Jain](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=ankurmitujjain) added a comment - [15/Jul/15 10:29](https://issues.apache.org/jira/browse/SPARK-2546?focusedCommentId=14627863&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-14627863)
This exists in SPARK 1.4 too...
[![ankurmitujjain](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Ankur Jain](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=ankurmitujjain) added a comment - [15/Jul/15 10:29](https://issues.apache.org/jira/browse/SPARK-2546?focusedCommentId=14627863&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-14627863) This exists in SPARK 1.4 too...
[![ozawa](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Tsuyoshi Ozawa](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=ozawa) added a comment - [15/Jul/15 11:29](https://issues.apache.org/jira/browse/SPARK-2546?focusedCommentId=14627909&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-14627909)
[anknai](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=anknai) cc: [joshrosen](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=joshrosen) the problem is fixed in Hadoop 2.7. Could you build spark with hadoop.version=2.7.1? I'll also backport the patch to 2.6.x, but it takes a bit time to release.
[![ozawa](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Tsuyoshi Ozawa](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=ozawa) added a comment - [15/Jul/15 11:29](https://issues.apache.org/jira/browse/SPARK-2546?focusedCommentId=14627909&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-14627909) anknai cc: joshrosen the problem is fixed in Hadoop 2.7. Could you build spark with hadoop.version=2.7.1? I'll also backport the patch to 2.6.x, but it takes a bit time to release.
[![ankurmitujjain](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Ankur Jain](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=ankurmitujjain) added a comment - [15/Jul/15 11:33](https://issues.apache.org/jira/browse/SPARK-2546?focusedCommentId=14627914&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-14627914)
Thanks Tsuyoshi...
I thought fix is already done for version 1.0.3, 1.1.1, 1.2.0.
So 1.4.0 should have this fix with it....
Anyways this means that on EMR we will face this issue as they are using Hadoop 2.4.0
[![ankurmitujjain](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Ankur Jain](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=ankurmitujjain) added a comment - [15/Jul/15 11:33](https://issues.apache.org/jira/browse/SPARK-2546?focusedCommentId=14627914&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-14627914) Thanks Tsuyoshi... I thought fix is already done for version 1.0.3, 1.1.1, 1.2.0. So 1.4.0 should have this fix with it.... Anyways this means that on EMR we will face this issue as they are using Hadoop 2.4.0
[![joshrosen](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Josh Rosen](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=joshrosen) added a comment - [17/Jul/15 15:24](https://issues.apache.org/jira/browse/SPARK-2546?focusedCommentId=14631465&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-14631465)
[ankurmitujjain](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=ankurmitujjain), you can try setting `spark.hadoop.cloneConf=true` in your SparkConf in order to enable additional defensive copying that is designed to guard against this issue. This setting is off by default because this cloning is actually fairly expensive because new `Configuration` objects are costly to create.
[![joshrosen](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Josh Rosen](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=joshrosen) added a comment - [17/Jul/15 15:24](https://issues.apache.org/jira/browse/SPARK-2546?focusedCommentId=14631465&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-14631465) ankurmitujjain , you can try setting spark.hadoop.cloneConf=true in your SparkConf in order to enable additional defensive copying that is designed to guard against this issue. This setting is off by default because this cloning is actually fairly expensive because new Configuration objects are costly to create.
#### People

Assignee:
     ![joshrosen](https://issues.apache.org/jira/secure/useravatar?size=small&avatarId=10452) Josh Rosen

Reporter:
     ![aash](https://issues.apache.org/jira/secure/useravatar?size=small&avatarId=10452) Andrew Ash

Votes:
     0 Vote for this issue

Watchers:
     9 Start watching this issue
#### Dates

Created:
     17/Jul/14 05:20

Updated:
     15/Sep/15 07:21

Resolved:
     19/Oct/14 07:40
  * Atlassian Jira [Project Management Software](https://www.atlassian.com/software/jira)
  * [About Jira](https://issues.apache.org/jira/secure/AboutPage.jspa/secure/AboutPage.jspa)
  * [Report a problem](https://issues.apache.org/jira/secure/CreateIssue!default.jspa)

Powered by a free Atlassian [Jira](http://www.atlassian.com/software/jira) open source license for Apache Software Foundation. Try Jira - [bug tracking software](http://www.atlassian.com/software/jira) for _your_ team.
[Atlassian](http://www.atlassian.com/)
[](javascript:;)[](javascript:;)

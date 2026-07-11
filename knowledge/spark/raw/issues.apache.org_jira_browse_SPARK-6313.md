[Log in](https://issues.apache.org/jira/login.jsp?os_destination=%2Fbrowse%2FSPARK-6313)[Skip to main content](https://issues.apache.org/jira/browse/SPARK-6313#main)[Skip to sidebar](https://issues.apache.org/jira/browse/SPARK-6313#sidebar)
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
  * [Log In](https://issues.apache.org/jira/login.jsp?os_destination=%2Fbrowse%2FSPARK-6313)


Public signup for this instance is **disabled**. Go to our [Self serve sign up page](https://selfserve.apache.org/jira-account.html) to request an account. Report potential security issues [privately](https://apache.org/security/#reporting-a-vulnerability)
[![Spark](https://issues.apache.org/jira/secure/projectavatar?pid=12315420&avatarId=27346)![Project Type: software](https://issues.apache.org/jira/browse/SPARK-6313)](https://issues.apache.org/jira/projects/SPARK/summary "Spark")
# 
[Spark](https://issues.apache.org/jira/projects/SPARK/summary "Spark")
  * [Issues](https://issues.apache.org/jira/projects/SPARK/issues)
  * [Reports](https://issues.apache.org/jira/projects/SPARK?selectedItem=com.atlassian.jira.jira-projects-plugin:report-page)
  * [Components](https://issues.apache.org/jira/projects/SPARK?selectedItem=com.atlassian.jira.jira-projects-plugin:components-page)
  * [Roadmap](https://issues.apache.org/jira/projects/SPARK?selectedItem=biz.everit.jira.epic-roadmap:erfj-sidebar-roadmap)


![Uploaded image for project: 'Spark'](https://issues.apache.org/jira/secure/projectavatar?pid=12315420&avatarId=27346)
  1. [Spark](https://issues.apache.org/jira/browse/SPARK)
  2. [SPARK-6313](https://issues.apache.org/jira/browse/SPARK-6313)


# Fetch File Lock file creation doesnt work when Spark working dir is on a NFS mount
[Log In](https://issues.apache.org/jira/login.jsp?os_destination=%2Fbrowse%2FSPARK-6313 "Log In")
[ Export](https://issues.apache.org/jira/browse/SPARK-6313)
[XML](https://issues.apache.org/jira/si/jira.issueviews:issue-xml/SPARK-6313/SPARK-6313.xml)[Word](https://issues.apache.org/jira/si/jira.issueviews:issue-word/SPARK-6313/SPARK-6313.doc)[Printable](https://issues.apache.org/jira/si/jira.issueviews:issue-html/SPARK-6313/SPARK-6313.html)[JSON](https://issues.apache.org/jira/si/com.atlassian.jira.plugins.jira-importers-plugin:issue-json/SPARK-6313/SPARK-6313.json) 

#### Details
  * ** Type: ** ![](https://issues.apache.org/jira/secure/viewavatar?size=xsmall&avatarId=21133&avatarType=issuetype) Bug 
  * **Status:** Resolved
  * ** Priority: ** ![](https://issues.apache.org/jira/images/icons/priorities/critical.svg) Critical 
  * **Resolution:** Fixed 
  * ** Affects Version/s: ** 1.2.0, 1.2.1, 1.3.0
  * ** Fix Version/s:  ** [1.2.2](https://issues.apache.org/jira/issues/?jql=project+%3D+SPARK+AND+fixVersion+%3D+1.2.2 "1.2.2 "), [1.3.1](https://issues.apache.org/jira/issues/?jql=project+%3D+SPARK+AND+fixVersion+%3D+1.3.1 "1.3.1 "), [1.4.0](https://issues.apache.org/jira/issues/?jql=project+%3D+SPARK+AND+fixVersion+%3D+1.4.0 "1.4.0 ")
  * ** Component/s: ** [Spark Core](https://issues.apache.org/jira/issues/?jql=project+%3D+SPARK+AND+component+%3D+%22Spark+Core%22 "Spark Core ")
  * ** Labels: **
None


  * ** Target Version/s: **
[1.3.1](https://issues.apache.org/jira/issues/?jql=project%3D%22SPARK%22%20AND%20%22Target+Version%2Fs%22%3D%221.3.1%22%20ORDER%20BY%20priority%20ASC "1.3.1")


#### Description
When running in cluster mode and mounting the spark work dir on a NFS volume (or some volume which doesn't support file locking), the fetchFile (used for downloading JARs etc on the executors) method in Spark Utils class will fail. This file locking was introduced as an improvement with [~~SPARK-2713~~](https://issues.apache.org/jira/browse/SPARK-2713 "Executors of same application in same host should only download files & jars once"). 
See <https://github.com/apache/spark/blob/master/core/src/main/scala/org/apache/spark/util/Utils.scala#L415>
Introduced in 1.2 in commit; <https://github.com/apache/spark/commit/7aacb7bfad4ec73fd8f18555c72ef696>
As this locking is for optimisation for fetching files, could we take a different approach here to create a temp/advisory lock file? 
Typically you would just mount local disks (in say ext4 format) and provide this as a comma separated list however we are trying to run Spark on MapR. With MapR we can do a loop back mount to a volume on the local node and take advantage of MapRs disk pools. This also means we dont need specific mounts for Spark and improves the generic nature of the cluster. 
#### Attachments
#### Issue Links 

links to
    
![Pull request #5036](https://assets-cdn.github.com/favicon.ico) [[Github] Pull Request #5036 (nemccarthy)](https://github.com/apache/spark/pull/5036)
#### Activity
  * [All](https://issues.apache.org/jira/browse/SPARK-6313?page=com.atlassian.jira.plugin.system.issuetabpanels:all-tabpanel)
  * Comments
  * [Work Log](https://issues.apache.org/jira/browse/SPARK-6313?page=com.atlassian.jira.plugin.system.issuetabpanels:worklog-tabpanel)
  * [History](https://issues.apache.org/jira/browse/SPARK-6313?page=com.atlassian.jira.plugin.system.issuetabpanels:changehistory-tabpanel)
  * [Activity](https://issues.apache.org/jira/browse/SPARK-6313?page=com.atlassian.streams.streams-jira-plugin:activity-stream-issue-tab)
  * [Transitions](https://issues.apache.org/jira/browse/SPARK-6313?page=com.googlecode.jira-suite-utilities:transitions-summary-tabpanel)


[ Ascending order - Click to sort in descending order ](https://issues.apache.org/jira/browse/SPARK-6313?actionOrder=desc "Ascending order - Click to sort in descending order")
[![nemccarthy](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Nathan McCarthy](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=nemccarthy) added a comment - [13/Mar/15 05:32](https://issues.apache.org/jira/browse/SPARK-6313?focusedCommentId=14359964&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-14359964)
Suggestion along the lines of;
<https://github.com/apache/lucene-solr/blob/5314a56924f46522993baf106e6deca0e48a967f/lucene/core/src/java/org/apache/lucene/store/SimpleFSLockFactory.java>   
or  
<https://github.com/graphhopper/graphhopper/blob/master/core/src/main/java/com/graphhopper/storage/SimpleFSLockFactory.java>
[![nemccarthy](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Nathan McCarthy](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=nemccarthy) added a comment - [13/Mar/15 05:32](https://issues.apache.org/jira/browse/SPARK-6313?focusedCommentId=14359964&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-14359964) Suggestion along the lines of; https://github.com/apache/lucene-solr/blob/5314a56924f46522993baf106e6deca0e48a967f/lucene/core/src/java/org/apache/lucene/store/SimpleFSLockFactory.java or https://github.com/graphhopper/graphhopper/blob/master/core/src/main/java/com/graphhopper/storage/SimpleFSLockFactory.java 
[![nemccarthy](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Nathan McCarthy](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=nemccarthy) added a comment - [13/Mar/15 05:36](https://issues.apache.org/jira/browse/SPARK-6313?focusedCommentId=14359972&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-14359972) - edited
Since the 

```
val lockFileName = s"${url.hashCode}${timestamp}_lock"
```

uses a timestamp I can't see there being too many problems with hanging/left over lock files. 
[![nemccarthy](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Nathan McCarthy](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=nemccarthy) added a comment - [13/Mar/15 05:36](https://issues.apache.org/jira/browse/SPARK-6313?focusedCommentId=14359972&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-14359972) - edited Since the val lockFileName = s "${url.hashCode}${timestamp}_lock" uses a timestamp I can't see there being too many problems with hanging/left over lock files. 
[![joshrosen](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Josh Rosen](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=joshrosen) added a comment - [13/Mar/15 18:13](https://issues.apache.org/jira/browse/SPARK-6313?focusedCommentId=14360842&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-14360842)
Could you update this ticket with more details on the error-message or symptom that you've observed (such as a stacktrace)? This would be helpful in order to make this issue more searchable / discoverable.
[![joshrosen](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Josh Rosen](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=joshrosen) added a comment - [13/Mar/15 18:13](https://issues.apache.org/jira/browse/SPARK-6313?focusedCommentId=14360842&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-14360842) Could you update this ticket with more details on the error-message or symptom that you've observed (such as a stacktrace)? This would be helpful in order to make this issue more searchable / discoverable. 
[![joshrosen](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Josh Rosen](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=joshrosen) added a comment - [13/Mar/15 18:40](https://issues.apache.org/jira/browse/SPARK-6313?focusedCommentId=14360896&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-14360896)
Thanks for the pointer to the Lucene lock factory code.
It's fine for the locks to be advisory in the sense that things shouldn't break if multiple executors acquire the lock and try to download the same file, but there's potentially a problem if the lock isn't released after the JVM that acquired it exits abnormally, since this could cause other executors to block indefinitely while waiting for the original lock owner to download the file. One approach might be to write the PID of the original lock owner into the lock file, which would allow blocked executors to timeout and re-attempt the lock acquisition if they detect that the original lock holder died. This might face its own portability challenges, though, and seems complex.
A simple hotfix might be to add a SparkConf setting to always force this caching to bypassed (this would be a two-line change to Executor.scala). This might lose the performance benefits of the caching, though.
If you're using NFS and the shared filesystem is mounted at the same path on all nodes, I think that you should be able to use use `local://path/to/nfs/` to specify the paths to your files / JARs, which will cause them to be read from the executor-local filesystem rather than fetched remotely. In this case, this would cause them to be read from NFS, so you may be able to use this technique to recover any performance benefits for large files that would be lost in disabling the caching.
I'd be happy to review patches for this issue.
[![joshrosen](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Josh Rosen](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=joshrosen) added a comment - [13/Mar/15 18:40](https://issues.apache.org/jira/browse/SPARK-6313?focusedCommentId=14360896&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-14360896) Thanks for the pointer to the Lucene lock factory code. It's fine for the locks to be advisory in the sense that things shouldn't break if multiple executors acquire the lock and try to download the same file, but there's potentially a problem if the lock isn't released after the JVM that acquired it exits abnormally, since this could cause other executors to block indefinitely while waiting for the original lock owner to download the file. One approach might be to write the PID of the original lock owner into the lock file, which would allow blocked executors to timeout and re-attempt the lock acquisition if they detect that the original lock holder died. This might face its own portability challenges, though, and seems complex. A simple hotfix might be to add a SparkConf setting to always force this caching to bypassed (this would be a two-line change to Executor.scala). This might lose the performance benefits of the caching, though. If you're using NFS and the shared filesystem is mounted at the same path on all nodes, I think that you should be able to use use local://path/to/nfs/ to specify the paths to your files / JARs, which will cause them to be read from the executor-local filesystem rather than fetched remotely. In this case, this would cause them to be read from NFS, so you may be able to use this technique to recover any performance benefits for large files that would be lost in disabling the caching. I'd be happy to review patches for this issue. 
[![nemccarthy](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Nathan McCarthy](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=nemccarthy) added a comment - [15/Mar/15 23:13](https://issues.apache.org/jira/browse/SPARK-6313?focusedCommentId=14362605&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-14362605)
Stacktrace;
14/12/12 18:18:24 WARN scheduler.TaskSetManager: Lost task 7.0 in stage 0.0 (TID 8, hadoop-016): java.io.IOException: Permission denied  
at sun.nio.ch.FileDispatcherImpl.lock0(Native Method)  
at sun.nio.ch.FileDispatcherImpl.lock(FileDispatcherImpl.java:91)  
at sun.nio.ch.FileChannelImpl.lock(FileChannelImpl.java:1022)  
at java.nio.channels.FileChannel.lock(FileChannel.java:1052)  
at org.apache.spark.util.Utils$.fetchFile(Utils.scala:379)  
at org.apache.spark.executor.Executor$$anonfun$org$apache$spark$executor$Executor$$updateDependencies$6.apply(Executor.scala:350)  
at org.apache.spark.executor.Executor$$anonfun$org$apache$spark$executor$Executor$$updateDependencies$6.apply(Executor.scala:347)  
at scala.collection.TraversableLike$WithFilter$$anonfun$foreach$1.apply(TraversableLike.scala:772)  
at scala.collection.mutable.HashMap$$anonfun$foreach$1.apply(HashMap.scala:98)  
at scala.collection.mutable.HashMap$$anonfun$foreach$1.apply(HashMap.scala:98)  
at scala.collection.mutable.HashTable$class.foreachEntry(HashTable.scala:226)  
at scala.collection.mutable.HashMap.foreachEntry(HashMap.scala:39)  
at scala.collection.mutable.HashMap.foreach(HashMap.scala:98)  
at scala.collection.TraversableLike$WithFilter.foreach(TraversableLike.scala:771)  
at org.apache.spark.executor.Executor.org$apache$spark$executor$Executor$$updateDependencies(Executor.scala:347)  
at org.apache.spark.executor.Executor$TaskRunner.run(Executor.scala:177)  
at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1145)  
at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:615)  
at java.lang.Thread.run(Thread.java:745)
[![nemccarthy](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Nathan McCarthy](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=nemccarthy) added a comment - [15/Mar/15 23:13](https://issues.apache.org/jira/browse/SPARK-6313?focusedCommentId=14362605&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-14362605) Stacktrace; 14/12/12 18:18:24 WARN scheduler.TaskSetManager: Lost task 7.0 in stage 0.0 (TID 8, hadoop-016): java.io.IOException: Permission denied at sun.nio.ch.FileDispatcherImpl.lock0(Native Method) at sun.nio.ch.FileDispatcherImpl.lock(FileDispatcherImpl.java:91) at sun.nio.ch.FileChannelImpl.lock(FileChannelImpl.java:1022) at java.nio.channels.FileChannel.lock(FileChannel.java:1052) at org.apache.spark.util.Utils$.fetchFile(Utils.scala:379) at org.apache.spark.executor.Executor$$anonfun$org$apache$spark$executor$Executor$$updateDependencies$6.apply(Executor.scala:350) at org.apache.spark.executor.Executor$$anonfun$org$apache$spark$executor$Executor$$updateDependencies$6.apply(Executor.scala:347) at scala.collection.TraversableLike$WithFilter$$anonfun$foreach$1.apply(TraversableLike.scala:772) at scala.collection.mutable.HashMap$$anonfun$foreach$1.apply(HashMap.scala:98) at scala.collection.mutable.HashMap$$anonfun$foreach$1.apply(HashMap.scala:98) at scala.collection.mutable.HashTable$class.foreachEntry(HashTable.scala:226) at scala.collection.mutable.HashMap.foreachEntry(HashMap.scala:39) at scala.collection.mutable.HashMap.foreach(HashMap.scala:98) at scala.collection.TraversableLike$WithFilter.foreach(TraversableLike.scala:771) at org.apache.spark.executor.Executor.org$apache$spark$executor$Executor$$updateDependencies(Executor.scala:347) at org.apache.spark.executor.Executor$TaskRunner.run(Executor.scala:177) at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1145) at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:615) at java.lang.Thread.run(Thread.java:745) 
[![pwendell](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Patrick Wendell](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=pwendell) added a comment - [16/Mar/15 03:28](https://issues.apache.org/jira/browse/SPARK-6313?focusedCommentId=14362687&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-14362687)
[joshrosen](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=joshrosen) changing default caching behavior seems like it could silently regress performance for the vas majority of users who aren't on NFS. What about a hotfix for 1.3.1 that just exposes the config for NFS users (this is very small population), but doesn't change the default. That may be sufficient in itself... or if we want a real fix that makes it work out-of-the-box on NDFS, we can put it in 1.4.
[![pwendell](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Patrick Wendell](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=pwendell) added a comment - [16/Mar/15 03:28](https://issues.apache.org/jira/browse/SPARK-6313?focusedCommentId=14362687&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-14362687) joshrosen changing default caching behavior seems like it could silently regress performance for the vas majority of users who aren't on NFS. What about a hotfix for 1.3.1 that just exposes the config for NFS users (this is very small population), but doesn't change the default. That may be sufficient in itself... or if we want a real fix that makes it work out-of-the-box on NDFS, we can put it in 1.4. 
[![apachespark](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Apache Spark](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=apachespark) added a comment - [16/Mar/15 06:46](https://issues.apache.org/jira/browse/SPARK-6313?focusedCommentId=14362818&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-14362818)
User 'nemccarthy' has created a pull request for this issue:  
<https://github.com/apache/spark/pull/5036>
[![apachespark](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Apache Spark](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=apachespark) added a comment - [16/Mar/15 06:46](https://issues.apache.org/jira/browse/SPARK-6313?focusedCommentId=14362818&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-14362818) User 'nemccarthy' has created a pull request for this issue: https://github.com/apache/spark/pull/5036 
[![nemccarthy](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Nathan McCarthy](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=nemccarthy) added a comment - [16/Mar/15 06:47](https://issues.apache.org/jira/browse/SPARK-6313?focusedCommentId=14362820&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-14362820)
Thanks for the feedback guys. The config option workaround seems like the path of least resistance for now with some more testing being required for a different implementation. For us it would be great if we could get a fix ASAP. Ive created PR 5603 <https://github.com/apache/spark/pull/5036>
[![nemccarthy](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Nathan McCarthy](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=nemccarthy) added a comment - [16/Mar/15 06:47](https://issues.apache.org/jira/browse/SPARK-6313?focusedCommentId=14362820&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-14362820) Thanks for the feedback guys. The config option workaround seems like the path of least resistance for now with some more testing being required for a different implementation. For us it would be great if we could get a fix ASAP. Ive created PR 5603 https://github.com/apache/spark/pull/5036 
[![joshrosen](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Josh Rosen](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=joshrosen) added a comment - [17/Mar/15 16:34](https://issues.apache.org/jira/browse/SPARK-6313?focusedCommentId=14365450&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-14365450)
Issue resolved by pull request 5036  
<https://github.com/apache/spark/pull/5036>
[![joshrosen](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Josh Rosen](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=joshrosen) added a comment - [17/Mar/15 16:34](https://issues.apache.org/jira/browse/SPARK-6313?focusedCommentId=14365450&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-14365450) Issue resolved by pull request 5036 https://github.com/apache/spark/pull/5036 
[![joshrosen](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Josh Rosen](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=joshrosen) added a comment - [17/Mar/15 16:35](https://issues.apache.org/jira/browse/SPARK-6313?focusedCommentId=14365452&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-14365452)
I've merged Nathan's patch into 1.4.0, 1.3.1, and 1.2.2. After this path, users can work around this bug by setting `spark.files.useFetchCache=false` in their SparkConf.
[![joshrosen](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Josh Rosen](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=joshrosen) added a comment - [17/Mar/15 16:35](https://issues.apache.org/jira/browse/SPARK-6313?focusedCommentId=14365452&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-14365452) I've merged Nathan's patch into 1.4.0, 1.3.1, and 1.2.2. After this path, users can work around this bug by setting spark.files.useFetchCache=false in their SparkConf. 
#### People 

Assignee: 
     ![nemccarthy](https://issues.apache.org/jira/secure/useravatar?size=small&avatarId=10452) Nathan McCarthy  

Reporter: 
     ![nemccarthy](https://issues.apache.org/jira/secure/useravatar?size=small&avatarId=10452) Nathan McCarthy  

Votes:
     0 Vote for this issue 

Watchers:
     5 Start watching this issue
#### Dates 

Created: 
     13/Mar/15 04:17 

Updated: 
     17/Mar/15 16:35 

Resolved: 
     17/Mar/15 16:34
  * Atlassian Jira [Project Management Software](https://www.atlassian.com/software/jira)
  * [About Jira](https://issues.apache.org/jira/secure/AboutPage.jspa/secure/AboutPage.jspa)
  * [Report a problem](https://issues.apache.org/jira/secure/CreateIssue!default.jspa)


Powered by a free Atlassian [Jira](http://www.atlassian.com/software/jira) open source license for Apache Software Foundation. Try Jira - [bug tracking software](http://www.atlassian.com/software/jira) for _your_ team. 
[Atlassian](http://www.atlassian.com/)
[](javascript:;)[](javascript:;)

[Log in](https://issues.apache.org/jira/login.jsp?os_destination=%2Fbrowse%2FYARN-11053)[Skip to main content](https://issues.apache.org/jira/browse/YARN-11053#main)[Skip to sidebar](https://issues.apache.org/jira/browse/YARN-11053#sidebar)
Linked Applications
Loading…
[![ASF Jira](https://issues.apache.org/jira/s/-vddc6b/820010/g3jj3a/_/jira-logo-scaled.png)](https://issues.apache.org/jira/secure/MyJiraHome.jspa)
  * [Dashboards](https://issues.apache.org/jira/secure/Dashboard.jspa "View and manage your dashboards")
  * [Projects](https://issues.apache.org/jira/browse/YARN "View recent projects and browse a list of projects")
  * [Issues](https://issues.apache.org/jira/issues/ "Search for issues and view recent issues")

  *   * [Help](https://docs.atlassian.com/jira/jcore-docs-0820/ "Help")
    * [Jira Core help](https://docs.atlassian.com/jira/jcore-docs-0820/ "Go to the online documentation for Jira Core")
    * [Keyboard Shortcuts](https://issues.apache.org/jira/secure/ViewKeyboardShortcuts!default.jspa "Get more information about Jira's Keyboard Shortcuts \( Type '?' \)")
    * [About Jira](https://issues.apache.org/jira/secure/AboutPage.jspa "Get more information about Jira")
    * [Jira Credits](https://issues.apache.org/jira/secure/credits/AroundTheWorld!default.jspa "See who did what")
  * [Log In](https://issues.apache.org/jira/login.jsp?os_destination=%2Fbrowse%2FYARN-11053)

Public signup for this instance is **disabled**. Go to our [Self serve sign up page](https://selfserve.apache.org/jira-account.html) to request an account. Report potential security issues [privately](https://apache.org/security/#reporting-a-vulnerability)
[![Hadoop YARN](https://issues.apache.org/jira/secure/projectavatar?pid=12313722&avatarId=15135)![Project Type: software](https://issues.apache.org/jira/browse/YARN-11053)](https://issues.apache.org/jira/projects/YARN/summary "Hadoop YARN")
#
[Hadoop YARN](https://issues.apache.org/jira/projects/YARN/summary "Hadoop YARN")
  * [Issues](https://issues.apache.org/jira/projects/YARN/issues)
  * [Reports](https://issues.apache.org/jira/projects/YARN?selectedItem=com.atlassian.jira.jira-projects-plugin:report-page)
  * [Components](https://issues.apache.org/jira/projects/YARN?selectedItem=com.atlassian.jira.jira-projects-plugin:components-page)
  * [Roadmap](https://issues.apache.org/jira/projects/YARN?selectedItem=biz.everit.jira.epic-roadmap:erfj-sidebar-roadmap)

![Uploaded image for project: 'Hadoop YARN'](https://issues.apache.org/jira/secure/projectavatar?pid=12313722&avatarId=15135)
  1. [Hadoop YARN](https://issues.apache.org/jira/browse/YARN)
  2. [YARN-11053](https://issues.apache.org/jira/browse/YARN-11053)

# AuxService should not use class name as default system classes
[Log In](https://issues.apache.org/jira/login.jsp?os_destination=%2Fbrowse%2FYARN-11053 "Log In")
[ Export](https://issues.apache.org/jira/browse/YARN-11053)
[XML](https://issues.apache.org/jira/si/jira.issueviews:issue-xml/YARN-11053/YARN-11053.xml)[Word](https://issues.apache.org/jira/si/jira.issueviews:issue-word/YARN-11053/YARN-11053.doc)[Printable](https://issues.apache.org/jira/si/jira.issueviews:issue-html/YARN-11053/YARN-11053.html)[JSON](https://issues.apache.org/jira/si/com.atlassian.jira.plugins.jira-importers-plugin:issue-json/YARN-11053/YARN-11053.json)

#### Details
  * ** Type: ** ![](https://issues.apache.org/jira/secure/viewavatar?size=xsmall&avatarId=21133&avatarType=issuetype) Bug
  * **Status:** Resolved
  * ** Priority: ** ![](https://issues.apache.org/jira/images/icons/priorities/major.svg) Major
  * **Resolution:** Fixed
  * ** Affects Version/s: ** 3.3.1
  * ** Fix Version/s:  ** [3.4.0](https://issues.apache.org/jira/issues/?jql=project+%3D+YARN+AND+fixVersion+%3D+3.4.0 "3.4.0 Hadoop 3.4.0"), [3.3.2](https://issues.apache.org/jira/issues/?jql=project+%3D+YARN+AND+fixVersion+%3D+3.3.2 "3.3.2 Hadoop 3.3.2")
  * ** Component/s: ** [auxservices](https://issues.apache.org/jira/issues/?jql=project+%3D+YARN+AND+component+%3D+auxservices "auxservices ")
  * ** Labels: **
    * [pull-request-available](https://issues.apache.org/jira/issues/?jql=labels+%3D+pull-request-available "pull-request-available")

#### Description
Following Apache Spark document to configure Spark Shuffle Service as YARN AuxService,
<https://spark.apache.org/docs/3.2.0/running-on-yarn.html#running-multiple-versions-of-the-spark-shuffle-service>

```
  <property>
    <name>yarn.nodemanager.aux-services</name>
    <value>spark_shuffle</value>
  </property>
  <property>
    <name>yarn.nodemanager.aux-services.spark_shuffle.classpath</name>
    <value>/opt/apache/spark/yarn/*</value>
  </property>
  <property>
    <name>yarn.nodemanager.aux-services.spark_shuffle.class&lt;/name>
    <value>org.apache.spark.network.yarn.YarnShuffleService</value>
  </property>
```

but failed with exception

```
2021-12-02 15:34:00,886 INFO util.ApplicationClassLoader: classpath: [file:/opt/apache/spark/yarn/spark-3.2.0-yarn-shuffle.jar]
2021-12-02 15:34:00,886 INFO util.ApplicationClassLoader: system classes: [org.apache.spark.network.yarn.YarnShuffleService]
2021-12-02 15:34:00,887 INFO service.AbstractService: Service org.apache.hadoop.yarn.server.nodemanager.containermanager.AuxServices failed in state INITED
org.apache.hadoop.yarn.exceptions.YarnRuntimeException: java.lang.ClassNotFoundException: org.apache.spark.network.yarn.YarnShuffleService
        at org.apache.hadoop.yarn.server.nodemanager.containermanager.AuxServices.initAuxService(AuxServices.java:482)
        at org.apache.hadoop.yarn.server.nodemanager.containermanager.AuxServices.serviceInit(AuxServices.java:761)
        at org.apache.hadoop.service.AbstractService.init(AbstractService.java:164)
        at org.apache.hadoop.service.CompositeService.serviceInit(CompositeService.java:109)
        at org.apache.hadoop.yarn.server.nodemanager.containermanager.ContainerManagerImpl.serviceInit(ContainerManagerImpl.java:327)
        at org.apache.hadoop.service.AbstractService.init(AbstractService.java:164)
        at org.apache.hadoop.service.CompositeService.serviceInit(CompositeService.java:109)
        at org.apache.hadoop.yarn.server.nodemanager.NodeManager.serviceInit(NodeManager.java:494)
        at org.apache.hadoop.service.AbstractService.init(AbstractService.java:164)
        at org.apache.hadoop.yarn.server.nodemanager.NodeManager.initAndStartNodeManager(NodeManager.java:962)
        at org.apache.hadoop.yarn.server.nodemanager.NodeManager.main(NodeManager.java:1042)
Caused by: java.lang.ClassNotFoundException: org.apache.spark.network.yarn.YarnShuffleService
        at java.net.URLClassLoader.findClass(URLClassLoader.java:387)
        at java.lang.ClassLoader.loadClass(ClassLoader.java:419)
        at sun.misc.Launcher$AppClassLoader.loadClass(Launcher.java:352)
        at java.lang.ClassLoader.loadClass(ClassLoader.java:352)
        at org.apache.hadoop.util.ApplicationClassLoader.loadClass(ApplicationClassLoader.java:189)
        at org.apache.hadoop.util.ApplicationClassLoader.loadClass(ApplicationClassLoader.java:157)
        at java.lang.Class.forName0(Native Method)
        at java.lang.Class.forName(Class.java:348)
        at org.apache.hadoop.yarn.server.nodemanager.containermanager.AuxiliaryServiceWithCustomClassLoader.getInstance(AuxiliaryServiceWithCustomClassLoader.java:165)
        at org.apache.hadoop.yarn.server.nodemanager.containermanager.AuxServices.createAuxServiceFromLocalClasspath(AuxServices.java:242)
        at org.apache.hadoop.yarn.server.nodemanager.containermanager.AuxServices.createAuxService(AuxServices.java:271)
        at org.apache.hadoop.yarn.server.nodemanager.containermanager.AuxServices.initAuxService(AuxServices.java:452)
        ... 10 more

```

A workaround is adding

```
<property>
    <name>yarn.nodemanager.aux-services.spark_shuffle.system-classes</name>
    <value>not.existed.class&amp;amp;lt;/value>
 </property>
```

#### Attachments
#### Issue Links

duplicates

![Bug - A problem which impairs or prevents the functions of the product.](https://issues.apache.org/jira/secure/viewavatar?size=xsmall&avatarId=21133&avatarType=issuetype) [YARN-9967](https://issues.apache.org/jira/browse/YARN-9967) Fix NodeManager failing to start when Hdfs Auxillary Jar is set
  * ![Major - Major loss of function.](https://issues.apache.org/jira/images/icons/priorities/major.svg)
  * Resolved

is caused by

![Sub-task - The sub-task of the issue](https://issues.apache.org/jira/secure/viewavatar?size=xsmall&avatarId=21146&avatarType=issuetype) [YARN-9075](https://issues.apache.org/jira/browse/YARN-9075) Dynamically add or remove auxiliary services
  * ![Major - Major loss of function.](https://issues.apache.org/jira/images/icons/priorities/major.svg)
  * Resolved

relates to

![Documentation - Documentation or Website](https://issues.apache.org/jira/images/icons/issuetypes/documentation.png) [SPARK-37925](https://issues.apache.org/jira/browse/SPARK-37925) Update document to mention the workaround for YARN-11053
  * ![Trivial - Cosmetic problem like misspelt words or misaligned text.](https://issues.apache.org/jira/images/icons/priorities/trivial.svg)
  * Closed

links to

![Web Link](https://github.com/favicon.ico) [GitHub Pull Request #3816](https://github.com/apache/hadoop/pull/3816)
#### Activity
  * [All](https://issues.apache.org/jira/browse/YARN-11053?page=com.atlassian.jira.plugin.system.issuetabpanels:all-tabpanel)
  * Comments
  * [Work Log](https://issues.apache.org/jira/browse/YARN-11053?page=com.atlassian.jira.plugin.system.issuetabpanels:worklog-tabpanel)
  * [History](https://issues.apache.org/jira/browse/YARN-11053?page=com.atlassian.jira.plugin.system.issuetabpanels:changehistory-tabpanel)
  * [Activity](https://issues.apache.org/jira/browse/YARN-11053?page=com.atlassian.streams.streams-jira-plugin:activity-stream-issue-tab)
  * [Transitions](https://issues.apache.org/jira/browse/YARN-11053?page=com.googlecode.jira-suite-utilities:transitions-summary-tabpanel)

[ Ascending order - Click to sort in descending order ](https://issues.apache.org/jira/browse/YARN-11053?actionOrder=desc "Ascending order - Click to sort in descending order")
[![aajisaka](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Akira Ajisaka](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=aajisaka) added a comment - [24/Dec/21 02:14](https://issues.apache.org/jira/browse/YARN-11053?focusedCommentId=17464865&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-17464865)
Committed to trunk and branch-3.3.
[![aajisaka](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Akira Ajisaka](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=aajisaka) added a comment - [24/Dec/21 02:14](https://issues.apache.org/jira/browse/YARN-11053?focusedCommentId=17464865&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-17464865) Committed to trunk and branch-3.3.
[![aajisaka](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Akira Ajisaka](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=aajisaka) added a comment - [04/Jan/22 04:14](https://issues.apache.org/jira/browse/YARN-11053?focusedCommentId=17468346&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-17468346)
Cherry-picked to branch-3.3.2.
[![aajisaka](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Akira Ajisaka](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=aajisaka) added a comment - [04/Jan/22 04:14](https://issues.apache.org/jira/browse/YARN-11053?focusedCommentId=17468346&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-17468346) Cherry-picked to branch-3.3.2.
#### People

Assignee:
     ![chengpan](https://issues.apache.org/jira/secure/useravatar?size=small&avatarId=10452) Cheng Pan

Reporter:
     ![chengpan](https://issues.apache.org/jira/secure/useravatar?size=small&avatarId=10452) Cheng Pan

Votes:
     0 Vote for this issue

Watchers:
     3 Start watching this issue
#### Dates

Created:
     18/Dec/21 12:35

Updated:
     24/Nov/22 00:38

Resolved:
     24/Dec/21 02:14
#### Time Tracking

Estimated:

|  ![Original Estimate - Not Specified](https://issues.apache.org/jira/images/border/spacer.gif)  |
| --- |      Not Specified

Remaining:

|  ![Remaining Estimate - 0h](https://issues.apache.org/jira/images/border/spacer.gif)  |
| --- |      0h

Logged:

|  ![Time Spent - 50m](https://issues.apache.org/jira/images/border/spacer.gif)  |
| --- |      50m
  * Atlassian Jira [Project Management Software](https://www.atlassian.com/software/jira)
  * [About Jira](https://issues.apache.org/jira/secure/AboutPage.jspa/secure/AboutPage.jspa)
  * [Report a problem](https://issues.apache.org/jira/secure/CreateIssue!default.jspa)

Powered by a free Atlassian [Jira](http://www.atlassian.com/software/jira) open source license for Apache Software Foundation. Try Jira - [bug tracking software](http://www.atlassian.com/software/jira) for _your_ team.
[Atlassian](http://www.atlassian.com/)
[](javascript:;)[](javascript:;)

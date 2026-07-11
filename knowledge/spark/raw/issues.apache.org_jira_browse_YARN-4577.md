[Log in](https://issues.apache.org/jira/login.jsp?os_destination=%2Fbrowse%2FYARN-4577)[Skip to main content](https://issues.apache.org/jira/browse/YARN-4577#main)[Skip to sidebar](https://issues.apache.org/jira/browse/YARN-4577#sidebar)
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
  * [Log In](https://issues.apache.org/jira/login.jsp?os_destination=%2Fbrowse%2FYARN-4577)


Public signup for this instance is **disabled**. Go to our [Self serve sign up page](https://selfserve.apache.org/jira-account.html) to request an account. Report potential security issues [privately](https://apache.org/security/#reporting-a-vulnerability)
[![Hadoop YARN](https://issues.apache.org/jira/secure/projectavatar?pid=12313722&avatarId=15135)![Project Type: software](https://issues.apache.org/jira/browse/YARN-4577)](https://issues.apache.org/jira/projects/YARN/summary "Hadoop YARN")
# 
[Hadoop YARN](https://issues.apache.org/jira/projects/YARN/summary "Hadoop YARN")
  * [Issues](https://issues.apache.org/jira/projects/YARN/issues)
  * [Reports](https://issues.apache.org/jira/projects/YARN?selectedItem=com.atlassian.jira.jira-projects-plugin:report-page)
  * [Components](https://issues.apache.org/jira/projects/YARN?selectedItem=com.atlassian.jira.jira-projects-plugin:components-page)
  * [Roadmap](https://issues.apache.org/jira/projects/YARN?selectedItem=biz.everit.jira.epic-roadmap:erfj-sidebar-roadmap)


![Uploaded image for project: 'Hadoop YARN'](https://issues.apache.org/jira/secure/projectavatar?pid=12313722&avatarId=15135)
  1. [Hadoop YARN](https://issues.apache.org/jira/browse/YARN)
  2. [YARN-4577](https://issues.apache.org/jira/browse/YARN-4577)


# Enable aux services to have their own custom classpath/jar file
[Log In](https://issues.apache.org/jira/login.jsp?os_destination=%2Fbrowse%2FYARN-4577 "Log In")
[ Export](https://issues.apache.org/jira/browse/YARN-4577)
[XML](https://issues.apache.org/jira/si/jira.issueviews:issue-xml/YARN-4577/YARN-4577.xml)[Word](https://issues.apache.org/jira/si/jira.issueviews:issue-word/YARN-4577/YARN-4577.doc)[Printable](https://issues.apache.org/jira/si/jira.issueviews:issue-html/YARN-4577/YARN-4577.html)[JSON](https://issues.apache.org/jira/si/com.atlassian.jira.plugins.jira-importers-plugin:issue-json/YARN-4577/YARN-4577.json) 

#### Details
  * ** Type: ** ![](https://issues.apache.org/jira/secure/viewavatar?size=xsmall&avatarId=21140&avatarType=issuetype) Improvement 
  * **Status:** Resolved
  * ** Priority: ** ![](https://issues.apache.org/jira/images/icons/priorities/major.svg) Major 
  * **Resolution:** Fixed 
  * ** Affects Version/s: ** 2.8.0
  * ** Fix Version/s:  ** [2.9.0](https://issues.apache.org/jira/issues/?jql=project+%3D+YARN+AND+fixVersion+%3D+2.9.0 "2.9.0 2.9.0 release"), [3.0.0-alpha1](https://issues.apache.org/jira/issues/?jql=project+%3D+YARN+AND+fixVersion+%3D+3.0.0-alpha1 "3.0.0-alpha1 3.0.0-alpha1 release")
  * ** Component/s: ** None 
  * ** Labels: **
None


  * ** Hadoop Flags: **
Reviewed


#### Description
Right now, users have to add their jars to the NM classpath directly, thus put them on the system classloader. But if multiple versions of the plugin are present on the classpath, there is no control over which version actually gets loaded. Or if there are any conflicts between the dependencies introduced by the auxiliary service and the NM itself, they can break the NM, the auxiliary service, or both.
The solution could be: to instantiate aux services using a classloader that is different from the system classloader.
#### Attachments
#### Attachments
  * Options
    * [Sort By Name](https://issues.apache.org/jira/browse/YARN-4577?attachmentSortBy=fileName#attachmentmodule "viewissue.subtasks.tab.show.all.name")
    * [Sort By Date](https://issues.apache.org/jira/browse/YARN-4577?attachmentSortBy=dateTime#attachmentmodule "Sort By Date")
    * [Ascending](https://issues.apache.org/jira/browse/YARN-4577?attachmentOrder=asc#attachmentmodule "Ascending")
    * [Descending](https://issues.apache.org/jira/browse/YARN-4577?attachmentOrder=desc#attachmentmodule "Descending")


  1. [](https://issues.apache.org/jira/secure/attachment/12781604/YARN-4577.1.patch) 

[YARN-4577.1.patch](https://issues.apache.org/jira/secure/attachment/12781604/YARN-4577.1.patch "Latest  11/Jan/16 17:36 - Xuan Gong")
    11/Jan/16 17:36     7 kB     Xuan Gong
  2. [](https://issues.apache.org/jira/secure/attachment/12781868/YARN-4577.2.patch) 

[YARN-4577.2.patch](https://issues.apache.org/jira/secure/attachment/12781868/YARN-4577.2.patch "Latest  12/Jan/16 17:54 - Xuan Gong")
    12/Jan/16 17:54     9 kB     Xuan Gong
  3. [](https://issues.apache.org/jira/secure/attachment/12783119/YARN-4577.20160119.1.patch) 

[YARN-4577.20160119.1.patch](https://issues.apache.org/jira/secure/attachment/12783119/YARN-4577.20160119.1.patch "Latest  19/Jan/16 15:17 - Xuan Gong")
    19/Jan/16 15:17     10 kB     Xuan Gong
  4. [](https://issues.apache.org/jira/secure/attachment/12786365/YARN-4577.20160204.patch) 

[YARN-4577.20160204.patch](https://issues.apache.org/jira/secure/attachment/12786365/YARN-4577.20160204.patch "Latest  05/Feb/16 00:45 - Xuan Gong")
    05/Feb/16 00:45     13 kB     Xuan Gong
  5. [](https://issues.apache.org/jira/secure/attachment/12801375/YARN-4577.20160428.patch) 

[YARN-4577.20160428.patch](https://issues.apache.org/jira/secure/attachment/12801375/YARN-4577.20160428.patch "Latest  29/Apr/16 03:34 - Xuan Gong")
    29/Apr/16 03:34     13 kB     Xuan Gong
  6. [](https://issues.apache.org/jira/secure/attachment/12803148/YARN-4577.20160509.patch) 

[YARN-4577.20160509.patch](https://issues.apache.org/jira/secure/attachment/12803148/YARN-4577.20160509.patch "Latest  10/May/16 03:44 - Xuan Gong")
    10/May/16 03:44     20 kB     Xuan Gong
  7. [](https://issues.apache.org/jira/secure/attachment/12803326/YARN-4577.20160510.patch) 

[YARN-4577.20160510.patch](https://issues.apache.org/jira/secure/attachment/12803326/YARN-4577.20160510.patch "Latest  10/May/16 22:06 - Xuan Gong")
    10/May/16 22:06     15 kB     Xuan Gong
  8. [](https://issues.apache.org/jira/secure/attachment/12803562/YARN-4577.20160511.1.patch) 

[YARN-4577.20160511.1.patch](https://issues.apache.org/jira/secure/attachment/12803562/YARN-4577.20160511.1.patch "Latest  12/May/16 02:57 - Xuan Gong")
    12/May/16 02:57     23 kB     Xuan Gong
  9. [](https://issues.apache.org/jira/secure/attachment/12803459/YARN-4577.20160511.patch) 

[YARN-4577.20160511.patch](https://issues.apache.org/jira/secure/attachment/12803459/YARN-4577.20160511.patch "Latest  11/May/16 17:17 - Xuan Gong")
    11/May/16 17:17     23 kB     Xuan Gong
  10. [](https://issues.apache.org/jira/secure/attachment/12782606/YARN-4577.3.patch) 

[YARN-4577.3.patch](https://issues.apache.org/jira/secure/attachment/12782606/YARN-4577.3.patch "Latest  15/Jan/16 21:05 - Xuan Gong")
    15/Jan/16 21:05     10 kB     Xuan Gong
  11. [](https://issues.apache.org/jira/secure/attachment/12782643/YARN-4577.3.rebase.patch) 

[YARN-4577.3.rebase.patch](https://issues.apache.org/jira/secure/attachment/12782643/YARN-4577.3.rebase.patch "Latest  16/Jan/16 00:09 - Xuan Gong")
    16/Jan/16 00:09     11 kB     Xuan Gong
  12. [](https://issues.apache.org/jira/secure/attachment/12782816/YARN-4577.4.patch) 

[YARN-4577.4.patch](https://issues.apache.org/jira/secure/attachment/12782816/YARN-4577.4.patch "Latest  18/Jan/16 07:07 - Xuan Gong")
    18/Jan/16 07:07     12 kB     Xuan Gong
  13. [](https://issues.apache.org/jira/secure/attachment/12801074/YARN-4577.5.patch) 

[YARN-4577.5.patch](https://issues.apache.org/jira/secure/attachment/12801074/YARN-4577.5.patch "Latest  27/Apr/16 17:35 - Xuan Gong")
    27/Apr/16 17:35     11 kB     Xuan Gong
  14. [](https://issues.apache.org/jira/secure/attachment/12799895/YARN-4577.poc.patch) 

[YARN-4577.poc.patch](https://issues.apache.org/jira/secure/attachment/12799895/YARN-4577.poc.patch "Latest  21/Apr/16 03:42 - Xuan Gong")
    21/Apr/16 03:42     11 kB     Xuan Gong


#### Issue Links 

breaks
    
![Bug - A problem which impairs or prevents the functions of the product.](https://issues.apache.org/jira/secure/viewavatar?size=xsmall&avatarId=21133&avatarType=issuetype) [YARN-6412](https://issues.apache.org/jira/browse/YARN-6412) aux-services classpath not documented
  * ![Minor - Minor loss of function, or other problem where easy workaround is present.](https://issues.apache.org/jira/images/icons/priorities/minor.svg)
  * Resolved



is depended upon by
    
![Bug - A problem which impairs or prevents the functions of the product.](https://issues.apache.org/jira/secure/viewavatar?size=xsmall&avatarId=21133&avatarType=issuetype) [SPARK-12807](https://issues.apache.org/jira/browse/SPARK-12807) Spark External Shuffle not working in Hadoop clusters with Jackson 2.2.3
  * ![Critical - Crashes, loss of data, severe memory leak.](https://issues.apache.org/jira/images/icons/priorities/critical.svg)
  * Resolved



relates to
    
![Bug - A problem which impairs or prevents the functions of the product.](https://issues.apache.org/jira/secure/viewavatar?size=xsmall&avatarId=21133&avatarType=issuetype) [YARN-7598](https://issues.apache.org/jira/browse/YARN-7598) Document how to use classpath isolation for aux-services in YARN
  * ![Major - Major loss of function.](https://issues.apache.org/jira/images/icons/priorities/major.svg)
  * Resolved

    
![Improvement - An improvement or enhancement to an existing feature or task.](https://issues.apache.org/jira/secure/viewavatar?size=xsmall&avatarId=21140&avatarType=issuetype) [YARN-1151](https://issues.apache.org/jira/browse/YARN-1151) Ability to configure auxiliary services from HDFS-based JAR files
  * ![Major - Major loss of function.](https://issues.apache.org/jira/images/icons/priorities/major.svg)
  * Resolved


#### Activity
  * [All](https://issues.apache.org/jira/browse/YARN-4577?page=com.atlassian.jira.plugin.system.issuetabpanels:all-tabpanel)
  * Comments
  * [Work Log](https://issues.apache.org/jira/browse/YARN-4577?page=com.atlassian.jira.plugin.system.issuetabpanels:worklog-tabpanel)
  * [History](https://issues.apache.org/jira/browse/YARN-4577?page=com.atlassian.jira.plugin.system.issuetabpanels:changehistory-tabpanel)
  * [Activity](https://issues.apache.org/jira/browse/YARN-4577?page=com.atlassian.streams.streams-jira-plugin:activity-stream-issue-tab)
  * [Transitions](https://issues.apache.org/jira/browse/YARN-4577?page=com.googlecode.jira-suite-utilities:transitions-summary-tabpanel)


[ Ascending order - Click to sort in descending order ](https://issues.apache.org/jira/browse/YARN-4577?actionOrder=desc "Ascending order - Click to sort in descending order")
[![xgong](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10443) Xuan Gong](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=xgong) added a comment - [11/Jan/16 17:37](https://issues.apache.org/jira/browse/YARN-4577?focusedCommentId=15092348&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15092348)
Add a patch to have the ability to load the aux-service class from local path/hdfs.
[![xgong](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10443) Xuan Gong](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=xgong) added a comment - [11/Jan/16 17:37](https://issues.apache.org/jira/browse/YARN-4577?focusedCommentId=15092348&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15092348) Add a patch to have the ability to load the aux-service class from local path/hdfs. 
[![hadoopqa](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Hadoop QA](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=hadoopqa) added a comment - [11/Jan/16 18:41](https://issues.apache.org/jira/browse/YARN-4577?focusedCommentId=15092451&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15092451)  
|  ![](https://issues.apache.org/jira/images/icons/emoticons/error.png) **-1 overall**  |  
| --- |  
  
  
  
|  Vote   |  Subsystem   |  Runtime   |  Comment   |  
| --- | --- | --- | --- |  
|  0  |  reexec   |  0m 1s   |  Docker mode activated.   |  
|  +1  |  @author   |  0m 0s   |  The patch does not contain any @author tags.   |  
|  +1  |  test4tests   |  0m 0s   |  The patch appears to include 1 new or modified test files.   |  
|  +1  |  mvninstall   |  8m 0s   |  trunk passed   |  
|  +1  |  compile   |  1m 51s   |  trunk passed with JDK v1.8.0_66   |  
|  +1  |  compile   |  2m 10s   |  trunk passed with JDK v1.7.0_91   |  
|  +1  |  checkstyle   |  0m 30s   |  trunk passed   |  
|  +1  |  mvnsite   |  0m 58s   |  trunk passed   |  
|  +1  |  mvneclipse   |  0m 22s   |  trunk passed   |  
|  +1  |  findbugs   |  2m 18s   |  trunk passed   |  
|  +1  |  javadoc   |  0m 58s   |  trunk passed with JDK v1.8.0_66   |  
|  +1  |  javadoc   |  3m 7s   |  trunk passed with JDK v1.7.0_91   |  
|  +1  |  mvninstall   |  0m 46s   |  the patch passed   |  
|  +1  |  compile   |  2m 19s   |  the patch passed with JDK v1.8.0_66   |  
|  +1  |  javac   |  2m 19s   |  the patch passed   |  
|  +1  |  compile   |  2m 5s   |  the patch passed with JDK v1.7.0_91   |  
|  +1  |  javac   |  2m 5s   |  the patch passed   |  
|  -1  |  checkstyle   |  0m 31s   |  Patch generated 4 new checkstyle issues in hadoop-yarn-project/hadoop-yarn (total was 261, now 264).   |  
|  +1  |  mvnsite   |  0m 55s   |  the patch passed   |  
|  +1  |  mvneclipse   |  0m 23s   |  the patch passed   |  
|  +1  |  whitespace   |  0m 0s   |  Patch has no whitespace issues.   |  
|  -1  |  findbugs   |  1m 7s   |  hadoop-yarn-project/hadoop-yarn/hadoop-yarn-server/hadoop-yarn-server-nodemanager introduced 1 new FindBugs issues.   |  
|  +1  |  javadoc   |  0m 55s   |  the patch passed with JDK v1.8.0_66   |  
|  +1  |  javadoc   |  3m 7s   |  the patch passed with JDK v1.7.0_91   |  
|  +1  |  unit   |  0m 20s   |  hadoop-yarn-api in the patch passed with JDK v1.8.0_66.   |  
|  +1  |  unit   |  8m 38s   |  hadoop-yarn-server-nodemanager in the patch passed with JDK v1.8.0_66.   |  
|  +1  |  unit   |  0m 22s   |  hadoop-yarn-api in the patch passed with JDK v1.7.0_91.   |  
|  +1  |  unit   |  9m 10s   |  hadoop-yarn-server-nodemanager in the patch passed with JDK v1.7.0_91.   |  
|  +1  |  asflicense   |  0m 18s   |  Patch does not generate ASF License warnings.   |  
|   |   |  53m 54s   |   |  
  
  
  
|  Reason   |  Tests   |  
| --- | --- |  
|  FindBugs   |  module:hadoop-yarn-project/hadoop-yarn/hadoop-yarn-server/hadoop-yarn-server-nodemanager   |  
|   |  org.apache.hadoop.yarn.server.nodemanager.containermanager.AuxServices.serviceInit(Configuration) creates a java.net.URLClassLoader classloader, which should be performed within a doPrivileged block At AuxServices.java:which should be performed within a doPrivileged block At AuxServices.java:[line 133]  |  
  
  
  
|  Subsystem   |  Report/Notes   |  
| --- | --- |  
|  Docker   |  Image:yetus/hadoop:0ca8df7   |  
|  JIRA Patch URL   |  <https://issues.apache.org/jira/secure/attachment/12781604/YARN-4577.1.patch>  |  
|  JIRA Issue   |  [~~YARN-4577~~](https://issues.apache.org/jira/browse/YARN-4577 "Enable aux services to have their own custom classpath/jar file")  |  
|  Optional Tests   |  asflicense compile javac javadoc mvninstall mvnsite unit findbugs checkstyle   |  
|  uname   |  Linux f64ed5ca774f 3.13.0-36-lowlatency #63-Ubuntu SMP PREEMPT Wed Sep 3 21:56:12 UTC 2014 x86_64 x86_64 x86_64 GNU/Linux   |  
|  Build tool   |  maven   |  
|  Personality   |  /testptch/hadoop/patchprocess/precommit/personality/provided.sh   |  
|  git revision   |  trunk / 95f3201   |  
|  Default Java   |  1.7.0_91   |  
|  Multi-JDK versions   |  /usr/lib/jvm/java-8-oracle:1.8.0_66 /usr/lib/jvm/java-7-openjdk-amd64:1.7.0_91   |  
|  findbugs   |  v3.0.0   |  
|  checkstyle   |  <https://builds.apache.org/job/PreCommit-YARN-Build/10228/artifact/patchprocess/diff-checkstyle-hadoop-yarn-project_hadoop-yarn.txt>  |  
|  findbugs   |  <https://builds.apache.org/job/PreCommit-YARN-Build/10228/artifact/patchprocess/new-findbugs-hadoop-yarn-project_hadoop-yarn_hadoop-yarn-server_hadoop-yarn-server-nodemanager.html>  |  
|  JDK v1.7.0_91 Test Results   |  <https://builds.apache.org/job/PreCommit-YARN-Build/10228/testReport/>  |  
|  modules   |  C: hadoop-yarn-project/hadoop-yarn/hadoop-yarn-api hadoop-yarn-project/hadoop-yarn/hadoop-yarn-server/hadoop-yarn-server-nodemanager U: hadoop-yarn-project/hadoop-yarn   |  
|  Max memory used   |  75MB   |  
|  Powered by   |  Apache Yetus 0.2.0-SNAPSHOT <http://yetus.apache.org>  |  
|  Console output   |  <https://builds.apache.org/job/PreCommit-YARN-Build/10228/console>  |  
This message was automatically generated.
[![hadoopqa](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Hadoop QA](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=hadoopqa) added a comment - [11/Jan/16 18:41](https://issues.apache.org/jira/browse/YARN-4577?focusedCommentId=15092451&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15092451) -1 overall Vote Subsystem Runtime Comment 0 reexec 0m 1s Docker mode activated. +1 @author 0m 0s The patch does not contain any @author tags. +1 test4tests 0m 0s The patch appears to include 1 new or modified test files. +1 mvninstall 8m 0s trunk passed +1 compile 1m 51s trunk passed with JDK v1.8.0_66 +1 compile 2m 10s trunk passed with JDK v1.7.0_91 +1 checkstyle 0m 30s trunk passed +1 mvnsite 0m 58s trunk passed +1 mvneclipse 0m 22s trunk passed +1 findbugs 2m 18s trunk passed +1 javadoc 0m 58s trunk passed with JDK v1.8.0_66 +1 javadoc 3m 7s trunk passed with JDK v1.7.0_91 +1 mvninstall 0m 46s the patch passed +1 compile 2m 19s the patch passed with JDK v1.8.0_66 +1 javac 2m 19s the patch passed +1 compile 2m 5s the patch passed with JDK v1.7.0_91 +1 javac 2m 5s the patch passed -1 checkstyle 0m 31s Patch generated 4 new checkstyle issues in hadoop-yarn-project/hadoop-yarn (total was 261, now 264). +1 mvnsite 0m 55s the patch passed +1 mvneclipse 0m 23s the patch passed +1 whitespace 0m 0s Patch has no whitespace issues. -1 findbugs 1m 7s hadoop-yarn-project/hadoop-yarn/hadoop-yarn-server/hadoop-yarn-server-nodemanager introduced 1 new FindBugs issues. +1 javadoc 0m 55s the patch passed with JDK v1.8.0_66 +1 javadoc 3m 7s the patch passed with JDK v1.7.0_91 +1 unit 0m 20s hadoop-yarn-api in the patch passed with JDK v1.8.0_66. +1 unit 8m 38s hadoop-yarn-server-nodemanager in the patch passed with JDK v1.8.0_66. +1 unit 0m 22s hadoop-yarn-api in the patch passed with JDK v1.7.0_91. +1 unit 9m 10s hadoop-yarn-server-nodemanager in the patch passed with JDK v1.7.0_91. +1 asflicense 0m 18s Patch does not generate ASF License warnings. 53m 54s Reason Tests FindBugs module:hadoop-yarn-project/hadoop-yarn/hadoop-yarn-server/hadoop-yarn-server-nodemanager org.apache.hadoop.yarn.server.nodemanager.containermanager.AuxServices.serviceInit(Configuration) creates a java.net.URLClassLoader classloader, which should be performed within a doPrivileged block At AuxServices.java:which should be performed within a doPrivileged block At AuxServices.java: [line 133] Subsystem Report/Notes Docker Image:yetus/hadoop:0ca8df7 JIRA Patch URL https://issues.apache.org/jira/secure/attachment/12781604/YARN-4577.1.patch JIRA Issue YARN-4577 Optional Tests asflicense compile javac javadoc mvninstall mvnsite unit findbugs checkstyle uname Linux f64ed5ca774f 3.13.0-36-lowlatency #63-Ubuntu SMP PREEMPT Wed Sep 3 21:56:12 UTC 2014 x86_64 x86_64 x86_64 GNU/Linux Build tool maven Personality /testptch/hadoop/patchprocess/precommit/personality/provided.sh git revision trunk / 95f3201 Default Java 1.7.0_91 Multi-JDK versions /usr/lib/jvm/java-8-oracle:1.8.0_66 /usr/lib/jvm/java-7-openjdk-amd64:1.7.0_91 findbugs v3.0.0 checkstyle https://builds.apache.org/job/PreCommit-YARN-Build/10228/artifact/patchprocess/diff-checkstyle-hadoop-yarn-project_hadoop-yarn.txt findbugs https://builds.apache.org/job/PreCommit-YARN-Build/10228/artifact/patchprocess/new-findbugs-hadoop-yarn-project_hadoop-yarn_hadoop-yarn-server_hadoop-yarn-server-nodemanager.html JDK v1.7.0_91 Test Results https://builds.apache.org/job/PreCommit-YARN-Build/10228/testReport/ modules C: hadoop-yarn-project/hadoop-yarn/hadoop-yarn-api hadoop-yarn-project/hadoop-yarn/hadoop-yarn-server/hadoop-yarn-server-nodemanager U: hadoop-yarn-project/hadoop-yarn Max memory used 75MB Powered by Apache Yetus 0.2.0-SNAPSHOT http://yetus.apache.org Console output https://builds.apache.org/job/PreCommit-YARN-Build/10228/console This message was automatically generated. 
[![sjlee0](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Sangjin Lee](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=sjlee0) added a comment - [11/Jan/16 19:37](https://issues.apache.org/jira/browse/YARN-4577?focusedCommentId=15092543&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15092543)
We do have a fairly generic isolated classloader under hadoop-common (ApplicationClassLoader): <https://github.com/apache/hadoop/blob/trunk/hadoop-common-project/hadoop-common/src/main/java/org/apache/hadoop/util/ApplicationClassLoader.java>
It's currently used by mapreduce (job classloader and the client-side job launcher classloader).
It seems that we should try to reuse the ApplicationClassLoader for this use case instead of creating another variant. Thoughts?
[![sjlee0](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Sangjin Lee](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=sjlee0) added a comment - [11/Jan/16 19:37](https://issues.apache.org/jira/browse/YARN-4577?focusedCommentId=15092543&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15092543) We do have a fairly generic isolated classloader under hadoop-common (ApplicationClassLoader): https://github.com/apache/hadoop/blob/trunk/hadoop-common-project/hadoop-common/src/main/java/org/apache/hadoop/util/ApplicationClassLoader.java It's currently used by mapreduce (job classloader and the client-side job launcher classloader). It seems that we should try to reuse the ApplicationClassLoader for this use case instead of creating another variant. Thoughts? 
[![xgong](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10443) Xuan Gong](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=xgong) added a comment - [11/Jan/16 21:29](https://issues.apache.org/jira/browse/YARN-4577?focusedCommentId=15092717&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15092717)
[sjlee0](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=sjlee0) Thanks for the information. Will check if we could re-use it.
[![xgong](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10443) Xuan Gong](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=xgong) added a comment - [11/Jan/16 21:29](https://issues.apache.org/jira/browse/YARN-4577?focusedCommentId=15092717&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15092717) sjlee0 Thanks for the information. Will check if we could re-use it. 
[![xgong](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10443) Xuan Gong](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=xgong) added a comment - [12/Jan/16 17:59](https://issues.apache.org/jira/browse/YARN-4577?focusedCommentId=15094397&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15094397)
Attached a new patch to fix -1 on findbug.
> It seems that we should try to reuse the ApplicationClassLoader for this use case instead of creating another variant. Thoughts?
For my understanding, The applicationClassLoader is to append Classes from the application JARs in preference to the parent loader. It can not fix our problem completely. 
[![xgong](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10443) Xuan Gong](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=xgong) added a comment - [12/Jan/16 17:59](https://issues.apache.org/jira/browse/YARN-4577?focusedCommentId=15094397&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15094397) Attached a new patch to fix -1 on findbug. It seems that we should try to reuse the ApplicationClassLoader for this use case instead of creating another variant. Thoughts? For my understanding, The applicationClassLoader is to append Classes from the application JARs in preference to the parent loader. It can not fix our problem completely. 
[![hadoopqa](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Hadoop QA](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=hadoopqa) added a comment - [12/Jan/16 19:21](https://issues.apache.org/jira/browse/YARN-4577?focusedCommentId=15094576&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15094576)  
|  ![](https://issues.apache.org/jira/images/icons/emoticons/error.png) **-1 overall**  |  
| --- |  
  
  
  
|  Vote   |  Subsystem   |  Runtime   |  Comment   |  
| --- | --- | --- | --- |  
|  0  |  reexec   |  0m 0s   |  Docker mode activated.   |  
|  +1  |  @author   |  0m 0s   |  The patch does not contain any @author tags.   |  
|  +1  |  test4tests   |  0m 0s   |  The patch appears to include 1 new or modified test files.   |  
|  +1  |  mvninstall   |  7m 26s   |  trunk passed   |  
|  +1  |  compile   |  1m 46s   |  trunk passed with JDK v1.8.0_66   |  
|  +1  |  compile   |  2m 7s   |  trunk passed with JDK v1.7.0_91   |  
|  +1  |  checkstyle   |  0m 30s   |  trunk passed   |  
|  +1  |  mvnsite   |  1m 28s   |  trunk passed   |  
|  +1  |  mvneclipse   |  0m 38s   |  trunk passed   |  
|  +1  |  findbugs   |  3m 30s   |  trunk passed   |  
|  +1  |  javadoc   |  1m 21s   |  trunk passed with JDK v1.8.0_66   |  
|  +1  |  javadoc   |  3m 36s   |  trunk passed with JDK v1.7.0_91   |  
|  +1  |  mvninstall   |  1m 14s   |  the patch passed   |  
|  +1  |  compile   |  1m 41s   |  the patch passed with JDK v1.8.0_66   |  
|  +1  |  javac   |  1m 41s   |  the patch passed   |  
|  +1  |  compile   |  2m 4s   |  the patch passed with JDK v1.7.0_91   |  
|  +1  |  javac   |  2m 4s   |  the patch passed   |  
|  -1  |  checkstyle   |  0m 30s   |  Patch generated 2 new checkstyle issues in hadoop-yarn-project/hadoop-yarn (total was 261, now 262).   |  
|  +1  |  mvnsite   |  1m 23s   |  the patch passed   |  
|  +1  |  mvneclipse   |  0m 31s   |  the patch passed   |  
|  -1  |  whitespace   |  0m 0s   |  The patch has 1 line(s) with tabs.   |  
|  +1  |  xml   |  0m 0s   |  The patch has no ill-formed XML file.   |  
|  +1  |  findbugs   |  3m 49s   |  the patch passed   |  
|  +1  |  javadoc   |  1m 17s   |  the patch passed with JDK v1.8.0_66   |  
|  +1  |  javadoc   |  3m 33s   |  the patch passed with JDK v1.7.0_91   |  
|  -1  |  unit   |  0m 20s   |  hadoop-yarn-api in the patch failed with JDK v1.8.0_66.   |  
|  +1  |  unit   |  1m 53s   |  hadoop-yarn-common in the patch passed with JDK v1.8.0_66.   |  
|  +1  |  unit   |  8m 30s   |  hadoop-yarn-server-nodemanager in the patch passed with JDK v1.8.0_66.   |  
|  -1  |  unit   |  0m 22s   |  hadoop-yarn-api in the patch failed with JDK v1.7.0_91.   |  
|  +1  |  unit   |  2m 7s   |  hadoop-yarn-common in the patch passed with JDK v1.7.0_91.   |  
|  +1  |  unit   |  9m 0s   |  hadoop-yarn-server-nodemanager in the patch passed with JDK v1.7.0_91.   |  
|  +1  |  asflicense   |  0m 18s   |  Patch does not generate ASF License warnings.   |  
|   |   |  62m 20s   |   |  
  
  
  
|  Reason   |  Tests   |  
| --- | --- |  
|  JDK v1.8.0_66 Failed junit tests   |  hadoop.yarn.conf.TestYarnConfigurationFields   |  
|  JDK v1.7.0_91 Failed junit tests   |  hadoop.yarn.conf.TestYarnConfigurationFields   |  
  
  
  
|  Subsystem   |  Report/Notes   |  
| --- | --- |  
|  Docker   |  Image:yetus/hadoop:0ca8df7   |  
|  JIRA Patch URL   |  <https://issues.apache.org/jira/secure/attachment/12781868/YARN-4577.2.patch>  |  
|  JIRA Issue   |  [~~YARN-4577~~](https://issues.apache.org/jira/browse/YARN-4577 "Enable aux services to have their own custom classpath/jar file")  |  
|  Optional Tests   |  asflicense compile javac javadoc mvninstall mvnsite unit findbugs checkstyle xml   |  
|  uname   |  Linux 7b4507c1515c 3.13.0-36-lowlatency #63-Ubuntu SMP PREEMPT Wed Sep 3 21:56:12 UTC 2014 x86_64 x86_64 x86_64 GNU/Linux   |  
|  Build tool   |  maven   |  
|  Personality   |  /testptch/hadoop/patchprocess/precommit/personality/provided.sh   |  
|  git revision   |  trunk / 25051c3   |  
|  Default Java   |  1.7.0_91   |  
|  Multi-JDK versions   |  /usr/lib/jvm/java-8-oracle:1.8.0_66 /usr/lib/jvm/java-7-openjdk-amd64:1.7.0_91   |  
|  findbugs   |  v3.0.0   |  
|  checkstyle   |  <https://builds.apache.org/job/PreCommit-YARN-Build/10247/artifact/patchprocess/diff-checkstyle-hadoop-yarn-project_hadoop-yarn.txt>  |  
|  whitespace   |  <https://builds.apache.org/job/PreCommit-YARN-Build/10247/artifact/patchprocess/whitespace-tabs.txt>  |  
|  unit   |  <https://builds.apache.org/job/PreCommit-YARN-Build/10247/artifact/patchprocess/patch-unit-hadoop-yarn-project_hadoop-yarn_hadoop-yarn-api-jdk1.8.0_66.txt>  |  
|  unit   |  <https://builds.apache.org/job/PreCommit-YARN-Build/10247/artifact/patchprocess/patch-unit-hadoop-yarn-project_hadoop-yarn_hadoop-yarn-api-jdk1.7.0_91.txt>  |  
|  unit test logs   |  <https://builds.apache.org/job/PreCommit-YARN-Build/10247/artifact/patchprocess/patch-unit-hadoop-yarn-project_hadoop-yarn_hadoop-yarn-api-jdk1.8.0_66.txt> <https://builds.apache.org/job/PreCommit-YARN-Build/10247/artifact/patchprocess/patch-unit-hadoop-yarn-project_hadoop-yarn_hadoop-yarn-api-jdk1.7.0_91.txt>  |  
|  JDK v1.7.0_91 Test Results   |  <https://builds.apache.org/job/PreCommit-YARN-Build/10247/testReport/>  |  
|  modules   |  C: hadoop-yarn-project/hadoop-yarn/hadoop-yarn-api hadoop-yarn-project/hadoop-yarn/hadoop-yarn-common hadoop-yarn-project/hadoop-yarn/hadoop-yarn-server/hadoop-yarn-server-nodemanager U: hadoop-yarn-project/hadoop-yarn   |  
|  Max memory used   |  75MB   |  
|  Powered by   |  Apache Yetus 0.2.0-SNAPSHOT <http://yetus.apache.org>  |  
|  Console output   |  <https://builds.apache.org/job/PreCommit-YARN-Build/10247/console>  |  
This message was automatically generated.
[![hadoopqa](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Hadoop QA](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=hadoopqa) added a comment - [12/Jan/16 19:21](https://issues.apache.org/jira/browse/YARN-4577?focusedCommentId=15094576&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15094576) -1 overall Vote Subsystem Runtime Comment 0 reexec 0m 0s Docker mode activated. +1 @author 0m 0s The patch does not contain any @author tags. +1 test4tests 0m 0s The patch appears to include 1 new or modified test files. +1 mvninstall 7m 26s trunk passed +1 compile 1m 46s trunk passed with JDK v1.8.0_66 +1 compile 2m 7s trunk passed with JDK v1.7.0_91 +1 checkstyle 0m 30s trunk passed +1 mvnsite 1m 28s trunk passed +1 mvneclipse 0m 38s trunk passed +1 findbugs 3m 30s trunk passed +1 javadoc 1m 21s trunk passed with JDK v1.8.0_66 +1 javadoc 3m 36s trunk passed with JDK v1.7.0_91 +1 mvninstall 1m 14s the patch passed +1 compile 1m 41s the patch passed with JDK v1.8.0_66 +1 javac 1m 41s the patch passed +1 compile 2m 4s the patch passed with JDK v1.7.0_91 +1 javac 2m 4s the patch passed -1 checkstyle 0m 30s Patch generated 2 new checkstyle issues in hadoop-yarn-project/hadoop-yarn (total was 261, now 262). +1 mvnsite 1m 23s the patch passed +1 mvneclipse 0m 31s the patch passed -1 whitespace 0m 0s The patch has 1 line(s) with tabs. +1 xml 0m 0s The patch has no ill-formed XML file. +1 findbugs 3m 49s the patch passed +1 javadoc 1m 17s the patch passed with JDK v1.8.0_66 +1 javadoc 3m 33s the patch passed with JDK v1.7.0_91 -1 unit 0m 20s hadoop-yarn-api in the patch failed with JDK v1.8.0_66. +1 unit 1m 53s hadoop-yarn-common in the patch passed with JDK v1.8.0_66. +1 unit 8m 30s hadoop-yarn-server-nodemanager in the patch passed with JDK v1.8.0_66. -1 unit 0m 22s hadoop-yarn-api in the patch failed with JDK v1.7.0_91. +1 unit 2m 7s hadoop-yarn-common in the patch passed with JDK v1.7.0_91. +1 unit 9m 0s hadoop-yarn-server-nodemanager in the patch passed with JDK v1.7.0_91. +1 asflicense 0m 18s Patch does not generate ASF License warnings. 62m 20s Reason Tests JDK v1.8.0_66 Failed junit tests hadoop.yarn.conf.TestYarnConfigurationFields JDK v1.7.0_91 Failed junit tests hadoop.yarn.conf.TestYarnConfigurationFields Subsystem Report/Notes Docker Image:yetus/hadoop:0ca8df7 JIRA Patch URL https://issues.apache.org/jira/secure/attachment/12781868/YARN-4577.2.patch JIRA Issue YARN-4577 Optional Tests asflicense compile javac javadoc mvninstall mvnsite unit findbugs checkstyle xml uname Linux 7b4507c1515c 3.13.0-36-lowlatency #63-Ubuntu SMP PREEMPT Wed Sep 3 21:56:12 UTC 2014 x86_64 x86_64 x86_64 GNU/Linux Build tool maven Personality /testptch/hadoop/patchprocess/precommit/personality/provided.sh git revision trunk / 25051c3 Default Java 1.7.0_91 Multi-JDK versions /usr/lib/jvm/java-8-oracle:1.8.0_66 /usr/lib/jvm/java-7-openjdk-amd64:1.7.0_91 findbugs v3.0.0 checkstyle https://builds.apache.org/job/PreCommit-YARN-Build/10247/artifact/patchprocess/diff-checkstyle-hadoop-yarn-project_hadoop-yarn.txt whitespace https://builds.apache.org/job/PreCommit-YARN-Build/10247/artifact/patchprocess/whitespace-tabs.txt unit https://builds.apache.org/job/PreCommit-YARN-Build/10247/artifact/patchprocess/patch-unit-hadoop-yarn-project_hadoop-yarn_hadoop-yarn-api-jdk1.8.0_66.txt unit https://builds.apache.org/job/PreCommit-YARN-Build/10247/artifact/patchprocess/patch-unit-hadoop-yarn-project_hadoop-yarn_hadoop-yarn-api-jdk1.7.0_91.txt unit test logs https://builds.apache.org/job/PreCommit-YARN-Build/10247/artifact/patchprocess/patch-unit-hadoop-yarn-project_hadoop-yarn_hadoop-yarn-api-jdk1.8.0_66.txt https://builds.apache.org/job/PreCommit-YARN-Build/10247/artifact/patchprocess/patch-unit-hadoop-yarn-project_hadoop-yarn_hadoop-yarn-api-jdk1.7.0_91.txt JDK v1.7.0_91 Test Results https://builds.apache.org/job/PreCommit-YARN-Build/10247/testReport/ modules C: hadoop-yarn-project/hadoop-yarn/hadoop-yarn-api hadoop-yarn-project/hadoop-yarn/hadoop-yarn-common hadoop-yarn-project/hadoop-yarn/hadoop-yarn-server/hadoop-yarn-server-nodemanager U: hadoop-yarn-project/hadoop-yarn Max memory used 75MB Powered by Apache Yetus 0.2.0-SNAPSHOT http://yetus.apache.org Console output https://builds.apache.org/job/PreCommit-YARN-Build/10247/console This message was automatically generated. 
[![kasha](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Karthik Kambatla](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=kasha) added a comment - [13/Jan/16 04:18](https://issues.apache.org/jira/browse/YARN-4577?focusedCommentId=15095573&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15095573)
Would it make sense to run these auxiliary services as a separate process, may be even in a container in isolation? If one aux service is problematic, it wouldn't affect rest of the NM. And, we could monitor resources. I am fine with limiting this JIRA to the classpath, and filing another JIRA for this. Just wanted to bring this up and hear people's thoughts. 
[![kasha](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Karthik Kambatla](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=kasha) added a comment - [13/Jan/16 04:18](https://issues.apache.org/jira/browse/YARN-4577?focusedCommentId=15095573&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15095573) Would it make sense to run these auxiliary services as a separate process, may be even in a container in isolation? If one aux service is problematic, it wouldn't affect rest of the NM. And, we could monitor resources. I am fine with limiting this JIRA to the classpath, and filing another JIRA for this. Just wanted to bring this up and hear people's thoughts. 
[![xgong](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10443) Xuan Gong](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=xgong) added a comment - [13/Jan/16 05:01](https://issues.apache.org/jira/browse/YARN-4577?focusedCommentId=15095615&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15095615)
[kasha](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=kasha) Yes, we will do that in future, and [YARN-1593](https://issues.apache.org/jira/browse/YARN-1593 "support out-of-proc AuxiliaryServices") has been created to track that.
[![xgong](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10443) Xuan Gong](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=xgong) added a comment - [13/Jan/16 05:01](https://issues.apache.org/jira/browse/YARN-4577?focusedCommentId=15095615&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15095615) kasha Yes, we will do that in future, and YARN-1593 has been created to track that. 
[![sjlee0](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Sangjin Lee](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=sjlee0) added a comment - [13/Jan/16 17:14](https://issues.apache.org/jira/browse/YARN-4577?focusedCommentId=15096584&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15096584)
Hi [xgong](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=xgong), it would be great if you could describe precisely the behavior of the classloading you desire in this solution. Then, we could discuss it a little better.
For your reference, here is what the ApplicationClassLoader does.
  * isolates the classloading and the classpath of the "application" from the hadoop stack
  * while this classloader is in place, it tries to load classes **first** from the user classpath (as opposed to system classpath), and if not found tries to load it from the system classpath/classloader
  * there are **"system classes"** (mainly hadoop classes and JDK classes) that are always loaded only by the system classloader to ensure consistency
  * outside the context of this classloader, the hadoop code does not see the user classpath at all, and uses only the system classloader
  * each application classloader is isolated from one another (obviously)
  * when the application classloader is in scope, it gets set onto the Configuration as well as the current thread's context classloader to ensure consistency for reflection-based classloading


This is essentially the same behavior as the webapp classloader of servlet engine implementations (Tomcat, Jetty, etc.).
From the description and the inferred behavior from the provided patch, I didn't see much that the application classloader cannot work for this use case. The desire here is to see if we can have a single generic solution that can address all the needs for isolated classloading, rather than creating more solutions as new use cases arise. If there are some things that are not addressed by the current application classloader implementation, we could consider modifying it to make it wider in scope. There are some HADOOP JIRAs filed (see [~~HADOOP-11656~~](https://issues.apache.org/jira/browse/HADOOP-11656 "Classpath isolation for downstream clients") for example) to adopt a single mechanism for classloading isolation and make it more formal and stricter .
Thoughts?
[![sjlee0](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Sangjin Lee](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=sjlee0) added a comment - [13/Jan/16 17:14](https://issues.apache.org/jira/browse/YARN-4577?focusedCommentId=15096584&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15096584) Hi xgong , it would be great if you could describe precisely the behavior of the classloading you desire in this solution. Then, we could discuss it a little better. For your reference, here is what the ApplicationClassLoader does. isolates the classloading and the classpath of the "application" from the hadoop stack while this classloader is in place, it tries to load classes first from the user classpath (as opposed to system classpath), and if not found tries to load it from the system classpath/classloader there are "system classes" (mainly hadoop classes and JDK classes) that are always loaded only by the system classloader to ensure consistency outside the context of this classloader, the hadoop code does not see the user classpath at all, and uses only the system classloader each application classloader is isolated from one another (obviously) when the application classloader is in scope, it gets set onto the Configuration as well as the current thread's context classloader to ensure consistency for reflection-based classloading This is essentially the same behavior as the webapp classloader of servlet engine implementations (Tomcat, Jetty, etc.). From the description and the inferred behavior from the provided patch, I didn't see much that the application classloader cannot work for this use case. The desire here is to see if we can have a single generic solution that can address all the needs for isolated classloading, rather than creating more solutions as new use cases arise. If there are some things that are not addressed by the current application classloader implementation, we could consider modifying it to make it wider in scope. There are some HADOOP JIRAs filed (see HADOOP-11656 for example) to adopt a single mechanism for classloading isolation and make it more formal and stricter . Thoughts? 
[![xgong](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10443) Xuan Gong](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=xgong) added a comment - [14/Jan/16 17:28](https://issues.apache.org/jira/browse/YARN-4577?focusedCommentId=15098461&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15098461)
Thanks, [sjlee0](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=sjlee0) for the comments and suggestions.
+1 for the suggestion to have a single generic solution that can address all the needs for isolated classloading. But i think that we still need some improvement on this. 
The use case here is simple: if we specify the aux-services classpath, either from local fs or from hdfs, we will load this service from the specified classpath (no matter we set the classpath in NM path or not). Otherwise, we load the service from the NM path. 
For ApplicationClassLoader, 

```
public ApplicationClassLoader(String classpath, ClassLoader parent,
      List<String> systemClasses)

```

looks like we have to specify classpath (we can not set it null). Also, it needs me to specify systemClasses which is not required in this use-case. There are some un-necessary checks, such as isSystemClass() when we call loadClass. Overall, i think that the ApplicationClassLoader is too complicate for this use-case.
[![xgong](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10443) Xuan Gong](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=xgong) added a comment - [14/Jan/16 17:28](https://issues.apache.org/jira/browse/YARN-4577?focusedCommentId=15098461&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15098461) Thanks, sjlee0 for the comments and suggestions. +1 for the suggestion to have a single generic solution that can address all the needs for isolated classloading. But i think that we still need some improvement on this. The use case here is simple: if we specify the aux-services classpath, either from local fs or from hdfs, we will load this service from the specified classpath (no matter we set the classpath in NM path or not). Otherwise, we load the service from the NM path. For ApplicationClassLoader, public ApplicationClassLoader( String classpath, ClassLoader parent, List< String > systemClasses) looks like we have to specify classpath (we can not set it null). Also, it needs me to specify systemClasses which is not required in this use-case. There are some un-necessary checks, such as isSystemClass() when we call loadClass. Overall, i think that the ApplicationClassLoader is too complicate for this use-case. 
[![stevel@apache.org](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Steve Loughran](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=stevel%40apache.org) added a comment - [14/Jan/16 18:18](https://issues.apache.org/jira/browse/YARN-4577?focusedCommentId=15098556&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15098556)
Test wise
  * `testLoadAuxServiceLocally` should be calling aux.close() in finally{} clauses. It's idempotent so you could so a close() in the main path (and so test it), but still clean up after.
  * it'd be nice for the asserts to include some text about why the asserts are failing, especially simple `assertTrue()` calls. The goal is that enough information is printed to enable someone who sees the Jenkins log to be able to diagnose the problem. An "assert failed line 315" doesn't do that much, leads to the "add more test diagnostics" patches and more iterations.


[![stevel@apache.org](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Steve Loughran](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=stevel%40apache.org) added a comment - [14/Jan/16 18:18](https://issues.apache.org/jira/browse/YARN-4577?focusedCommentId=15098556&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15098556) Test wise testLoadAuxServiceLocally should be calling aux.close() in finally{} clauses. It's idempotent so you could so a close() in the main path (and so test it), but still clean up after. it'd be nice for the asserts to include some text about why the asserts are failing, especially simple assertTrue() calls. The goal is that enough information is printed to enable someone who sees the Jenkins log to be able to diagnose the problem. An "assert failed line 315" doesn't do that much, leads to the "add more test diagnostics" patches and more iterations. 
[![sjlee0](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Sangjin Lee](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=sjlee0) added a comment - [15/Jan/16 00:29](https://issues.apache.org/jira/browse/YARN-4577?focusedCommentId=15099191&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15099191)
> The use case here is simple: if we specify the aux-services classpath, either from local fs or from hdfs, we will load this service from the specified classpath (no matter we set the classpath in NM path or not). Otherwise, we load the service from the NM path.
Hmm, is one of the goals to preserve aux service's dependencies against hadoop's dependencies (as I see in the linked ticket [~~SPARK-12807~~](https://issues.apache.org/jira/browse/SPARK-12807 "Spark External Shuffle not working in Hadoop clusters with Jackson 2.2.3"))? If so, I don't think the current approach in the patch does that. Note that URLClassLoader (or any simple extension of ClassLoader) always **delegates classloading to the parent classloader first** , and loads the class **only if** the parent classloader doesn't load/have it. In other words, any classpath the URLClassLoader owns is effectively **appended** , not prepended. That's precisely why ApplicationClassLoader inverts that order to create isolation.
Could you write a simple test program to verify this behavior? I'm pretty sure you'll find that your classpath will still be shadowed by the system classpath.
Also, as for using the ApplicationClassLoader, it shouldn't be too difficult. You pass in `URL[]` to the URLClassLoader too, so that's common. You can simply pass in the classloader of the calling class as the parent classloader. Also, you can simply pass null for the system classes, in which case the sensible default will be used.
If it helps anyway, we could introduce a simpler constructor like the following:

```
public ApplicationClassLoader(URL[] classpath) {
  this(classpath, getClass().getClassLoader(), null);
}

```

[![sjlee0](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Sangjin Lee](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=sjlee0) added a comment - [15/Jan/16 00:29](https://issues.apache.org/jira/browse/YARN-4577?focusedCommentId=15099191&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15099191) The use case here is simple: if we specify the aux-services classpath, either from local fs or from hdfs, we will load this service from the specified classpath (no matter we set the classpath in NM path or not). Otherwise, we load the service from the NM path. Hmm, is one of the goals to preserve aux service's dependencies against hadoop's dependencies (as I see in the linked ticket SPARK-12807 )? If so, I don't think the current approach in the patch does that. Note that URLClassLoader (or any simple extension of ClassLoader) always delegates classloading to the parent classloader first , and loads the class only if the parent classloader doesn't load/have it. In other words, any classpath the URLClassLoader owns is effectively appended , not prepended. That's precisely why ApplicationClassLoader inverts that order to create isolation. Could you write a simple test program to verify this behavior? I'm pretty sure you'll find that your classpath will still be shadowed by the system classpath. Also, as for using the ApplicationClassLoader, it shouldn't be too difficult. You pass in URL[] to the URLClassLoader too, so that's common. You can simply pass in the classloader of the calling class as the parent classloader. Also, you can simply pass null for the system classes, in which case the sensible default will be used. If it helps anyway, we could introduce a simpler constructor like the following: public ApplicationClassLoader(URL[] classpath) { this (classpath, getClass().getClassLoader(), null ); } 
[![xgong](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10443) Xuan Gong](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=xgong) added a comment - [15/Jan/16 21:10](https://issues.apache.org/jira/browse/YARN-4577?focusedCommentId=15102469&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15102469)
Thanks for the comments, [sjlee0](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=sjlee0)
Attached a new patch to use ApplicationClassLoader. One issue here is: ApplicationClassLoader does not work for HDFS, especially for loading jar if we only specify hdfs dir. Create a private function in AuxService.java to fix this. Maybe, this is the one that we can improve on ApplicationClassLoader. 
[![xgong](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10443) Xuan Gong](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=xgong) added a comment - [15/Jan/16 21:10](https://issues.apache.org/jira/browse/YARN-4577?focusedCommentId=15102469&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15102469) Thanks for the comments, sjlee0 Attached a new patch to use ApplicationClassLoader. One issue here is: ApplicationClassLoader does not work for HDFS, especially for loading jar if we only specify hdfs dir. Create a private function in AuxService.java to fix this. Maybe, this is the one that we can improve on ApplicationClassLoader. 
[![hadoopqa](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Hadoop QA](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=hadoopqa) added a comment - [15/Jan/16 21:22](https://issues.apache.org/jira/browse/YARN-4577?focusedCommentId=15102479&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15102479)  
|  ![](https://issues.apache.org/jira/images/icons/emoticons/error.png) **-1 overall**  |  
| --- |  
  
  
  
|  Vote   |  Subsystem   |  Runtime   |  Comment   |  
| --- | --- | --- | --- |  
|  -1  |  patch   |  0m 4s   |  [~~YARN-4577~~](https://issues.apache.org/jira/browse/YARN-4577 "Enable aux services to have their own custom classpath/jar file") does not apply to trunk. Rebase required? Wrong Branch? See <https://wiki.apache.org/hadoop/HowToContribute> for help.   |  
  
  
  
|  Subsystem   |  Report/Notes   |  
| --- | --- |  
|  JIRA Patch URL   |  <https://issues.apache.org/jira/secure/attachment/12782606/YARN-4577.3.patch>  |  
|  JIRA Issue   |  [~~YARN-4577~~](https://issues.apache.org/jira/browse/YARN-4577 "Enable aux services to have their own custom classpath/jar file")  |  
|  Powered by   |  Apache Yetus 0.2.0-SNAPSHOT <http://yetus.apache.org>  |  
|  Console output   |  <https://builds.apache.org/job/PreCommit-YARN-Build/10307/console>  |  
This message was automatically generated.
[![hadoopqa](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Hadoop QA](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=hadoopqa) added a comment - [15/Jan/16 21:22](https://issues.apache.org/jira/browse/YARN-4577?focusedCommentId=15102479&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15102479) -1 overall Vote Subsystem Runtime Comment -1 patch 0m 4s YARN-4577 does not apply to trunk. Rebase required? Wrong Branch? See https://wiki.apache.org/hadoop/HowToContribute for help. Subsystem Report/Notes JIRA Patch URL https://issues.apache.org/jira/secure/attachment/12782606/YARN-4577.3.patch JIRA Issue YARN-4577 Powered by Apache Yetus 0.2.0-SNAPSHOT http://yetus.apache.org Console output https://builds.apache.org/job/PreCommit-YARN-Build/10307/console This message was automatically generated. 
[![gtcarrera9](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Li Lu](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=gtcarrera9) added a comment - [15/Jan/16 23:41](https://issues.apache.org/jira/browse/YARN-4577?focusedCommentId=15102704&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15102704)
Thanks [xgong](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=xgong) for the work! The overall logic of reusing ApplicationClassLoader looks fine to me. While we are seeking for a solution to load jars from HDFS, maybe we can decide on the "interface" part of the design, such as the name of the config? I personally feel the "classloader.location" is a little bit confusing (which may mean the location of the classloader itself). Any special considerations here? Thanks! 
[![gtcarrera9](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Li Lu](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=gtcarrera9) added a comment - [15/Jan/16 23:41](https://issues.apache.org/jira/browse/YARN-4577?focusedCommentId=15102704&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15102704) Thanks xgong for the work! The overall logic of reusing ApplicationClassLoader looks fine to me. While we are seeking for a solution to load jars from HDFS, maybe we can decide on the "interface" part of the design, such as the name of the config? I personally feel the "classloader.location" is a little bit confusing (which may mean the location of the classloader itself). Any special considerations here? Thanks! 
[![gtcarrera9](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Li Lu](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=gtcarrera9) added a comment - [15/Jan/16 23:49](https://issues.apache.org/jira/browse/YARN-4577?focusedCommentId=15102712&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15102712)
BTW I tried this patch locally but it does not apply on the latest trunk. I hit some problems with yarn-default.xml. Not sure if this is a problem of the patch. 
[![gtcarrera9](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Li Lu](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=gtcarrera9) added a comment - [15/Jan/16 23:49](https://issues.apache.org/jira/browse/YARN-4577?focusedCommentId=15102712&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15102712) BTW I tried this patch locally but it does not apply on the latest trunk. I hit some problems with yarn-default.xml. Not sure if this is a problem of the patch. 
[![xgong](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10443) Xuan Gong](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=xgong) added a comment - [16/Jan/16 00:09](https://issues.apache.org/jira/browse/YARN-4577?focusedCommentId=15102747&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15102747)
rebase the patch
[![xgong](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10443) Xuan Gong](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=xgong) added a comment - [16/Jan/16 00:09](https://issues.apache.org/jira/browse/YARN-4577?focusedCommentId=15102747&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15102747) rebase the patch 
[![sjlee0](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Sangjin Lee](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=sjlee0) added a comment - [16/Jan/16 00:41](https://issues.apache.org/jira/browse/YARN-4577?focusedCommentId=15102794&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15102794)
Thanks for the updated patch [xgong](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=xgong)!
I had bit of time to sit down to go over the patch and think about related points.
(1) `URL.setURLStreamHandlerFactory()` (and supporting non-local paths)  
Regarding setting the `URLStreamHandlerFactory`, you can call `URL.setURLStreamHandlerFactory()` at most once on a JVM, and any attempt to set it again within the same process will throw an error:
Sets an application's `URLStreamHandlerFactory`. This method can be called at most once in a given Java Virtual Machine.
In the patch, this is being called inside a for loop. This will throw an `Error` for any subsequent initialization of aux services. If this was needed to be able to handle non-local paths (like hdfs), then we would need to find a different way than this method to handle it.
On a related note, how important is it to support non-local classpaths? If implementing it is not trivial, you might want to separate that work into a separate JIRA and address that. I'd be curious to hear how important that part of the feature is.
(2) other types of classloading  
The patch will ensure that the aux service class itself will be loaded by the application classloader and any class that needs to be loaded **in a normal manner** as part of executing the aux service class. However, there are other types of classloading that can happen. Two major types you need to consider are classloading via `Configuration.getClass()` and reflection using thread context classloader (via `Thread.currentThread().getContextClassLoader()`).
For example, if the aux service code depends on another class property (owned by the aux service) in the configuration, that will be invoked via `Configuration.getClass()`, and it will still use the system classloader to load that class. Then it's very likely that you'll get a `ClassNotFoundException`.
The thread context classloader represents another similar problem. The moment the aux service code hits a code path that does `Class.forName()` that loads classes via the thread context classloader, and it needs to load an aux service-related class (that is not present in the main NM classpath), you will get a `ClassNotFoundException`.
If you look at the existing uses of the `ApplicationClassLoader`, you'll see we usually try to demarcate the code regions that need to run under the `ApplicationClassLoader`, and set and unset both the `Configuration` classloader and the thread context classloader. You might need to do the same thing with executing the aux service code. Luckily, I believe there are well-defined entry points and exit points for the aux service code, so hopefully it is not too difficult to do it completely.
(3) configuration property  
The configuration property "...classloader.location" doesn't seem quite natural. It is really about the classpath. How about simply "...classpath" instead?
Also, it would be good to document that this is a comma-separated classpath somewhere.
(4) unit test  
l.366: I'm quite confused by the comment and the code. If I'm reading this correctly, it is setting the classname configuration property with the TEST_DIR location, which is pretty much a bogus value. So it's understandable this won't work. But it's not really setting the **classpath** to a different location. Does it verify or confirm anything about this feature?
l.383: should we delete TEST_DIR here? It seems like the directory is deleted in another unit test. I don't think it's created again for each of the unit tests. It doesn't seem like it's necessary to delete this directory at all here. Did I miss something?
Overall, you might want to take a look at the `TestApplicationClassLoader` test to see how you can formulate the test. Note that all `org.apache.hadoop.*` classes are considered system classes and are exempt from the loading from the `ApplicationClassLoader`, so playing with the system classes is needed to test this (unless you can create test classes outside `org.apache.hadoop`).
[![sjlee0](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Sangjin Lee](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=sjlee0) added a comment - [16/Jan/16 00:41](https://issues.apache.org/jira/browse/YARN-4577?focusedCommentId=15102794&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15102794) Thanks for the updated patch xgong ! I had bit of time to sit down to go over the patch and think about related points. (1) URL.setURLStreamHandlerFactory() (and supporting non-local paths) Regarding setting the URLStreamHandlerFactory , you can call URL.setURLStreamHandlerFactory() at most once on a JVM, and any attempt to set it again within the same process will throw an error: Sets an application's URLStreamHandlerFactory . This method can be called at most once in a given Java Virtual Machine. In the patch, this is being called inside a for loop. This will throw an Error for any subsequent initialization of aux services. If this was needed to be able to handle non-local paths (like hdfs), then we would need to find a different way than this method to handle it. On a related note, how important is it to support non-local classpaths? If implementing it is not trivial, you might want to separate that work into a separate JIRA and address that. I'd be curious to hear how important that part of the feature is. (2) other types of classloading The patch will ensure that the aux service class itself will be loaded by the application classloader and any class that needs to be loaded in a normal manner as part of executing the aux service class. However, there are other types of classloading that can happen. Two major types you need to consider are classloading via Configuration.getClass() and reflection using thread context classloader (via Thread.currentThread().getContextClassLoader() ). For example, if the aux service code depends on another class property (owned by the aux service) in the configuration, that will be invoked via Configuration.getClass() , and it will still use the system classloader to load that class. Then it's very likely that you'll get a ClassNotFoundException . The thread context classloader represents another similar problem. The moment the aux service code hits a code path that does Class.forName() that loads classes via the thread context classloader, and it needs to load an aux service-related class (that is not present in the main NM classpath), you will get a ClassNotFoundException . If you look at the existing uses of the ApplicationClassLoader , you'll see we usually try to demarcate the code regions that need to run under the ApplicationClassLoader , and set and unset both the Configuration classloader and the thread context classloader. You might need to do the same thing with executing the aux service code. Luckily, I believe there are well-defined entry points and exit points for the aux service code, so hopefully it is not too difficult to do it completely. (3) configuration property The configuration property "...classloader.location" doesn't seem quite natural. It is really about the classpath. How about simply "...classpath" instead? Also, it would be good to document that this is a comma-separated classpath somewhere. (4) unit test l.366: I'm quite confused by the comment and the code. If I'm reading this correctly, it is setting the classname configuration property with the TEST_DIR location, which is pretty much a bogus value. So it's understandable this won't work. But it's not really setting the classpath to a different location. Does it verify or confirm anything about this feature? l.383: should we delete TEST_DIR here? It seems like the directory is deleted in another unit test. I don't think it's created again for each of the unit tests. It doesn't seem like it's necessary to delete this directory at all here. Did I miss something? Overall, you might want to take a look at the TestApplicationClassLoader test to see how you can formulate the test. Note that all org.apache.hadoop.* classes are considered system classes and are exempt from the loading from the ApplicationClassLoader , so playing with the system classes is needed to test this (unless you can create test classes outside org.apache.hadoop ). 
[![hadoopqa](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Hadoop QA](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=hadoopqa) added a comment - [16/Jan/16 01:31](https://issues.apache.org/jira/browse/YARN-4577?focusedCommentId=15102884&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15102884)  
|  ![](https://issues.apache.org/jira/images/icons/emoticons/error.png) **-1 overall**  |  
| --- |  
  
  
  
|  Vote   |  Subsystem   |  Runtime   |  Comment   |  
| --- | --- | --- | --- |  
|  0  |  reexec   |  0m 0s   |  Docker mode activated.   |  
|  +1  |  @author   |  0m 0s   |  The patch does not contain any @author tags.   |  
|  +1  |  test4tests   |  0m 0s   |  The patch appears to include 1 new or modified test files.   |  
|  0  |  mvndep   |  0m 31s   |  Maven dependency ordering for branch   |  
|  +1  |  mvninstall   |  7m 56s   |  trunk passed   |  
|  +1  |  compile   |  1m 56s   |  trunk passed with JDK v1.8.0_66   |  
|  +1  |  compile   |  2m 12s   |  trunk passed with JDK v1.7.0_91   |  
|  +1  |  checkstyle   |  0m 32s   |  trunk passed   |  
|  +1  |  mvnsite   |  1m 32s   |  trunk passed   |  
|  +1  |  mvneclipse   |  0m 38s   |  trunk passed   |  
|  +1  |  findbugs   |  3m 50s   |  trunk passed   |  
|  +1  |  javadoc   |  1m 30s   |  trunk passed with JDK v1.8.0_66   |  
|  +1  |  javadoc   |  3m 54s   |  trunk passed with JDK v1.7.0_91   |  
|  0  |  mvndep   |  0m 24s   |  Maven dependency ordering for patch   |  
|  +1  |  mvninstall   |  1m 20s   |  the patch passed   |  
|  +1  |  compile   |  2m 2s   |  the patch passed with JDK v1.8.0_66   |  
|  +1  |  javac   |  2m 2s   |  the patch passed   |  
|  +1  |  compile   |  2m 12s   |  the patch passed with JDK v1.7.0_91   |  
|  +1  |  javac   |  2m 12s   |  the patch passed   |  
|  -1  |  checkstyle   |  0m 32s   |  Patch generated 5 new checkstyle issues in hadoop-yarn-project/hadoop-yarn (total was 258, now 263).   |  
|  +1  |  mvnsite   |  1m 28s   |  the patch passed   |  
|  +1  |  mvneclipse   |  0m 33s   |  the patch passed   |  
|  +1  |  whitespace   |  0m 0s   |  Patch has no whitespace issues.   |  
|  +1  |  xml   |  0m 1s   |  The patch has no ill-formed XML file.   |  
|  -1  |  findbugs   |  1m 8s   |  hadoop-yarn-project/hadoop-yarn/hadoop-yarn-server/hadoop-yarn-server-nodemanager introduced 1 new FindBugs issues.   |  
|  +1  |  javadoc   |  1m 23s   |  the patch passed with JDK v1.8.0_66   |  
|  +1  |  javadoc   |  3m 46s   |  the patch passed with JDK v1.7.0_91   |  
|  -1  |  unit   |  0m 23s   |  hadoop-yarn-api in the patch failed with JDK v1.8.0_66.   |  
|  +1  |  unit   |  2m 0s   |  hadoop-yarn-common in the patch passed with JDK v1.8.0_66.   |  
|  -1  |  unit   |  8m 46s   |  hadoop-yarn-server-nodemanager in the patch failed with JDK v1.8.0_66.   |  
|  -1  |  unit   |  0m 25s   |  hadoop-yarn-api in the patch failed with JDK v1.7.0_91.   |  
|  +1  |  unit   |  2m 14s   |  hadoop-yarn-common in the patch passed with JDK v1.7.0_91.   |  
|  -1  |  unit   |  9m 12s   |  hadoop-yarn-server-nodemanager in the patch failed with JDK v1.7.0_91.   |  
|  +1  |  asflicense   |  0m 19s   |  Patch does not generate ASF License warnings.   |  
|   |   |  67m 11s   |   |  
  
  
  
|  Reason   |  Tests   |  
| --- | --- |  
|  FindBugs   |  module:hadoop-yarn-project/hadoop-yarn/hadoop-yarn-server/hadoop-yarn-server-nodemanager   |  
|   |  org.apache.hadoop.yarn.server.nodemanager.containermanager.AuxServices.serviceInit(Configuration) creates a org.apache.hadoop.util.ApplicationClassLoader classloader, which should be performed within a doPrivileged block At AuxServices.java:which should be performed within a doPrivileged block At AuxServices.java:[line 147]  |  
|  JDK v1.8.0_66 Failed junit tests   |  hadoop.yarn.conf.TestYarnConfigurationFields   |  
|  JDK v1.7.0_91 Failed junit tests   |  hadoop.yarn.conf.TestYarnConfigurationFields   |  
  
  
  
|  Subsystem   |  Report/Notes   |  
| --- | --- |  
|  Docker   |  Image:yetus/hadoop:0ca8df7   |  
|  JIRA Patch URL   |  <https://issues.apache.org/jira/secure/attachment/12782643/YARN-4577.3.rebase.patch>  |  
|  JIRA Issue   |  [~~YARN-4577~~](https://issues.apache.org/jira/browse/YARN-4577 "Enable aux services to have their own custom classpath/jar file")  |  
|  Optional Tests   |  asflicense compile javac javadoc mvninstall mvnsite unit findbugs checkstyle xml   |  
|  uname   |  Linux 997b7054b090 3.13.0-36-lowlatency #63-Ubuntu SMP PREEMPT Wed Sep 3 21:56:12 UTC 2014 x86_64 x86_64 x86_64 GNU/Linux   |  
|  Build tool   |  maven   |  
|  Personality   |  /testptch/hadoop/patchprocess/precommit/personality/provided.sh   |  
|  git revision   |  trunk / 2a30386   |  
|  Default Java   |  1.7.0_91   |  
|  Multi-JDK versions   |  /usr/lib/jvm/java-8-oracle:1.8.0_66 /usr/lib/jvm/java-7-openjdk-amd64:1.7.0_91   |  
|  findbugs   |  v3.0.0   |  
|  checkstyle   |  <https://builds.apache.org/job/PreCommit-YARN-Build/10310/artifact/patchprocess/diff-checkstyle-hadoop-yarn-project_hadoop-yarn.txt>  |  
|  findbugs   |  <https://builds.apache.org/job/PreCommit-YARN-Build/10310/artifact/patchprocess/new-findbugs-hadoop-yarn-project_hadoop-yarn_hadoop-yarn-server_hadoop-yarn-server-nodemanager.html>  |  
|  unit   |  <https://builds.apache.org/job/PreCommit-YARN-Build/10310/artifact/patchprocess/patch-unit-hadoop-yarn-project_hadoop-yarn_hadoop-yarn-api-jdk1.8.0_66.txt>  |  
|  unit   |  <https://builds.apache.org/job/PreCommit-YARN-Build/10310/artifact/patchprocess/patch-unit-hadoop-yarn-project_hadoop-yarn_hadoop-yarn-server_hadoop-yarn-server-nodemanager-jdk1.8.0_66.txt>  |  
|  unit   |  <https://builds.apache.org/job/PreCommit-YARN-Build/10310/artifact/patchprocess/patch-unit-hadoop-yarn-project_hadoop-yarn_hadoop-yarn-api-jdk1.7.0_91.txt>  |  
|  unit   |  <https://builds.apache.org/job/PreCommit-YARN-Build/10310/artifact/patchprocess/patch-unit-hadoop-yarn-project_hadoop-yarn_hadoop-yarn-server_hadoop-yarn-server-nodemanager-jdk1.7.0_91.txt>  |  
|  unit test logs   |  <https://builds.apache.org/job/PreCommit-YARN-Build/10310/artifact/patchprocess/patch-unit-hadoop-yarn-project_hadoop-yarn_hadoop-yarn-api-jdk1.8.0_66.txt> <https://builds.apache.org/job/PreCommit-YARN-Build/10310/artifact/patchprocess/patch-unit-hadoop-yarn-project_hadoop-yarn_hadoop-yarn-api-jdk1.7.0_91.txt>  |  
|  JDK v1.7.0_91 Test Results   |  <https://builds.apache.org/job/PreCommit-YARN-Build/10310/testReport/>  |  
|  modules   |  C: hadoop-yarn-project/hadoop-yarn/hadoop-yarn-api hadoop-yarn-project/hadoop-yarn/hadoop-yarn-common hadoop-yarn-project/hadoop-yarn/hadoop-yarn-server/hadoop-yarn-server-nodemanager U: hadoop-yarn-project/hadoop-yarn   |  
|  Max memory used   |  76MB   |  
|  Powered by   |  Apache Yetus 0.2.0-SNAPSHOT <http://yetus.apache.org>  |  
|  Console output   |  <https://builds.apache.org/job/PreCommit-YARN-Build/10310/console>  |  
This message was automatically generated.
[![hadoopqa](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Hadoop QA](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=hadoopqa) added a comment - [16/Jan/16 01:31](https://issues.apache.org/jira/browse/YARN-4577?focusedCommentId=15102884&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15102884) -1 overall Vote Subsystem Runtime Comment 0 reexec 0m 0s Docker mode activated. +1 @author 0m 0s The patch does not contain any @author tags. +1 test4tests 0m 0s The patch appears to include 1 new or modified test files. 0 mvndep 0m 31s Maven dependency ordering for branch +1 mvninstall 7m 56s trunk passed +1 compile 1m 56s trunk passed with JDK v1.8.0_66 +1 compile 2m 12s trunk passed with JDK v1.7.0_91 +1 checkstyle 0m 32s trunk passed +1 mvnsite 1m 32s trunk passed +1 mvneclipse 0m 38s trunk passed +1 findbugs 3m 50s trunk passed +1 javadoc 1m 30s trunk passed with JDK v1.8.0_66 +1 javadoc 3m 54s trunk passed with JDK v1.7.0_91 0 mvndep 0m 24s Maven dependency ordering for patch +1 mvninstall 1m 20s the patch passed +1 compile 2m 2s the patch passed with JDK v1.8.0_66 +1 javac 2m 2s the patch passed +1 compile 2m 12s the patch passed with JDK v1.7.0_91 +1 javac 2m 12s the patch passed -1 checkstyle 0m 32s Patch generated 5 new checkstyle issues in hadoop-yarn-project/hadoop-yarn (total was 258, now 263). +1 mvnsite 1m 28s the patch passed +1 mvneclipse 0m 33s the patch passed +1 whitespace 0m 0s Patch has no whitespace issues. +1 xml 0m 1s The patch has no ill-formed XML file. -1 findbugs 1m 8s hadoop-yarn-project/hadoop-yarn/hadoop-yarn-server/hadoop-yarn-server-nodemanager introduced 1 new FindBugs issues. +1 javadoc 1m 23s the patch passed with JDK v1.8.0_66 +1 javadoc 3m 46s the patch passed with JDK v1.7.0_91 -1 unit 0m 23s hadoop-yarn-api in the patch failed with JDK v1.8.0_66. +1 unit 2m 0s hadoop-yarn-common in the patch passed with JDK v1.8.0_66. -1 unit 8m 46s hadoop-yarn-server-nodemanager in the patch failed with JDK v1.8.0_66. -1 unit 0m 25s hadoop-yarn-api in the patch failed with JDK v1.7.0_91. +1 unit 2m 14s hadoop-yarn-common in the patch passed with JDK v1.7.0_91. -1 unit 9m 12s hadoop-yarn-server-nodemanager in the patch failed with JDK v1.7.0_91. +1 asflicense 0m 19s Patch does not generate ASF License warnings. 67m 11s Reason Tests FindBugs module:hadoop-yarn-project/hadoop-yarn/hadoop-yarn-server/hadoop-yarn-server-nodemanager org.apache.hadoop.yarn.server.nodemanager.containermanager.AuxServices.serviceInit(Configuration) creates a org.apache.hadoop.util.ApplicationClassLoader classloader, which should be performed within a doPrivileged block At AuxServices.java:which should be performed within a doPrivileged block At AuxServices.java: [line 147] JDK v1.8.0_66 Failed junit tests hadoop.yarn.conf.TestYarnConfigurationFields JDK v1.7.0_91 Failed junit tests hadoop.yarn.conf.TestYarnConfigurationFields Subsystem Report/Notes Docker Image:yetus/hadoop:0ca8df7 JIRA Patch URL https://issues.apache.org/jira/secure/attachment/12782643/YARN-4577.3.rebase.patch JIRA Issue YARN-4577 Optional Tests asflicense compile javac javadoc mvninstall mvnsite unit findbugs checkstyle xml uname Linux 997b7054b090 3.13.0-36-lowlatency #63-Ubuntu SMP PREEMPT Wed Sep 3 21:56:12 UTC 2014 x86_64 x86_64 x86_64 GNU/Linux Build tool maven Personality /testptch/hadoop/patchprocess/precommit/personality/provided.sh git revision trunk / 2a30386 Default Java 1.7.0_91 Multi-JDK versions /usr/lib/jvm/java-8-oracle:1.8.0_66 /usr/lib/jvm/java-7-openjdk-amd64:1.7.0_91 findbugs v3.0.0 checkstyle https://builds.apache.org/job/PreCommit-YARN-Build/10310/artifact/patchprocess/diff-checkstyle-hadoop-yarn-project_hadoop-yarn.txt findbugs https://builds.apache.org/job/PreCommit-YARN-Build/10310/artifact/patchprocess/new-findbugs-hadoop-yarn-project_hadoop-yarn_hadoop-yarn-server_hadoop-yarn-server-nodemanager.html unit https://builds.apache.org/job/PreCommit-YARN-Build/10310/artifact/patchprocess/patch-unit-hadoop-yarn-project_hadoop-yarn_hadoop-yarn-api-jdk1.8.0_66.txt unit https://builds.apache.org/job/PreCommit-YARN-Build/10310/artifact/patchprocess/patch-unit-hadoop-yarn-project_hadoop-yarn_hadoop-yarn-server_hadoop-yarn-server-nodemanager-jdk1.8.0_66.txt unit https://builds.apache.org/job/PreCommit-YARN-Build/10310/artifact/patchprocess/patch-unit-hadoop-yarn-project_hadoop-yarn_hadoop-yarn-api-jdk1.7.0_91.txt unit https://builds.apache.org/job/PreCommit-YARN-Build/10310/artifact/patchprocess/patch-unit-hadoop-yarn-project_hadoop-yarn_hadoop-yarn-server_hadoop-yarn-server-nodemanager-jdk1.7.0_91.txt unit test logs https://builds.apache.org/job/PreCommit-YARN-Build/10310/artifact/patchprocess/patch-unit-hadoop-yarn-project_hadoop-yarn_hadoop-yarn-api-jdk1.8.0_66.txt https://builds.apache.org/job/PreCommit-YARN-Build/10310/artifact/patchprocess/patch-unit-hadoop-yarn-project_hadoop-yarn_hadoop-yarn-api-jdk1.7.0_91.txt JDK v1.7.0_91 Test Results https://builds.apache.org/job/PreCommit-YARN-Build/10310/testReport/ modules C: hadoop-yarn-project/hadoop-yarn/hadoop-yarn-api hadoop-yarn-project/hadoop-yarn/hadoop-yarn-common hadoop-yarn-project/hadoop-yarn/hadoop-yarn-server/hadoop-yarn-server-nodemanager U: hadoop-yarn-project/hadoop-yarn Max memory used 76MB Powered by Apache Yetus 0.2.0-SNAPSHOT http://yetus.apache.org Console output https://builds.apache.org/job/PreCommit-YARN-Build/10310/console This message was automatically generated. 
[![xgong](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10443) Xuan Gong](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=xgong) added a comment - [18/Jan/16 07:07](https://issues.apache.org/jira/browse/YARN-4577?focusedCommentId=15104873&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15104873)
Thanks for the comments, [sjlee0](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=sjlee0)
> "how important is it to support non-local classpaths"
It is important to support non-local classpath, especially HDFS classpath. It is one of the requirement for this feature. Of course, the changes are not trivial. I think that supporting HDFS could be one of the improvement for the ApplicationClassLoader if we are planning to do it. If ApplicationClassLoader supports it in future, we could replace it. But i still prefer to do it here since it is part of the requirement.
> and "Regarding setting the URLStreamHandlerFactory, you can call URL.setURLStreamHandlerFactory() at most once on a JVM, and any attempt to set it again within the same process will throw an error:"
Good point. Added a static method to call it in AuxService.java. But I can not find a better way to solve it. Any better suggestions ?
> other types of classloading
Actually, I do not even need a parent classloader here. For me, if the user provided a specific classpath for the aux-service, it is user's responsibility to make sure the provided jar file includes everything, includes the dependency. And when we initiate the related aux-service, we only look for the specific classpath. If the aux-service can not be initiated successfully with the specific classpath, it should throw an exception instead of trying to load it from parent classloader.
> unit test: l.366: I'm quite confused by the comment and the code
This unit test is used to test my previous comment.
[![xgong](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10443) Xuan Gong](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=xgong) added a comment - [18/Jan/16 07:07](https://issues.apache.org/jira/browse/YARN-4577?focusedCommentId=15104873&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15104873) Thanks for the comments, sjlee0 "how important is it to support non-local classpaths" It is important to support non-local classpath, especially HDFS classpath. It is one of the requirement for this feature. Of course, the changes are not trivial. I think that supporting HDFS could be one of the improvement for the ApplicationClassLoader if we are planning to do it. If ApplicationClassLoader supports it in future, we could replace it. But i still prefer to do it here since it is part of the requirement. and "Regarding setting the URLStreamHandlerFactory, you can call URL.setURLStreamHandlerFactory() at most once on a JVM, and any attempt to set it again within the same process will throw an error:" Good point. Added a static method to call it in AuxService.java. But I can not find a better way to solve it. Any better suggestions ? other types of classloading Actually, I do not even need a parent classloader here. For me, if the user provided a specific classpath for the aux-service, it is user's responsibility to make sure the provided jar file includes everything, includes the dependency. And when we initiate the related aux-service, we only look for the specific classpath. If the aux-service can not be initiated successfully with the specific classpath, it should throw an exception instead of trying to load it from parent classloader. unit test: l.366: I'm quite confused by the comment and the code This unit test is used to test my previous comment. 
[![hadoopqa](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Hadoop QA](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=hadoopqa) added a comment - [18/Jan/16 08:15](https://issues.apache.org/jira/browse/YARN-4577?focusedCommentId=15104910&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15104910)  
|  ![](https://issues.apache.org/jira/images/icons/emoticons/error.png) **-1 overall**  |  
| --- |  
  
  
  
|  Vote   |  Subsystem   |  Runtime   |  Comment   |  
| --- | --- | --- | --- |  
|  0  |  reexec   |  0m 0s   |  Docker mode activated.   |  
|  +1  |  @author   |  0m 0s   |  The patch does not contain any @author tags.   |  
|  +1  |  test4tests   |  0m 0s   |  The patch appears to include 2 new or modified test files.   |  
|  0  |  mvndep   |  0m 32s   |  Maven dependency ordering for branch   |  
|  +1  |  mvninstall   |  7m 54s   |  trunk passed   |  
|  +1  |  compile   |  1m 48s   |  trunk passed with JDK v1.8.0_66   |  
|  +1  |  compile   |  2m 10s   |  trunk passed with JDK v1.7.0_91   |  
|  +1  |  checkstyle   |  0m 32s   |  trunk passed   |  
|  +1  |  mvnsite   |  1m 32s   |  trunk passed   |  
|  +1  |  mvneclipse   |  0m 41s   |  trunk passed   |  
|  +1  |  findbugs   |  3m 38s   |  trunk passed   |  
|  +1  |  javadoc   |  1m 27s   |  trunk passed with JDK v1.8.0_66   |  
|  +1  |  javadoc   |  3m 55s   |  trunk passed with JDK v1.7.0_91   |  
|  0  |  mvndep   |  0m 24s   |  Maven dependency ordering for patch   |  
|  +1  |  mvninstall   |  1m 13s   |  the patch passed   |  
|  +1  |  compile   |  1m 52s   |  the patch passed with JDK v1.8.0_66   |  
|  +1  |  javac   |  1m 52s   |  the patch passed   |  
|  +1  |  compile   |  2m 10s   |  the patch passed with JDK v1.7.0_91   |  
|  +1  |  javac   |  2m 10s   |  the patch passed   |  
|  -1  |  checkstyle   |  0m 31s   |  hadoop-yarn-project/hadoop-yarn: patch generated 1 new + 258 unchanged - 0 fixed = 259 total (was 258)   |  
|  +1  |  mvnsite   |  1m 23s   |  the patch passed   |  
|  +1  |  mvneclipse   |  0m 32s   |  the patch passed   |  
|  +1  |  whitespace   |  0m 0s   |  Patch has no whitespace issues.   |  
|  +1  |  xml   |  0m 0s   |  The patch has no ill-formed XML file.   |  
|  +1  |  findbugs   |  4m 12s   |  the patch passed   |  
|  +1  |  javadoc   |  1m 21s   |  the patch passed with JDK v1.8.0_66   |  
|  +1  |  javadoc   |  3m 38s   |  the patch passed with JDK v1.7.0_91   |  
|  -1  |  unit   |  0m 21s   |  hadoop-yarn-api in the patch failed with JDK v1.8.0_66.   |  
|  +1  |  unit   |  1m 58s   |  hadoop-yarn-common in the patch passed with JDK v1.8.0_66.   |  
|  -1  |  unit   |  8m 45s   |  hadoop-yarn-server-nodemanager in the patch failed with JDK v1.8.0_66.   |  
|  -1  |  unit   |  0m 23s   |  hadoop-yarn-api in the patch failed with JDK v1.7.0_91.   |  
|  +1  |  unit   |  2m 10s   |  hadoop-yarn-common in the patch passed with JDK v1.7.0_91.   |  
|  -1  |  unit   |  9m 21s   |  hadoop-yarn-server-nodemanager in the patch failed with JDK v1.7.0_91.   |  
|  +1  |  asflicense   |  0m 20s   |  Patch does not generate ASF License warnings.   |  
|   |   |  66m 32s   |   |  
  
  
  
|  Reason   |  Tests   |  
| --- | --- |  
|  JDK v1.8.0_66 Failed junit tests   |  hadoop.yarn.conf.TestYarnConfigurationFields   |  
|  JDK v1.7.0_91 Failed junit tests   |  hadoop.yarn.conf.TestYarnConfigurationFields   |  
  
  
  
|  Subsystem   |  Report/Notes   |  
| --- | --- |  
|  Docker   |  Image:yetus/hadoop:0ca8df7   |  
|  JIRA Patch URL   |  <https://issues.apache.org/jira/secure/attachment/12782816/YARN-4577.4.patch>  |  
|  JIRA Issue   |  [~~YARN-4577~~](https://issues.apache.org/jira/browse/YARN-4577 "Enable aux services to have their own custom classpath/jar file")  |  
|  Optional Tests   |  asflicense compile javac javadoc mvninstall mvnsite unit findbugs checkstyle xml   |  
|  uname   |  Linux 3b687b178b1f 3.13.0-36-lowlatency #63-Ubuntu SMP PREEMPT Wed Sep 3 21:56:12 UTC 2014 x86_64 x86_64 x86_64 GNU/Linux   |  
|  Build tool   |  maven   |  
|  Personality   |  /testptch/hadoop/patchprocess/precommit/personality/provided.sh   |  
|  git revision   |  trunk / b08ecf5   |  
|  Default Java   |  1.7.0_91   |  
|  Multi-JDK versions   |  /usr/lib/jvm/java-8-oracle:1.8.0_66 /usr/lib/jvm/java-7-openjdk-amd64:1.7.0_91   |  
|  findbugs   |  v3.0.0   |  
|  checkstyle   |  <https://builds.apache.org/job/PreCommit-YARN-Build/10316/artifact/patchprocess/diff-checkstyle-hadoop-yarn-project_hadoop-yarn.txt>  |  
|  unit   |  <https://builds.apache.org/job/PreCommit-YARN-Build/10316/artifact/patchprocess/patch-unit-hadoop-yarn-project_hadoop-yarn_hadoop-yarn-api-jdk1.8.0_66.txt>  |  
|  unit   |  <https://builds.apache.org/job/PreCommit-YARN-Build/10316/artifact/patchprocess/patch-unit-hadoop-yarn-project_hadoop-yarn_hadoop-yarn-server_hadoop-yarn-server-nodemanager-jdk1.8.0_66.txt>  |  
|  unit   |  <https://builds.apache.org/job/PreCommit-YARN-Build/10316/artifact/patchprocess/patch-unit-hadoop-yarn-project_hadoop-yarn_hadoop-yarn-api-jdk1.7.0_91.txt>  |  
|  unit   |  <https://builds.apache.org/job/PreCommit-YARN-Build/10316/artifact/patchprocess/patch-unit-hadoop-yarn-project_hadoop-yarn_hadoop-yarn-server_hadoop-yarn-server-nodemanager-jdk1.7.0_91.txt>  |  
|  unit test logs   |  <https://builds.apache.org/job/PreCommit-YARN-Build/10316/artifact/patchprocess/patch-unit-hadoop-yarn-project_hadoop-yarn_hadoop-yarn-api-jdk1.8.0_66.txt> <https://builds.apache.org/job/PreCommit-YARN-Build/10316/artifact/patchprocess/patch-unit-hadoop-yarn-project_hadoop-yarn_hadoop-yarn-api-jdk1.7.0_91.txt>  |  
|  JDK v1.7.0_91 Test Results   |  <https://builds.apache.org/job/PreCommit-YARN-Build/10316/testReport/>  |  
|  modules   |  C: hadoop-yarn-project/hadoop-yarn/hadoop-yarn-api hadoop-yarn-project/hadoop-yarn/hadoop-yarn-common hadoop-yarn-project/hadoop-yarn/hadoop-yarn-server/hadoop-yarn-server-nodemanager U: hadoop-yarn-project/hadoop-yarn   |  
|  Max memory used   |  77MB   |  
|  Powered by   |  Apache Yetus 0.2.0-SNAPSHOT <http://yetus.apache.org>  |  
|  Console output   |  <https://builds.apache.org/job/PreCommit-YARN-Build/10316/console>  |  
This message was automatically generated.
[![hadoopqa](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Hadoop QA](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=hadoopqa) added a comment - [18/Jan/16 08:15](https://issues.apache.org/jira/browse/YARN-4577?focusedCommentId=15104910&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15104910) -1 overall Vote Subsystem Runtime Comment 0 reexec 0m 0s Docker mode activated. +1 @author 0m 0s The patch does not contain any @author tags. +1 test4tests 0m 0s The patch appears to include 2 new or modified test files. 0 mvndep 0m 32s Maven dependency ordering for branch +1 mvninstall 7m 54s trunk passed +1 compile 1m 48s trunk passed with JDK v1.8.0_66 +1 compile 2m 10s trunk passed with JDK v1.7.0_91 +1 checkstyle 0m 32s trunk passed +1 mvnsite 1m 32s trunk passed +1 mvneclipse 0m 41s trunk passed +1 findbugs 3m 38s trunk passed +1 javadoc 1m 27s trunk passed with JDK v1.8.0_66 +1 javadoc 3m 55s trunk passed with JDK v1.7.0_91 0 mvndep 0m 24s Maven dependency ordering for patch +1 mvninstall 1m 13s the patch passed +1 compile 1m 52s the patch passed with JDK v1.8.0_66 +1 javac 1m 52s the patch passed +1 compile 2m 10s the patch passed with JDK v1.7.0_91 +1 javac 2m 10s the patch passed -1 checkstyle 0m 31s hadoop-yarn-project/hadoop-yarn: patch generated 1 new + 258 unchanged - 0 fixed = 259 total (was 258) +1 mvnsite 1m 23s the patch passed +1 mvneclipse 0m 32s the patch passed +1 whitespace 0m 0s Patch has no whitespace issues. +1 xml 0m 0s The patch has no ill-formed XML file. +1 findbugs 4m 12s the patch passed +1 javadoc 1m 21s the patch passed with JDK v1.8.0_66 +1 javadoc 3m 38s the patch passed with JDK v1.7.0_91 -1 unit 0m 21s hadoop-yarn-api in the patch failed with JDK v1.8.0_66. +1 unit 1m 58s hadoop-yarn-common in the patch passed with JDK v1.8.0_66. -1 unit 8m 45s hadoop-yarn-server-nodemanager in the patch failed with JDK v1.8.0_66. -1 unit 0m 23s hadoop-yarn-api in the patch failed with JDK v1.7.0_91. +1 unit 2m 10s hadoop-yarn-common in the patch passed with JDK v1.7.0_91. -1 unit 9m 21s hadoop-yarn-server-nodemanager in the patch failed with JDK v1.7.0_91. +1 asflicense 0m 20s Patch does not generate ASF License warnings. 66m 32s Reason Tests JDK v1.8.0_66 Failed junit tests hadoop.yarn.conf.TestYarnConfigurationFields JDK v1.7.0_91 Failed junit tests hadoop.yarn.conf.TestYarnConfigurationFields Subsystem Report/Notes Docker Image:yetus/hadoop:0ca8df7 JIRA Patch URL https://issues.apache.org/jira/secure/attachment/12782816/YARN-4577.4.patch JIRA Issue YARN-4577 Optional Tests asflicense compile javac javadoc mvninstall mvnsite unit findbugs checkstyle xml uname Linux 3b687b178b1f 3.13.0-36-lowlatency #63-Ubuntu SMP PREEMPT Wed Sep 3 21:56:12 UTC 2014 x86_64 x86_64 x86_64 GNU/Linux Build tool maven Personality /testptch/hadoop/patchprocess/precommit/personality/provided.sh git revision trunk / b08ecf5 Default Java 1.7.0_91 Multi-JDK versions /usr/lib/jvm/java-8-oracle:1.8.0_66 /usr/lib/jvm/java-7-openjdk-amd64:1.7.0_91 findbugs v3.0.0 checkstyle https://builds.apache.org/job/PreCommit-YARN-Build/10316/artifact/patchprocess/diff-checkstyle-hadoop-yarn-project_hadoop-yarn.txt unit https://builds.apache.org/job/PreCommit-YARN-Build/10316/artifact/patchprocess/patch-unit-hadoop-yarn-project_hadoop-yarn_hadoop-yarn-api-jdk1.8.0_66.txt unit https://builds.apache.org/job/PreCommit-YARN-Build/10316/artifact/patchprocess/patch-unit-hadoop-yarn-project_hadoop-yarn_hadoop-yarn-server_hadoop-yarn-server-nodemanager-jdk1.8.0_66.txt unit https://builds.apache.org/job/PreCommit-YARN-Build/10316/artifact/patchprocess/patch-unit-hadoop-yarn-project_hadoop-yarn_hadoop-yarn-api-jdk1.7.0_91.txt unit https://builds.apache.org/job/PreCommit-YARN-Build/10316/artifact/patchprocess/patch-unit-hadoop-yarn-project_hadoop-yarn_hadoop-yarn-server_hadoop-yarn-server-nodemanager-jdk1.7.0_91.txt unit test logs https://builds.apache.org/job/PreCommit-YARN-Build/10316/artifact/patchprocess/patch-unit-hadoop-yarn-project_hadoop-yarn_hadoop-yarn-api-jdk1.8.0_66.txt https://builds.apache.org/job/PreCommit-YARN-Build/10316/artifact/patchprocess/patch-unit-hadoop-yarn-project_hadoop-yarn_hadoop-yarn-api-jdk1.7.0_91.txt JDK v1.7.0_91 Test Results https://builds.apache.org/job/PreCommit-YARN-Build/10316/testReport/ modules C: hadoop-yarn-project/hadoop-yarn/hadoop-yarn-api hadoop-yarn-project/hadoop-yarn/hadoop-yarn-common hadoop-yarn-project/hadoop-yarn/hadoop-yarn-server/hadoop-yarn-server-nodemanager U: hadoop-yarn-project/hadoop-yarn Max memory used 77MB Powered by Apache Yetus 0.2.0-SNAPSHOT http://yetus.apache.org Console output https://builds.apache.org/job/PreCommit-YARN-Build/10316/console This message was automatically generated. 
[![xgong](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10443) Xuan Gong](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=xgong) added a comment - [18/Jan/16 17:37](https://issues.apache.org/jira/browse/YARN-4577?focusedCommentId=15105561&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15105561)
[sjlee0](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=sjlee0)
> how important is it to support non-local classpaths
We can do it separately. Right now, for this ticket, we are focusing on supporting the local classpath.
> other types of classloading
Do we have any examples for this ? I can only find the MRApp and RunJar are using ApplicationClassLoader. 
[![xgong](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10443) Xuan Gong](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=xgong) added a comment - [18/Jan/16 17:37](https://issues.apache.org/jira/browse/YARN-4577?focusedCommentId=15105561&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15105561) sjlee0 how important is it to support non-local classpaths We can do it separately. Right now, for this ticket, we are focusing on supporting the local classpath. other types of classloading Do we have any examples for this ? I can only find the MRApp and RunJar are using ApplicationClassLoader. 
[![sjlee0](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Sangjin Lee](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=sjlee0) added a comment - [26/Jan/16 00:35](https://issues.apache.org/jira/browse/YARN-4577?focusedCommentId=15116379&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15116379)
> Do we have any examples for this ? I can only find the MRApp and RunJar are using ApplicationClassLoader.
Currently there are 3 places where the application classloader is used: RunJar (for running the hadoop jar command), YarnChild and MRAppMaster for MR.
A standard pattern is to surround the code that needs to execute user code (and needs the user classloader) with setting the config classloader as well as the thread context classloader. You can look at things like MRApps.setJobClassLoader() and MRAppMaster.callWithJobClassLoader().
[![sjlee0](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Sangjin Lee](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=sjlee0) added a comment - [26/Jan/16 00:35](https://issues.apache.org/jira/browse/YARN-4577?focusedCommentId=15116379&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15116379) Do we have any examples for this ? I can only find the MRApp and RunJar are using ApplicationClassLoader. Currently there are 3 places where the application classloader is used: RunJar (for running the hadoop jar command), YarnChild and MRAppMaster for MR. A standard pattern is to surround the code that needs to execute user code (and needs the user classloader) with setting the config classloader as well as the thread context classloader. You can look at things like MRApps.setJobClassLoader() and MRAppMaster.callWithJobClassLoader(). 
[![hadoopqa](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Hadoop QA](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=hadoopqa) added a comment - [26/Jan/16 01:50](https://issues.apache.org/jira/browse/YARN-4577?focusedCommentId=15116488&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15116488)  
|  ![](https://issues.apache.org/jira/images/icons/emoticons/error.png) **-1 overall**  |  
| --- |  
  
  
  
|  Vote   |  Subsystem   |  Runtime   |  Comment   |  
| --- | --- | --- | --- |  
|  0  |  reexec   |  0m 0s   |  Docker mode activated.   |  
|  +1  |  @author   |  0m 0s   |  The patch does not contain any @author tags.   |  
|  +1  |  test4tests   |  0m 0s   |  The patch appears to include 2 new or modified test files.   |  
|  0  |  mvndep   |  0m 34s   |  Maven dependency ordering for branch   |  
|  +1  |  mvninstall   |  8m 49s   |  trunk passed   |  
|  +1  |  compile   |  2m 48s   |  trunk passed with JDK v1.8.0_66   |  
|  +1  |  compile   |  2m 20s   |  trunk passed with JDK v1.7.0_91   |  
|  +1  |  checkstyle   |  0m 39s   |  trunk passed   |  
|  +1  |  mvnsite   |  1m 38s   |  trunk passed   |  
|  +1  |  mvneclipse   |  0m 42s   |  trunk passed   |  
|  +1  |  findbugs   |  4m 8s   |  trunk passed   |  
|  +1  |  javadoc   |  1m 32s   |  trunk passed with JDK v1.8.0_66   |  
|  +1  |  javadoc   |  3m 58s   |  trunk passed with JDK v1.7.0_91   |  
|  0  |  mvndep   |  0m 26s   |  Maven dependency ordering for patch   |  
|  +1  |  mvninstall   |  1m 23s   |  the patch passed   |  
|  +1  |  compile   |  2m 20s   |  the patch passed with JDK v1.8.0_66   |  
|  +1  |  javac   |  2m 20s   |  the patch passed   |  
|  +1  |  compile   |  2m 20s   |  the patch passed with JDK v1.7.0_91   |  
|  +1  |  javac   |  2m 20s   |  the patch passed   |  
|  -1  |  checkstyle   |  0m 38s   |  hadoop-yarn-project/hadoop-yarn: patch generated 13 new + 258 unchanged - 0 fixed = 271 total (was 258)   |  
|  +1  |  mvnsite   |  1m 31s   |  the patch passed   |  
|  +1  |  mvneclipse   |  0m 34s   |  the patch passed   |  
|  +1  |  whitespace   |  0m 0s   |  Patch has no whitespace issues.   |  
|  +1  |  xml   |  0m 1s   |  The patch has no ill-formed XML file.   |  
|  +1  |  findbugs   |  4m 32s   |  the patch passed   |  
|  +1  |  javadoc   |  1m 26s   |  the patch passed with JDK v1.8.0_66   |  
|  +1  |  javadoc   |  3m 43s   |  the patch passed with JDK v1.7.0_91   |  
|  +1  |  unit   |  0m 22s   |  hadoop-yarn-api in the patch passed with JDK v1.8.0_66.   |  
|  +1  |  unit   |  2m 5s   |  hadoop-yarn-common in the patch passed with JDK v1.8.0_66.   |  
|  -1  |  unit   |  8m 53s   |  hadoop-yarn-server-nodemanager in the patch failed with JDK v1.8.0_66.   |  
|  +1  |  unit   |  0m 25s   |  hadoop-yarn-api in the patch passed with JDK v1.7.0_91.   |  
|  +1  |  unit   |  2m 16s   |  hadoop-yarn-common in the patch passed with JDK v1.7.0_91.   |  
|  -1  |  unit   |  9m 15s   |  hadoop-yarn-server-nodemanager in the patch failed with JDK v1.7.0_91.   |  
|  +1  |  asflicense   |  0m 20s   |  Patch does not generate ASF License warnings.   |  
|   |   |  71m 13s   |   |  
  
  
  
|  Subsystem   |  Report/Notes   |  
| --- | --- |  
|  Docker   |  Image:yetus/hadoop:0ca8df7   |  
|  JIRA Patch URL   |  <https://issues.apache.org/jira/secure/attachment/12783119/YARN-4577.20160119.1.patch>  |  
|  JIRA Issue   |  [~~YARN-4577~~](https://issues.apache.org/jira/browse/YARN-4577 "Enable aux services to have their own custom classpath/jar file")  |  
|  Optional Tests   |  asflicense compile javac javadoc mvninstall mvnsite unit findbugs checkstyle xml   |  
|  uname   |  Linux 9446af938ee9 3.13.0-36-lowlatency #63-Ubuntu SMP PREEMPT Wed Sep 3 21:56:12 UTC 2014 x86_64 x86_64 x86_64 GNU/Linux   |  
|  Build tool   |  maven   |  
|  Personality   |  /testptch/hadoop/patchprocess/precommit/personality/provided.sh   |  
|  git revision   |  trunk / 2085e60   |  
|  Default Java   |  1.7.0_91   |  
|  Multi-JDK versions   |  /usr/lib/jvm/java-8-oracle:1.8.0_66 /usr/lib/jvm/java-7-openjdk-amd64:1.7.0_91   |  
|  findbugs   |  v3.0.0   |  
|  checkstyle   |  <https://builds.apache.org/job/PreCommit-YARN-Build/10385/artifact/patchprocess/diff-checkstyle-hadoop-yarn-project_hadoop-yarn.txt>  |  
|  unit   |  <https://builds.apache.org/job/PreCommit-YARN-Build/10385/artifact/patchprocess/patch-unit-hadoop-yarn-project_hadoop-yarn_hadoop-yarn-server_hadoop-yarn-server-nodemanager-jdk1.8.0_66.txt>  |  
|  unit   |  <https://builds.apache.org/job/PreCommit-YARN-Build/10385/artifact/patchprocess/patch-unit-hadoop-yarn-project_hadoop-yarn_hadoop-yarn-server_hadoop-yarn-server-nodemanager-jdk1.7.0_91.txt>  |  
|  JDK v1.7.0_91 Test Results   |  <https://builds.apache.org/job/PreCommit-YARN-Build/10385/testReport/>  |  
|  modules   |  C: hadoop-yarn-project/hadoop-yarn/hadoop-yarn-api hadoop-yarn-project/hadoop-yarn/hadoop-yarn-common hadoop-yarn-project/hadoop-yarn/hadoop-yarn-server/hadoop-yarn-server-nodemanager U: hadoop-yarn-project/hadoop-yarn   |  
|  Max memory used   |  77MB   |  
|  Powered by   |  Apache Yetus 0.2.0-SNAPSHOT <http://yetus.apache.org>  |  
|  Console output   |  <https://builds.apache.org/job/PreCommit-YARN-Build/10385/console>  |  
This message was automatically generated.
[![hadoopqa](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Hadoop QA](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=hadoopqa) added a comment - [26/Jan/16 01:50](https://issues.apache.org/jira/browse/YARN-4577?focusedCommentId=15116488&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15116488) -1 overall Vote Subsystem Runtime Comment 0 reexec 0m 0s Docker mode activated. +1 @author 0m 0s The patch does not contain any @author tags. +1 test4tests 0m 0s The patch appears to include 2 new or modified test files. 0 mvndep 0m 34s Maven dependency ordering for branch +1 mvninstall 8m 49s trunk passed +1 compile 2m 48s trunk passed with JDK v1.8.0_66 +1 compile 2m 20s trunk passed with JDK v1.7.0_91 +1 checkstyle 0m 39s trunk passed +1 mvnsite 1m 38s trunk passed +1 mvneclipse 0m 42s trunk passed +1 findbugs 4m 8s trunk passed +1 javadoc 1m 32s trunk passed with JDK v1.8.0_66 +1 javadoc 3m 58s trunk passed with JDK v1.7.0_91 0 mvndep 0m 26s Maven dependency ordering for patch +1 mvninstall 1m 23s the patch passed +1 compile 2m 20s the patch passed with JDK v1.8.0_66 +1 javac 2m 20s the patch passed +1 compile 2m 20s the patch passed with JDK v1.7.0_91 +1 javac 2m 20s the patch passed -1 checkstyle 0m 38s hadoop-yarn-project/hadoop-yarn: patch generated 13 new + 258 unchanged - 0 fixed = 271 total (was 258) +1 mvnsite 1m 31s the patch passed +1 mvneclipse 0m 34s the patch passed +1 whitespace 0m 0s Patch has no whitespace issues. +1 xml 0m 1s The patch has no ill-formed XML file. +1 findbugs 4m 32s the patch passed +1 javadoc 1m 26s the patch passed with JDK v1.8.0_66 +1 javadoc 3m 43s the patch passed with JDK v1.7.0_91 +1 unit 0m 22s hadoop-yarn-api in the patch passed with JDK v1.8.0_66. +1 unit 2m 5s hadoop-yarn-common in the patch passed with JDK v1.8.0_66. -1 unit 8m 53s hadoop-yarn-server-nodemanager in the patch failed with JDK v1.8.0_66. +1 unit 0m 25s hadoop-yarn-api in the patch passed with JDK v1.7.0_91. +1 unit 2m 16s hadoop-yarn-common in the patch passed with JDK v1.7.0_91. -1 unit 9m 15s hadoop-yarn-server-nodemanager in the patch failed with JDK v1.7.0_91. +1 asflicense 0m 20s Patch does not generate ASF License warnings. 71m 13s Subsystem Report/Notes Docker Image:yetus/hadoop:0ca8df7 JIRA Patch URL https://issues.apache.org/jira/secure/attachment/12783119/YARN-4577.20160119.1.patch JIRA Issue YARN-4577 Optional Tests asflicense compile javac javadoc mvninstall mvnsite unit findbugs checkstyle xml uname Linux 9446af938ee9 3.13.0-36-lowlatency #63-Ubuntu SMP PREEMPT Wed Sep 3 21:56:12 UTC 2014 x86_64 x86_64 x86_64 GNU/Linux Build tool maven Personality /testptch/hadoop/patchprocess/precommit/personality/provided.sh git revision trunk / 2085e60 Default Java 1.7.0_91 Multi-JDK versions /usr/lib/jvm/java-8-oracle:1.8.0_66 /usr/lib/jvm/java-7-openjdk-amd64:1.7.0_91 findbugs v3.0.0 checkstyle https://builds.apache.org/job/PreCommit-YARN-Build/10385/artifact/patchprocess/diff-checkstyle-hadoop-yarn-project_hadoop-yarn.txt unit https://builds.apache.org/job/PreCommit-YARN-Build/10385/artifact/patchprocess/patch-unit-hadoop-yarn-project_hadoop-yarn_hadoop-yarn-server_hadoop-yarn-server-nodemanager-jdk1.8.0_66.txt unit https://builds.apache.org/job/PreCommit-YARN-Build/10385/artifact/patchprocess/patch-unit-hadoop-yarn-project_hadoop-yarn_hadoop-yarn-server_hadoop-yarn-server-nodemanager-jdk1.7.0_91.txt JDK v1.7.0_91 Test Results https://builds.apache.org/job/PreCommit-YARN-Build/10385/testReport/ modules C: hadoop-yarn-project/hadoop-yarn/hadoop-yarn-api hadoop-yarn-project/hadoop-yarn/hadoop-yarn-common hadoop-yarn-project/hadoop-yarn/hadoop-yarn-server/hadoop-yarn-server-nodemanager U: hadoop-yarn-project/hadoop-yarn Max memory used 77MB Powered by Apache Yetus 0.2.0-SNAPSHOT http://yetus.apache.org Console output https://builds.apache.org/job/PreCommit-YARN-Build/10385/console This message was automatically generated. 
[![xgong](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10443) Xuan Gong](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=xgong) added a comment - [05/Feb/16 00:46](https://issues.apache.org/jira/browse/YARN-4577?focusedCommentId=15133428&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15133428)
[sjlee0](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=sjlee0)  
Thanks for the information.
Attached a new patch. Could you take a look, please ?
[![xgong](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10443) Xuan Gong](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=xgong) added a comment - [05/Feb/16 00:46](https://issues.apache.org/jira/browse/YARN-4577?focusedCommentId=15133428&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15133428) sjlee0 Thanks for the information. Attached a new patch. Could you take a look, please ? 
[![hadoopqa](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Hadoop QA](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=hadoopqa) added a comment - [05/Feb/16 01:57](https://issues.apache.org/jira/browse/YARN-4577?focusedCommentId=15133494&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15133494)  
|  ![](https://issues.apache.org/jira/images/icons/emoticons/error.png) **-1 overall**  |  
| --- |  
  
  
  
|  Vote   |  Subsystem   |  Runtime   |  Comment   |  
| --- | --- | --- | --- |  
|  0  |  reexec   |  0m 11s   |  Docker mode activated.   |  
|  +1  |  @author   |  0m 0s   |  The patch does not contain any @author tags.   |  
|  +1  |  test4tests   |  0m 0s   |  The patch appears to include 2 new or modified test files.   |  
|  0  |  mvndep   |  0m 26s   |  Maven dependency ordering for branch   |  
|  +1  |  mvninstall   |  7m 13s   |  trunk passed   |  
|  +1  |  compile   |  2m 4s   |  trunk passed with JDK v1.8.0_66   |  
|  +1  |  compile   |  2m 18s   |  trunk passed with JDK v1.7.0_91   |  
|  +1  |  checkstyle   |  0m 38s   |  trunk passed   |  
|  +1  |  mvnsite   |  1m 32s   |  trunk passed   |  
|  +1  |  mvneclipse   |  0m 37s   |  trunk passed   |  
|  +1  |  findbugs   |  3m 22s   |  trunk passed   |  
|  +1  |  javadoc   |  1m 31s   |  trunk passed with JDK v1.8.0_66   |  
|  +1  |  javadoc   |  4m 5s   |  trunk passed with JDK v1.7.0_91   |  
|  0  |  mvndep   |  0m 25s   |  Maven dependency ordering for patch   |  
|  +1  |  mvninstall   |  1m 18s   |  the patch passed   |  
|  +1  |  compile   |  2m 3s   |  the patch passed with JDK v1.8.0_66   |  
|  +1  |  javac   |  2m 3s   |  the patch passed   |  
|  +1  |  compile   |  2m 14s   |  the patch passed with JDK v1.7.0_91   |  
|  +1  |  javac   |  2m 14s   |  the patch passed   |  
|  -1  |  checkstyle   |  0m 35s   |  hadoop-yarn-project/hadoop-yarn: patch generated 2 new + 258 unchanged - 0 fixed = 260 total (was 258)   |  
|  +1  |  mvnsite   |  1m 28s   |  the patch passed   |  
|  +1  |  mvneclipse   |  0m 34s   |  the patch passed   |  
|  +1  |  whitespace   |  0m 0s   |  Patch has no whitespace issues.   |  
|  +1  |  xml   |  0m 1s   |  The patch has no ill-formed XML file.   |  
|  +1  |  findbugs   |  4m 17s   |  the patch passed   |  
|  +1  |  javadoc   |  1m 26s   |  the patch passed with JDK v1.8.0_66   |  
|  +1  |  javadoc   |  3m 56s   |  the patch passed with JDK v1.7.0_91   |  
|  +1  |  unit   |  0m 22s   |  hadoop-yarn-api in the patch passed with JDK v1.8.0_66.   |  
|  +1  |  unit   |  2m 0s   |  hadoop-yarn-common in the patch passed with JDK v1.8.0_66.   |  
|  +1  |  unit   |  8m 57s   |  hadoop-yarn-server-nodemanager in the patch passed with JDK v1.8.0_66.   |  
|  +1  |  unit   |  0m 25s   |  hadoop-yarn-api in the patch passed with JDK v1.7.0_91.   |  
|  +1  |  unit   |  2m 22s   |  hadoop-yarn-common in the patch passed with JDK v1.7.0_91.   |  
|  +1  |  unit   |  9m 48s   |  hadoop-yarn-server-nodemanager in the patch passed with JDK v1.7.0_91.   |  
|  +1  |  asflicense   |  0m 23s   |  Patch does not generate ASF License warnings.   |  
|   |   |  68m 0s   |   |  
  
  
  
|  Subsystem   |  Report/Notes   |  
| --- | --- |  
|  Docker   |  Image:yetus/hadoop:0ca8df7   |  
|  JIRA Patch URL   |  <https://issues.apache.org/jira/secure/attachment/12786365/YARN-4577.20160204.patch>  |  
|  JIRA Issue   |  [~~YARN-4577~~](https://issues.apache.org/jira/browse/YARN-4577 "Enable aux services to have their own custom classpath/jar file")  |  
|  Optional Tests   |  asflicense compile javac javadoc mvninstall mvnsite unit findbugs checkstyle xml   |  
|  uname   |  Linux ab1657c5306b 3.13.0-36-lowlatency #63-Ubuntu SMP PREEMPT Wed Sep 3 21:56:12 UTC 2014 x86_64 x86_64 x86_64 GNU/Linux   |  
|  Build tool   |  maven   |  
|  Personality   |  /testptch/hadoop/patchprocess/precommit/personality/provided.sh   |  
|  git revision   |  trunk / 1bcfab8   |  
|  Default Java   |  1.7.0_91   |  
|  Multi-JDK versions   |  /usr/lib/jvm/java-8-oracle:1.8.0_66 /usr/lib/jvm/java-7-openjdk-amd64:1.7.0_91   |  
|  findbugs   |  v3.0.0   |  
|  checkstyle   |  <https://builds.apache.org/job/PreCommit-YARN-Build/10496/artifact/patchprocess/diff-checkstyle-hadoop-yarn-project_hadoop-yarn.txt>  |  
|  JDK v1.7.0_91 Test Results   |  <https://builds.apache.org/job/PreCommit-YARN-Build/10496/testReport/>  |  
|  modules   |  C: hadoop-yarn-project/hadoop-yarn/hadoop-yarn-api hadoop-yarn-project/hadoop-yarn/hadoop-yarn-common hadoop-yarn-project/hadoop-yarn/hadoop-yarn-server/hadoop-yarn-server-nodemanager U: hadoop-yarn-project/hadoop-yarn   |  
|  Max memory used   |  77MB   |  
|  Console output   |  <https://builds.apache.org/job/PreCommit-YARN-Build/10496/console>  |  
|  Powered by   |  Apache Yetus 0.2.0-SNAPSHOT <http://yetus.apache.org>  |  
This message was automatically generated.
[![hadoopqa](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Hadoop QA](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=hadoopqa) added a comment - [05/Feb/16 01:57](https://issues.apache.org/jira/browse/YARN-4577?focusedCommentId=15133494&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15133494) -1 overall Vote Subsystem Runtime Comment 0 reexec 0m 11s Docker mode activated. +1 @author 0m 0s The patch does not contain any @author tags. +1 test4tests 0m 0s The patch appears to include 2 new or modified test files. 0 mvndep 0m 26s Maven dependency ordering for branch +1 mvninstall 7m 13s trunk passed +1 compile 2m 4s trunk passed with JDK v1.8.0_66 +1 compile 2m 18s trunk passed with JDK v1.7.0_91 +1 checkstyle 0m 38s trunk passed +1 mvnsite 1m 32s trunk passed +1 mvneclipse 0m 37s trunk passed +1 findbugs 3m 22s trunk passed +1 javadoc 1m 31s trunk passed with JDK v1.8.0_66 +1 javadoc 4m 5s trunk passed with JDK v1.7.0_91 0 mvndep 0m 25s Maven dependency ordering for patch +1 mvninstall 1m 18s the patch passed +1 compile 2m 3s the patch passed with JDK v1.8.0_66 +1 javac 2m 3s the patch passed +1 compile 2m 14s the patch passed with JDK v1.7.0_91 +1 javac 2m 14s the patch passed -1 checkstyle 0m 35s hadoop-yarn-project/hadoop-yarn: patch generated 2 new + 258 unchanged - 0 fixed = 260 total (was 258) +1 mvnsite 1m 28s the patch passed +1 mvneclipse 0m 34s the patch passed +1 whitespace 0m 0s Patch has no whitespace issues. +1 xml 0m 1s The patch has no ill-formed XML file. +1 findbugs 4m 17s the patch passed +1 javadoc 1m 26s the patch passed with JDK v1.8.0_66 +1 javadoc 3m 56s the patch passed with JDK v1.7.0_91 +1 unit 0m 22s hadoop-yarn-api in the patch passed with JDK v1.8.0_66. +1 unit 2m 0s hadoop-yarn-common in the patch passed with JDK v1.8.0_66. +1 unit 8m 57s hadoop-yarn-server-nodemanager in the patch passed with JDK v1.8.0_66. +1 unit 0m 25s hadoop-yarn-api in the patch passed with JDK v1.7.0_91. +1 unit 2m 22s hadoop-yarn-common in the patch passed with JDK v1.7.0_91. +1 unit 9m 48s hadoop-yarn-server-nodemanager in the patch passed with JDK v1.7.0_91. +1 asflicense 0m 23s Patch does not generate ASF License warnings. 68m 0s Subsystem Report/Notes Docker Image:yetus/hadoop:0ca8df7 JIRA Patch URL https://issues.apache.org/jira/secure/attachment/12786365/YARN-4577.20160204.patch JIRA Issue YARN-4577 Optional Tests asflicense compile javac javadoc mvninstall mvnsite unit findbugs checkstyle xml uname Linux ab1657c5306b 3.13.0-36-lowlatency #63-Ubuntu SMP PREEMPT Wed Sep 3 21:56:12 UTC 2014 x86_64 x86_64 x86_64 GNU/Linux Build tool maven Personality /testptch/hadoop/patchprocess/precommit/personality/provided.sh git revision trunk / 1bcfab8 Default Java 1.7.0_91 Multi-JDK versions /usr/lib/jvm/java-8-oracle:1.8.0_66 /usr/lib/jvm/java-7-openjdk-amd64:1.7.0_91 findbugs v3.0.0 checkstyle https://builds.apache.org/job/PreCommit-YARN-Build/10496/artifact/patchprocess/diff-checkstyle-hadoop-yarn-project_hadoop-yarn.txt JDK v1.7.0_91 Test Results https://builds.apache.org/job/PreCommit-YARN-Build/10496/testReport/ modules C: hadoop-yarn-project/hadoop-yarn/hadoop-yarn-api hadoop-yarn-project/hadoop-yarn/hadoop-yarn-common hadoop-yarn-project/hadoop-yarn/hadoop-yarn-server/hadoop-yarn-server-nodemanager U: hadoop-yarn-project/hadoop-yarn Max memory used 77MB Console output https://builds.apache.org/job/PreCommit-YARN-Build/10496/console Powered by Apache Yetus 0.2.0-SNAPSHOT http://yetus.apache.org This message was automatically generated. 
[![sjlee0](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Sangjin Lee](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=sjlee0) added a comment - [10/Feb/16 02:02](https://issues.apache.org/jira/browse/YARN-4577?focusedCommentId=15140203&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15140203)
Thanks for updating the patch [xgong](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=xgong).
(1)  
It looks like the secondary classloading pattern has still not been addressed. I'm referring to setting the created classloader onto the configuration as well as thread context classloader. It is not sufficient to simply load the main aux service class using that classloader. That works for the cases where other dependent classes are loaded via normal class references from it, but does nothing to handle classloading via `Configuration.getClass()` or reflection using the thread context classloader. If we do not address them, we will get fatal errors the moment an aux service does those types of classloading, each of which will become a bug. This is definitely a requirement IMO.
Fortunately we have a fairly well-defined set of call points that call into the aux services. We can surround them with setting and unsetting the configuration classloader as well as thread context classloader (see the comments above for how it is done). It is not exact, but it is certainly necessary. Let me know if you have any questions.
(2)  
Are we supporting hdfs paths as part of the aux classpaths? I thought that you mentioned that it does not have to be done as part of this JIRA. If that is the case, why do we still need to set the URL stream handler factory? The JVM's URL stream handler factory is capable of handling all local paths.
(3)  
Assuming we don't need to support hdfs paths, can't we simply rely on `ApplicationClassLoader` to construct the URLs from the classpath? Is there a reason we need to replicate the `constructUrlsFromClasspath()`? It would be good if we can rely on the common implementation, and improve it if there is a missing piece.
[![sjlee0](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Sangjin Lee](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=sjlee0) added a comment - [10/Feb/16 02:02](https://issues.apache.org/jira/browse/YARN-4577?focusedCommentId=15140203&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15140203) Thanks for updating the patch xgong . (1) It looks like the secondary classloading pattern has still not been addressed. I'm referring to setting the created classloader onto the configuration as well as thread context classloader. It is not sufficient to simply load the main aux service class using that classloader. That works for the cases where other dependent classes are loaded via normal class references from it, but does nothing to handle classloading via Configuration.getClass() or reflection using the thread context classloader. If we do not address them, we will get fatal errors the moment an aux service does those types of classloading, each of which will become a bug. This is definitely a requirement IMO. Fortunately we have a fairly well-defined set of call points that call into the aux services. We can surround them with setting and unsetting the configuration classloader as well as thread context classloader (see the comments above for how it is done). It is not exact, but it is certainly necessary. Let me know if you have any questions. (2) Are we supporting hdfs paths as part of the aux classpaths? I thought that you mentioned that it does not have to be done as part of this JIRA. If that is the case, why do we still need to set the URL stream handler factory? The JVM's URL stream handler factory is capable of handling all local paths. (3) Assuming we don't need to support hdfs paths, can't we simply rely on ApplicationClassLoader to construct the URLs from the classpath? Is there a reason we need to replicate the constructUrlsFromClasspath() ? It would be good if we can rely on the common implementation, and improve it if there is a missing piece. 
[![xgong](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10443) Xuan Gong](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=xgong) added a comment - [11/Feb/16 18:27](https://issues.apache.org/jira/browse/YARN-4577?focusedCommentId=15143207&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15143207)
[sjlee0](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=sjlee0) Thanks for the review. Looks like we reviewed a incorrect patch.
<https://issues.apache.org/jira/secure/attachment/12786365/YARN-4577.20160204.patch> is correct one..
Sorry for the inconsistent naming of the patch. Could you review the patch ?
[![xgong](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10443) Xuan Gong](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=xgong) added a comment - [11/Feb/16 18:27](https://issues.apache.org/jira/browse/YARN-4577?focusedCommentId=15143207&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15143207) sjlee0 Thanks for the review. Looks like we reviewed a incorrect patch. https://issues.apache.org/jira/secure/attachment/12786365/YARN-4577.20160204.patch is correct one.. Sorry for the inconsistent naming of the patch. Could you review the patch ? 
[![sjlee0](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Sangjin Lee](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=sjlee0) added a comment - [12/Feb/16 01:21](https://issues.apache.org/jira/browse/YARN-4577?focusedCommentId=15143841&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15143841)
My apologies [xgong](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=xgong)! I must have looked at the last attachments. I'll take a look at it, and get back to you soon.
[![sjlee0](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Sangjin Lee](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=sjlee0) added a comment - [12/Feb/16 01:21](https://issues.apache.org/jira/browse/YARN-4577?focusedCommentId=15143841&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15143841) My apologies xgong ! I must have looked at the last attachments. I'll take a look at it, and get back to you soon. 
[![sjlee0](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Sangjin Lee](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=sjlee0) added a comment - [12/Feb/16 19:09](https://issues.apache.org/jira/browse/YARN-4577?focusedCommentId=15145099&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15145099)
I think I need to clarify a little more what needs to be done with the custom classloader. The custom classloader for a given aux service must be created only once and used throughout for any code that exercises that aux service's code.
I don't think you need to wrap creating the aux service with a `callWithClassLoader()` call. That's really not necessary. What you do need is, you need to intercept **subsequent** calls on the aux service and wrap them with `callWithClassLoader()`. And when you do, you'd need to provide that exact custom classloader instance you created when you created the aux service. Otherwise, things like `ClassCastException` can ensue.
So **all** overridable calls to the public methods like `initializeApplication()`, `stopApplication()`, `getMetaData()`, `initializeContainer()`, `stopContainer()`, as well as service lifecycle methods such as `serviceStart()`, `serviceInit()`, and `serviceStop()` should be intercepted.
Now, intercepting the aux-service-specific methods is easier as there are explicit places where they are invoked. What's more difficult is the service lifecycle methods as they are invoked from `AuxServices` only indirectly.
I can see 2 approaches to this (there may be more). First, we could consider adding a wrapper class that can do this within the wrapper code. It might be something like

```
class AuxiliaryServiceWithCustomClassLoader extends AuxiliaryService {
  private final AuxiliaryService wrapped;
  private final ClassLoader customClassLoader;
  
  public AuxiliaryServiceWithCustomClassLoader(AuxiliaryService s, ClassLoader cl) {
    this.wrapped = s;
    this.customClassLoader = cl;
  }
  ...
  @Override
  protected void serviceStart() throws Exception {
    callWithCustomClassLoader(wrapped.serviceStart());
  }
  ...
  @Override
  public void initializeApplication(ApplicationInitializationContext context) {
    callWithCustomClassLoader(wrapper.initializeApplication(context));
  }
  ...
  private callWithCustomClassLoader(...) {
  }
}

```

The other approach may be to abandon dealing with the `Configuration.getClass()` and the thread context classloader scenario, and **requiring** any aux service that wants to use a custom classpath **NOT** to do anything that will trigger `Configuration.getClass()` or the use of the TCCL, either directly or indirectly. Then we don't need to do all this wrapping business.
What I'm not sure of is how practical this requirement would be for those aux services. Note that this has to be true even directly.
I also need to point out one potential risk with this wrapping. One potential risk is that the configuration is a shared object. If one aux service resets the configuration classloader to invoke its code, any other NM code that's running concurrently could be impacted potentially. For example, if two aux services have a race (on separate threads) setting the configuration class, then we could have a nasty problem.
Could you consider the implications of these options? Perhaps requiring these aux services not to do any `Configuration.getClass()` might not be that unreasonable...
[![sjlee0](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Sangjin Lee](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=sjlee0) added a comment - [12/Feb/16 19:09](https://issues.apache.org/jira/browse/YARN-4577?focusedCommentId=15145099&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15145099) I think I need to clarify a little more what needs to be done with the custom classloader. The custom classloader for a given aux service must be created only once and used throughout for any code that exercises that aux service's code. I don't think you need to wrap creating the aux service with a callWithClassLoader() call. That's really not necessary. What you do need is, you need to intercept subsequent calls on the aux service and wrap them with callWithClassLoader() . And when you do, you'd need to provide that exact custom classloader instance you created when you created the aux service. Otherwise, things like ClassCastException can ensue. So all overridable calls to the public methods like initializeApplication() , stopApplication() , getMetaData() , initializeContainer() , stopContainer() , as well as service lifecycle methods such as serviceStart() , serviceInit() , and serviceStop() should be intercepted. Now, intercepting the aux-service-specific methods is easier as there are explicit places where they are invoked. What's more difficult is the service lifecycle methods as they are invoked from AuxServices only indirectly. I can see 2 approaches to this (there may be more). First, we could consider adding a wrapper class that can do this within the wrapper code. It might be something like class AuxiliaryServiceWithCustomClassLoader extends AuxiliaryService { private final AuxiliaryService wrapped; private final ClassLoader customClassLoader; public AuxiliaryServiceWithCustomClassLoader(AuxiliaryService s, ClassLoader cl) { this .wrapped = s; this .customClassLoader = cl; } ... @Override protected void serviceStart() throws Exception { callWithCustomClassLoader(wrapped.serviceStart()); } ... @Override public void initializeApplication(ApplicationInitializationContext context) { callWithCustomClassLoader(wrapper.initializeApplication(context)); } ... private callWithCustomClassLoader(...) { } } The other approach may be to abandon dealing with the Configuration.getClass() and the thread context classloader scenario, and requiring any aux service that wants to use a custom classpath NOT to do anything that will trigger Configuration.getClass() or the use of the TCCL, either directly or indirectly. Then we don't need to do all this wrapping business. What I'm not sure of is how practical this requirement would be for those aux services. Note that this has to be true even directly. I also need to point out one potential risk with this wrapping. One potential risk is that the configuration is a shared object. If one aux service resets the configuration classloader to invoke its code, any other NM code that's running concurrently could be impacted potentially. For example, if two aux services have a race (on separate threads) setting the configuration class, then we could have a nasty problem. Could you consider the implications of these options? Perhaps requiring these aux services not to do any Configuration.getClass() might not be that unreasonable... 
[![vinodkv](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Vinod Kumar Vavilapalli](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=vinodkv) added a comment - [14/Apr/16 05:57](https://issues.apache.org/jira/browse/YARN-4577?focusedCommentId=15240658&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15240658)
Just caught up with the wall of comments.
+1 in general for the ApplicationClassloader based solution. Aux-services was always a hack since Chris Douglas and I originally introduced it, the better solution is to move these services as first-class apps on top of YARN, but we are where we are.
[sjlee0](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=sjlee0),
> For example, if the aux service code depends on another class property (owned by the aux service) in the configuration, that will be invoked via Configuration.getClass(), and it will still use the system classloader to load that class. Then it's very likely that you'll get a ClassNotFoundException.
Sangjin, you may be missing one important thing here - unlike in the MapReduce case, there is no shared Configuration object between NodeManager and the specific aux-service implementation here. We simply do not pass in any configuration anywhere as part of the AuxService APIs - so this entire thread of reasoning about getClass() is no long a problem? If needed, we can document advising against adding Conf as part of future API changes.
> The thread context classloader represents another similar problem. The moment the aux service code hits a code path that does Class.forName() that loads classes via the thread context classloader, and it needs to load an aux service-related class (that is not present in the main NM classpath), you will get a ClassNotFoundException.
In addition to wrapping aux-service API calls under a class-loader, wouldn't it suffice to simply have NM make all aux-services API calls in a separate thread whose ContextClassLoader is changed to be another custom one that resolves both System classes as well as AuxServices classes?
[![vinodkv](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Vinod Kumar Vavilapalli](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=vinodkv) added a comment - [14/Apr/16 05:57](https://issues.apache.org/jira/browse/YARN-4577?focusedCommentId=15240658&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15240658) Just caught up with the wall of comments. +1 in general for the ApplicationClassloader based solution. Aux-services was always a hack since Chris Douglas and I originally introduced it, the better solution is to move these services as first-class apps on top of YARN, but we are where we are. sjlee0 , For example, if the aux service code depends on another class property (owned by the aux service) in the configuration, that will be invoked via Configuration.getClass(), and it will still use the system classloader to load that class. Then it's very likely that you'll get a ClassNotFoundException. Sangjin, you may be missing one important thing here - unlike in the MapReduce case, there is no shared Configuration object between NodeManager and the specific aux-service implementation here. We simply do not pass in any configuration anywhere as part of the AuxService APIs - so this entire thread of reasoning about getClass() is no long a problem? If needed, we can document advising against adding Conf as part of future API changes. The thread context classloader represents another similar problem. The moment the aux service code hits a code path that does Class.forName() that loads classes via the thread context classloader, and it needs to load an aux service-related class (that is not present in the main NM classpath), you will get a ClassNotFoundException. In addition to wrapping aux-service API calls under a class-loader, wouldn't it suffice to simply have NM make all aux-services API calls in a separate thread whose ContextClassLoader is changed to be another custom one that resolves both System classes as well as AuxServices classes? 
[![vinodkv](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Vinod Kumar Vavilapalli](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=vinodkv) added a comment - [15/Apr/16 20:49](https://issues.apache.org/jira/browse/YARN-4577?focusedCommentId=15243588&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15243588)
> We simply do not pass in any configuration anywhere as part of the AuxService APIs - so this entire thread of reasoning about getClass() is no long a problem?
[xgong](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=xgong) reminded me offline that we do pass a shared configuration as part of serviceInit(). In that case, the solution is simply to pass a private cloned Configuration for each of the aux-services?
[![vinodkv](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Vinod Kumar Vavilapalli](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=vinodkv) added a comment - [15/Apr/16 20:49](https://issues.apache.org/jira/browse/YARN-4577?focusedCommentId=15243588&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15243588) We simply do not pass in any configuration anywhere as part of the AuxService APIs - so this entire thread of reasoning about getClass() is no long a problem? xgong reminded me offline that we do pass a shared configuration as part of serviceInit(). In that case, the solution is simply to pass a private cloned Configuration for each of the aux-services? 
[![sjlee0](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Sangjin Lee](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=sjlee0) added a comment - [18/Apr/16 17:58](https://issues.apache.org/jira/browse/YARN-4577?focusedCommentId=15246170&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15246170)
Thanks for your comments [vinodkv](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=vinodkv).
> Xuan Gong reminded me offline that we do pass a shared configuration as part of serviceInit(). In that case, the solution is simply to pass a private cloned Configuration for each of the aux-services?
Yes, that's exactly the scenario under which an aux service gets a reference to the shared configuration. Resetting the configuration classloader on a shared configuration is a big risk.
I like your idea about creating a copy of the configuration. The only implication is that the aux services will then never see any changes made to the configuration past `serviceInit()`. I don't think that's a deal breaker. We could tweak the above code pattern I suggested to achieve this:

```
class AuxiliaryServiceWithCustomClassLoader extends AuxiliaryService {
  private final AuxiliaryService wrapped;
  private final ClassLoader customClassLoader;
  private Configuration conf;
  
  public AuxiliaryServiceWithCustomClassLoader(AuxiliaryService s, ClassLoader cl) {
    this.wrapped = s;
    this.customClassLoader = cl;
  }

  @Override
  protected void serviceInit(Configuration conf) throws Exception {
    this.conf = new Configuration(conf);
    this.conf.setClassLoader(customClassLoader);
    // call the wrapped service
    callWithCustomClassLoader(wrapped.serviceInit(this.conf));
  }
  ...
  @Override
  protected void serviceStart() throws Exception {
    callWithCustomClassLoader(wrapped.serviceStart());
  }
  ...
  @Override
  public void initializeApplication(ApplicationInitializationContext context) {
    callWithCustomClassLoader(wrapper.initializeApplication(context));
  }
  ...
  private callWithCustomClassLoader(...) {
  }
}

```

Then the only thing `callWithCustomClassLoader()` needs to deal with is setting and unsetting the thread context classloader.
> In addition to wrapping aux-service API calls under a class-loader, wouldn't it suffice to simply have NM make all aux-services API calls in a separate thread whose ContextClassLoader is changed to be another custom one that resolves both System classes as well as AuxServices classes?
If you can dedicate a thread for each aux service, that can work too. However, we need to ensure **all** calls to the aux services (**including** the `service*()` methods) are made on those threads and not on any other thread. I think that might make things more complicated than the other way around. The `callWithCustomClassLoader()` method can be very simple. All it needs to do is

```
ClassLoader original = Thread.currentThread().getContextClassLoader();
Thread.currentThread().setContextClassLoader(customClassLoader);
try {
  // the code that is being wrapped
} finally {
  Thread.currentThread().setContextClassLoader(original);
}

```

[![sjlee0](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Sangjin Lee](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=sjlee0) added a comment - [18/Apr/16 17:58](https://issues.apache.org/jira/browse/YARN-4577?focusedCommentId=15246170&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15246170) Thanks for your comments vinodkv . Xuan Gong reminded me offline that we do pass a shared configuration as part of serviceInit(). In that case, the solution is simply to pass a private cloned Configuration for each of the aux-services? Yes, that's exactly the scenario under which an aux service gets a reference to the shared configuration. Resetting the configuration classloader on a shared configuration is a big risk. I like your idea about creating a copy of the configuration. The only implication is that the aux services will then never see any changes made to the configuration past serviceInit() . I don't think that's a deal breaker. We could tweak the above code pattern I suggested to achieve this: class AuxiliaryServiceWithCustomClassLoader extends AuxiliaryService { private final AuxiliaryService wrapped; private final ClassLoader customClassLoader; private Configuration conf; public AuxiliaryServiceWithCustomClassLoader(AuxiliaryService s, ClassLoader cl) { this .wrapped = s; this .customClassLoader = cl; } @Override protected void serviceInit(Configuration conf) throws Exception { this .conf = new Configuration(conf); this .conf.setClassLoader(customClassLoader); // call the wrapped service callWithCustomClassLoader(wrapped.serviceInit( this .conf)); } ... @Override protected void serviceStart() throws Exception { callWithCustomClassLoader(wrapped.serviceStart()); } ... @Override public void initializeApplication(ApplicationInitializationContext context) { callWithCustomClassLoader(wrapper.initializeApplication(context)); } ... private callWithCustomClassLoader(...) { } } Then the only thing callWithCustomClassLoader() needs to deal with is setting and unsetting the thread context classloader. In addition to wrapping aux-service API calls under a class-loader, wouldn't it suffice to simply have NM make all aux-services API calls in a separate thread whose ContextClassLoader is changed to be another custom one that resolves both System classes as well as AuxServices classes? If you can dedicate a thread for each aux service, that can work too. However, we need to ensure all calls to the aux services ( including the service*() methods) are made on those threads and not on any other thread. I think that might make things more complicated than the other way around. The callWithCustomClassLoader() method can be very simple. All it needs to do is ClassLoader original = Thread .currentThread().getContextClassLoader(); Thread .currentThread().setContextClassLoader(customClassLoader); try { // the code that is being wrapped } finally { Thread .currentThread().setContextClassLoader(original); } 
[![sjlee0](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Sangjin Lee](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=sjlee0) added a comment - [18/Apr/16 17:59](https://issues.apache.org/jira/browse/YARN-4577?focusedCommentId=15246173&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15246173)
I think the above should be a viable solution that addresses all types of classloading.
[![sjlee0](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Sangjin Lee](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=sjlee0) added a comment - [18/Apr/16 17:59](https://issues.apache.org/jira/browse/YARN-4577?focusedCommentId=15246173&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15246173) I think the above should be a viable solution that addresses all types of classloading. 
[![xgong](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10443) Xuan Gong](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=xgong) added a comment - [21/Apr/16 03:43](https://issues.apache.org/jira/browse/YARN-4577?focusedCommentId=15251193&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15251193)
[sjlee0](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=sjlee0) Thanks for the suggestion. I have uploaded a poc patch for this. Could you take a look, please ?
[![xgong](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10443) Xuan Gong](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=xgong) added a comment - [21/Apr/16 03:43](https://issues.apache.org/jira/browse/YARN-4577?focusedCommentId=15251193&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15251193) sjlee0 Thanks for the suggestion. I have uploaded a poc patch for this. Could you take a look, please ? 
[![hadoopqa](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Hadoop QA](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=hadoopqa) added a comment - [21/Apr/16 04:55](https://issues.apache.org/jira/browse/YARN-4577?focusedCommentId=15251266&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15251266)  
|  ![](https://issues.apache.org/jira/images/icons/emoticons/error.png) **-1 overall**  |  
| --- |  
  
  
  
|  Vote   |  Subsystem   |  Runtime   |  Comment   |  
| --- | --- | --- | --- |  
|  0  |  reexec   |  0m 11s   |  Docker mode activated.   |  
|  +1  |  @author   |  0m 0s   |  The patch does not contain any @author tags.   |  
|  -1  |  test4tests   |  0m 0s   |  The patch doesn't appear to include any new or modified tests. Please justify why no new tests are needed for this patch. Also please list what manual steps were performed to verify this patch.   |  
|  0  |  mvndep   |  0m 20s   |  Maven dependency ordering for branch   |  
|  +1  |  mvninstall   |  6m 57s   |  trunk passed   |  
|  +1  |  compile   |  1m 50s   |  trunk passed with JDK v1.8.0_77   |  
|  +1  |  compile   |  2m 6s   |  trunk passed with JDK v1.7.0_95   |  
|  +1  |  checkstyle   |  0m 37s   |  trunk passed   |  
|  +1  |  mvnsite   |  0m 55s   |  trunk passed   |  
|  +1  |  mvneclipse   |  0m 25s   |  trunk passed   |  
|  +1  |  findbugs   |  2m 3s   |  trunk passed   |  
|  +1  |  javadoc   |  0m 57s   |  trunk passed with JDK v1.8.0_77   |  
|  +1  |  javadoc   |  3m 16s   |  trunk passed with JDK v1.7.0_95   |  
|  0  |  mvndep   |  0m 10s   |  Maven dependency ordering for patch   |  
|  +1  |  mvninstall   |  0m 46s   |  the patch passed   |  
|  +1  |  compile   |  1m 50s   |  the patch passed with JDK v1.8.0_77   |  
|  -1  |  javac   |  2m 46s   |  hadoop-yarn-project_hadoop-yarn-jdk1.8.0_77 with JDK v1.8.0_77 generated 1 new + 22 unchanged - 0 fixed = 23 total (was 22)   |  
|  +1  |  javac   |  1m 50s   |  the patch passed   |  
|  +1  |  compile   |  2m 7s   |  the patch passed with JDK v1.7.0_95   |  
|  -1  |  javac   |  4m 53s   |  hadoop-yarn-project_hadoop-yarn-jdk1.7.0_95 with JDK v1.7.0_95 generated 1 new + 25 unchanged - 0 fixed = 26 total (was 25)   |  
|  +1  |  javac   |  2m 7s   |  the patch passed   |  
|  -1  |  checkstyle   |  0m 35s   |  hadoop-yarn-project/hadoop-yarn: patch generated 2 new + 261 unchanged - 0 fixed = 263 total (was 261)   |  
|  +1  |  mvnsite   |  0m 52s   |  the patch passed   |  
|  +1  |  mvneclipse   |  0m 20s   |  the patch passed   |  
|  +1  |  whitespace   |  0m 0s   |  Patch has no whitespace issues.   |  
|  -1  |  findbugs   |  1m 4s   |  hadoop-yarn-project/hadoop-yarn/hadoop-yarn-server/hadoop-yarn-server-nodemanager generated 1 new + 0 unchanged - 0 fixed = 1 total (was 0)   |  
|  +1  |  javadoc   |  0m 53s   |  the patch passed with JDK v1.8.0_77   |  
|  +1  |  javadoc   |  3m 21s   |  the patch passed with JDK v1.7.0_95   |  
|  +1  |  unit   |  0m 22s   |  hadoop-yarn-api in the patch passed with JDK v1.8.0_77.   |  
|  +1  |  unit   |  11m 2s   |  hadoop-yarn-server-nodemanager in the patch passed with JDK v1.8.0_77.   |  
|  +1  |  unit   |  0m 23s   |  hadoop-yarn-api in the patch passed with JDK v1.7.0_95.   |  
|  +1  |  unit   |  11m 33s   |  hadoop-yarn-server-nodemanager in the patch passed with JDK v1.7.0_95.   |  
|  +1  |  asflicense   |  0m 19s   |  Patch does not generate ASF License warnings.   |  
|   |   |  57m 49s   |   |  
  
  
  
|  Reason   |  Tests   |  
| --- | --- |  
|  FindBugs   |  module:hadoop-yarn-project/hadoop-yarn/hadoop-yarn-server/hadoop-yarn-server-nodemanager   |  
|   |  org.apache.hadoop.yarn.server.nodemanager.containermanager.AuxServices.serviceInit(Configuration) creates a org.apache.hadoop.util.ApplicationClassLoader classloader, which should be performed within a doPrivileged block At AuxServices.java:which should be performed within a doPrivileged block At AuxServices.java:[line 133]  |  
  
  
  
|  Subsystem   |  Report/Notes   |  
| --- | --- |  
|  Docker   |  Image:yetus/hadoop:fbe3e86   |  
|  JIRA Patch URL   |  <https://issues.apache.org/jira/secure/attachment/12799895/YARN-4577.poc.patch>  |  
|  JIRA Issue   |  [~~YARN-4577~~](https://issues.apache.org/jira/browse/YARN-4577 "Enable aux services to have their own custom classpath/jar file")  |  
|  Optional Tests   |  asflicense compile javac javadoc mvninstall mvnsite unit findbugs checkstyle   |  
|  uname   |  Linux 5189f947e974 3.13.0-36-lowlatency #63-Ubuntu SMP PREEMPT Wed Sep 3 21:56:12 UTC 2014 x86_64 x86_64 x86_64 GNU/Linux   |  
|  Build tool   |  maven   |  
|  Personality   |  /testptch/hadoop/patchprocess/precommit/personality/provided.sh   |  
|  git revision   |  trunk / 1e48eef   |  
|  Default Java   |  1.7.0_95   |  
|  Multi-JDK versions   |  /usr/lib/jvm/java-8-oracle:1.8.0_77 /usr/lib/jvm/java-7-openjdk-amd64:1.7.0_95   |  
|  findbugs   |  v3.0.0   |  
|  javac   |  hadoop-yarn-project_hadoop-yarn-jdk1.8.0_77: <https://builds.apache.org/job/PreCommit-YARN-Build/11153/artifact/patchprocess/diff-compile-javac-hadoop-yarn-project_hadoop-yarn-jdk1.8.0_77.txt>  |  
|  javac   |  hadoop-yarn-project_hadoop-yarn-jdk1.7.0_95: <https://builds.apache.org/job/PreCommit-YARN-Build/11153/artifact/patchprocess/diff-compile-javac-hadoop-yarn-project_hadoop-yarn-jdk1.7.0_95.txt>  |  
|  checkstyle   |  <https://builds.apache.org/job/PreCommit-YARN-Build/11153/artifact/patchprocess/diff-checkstyle-hadoop-yarn-project_hadoop-yarn.txt>  |  
|  findbugs   |  <https://builds.apache.org/job/PreCommit-YARN-Build/11153/artifact/patchprocess/new-findbugs-hadoop-yarn-project_hadoop-yarn_hadoop-yarn-server_hadoop-yarn-server-nodemanager.html>  |  
|  JDK v1.7.0_95 Test Results   |  <https://builds.apache.org/job/PreCommit-YARN-Build/11153/testReport/>  |  
|  modules   |  C: hadoop-yarn-project/hadoop-yarn/hadoop-yarn-api hadoop-yarn-project/hadoop-yarn/hadoop-yarn-server/hadoop-yarn-server-nodemanager U: hadoop-yarn-project/hadoop-yarn   |  
|  Console output   |  <https://builds.apache.org/job/PreCommit-YARN-Build/11153/console>  |  
|  Powered by   |  Apache Yetus 0.2.0 <http://yetus.apache.org>  |  
This message was automatically generated.
[![hadoopqa](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Hadoop QA](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=hadoopqa) added a comment - [21/Apr/16 04:55](https://issues.apache.org/jira/browse/YARN-4577?focusedCommentId=15251266&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15251266) -1 overall Vote Subsystem Runtime Comment 0 reexec 0m 11s Docker mode activated. +1 @author 0m 0s The patch does not contain any @author tags. -1 test4tests 0m 0s The patch doesn't appear to include any new or modified tests. Please justify why no new tests are needed for this patch. Also please list what manual steps were performed to verify this patch. 0 mvndep 0m 20s Maven dependency ordering for branch +1 mvninstall 6m 57s trunk passed +1 compile 1m 50s trunk passed with JDK v1.8.0_77 +1 compile 2m 6s trunk passed with JDK v1.7.0_95 +1 checkstyle 0m 37s trunk passed +1 mvnsite 0m 55s trunk passed +1 mvneclipse 0m 25s trunk passed +1 findbugs 2m 3s trunk passed +1 javadoc 0m 57s trunk passed with JDK v1.8.0_77 +1 javadoc 3m 16s trunk passed with JDK v1.7.0_95 0 mvndep 0m 10s Maven dependency ordering for patch +1 mvninstall 0m 46s the patch passed +1 compile 1m 50s the patch passed with JDK v1.8.0_77 -1 javac 2m 46s hadoop-yarn-project_hadoop-yarn-jdk1.8.0_77 with JDK v1.8.0_77 generated 1 new + 22 unchanged - 0 fixed = 23 total (was 22) +1 javac 1m 50s the patch passed +1 compile 2m 7s the patch passed with JDK v1.7.0_95 -1 javac 4m 53s hadoop-yarn-project_hadoop-yarn-jdk1.7.0_95 with JDK v1.7.0_95 generated 1 new + 25 unchanged - 0 fixed = 26 total (was 25) +1 javac 2m 7s the patch passed -1 checkstyle 0m 35s hadoop-yarn-project/hadoop-yarn: patch generated 2 new + 261 unchanged - 0 fixed = 263 total (was 261) +1 mvnsite 0m 52s the patch passed +1 mvneclipse 0m 20s the patch passed +1 whitespace 0m 0s Patch has no whitespace issues. -1 findbugs 1m 4s hadoop-yarn-project/hadoop-yarn/hadoop-yarn-server/hadoop-yarn-server-nodemanager generated 1 new + 0 unchanged - 0 fixed = 1 total (was 0) +1 javadoc 0m 53s the patch passed with JDK v1.8.0_77 +1 javadoc 3m 21s the patch passed with JDK v1.7.0_95 +1 unit 0m 22s hadoop-yarn-api in the patch passed with JDK v1.8.0_77. +1 unit 11m 2s hadoop-yarn-server-nodemanager in the patch passed with JDK v1.8.0_77. +1 unit 0m 23s hadoop-yarn-api in the patch passed with JDK v1.7.0_95. +1 unit 11m 33s hadoop-yarn-server-nodemanager in the patch passed with JDK v1.7.0_95. +1 asflicense 0m 19s Patch does not generate ASF License warnings. 57m 49s Reason Tests FindBugs module:hadoop-yarn-project/hadoop-yarn/hadoop-yarn-server/hadoop-yarn-server-nodemanager org.apache.hadoop.yarn.server.nodemanager.containermanager.AuxServices.serviceInit(Configuration) creates a org.apache.hadoop.util.ApplicationClassLoader classloader, which should be performed within a doPrivileged block At AuxServices.java:which should be performed within a doPrivileged block At AuxServices.java: [line 133] Subsystem Report/Notes Docker Image:yetus/hadoop:fbe3e86 JIRA Patch URL https://issues.apache.org/jira/secure/attachment/12799895/YARN-4577.poc.patch JIRA Issue YARN-4577 Optional Tests asflicense compile javac javadoc mvninstall mvnsite unit findbugs checkstyle uname Linux 5189f947e974 3.13.0-36-lowlatency #63-Ubuntu SMP PREEMPT Wed Sep 3 21:56:12 UTC 2014 x86_64 x86_64 x86_64 GNU/Linux Build tool maven Personality /testptch/hadoop/patchprocess/precommit/personality/provided.sh git revision trunk / 1e48eef Default Java 1.7.0_95 Multi-JDK versions /usr/lib/jvm/java-8-oracle:1.8.0_77 /usr/lib/jvm/java-7-openjdk-amd64:1.7.0_95 findbugs v3.0.0 javac hadoop-yarn-project_hadoop-yarn-jdk1.8.0_77: https://builds.apache.org/job/PreCommit-YARN-Build/11153/artifact/patchprocess/diff-compile-javac-hadoop-yarn-project_hadoop-yarn-jdk1.8.0_77.txt javac hadoop-yarn-project_hadoop-yarn-jdk1.7.0_95: https://builds.apache.org/job/PreCommit-YARN-Build/11153/artifact/patchprocess/diff-compile-javac-hadoop-yarn-project_hadoop-yarn-jdk1.7.0_95.txt checkstyle https://builds.apache.org/job/PreCommit-YARN-Build/11153/artifact/patchprocess/diff-checkstyle-hadoop-yarn-project_hadoop-yarn.txt findbugs https://builds.apache.org/job/PreCommit-YARN-Build/11153/artifact/patchprocess/new-findbugs-hadoop-yarn-project_hadoop-yarn_hadoop-yarn-server_hadoop-yarn-server-nodemanager.html JDK v1.7.0_95 Test Results https://builds.apache.org/job/PreCommit-YARN-Build/11153/testReport/ modules C: hadoop-yarn-project/hadoop-yarn/hadoop-yarn-api hadoop-yarn-project/hadoop-yarn/hadoop-yarn-server/hadoop-yarn-server-nodemanager U: hadoop-yarn-project/hadoop-yarn Console output https://builds.apache.org/job/PreCommit-YARN-Build/11153/console Powered by Apache Yetus 0.2.0 http://yetus.apache.org This message was automatically generated. 
[![sjlee0](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Sangjin Lee](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=sjlee0) added a comment - [22/Apr/16 00:59](https://issues.apache.org/jira/browse/YARN-4577?focusedCommentId=15253112&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15253112)
Yes I think the POC patch is pretty close to what I had in mind too.
A couple of more minor suggestions:
  * I probably wouldn't make `AuxServiceWithCustomClassLoader` public. It should be really visible only to `AuxServices`. Package scope should be fine.
  * I understand `callWithCustomClassLoader()` is bit complicated because it has to support methods with different signatures. I would simply inline the code (as you are doing with `service*()` methods). Then you don't have to do any reflection business to do this.


Don't forget to test it with a real-life use case! Thanks.
[![sjlee0](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Sangjin Lee](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=sjlee0) added a comment - [22/Apr/16 00:59](https://issues.apache.org/jira/browse/YARN-4577?focusedCommentId=15253112&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15253112) Yes I think the POC patch is pretty close to what I had in mind too. A couple of more minor suggestions: I probably wouldn't make AuxServiceWithCustomClassLoader public. It should be really visible only to AuxServices . Package scope should be fine. I understand callWithCustomClassLoader() is bit complicated because it has to support methods with different signatures. I would simply inline the code (as you are doing with service*() methods). Then you don't have to do any reflection business to do this. Don't forget to test it with a real-life use case! Thanks. 
[![hadoopqa](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Hadoop QA](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=hadoopqa) added a comment - [27/Apr/16 17:49](https://issues.apache.org/jira/browse/YARN-4577?focusedCommentId=15260589&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15260589)  
|  ![](https://issues.apache.org/jira/images/icons/emoticons/error.png) **-1 overall**  |  
| --- |  
  
  
  
|  Vote   |  Subsystem   |  Runtime   |  Comment   |  
| --- | --- | --- | --- |  
|  0  |  reexec   |  0m 0s   |  Docker mode activated.   |  
|  -1  |  docker   |  0m 2s   |  Docker failed to build yetus/hadoop:7b1c37a.   |  
  
  
  
|  Subsystem   |  Report/Notes   |  
| --- | --- |  
|  JIRA Patch URL   |  <https://issues.apache.org/jira/secure/attachment/12801074/YARN-4577.5.patch>  |  
|  JIRA Issue   |  [~~YARN-4577~~](https://issues.apache.org/jira/browse/YARN-4577 "Enable aux services to have their own custom classpath/jar file")  |  
|  Console output   |  <https://builds.apache.org/job/PreCommit-YARN-Build/11242/console>  |  
|  Powered by   |  Apache Yetus 0.2.0 <http://yetus.apache.org>  |  
This message was automatically generated.
[![hadoopqa](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Hadoop QA](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=hadoopqa) added a comment - [27/Apr/16 17:49](https://issues.apache.org/jira/browse/YARN-4577?focusedCommentId=15260589&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15260589) -1 overall Vote Subsystem Runtime Comment 0 reexec 0m 0s Docker mode activated. -1 docker 0m 2s Docker failed to build yetus/hadoop:7b1c37a. Subsystem Report/Notes JIRA Patch URL https://issues.apache.org/jira/secure/attachment/12801074/YARN-4577.5.patch JIRA Issue YARN-4577 Console output https://builds.apache.org/job/PreCommit-YARN-Build/11242/console Powered by Apache Yetus 0.2.0 http://yetus.apache.org This message was automatically generated. 
[![xgong](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10443) Xuan Gong](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=xgong) added a comment - [27/Apr/16 17:55](https://issues.apache.org/jira/browse/YARN-4577?focusedCommentId=15260609&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15260609)
[sjlee0](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=sjlee0) Thanks for the review.
Attached a new patch to address the comments.
Unfortunately, I am not able to create a unit test for this. But I did test it manually.
Here is how I test it:  
1. Create a customized TestAuxService which extends AuxiliaryService.  
2. Create two jar file which have the same jar file name: TestAuxSerivce.jar and have the same class name: TestAuxService.java  
3. Each TestAuxService.java has different log message. something like "TestAuxService in NM ClassPath" and "TestAuxService in Customer ClassPath"  
4. Put one TestAuxService.jar into NM ClassPath, and put another TestAuxService.jar into customer class path, such as "/Users/xuan/dep/TestAuxService.jar"  
5. modify several configuration in YARN-SITE.XML

```
    <property>
        <name>yarn.nodemanager.aux-services</name>
        <value>mapreduce_shuffle,TestAuxService</value>
        <description>shuffle service that needs to be set for Map Reduce to run </description>
    </property>

  <property>
      <name>yarn.nodemanager.aux-services.TestAuxService.class&lt;/name>
      <value>org.aux.TestAuxService</value>
  </property>

```

6. start NM, and verified the log message in NM logs, we can see

```
Test My AuxService in NM ClassPath in Service Init stage
Test My AuxService in NM ClassPath in Service Start stage

```

And we can verify that we load the TestAuxService class from NM Class Path  
7. add one more configuration into yarn-site.xml

```
    <property>
        <name>yarn.nodemanager.aux-services.TestAuxService.class.classpath</name>
        <value>/Users/xuan/dep/TestAuxService.jar</value>
    </property>

```

8. Start NM, and check log message in NM log, we can find 

```
Test My AuxService in Customer ClassPath in Service Init stage
Test My AuxService in Customer ClassPath in Service Start stage

```

we can verify that if we set the customer class path, we would load TestAuxService from customer class path instead of NM classpath.
[![xgong](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10443) Xuan Gong](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=xgong) added a comment - [27/Apr/16 17:55](https://issues.apache.org/jira/browse/YARN-4577?focusedCommentId=15260609&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15260609) sjlee0 Thanks for the review. Attached a new patch to address the comments. Unfortunately, I am not able to create a unit test for this. But I did test it manually. Here is how I test it: 1. Create a customized TestAuxService which extends AuxiliaryService. 2. Create two jar file which have the same jar file name: TestAuxSerivce.jar and have the same class name: TestAuxService.java 3. Each TestAuxService.java has different log message. something like "TestAuxService in NM ClassPath" and "TestAuxService in Customer ClassPath" 4. Put one TestAuxService.jar into NM ClassPath, and put another TestAuxService.jar into customer class path, such as "/Users/xuan/dep/TestAuxService.jar" 5. modify several configuration in YARN-SITE.XML <property> <name>yarn.nodemanager.aux-services</name> <value>mapreduce_shuffle,TestAuxService</value> <description>shuffle service that needs to be set for Map Reduce to run </description> </property> <property> <name>yarn.nodemanager.aux-services.TestAuxService. class& lt;/name> <value>org.aux.TestAuxService</value> </property> 6. start NM, and verified the log message in NM logs, we can see Test My AuxService in NM ClassPath in Service Init stage Test My AuxService in NM ClassPath in Service Start stage And we can verify that we load the TestAuxService class from NM Class Path 7. add one more configuration into yarn-site.xml <property> <name>yarn.nodemanager.aux-services.TestAuxService. class. classpath</name> <value>/Users/xuan/dep/TestAuxService.jar</value> </property> 8. Start NM, and check log message in NM log, we can find Test My AuxService in Customer ClassPath in Service Init stage Test My AuxService in Customer ClassPath in Service Start stage we can verify that if we set the customer class path, we would load TestAuxService from customer class path instead of NM classpath. 
[![hadoopqa](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Hadoop QA](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=hadoopqa) added a comment - [27/Apr/16 17:58](https://issues.apache.org/jira/browse/YARN-4577?focusedCommentId=15260614&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15260614)  
|  ![](https://issues.apache.org/jira/images/icons/emoticons/error.png) **-1 overall**  |  
| --- |  
  
  
  
|  Vote   |  Subsystem   |  Runtime   |  Comment   |  
| --- | --- | --- | --- |  
|  0  |  reexec   |  0m 0s   |  Docker mode activated.   |  
|  -1  |  docker   |  0m 4s   |  Docker failed to build yetus/hadoop:7b1c37a.   |  
  
  
  
|  Subsystem   |  Report/Notes   |  
| --- | --- |  
|  JIRA Patch URL   |  <https://issues.apache.org/jira/secure/attachment/12801074/YARN-4577.5.patch>  |  
|  JIRA Issue   |  [~~YARN-4577~~](https://issues.apache.org/jira/browse/YARN-4577 "Enable aux services to have their own custom classpath/jar file")  |  
|  Console output   |  <https://builds.apache.org/job/PreCommit-YARN-Build/11244/console>  |  
|  Powered by   |  Apache Yetus 0.2.0 <http://yetus.apache.org>  |  
This message was automatically generated.
[![hadoopqa](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Hadoop QA](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=hadoopqa) added a comment - [27/Apr/16 17:58](https://issues.apache.org/jira/browse/YARN-4577?focusedCommentId=15260614&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15260614) -1 overall Vote Subsystem Runtime Comment 0 reexec 0m 0s Docker mode activated. -1 docker 0m 4s Docker failed to build yetus/hadoop:7b1c37a. Subsystem Report/Notes JIRA Patch URL https://issues.apache.org/jira/secure/attachment/12801074/YARN-4577.5.patch JIRA Issue YARN-4577 Console output https://builds.apache.org/job/PreCommit-YARN-Build/11244/console Powered by Apache Yetus 0.2.0 http://yetus.apache.org This message was automatically generated. 
[![hadoopqa](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Hadoop QA](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=hadoopqa) added a comment - [29/Apr/16 00:20](https://issues.apache.org/jira/browse/YARN-4577?focusedCommentId=15263309&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15263309)  
|  ![](https://issues.apache.org/jira/images/icons/emoticons/error.png) **-1 overall**  |  
| --- |  
  
  
  
|  Vote   |  Subsystem   |  Runtime   |  Comment   |  
| --- | --- | --- | --- |  
|  0  |  reexec   |  0m 19s   |  Docker mode activated.   |  
|  +1  |  @author   |  0m 0s   |  The patch does not contain any @author tags.   |  
|  -1  |  test4tests   |  0m 0s   |  The patch doesn't appear to include any new or modified tests. Please justify why no new tests are needed for this patch. Also please list what manual steps were performed to verify this patch.   |  
|  0  |  mvndep   |  0m 11s   |  Maven dependency ordering for branch   |  
|  +1  |  mvninstall   |  8m 20s   |  trunk passed   |  
|  +1  |  compile   |  2m 52s   |  trunk passed with JDK v1.8.0_92   |  
|  +1  |  compile   |  2m 46s   |  trunk passed with JDK v1.7.0_95   |  
|  +1  |  checkstyle   |  0m 40s   |  trunk passed   |  
|  +1  |  mvnsite   |  1m 6s   |  trunk passed   |  
|  +1  |  mvneclipse   |  0m 27s   |  trunk passed   |  
|  +1  |  findbugs   |  2m 26s   |  trunk passed   |  
|  +1  |  javadoc   |  1m 20s   |  trunk passed with JDK v1.8.0_92   |  
|  +1  |  javadoc   |  3m 26s   |  trunk passed with JDK v1.7.0_95   |  
|  0  |  mvndep   |  0m 11s   |  Maven dependency ordering for patch   |  
|  +1  |  mvninstall   |  1m 0s   |  the patch passed   |  
|  +1  |  compile   |  3m 35s   |  the patch passed with JDK v1.8.0_92   |  
|  +1  |  javac   |  3m 35s   |  the patch passed   |  
|  +1  |  compile   |  2m 47s   |  the patch passed with JDK v1.7.0_95   |  
|  +1  |  javac   |  2m 47s   |  the patch passed   |  
|  -1  |  checkstyle   |  0m 39s   |  hadoop-yarn-project/hadoop-yarn: patch generated 1 new + 263 unchanged - 0 fixed = 264 total (was 263)   |  
|  +1  |  mvnsite   |  1m 5s   |  the patch passed   |  
|  +1  |  mvneclipse   |  0m 26s   |  the patch passed   |  
|  +1  |  whitespace   |  0m 0s   |  Patch has no whitespace issues.   |  
|  -1  |  findbugs   |  1m 23s   |  hadoop-yarn-project/hadoop-yarn/hadoop-yarn-server/hadoop-yarn-server-nodemanager generated 1 new + 0 unchanged - 0 fixed = 1 total (was 0)   |  
|  +1  |  javadoc   |  1m 26s   |  the patch passed with JDK v1.8.0_92   |  
|  +1  |  javadoc   |  3m 23s   |  the patch passed with JDK v1.7.0_95   |  
|  +1  |  unit   |  0m 37s   |  hadoop-yarn-api in the patch passed with JDK v1.8.0_92.   |  
|  +1  |  unit   |  12m 43s   |  hadoop-yarn-server-nodemanager in the patch passed with JDK v1.8.0_92.   |  
|  +1  |  unit   |  0m 30s   |  hadoop-yarn-api in the patch passed with JDK v1.7.0_95.   |  
|  +1  |  unit   |  12m 28s   |  hadoop-yarn-server-nodemanager in the patch passed with JDK v1.7.0_95.   |  
|  +1  |  asflicense   |  0m 25s   |  Patch does not generate ASF License warnings.   |  
|   |   |  69m 51s   |   |  
  
  
  
|  Reason   |  Tests   |  
| --- | --- |  
|  FindBugs   |  module:hadoop-yarn-project/hadoop-yarn/hadoop-yarn-server/hadoop-yarn-server-nodemanager   |  
|   |  org.apache.hadoop.yarn.server.nodemanager.containermanager.AuxServices.serviceInit(Configuration) creates a org.apache.hadoop.util.ApplicationClassLoader classloader, which should be performed within a doPrivileged block At AuxServices.java:which should be performed within a doPrivileged block At AuxServices.java:[line 132]  |  
  
  
  
|  Subsystem   |  Report/Notes   |  
| --- | --- |  
|  Docker   |  Image:yetus/hadoop:cf2ee45   |  
|  JIRA Patch URL   |  <https://issues.apache.org/jira/secure/attachment/12801074/YARN-4577.5.patch>  |  
|  JIRA Issue   |  [~~YARN-4577~~](https://issues.apache.org/jira/browse/YARN-4577 "Enable aux services to have their own custom classpath/jar file")  |  
|  Optional Tests   |  asflicense compile javac javadoc mvninstall mvnsite unit findbugs checkstyle   |  
|  uname   |  Linux a23f8d9763a7 3.13.0-36-lowlatency #63-Ubuntu SMP PREEMPT Wed Sep 3 21:56:12 UTC 2014 x86_64 x86_64 x86_64 GNU/Linux   |  
|  Build tool   |  maven   |  
|  Personality   |  /testptch/hadoop/patchprocess/precommit/personality/provided.sh   |  
|  git revision   |  trunk / 6243eab   |  
|  Default Java   |  1.7.0_95   |  
|  Multi-JDK versions   |  /usr/lib/jvm/java-8-oracle:1.8.0_92 /usr/lib/jvm/java-7-openjdk-amd64:1.7.0_95   |  
|  findbugs   |  v3.0.0   |  
|  checkstyle   |  <https://builds.apache.org/job/PreCommit-YARN-Build/11276/artifact/patchprocess/diff-checkstyle-hadoop-yarn-project_hadoop-yarn.txt>  |  
|  findbugs   |  <https://builds.apache.org/job/PreCommit-YARN-Build/11276/artifact/patchprocess/new-findbugs-hadoop-yarn-project_hadoop-yarn_hadoop-yarn-server_hadoop-yarn-server-nodemanager.html>  |  
|  JDK v1.7.0_95 Test Results   |  <https://builds.apache.org/job/PreCommit-YARN-Build/11276/testReport/>  |  
|  modules   |  C: hadoop-yarn-project/hadoop-yarn/hadoop-yarn-api hadoop-yarn-project/hadoop-yarn/hadoop-yarn-server/hadoop-yarn-server-nodemanager U: hadoop-yarn-project/hadoop-yarn   |  
|  Console output   |  <https://builds.apache.org/job/PreCommit-YARN-Build/11276/console>  |  
|  Powered by   |  Apache Yetus 0.2.0 <http://yetus.apache.org>  |  
This message was automatically generated.
[![hadoopqa](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Hadoop QA](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=hadoopqa) added a comment - [29/Apr/16 00:20](https://issues.apache.org/jira/browse/YARN-4577?focusedCommentId=15263309&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15263309) -1 overall Vote Subsystem Runtime Comment 0 reexec 0m 19s Docker mode activated. +1 @author 0m 0s The patch does not contain any @author tags. -1 test4tests 0m 0s The patch doesn't appear to include any new or modified tests. Please justify why no new tests are needed for this patch. Also please list what manual steps were performed to verify this patch. 0 mvndep 0m 11s Maven dependency ordering for branch +1 mvninstall 8m 20s trunk passed +1 compile 2m 52s trunk passed with JDK v1.8.0_92 +1 compile 2m 46s trunk passed with JDK v1.7.0_95 +1 checkstyle 0m 40s trunk passed +1 mvnsite 1m 6s trunk passed +1 mvneclipse 0m 27s trunk passed +1 findbugs 2m 26s trunk passed +1 javadoc 1m 20s trunk passed with JDK v1.8.0_92 +1 javadoc 3m 26s trunk passed with JDK v1.7.0_95 0 mvndep 0m 11s Maven dependency ordering for patch +1 mvninstall 1m 0s the patch passed +1 compile 3m 35s the patch passed with JDK v1.8.0_92 +1 javac 3m 35s the patch passed +1 compile 2m 47s the patch passed with JDK v1.7.0_95 +1 javac 2m 47s the patch passed -1 checkstyle 0m 39s hadoop-yarn-project/hadoop-yarn: patch generated 1 new + 263 unchanged - 0 fixed = 264 total (was 263) +1 mvnsite 1m 5s the patch passed +1 mvneclipse 0m 26s the patch passed +1 whitespace 0m 0s Patch has no whitespace issues. -1 findbugs 1m 23s hadoop-yarn-project/hadoop-yarn/hadoop-yarn-server/hadoop-yarn-server-nodemanager generated 1 new + 0 unchanged - 0 fixed = 1 total (was 0) +1 javadoc 1m 26s the patch passed with JDK v1.8.0_92 +1 javadoc 3m 23s the patch passed with JDK v1.7.0_95 +1 unit 0m 37s hadoop-yarn-api in the patch passed with JDK v1.8.0_92. +1 unit 12m 43s hadoop-yarn-server-nodemanager in the patch passed with JDK v1.8.0_92. +1 unit 0m 30s hadoop-yarn-api in the patch passed with JDK v1.7.0_95. +1 unit 12m 28s hadoop-yarn-server-nodemanager in the patch passed with JDK v1.7.0_95. +1 asflicense 0m 25s Patch does not generate ASF License warnings. 69m 51s Reason Tests FindBugs module:hadoop-yarn-project/hadoop-yarn/hadoop-yarn-server/hadoop-yarn-server-nodemanager org.apache.hadoop.yarn.server.nodemanager.containermanager.AuxServices.serviceInit(Configuration) creates a org.apache.hadoop.util.ApplicationClassLoader classloader, which should be performed within a doPrivileged block At AuxServices.java:which should be performed within a doPrivileged block At AuxServices.java: [line 132] Subsystem Report/Notes Docker Image:yetus/hadoop:cf2ee45 JIRA Patch URL https://issues.apache.org/jira/secure/attachment/12801074/YARN-4577.5.patch JIRA Issue YARN-4577 Optional Tests asflicense compile javac javadoc mvninstall mvnsite unit findbugs checkstyle uname Linux a23f8d9763a7 3.13.0-36-lowlatency #63-Ubuntu SMP PREEMPT Wed Sep 3 21:56:12 UTC 2014 x86_64 x86_64 x86_64 GNU/Linux Build tool maven Personality /testptch/hadoop/patchprocess/precommit/personality/provided.sh git revision trunk / 6243eab Default Java 1.7.0_95 Multi-JDK versions /usr/lib/jvm/java-8-oracle:1.8.0_92 /usr/lib/jvm/java-7-openjdk-amd64:1.7.0_95 findbugs v3.0.0 checkstyle https://builds.apache.org/job/PreCommit-YARN-Build/11276/artifact/patchprocess/diff-checkstyle-hadoop-yarn-project_hadoop-yarn.txt findbugs https://builds.apache.org/job/PreCommit-YARN-Build/11276/artifact/patchprocess/new-findbugs-hadoop-yarn-project_hadoop-yarn_hadoop-yarn-server_hadoop-yarn-server-nodemanager.html JDK v1.7.0_95 Test Results https://builds.apache.org/job/PreCommit-YARN-Build/11276/testReport/ modules C: hadoop-yarn-project/hadoop-yarn/hadoop-yarn-api hadoop-yarn-project/hadoop-yarn/hadoop-yarn-server/hadoop-yarn-server-nodemanager U: hadoop-yarn-project/hadoop-yarn Console output https://builds.apache.org/job/PreCommit-YARN-Build/11276/console Powered by Apache Yetus 0.2.0 http://yetus.apache.org This message was automatically generated. 
[![sjlee0](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Sangjin Lee](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=sjlee0) added a comment - [29/Apr/16 00:41](https://issues.apache.org/jira/browse/YARN-4577?focusedCommentId=15263335&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15263335)
Would you be able to come up with a unit test still? I know it's somewhat tricky, but you might be able to find a way to test a few things. You might want to take a look at `TestRunJar.testClientClassLoader()` to see if you can reuse some of the ideas there.
Coupled with the unit test strategy, you might want to consider supporting some type of an override mechanism for system classes. Other use cases of `ApplicationClassLoader` provide this (although it's case by case). If users ever run into a classloading issue which can be fixed by a small modification to the system classes, providing the override mechanism would be a big win. And it might come in handy in writing unit tests too.
Also, please take a look at the checkstyle and findbug issues.
(AuxServices.java)
  * l.132: some INFO level logging here would be helpful (like the name of the aux service that's using the custom classloader, etc.)
  * l.146: I know it's existing code, but the C-style equal check is not necessary with java. I would simply go with `sClass == null`.
  * l.160: same as above.


(AuxiliaryServiceWithCustomClassLoader.java)
  * in `serviceInit()`, `serviceStart()`, `serviceStop()`, shouldn't we call `wrapped.serviceInit()` instead of `wrapper.init()`, and so on?
  * l.46: We might want to change this a little. It appears `AbstractService.init()` already sets the configuration (with the original configuration) before `AuxiliaryServiceWithCustomClassLoader.serviceInit()` is invoked. This may lead to confusion down the road. Let's reset the configuration here via `setConfig()`. In other words, 

```
@Override
protected void serviceInit(Configuration conf) throws Exception {
  Configuration config = new Configuration(conf);
  // reset the service configuration
  setConfig(config);
  config.setClassLoader(customClassLoader);
  ClassLoader original = Thread.currentThread().getContextClassLoader();
  Thread.currentThread().setContextClassLoader(customClassLoader);
  try {
    wrapped.serviceInit(config);
  } finally {
    Thread.currentThread().setContextClassLoader(original);
  }
}

```

Also, I don't think we need `Configuration` as a member variable.


[![sjlee0](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Sangjin Lee](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=sjlee0) added a comment - [29/Apr/16 00:41](https://issues.apache.org/jira/browse/YARN-4577?focusedCommentId=15263335&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15263335) Would you be able to come up with a unit test still? I know it's somewhat tricky, but you might be able to find a way to test a few things. You might want to take a look at TestRunJar.testClientClassLoader() to see if you can reuse some of the ideas there. Coupled with the unit test strategy, you might want to consider supporting some type of an override mechanism for system classes. Other use cases of ApplicationClassLoader provide this (although it's case by case). If users ever run into a classloading issue which can be fixed by a small modification to the system classes, providing the override mechanism would be a big win. And it might come in handy in writing unit tests too. Also, please take a look at the checkstyle and findbug issues. (AuxServices.java) l.132: some INFO level logging here would be helpful (like the name of the aux service that's using the custom classloader, etc.) l.146: I know it's existing code, but the C-style equal check is not necessary with java. I would simply go with sClass == null . l.160: same as above. (AuxiliaryServiceWithCustomClassLoader.java) in serviceInit() , serviceStart() , serviceStop() , shouldn't we call wrapped.serviceInit() instead of wrapper.init() , and so on? l.46: We might want to change this a little. It appears AbstractService.init() already sets the configuration (with the original configuration) before AuxiliaryServiceWithCustomClassLoader.serviceInit() is invoked. This may lead to confusion down the road. Let's reset the configuration here via setConfig() . In other words, @Override protected void serviceInit(Configuration conf) throws Exception { Configuration config = new Configuration(conf); // reset the service configuration setConfig(config); config.setClassLoader(customClassLoader); ClassLoader original = Thread .currentThread().getContextClassLoader(); Thread .currentThread().setContextClassLoader(customClassLoader); try { wrapped.serviceInit(config); } finally { Thread .currentThread().setContextClassLoader(original); } } Also, I don't think we need Configuration as a member variable. 
[![xgong](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10443) Xuan Gong](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=xgong) added a comment - [29/Apr/16 03:39](https://issues.apache.org/jira/browse/YARN-4577?focusedCommentId=15263481&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15263481)
Thanks for the view, [sjlee0](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=sjlee0)
> in serviceInit(), serviceStart(), serviceStop(), shouldn't we call wrapped.serviceInit() instead of wrapper.init(), and so on?
Looks like the serviceInit/serviceStart/serviceStop are protected functions, so we can not do that. When we call init(), it would automatically call serviceInit.
> Coupled with the unit test strategy, you might want to consider supporting some type of an override mechanism for system classes. Other use cases of ApplicationClassLoader provide this (although it's case by case). 
Thought about it. Add the improvement for it.
> Would you be able to come up with a unit test still? I know it's somewhat tricky, but you might be able to find a way to test a few things. You might want to take a look at TestRunJar.testClientClassLoader() to see if you can reuse some of the ideas there.
Tried several different ways to test it. But it is hard. A good unit test for this could be similar as I did for the manual testing. But unfortunately, I do not know how to do it.
[![xgong](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10443) Xuan Gong](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=xgong) added a comment - [29/Apr/16 03:39](https://issues.apache.org/jira/browse/YARN-4577?focusedCommentId=15263481&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15263481) Thanks for the view, sjlee0 in serviceInit(), serviceStart(), serviceStop(), shouldn't we call wrapped.serviceInit() instead of wrapper.init(), and so on? Looks like the serviceInit/serviceStart/serviceStop are protected functions, so we can not do that. When we call init(), it would automatically call serviceInit. Coupled with the unit test strategy, you might want to consider supporting some type of an override mechanism for system classes. Other use cases of ApplicationClassLoader provide this (although it's case by case). Thought about it. Add the improvement for it. Would you be able to come up with a unit test still? I know it's somewhat tricky, but you might be able to find a way to test a few things. You might want to take a look at TestRunJar.testClientClassLoader() to see if you can reuse some of the ideas there. Tried several different ways to test it. But it is hard. A good unit test for this could be similar as I did for the manual testing. But unfortunately, I do not know how to do it. 
[![xgong](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10443) Xuan Gong](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=xgong) added a comment - [29/Apr/16 03:40](https://issues.apache.org/jira/browse/YARN-4577?focusedCommentId=15263483&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15263483)
Uploaded a new patch: <https://issues.apache.org/jira/secure/attachment/12801375/YARN-4577.20160428.patch>
[![xgong](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10443) Xuan Gong](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=xgong) added a comment - [29/Apr/16 03:40](https://issues.apache.org/jira/browse/YARN-4577?focusedCommentId=15263483&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15263483) Uploaded a new patch: https://issues.apache.org/jira/secure/attachment/12801375/YARN-4577.20160428.patch 
[![hadoopqa](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Hadoop QA](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=hadoopqa) added a comment - [29/Apr/16 04:36](https://issues.apache.org/jira/browse/YARN-4577?focusedCommentId=15263524&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15263524)  
|  ![](https://issues.apache.org/jira/images/icons/emoticons/error.png) **-1 overall**  |  
| --- |  
  
  
  
|  Vote   |  Subsystem   |  Runtime   |  Comment   |  
| --- | --- | --- | --- |  
|  0  |  reexec   |  0m 27s   |  Docker mode activated.   |  
|  +1  |  @author   |  0m 0s   |  The patch does not contain any @author tags.   |  
|  -1  |  test4tests   |  0m 0s   |  The patch doesn't appear to include any new or modified tests. Please justify why no new tests are needed for this patch. Also please list what manual steps were performed to verify this patch.   |  
|  0  |  mvndep   |  0m 15s   |  Maven dependency ordering for branch   |  
|  +1  |  mvninstall   |  6m 31s   |  trunk passed   |  
|  +1  |  compile   |  1m 45s   |  trunk passed with JDK v1.8.0_91   |  
|  +1  |  compile   |  2m 4s   |  trunk passed with JDK v1.7.0_95   |  
|  +1  |  checkstyle   |  0m 35s   |  trunk passed   |  
|  +1  |  mvnsite   |  0m 54s   |  trunk passed   |  
|  +1  |  mvneclipse   |  0m 25s   |  trunk passed   |  
|  +1  |  findbugs   |  2m 0s   |  trunk passed   |  
|  +1  |  javadoc   |  0m 54s   |  trunk passed with JDK v1.8.0_91   |  
|  +1  |  javadoc   |  3m 13s   |  trunk passed with JDK v1.7.0_95   |  
|  0  |  mvndep   |  0m 10s   |  Maven dependency ordering for patch   |  
|  +1  |  mvninstall   |  0m 47s   |  the patch passed   |  
|  +1  |  compile   |  1m 43s   |  the patch passed with JDK v1.8.0_91   |  
|  +1  |  javac   |  1m 43s   |  the patch passed   |  
|  +1  |  compile   |  2m 2s   |  the patch passed with JDK v1.7.0_95   |  
|  +1  |  javac   |  2m 2s   |  the patch passed   |  
|  -1  |  checkstyle   |  0m 34s   |  hadoop-yarn-project/hadoop-yarn: patch generated 1 new + 263 unchanged - 0 fixed = 264 total (was 263)   |  
|  +1  |  mvnsite   |  0m 51s   |  the patch passed   |  
|  +1  |  mvneclipse   |  0m 21s   |  the patch passed   |  
|  +1  |  whitespace   |  0m 0s   |  Patch has no whitespace issues.   |  
|  +1  |  findbugs   |  2m 21s   |  the patch passed   |  
|  +1  |  javadoc   |  0m 50s   |  the patch passed with JDK v1.8.0_91   |  
|  +1  |  javadoc   |  3m 13s   |  the patch passed with JDK v1.7.0_95   |  
|  +1  |  unit   |  0m 20s   |  hadoop-yarn-api in the patch passed with JDK v1.8.0_91.   |  
|  +1  |  unit   |  11m 6s   |  hadoop-yarn-server-nodemanager in the patch passed with JDK v1.8.0_91.   |  
|  +1  |  unit   |  0m 22s   |  hadoop-yarn-api in the patch passed with JDK v1.7.0_95.   |  
|  +1  |  unit   |  11m 44s   |  hadoop-yarn-server-nodemanager in the patch passed with JDK v1.7.0_95.   |  
|  +1  |  asflicense   |  0m 20s   |  Patch does not generate ASF License warnings.   |  
|   |   |  57m 2s   |   |  
  
  
  
|  Subsystem   |  Report/Notes   |  
| --- | --- |  
|  Docker   |  Image:yetus/hadoop:cf2ee45   |  
|  JIRA Patch URL   |  <https://issues.apache.org/jira/secure/attachment/12801375/YARN-4577.20160428.patch>  |  
|  JIRA Issue   |  [~~YARN-4577~~](https://issues.apache.org/jira/browse/YARN-4577 "Enable aux services to have their own custom classpath/jar file")  |  
|  Optional Tests   |  asflicense compile javac javadoc mvninstall mvnsite unit findbugs checkstyle   |  
|  uname   |  Linux f6d325834bde 3.13.0-36-lowlatency #63-Ubuntu SMP PREEMPT Wed Sep 3 21:56:12 UTC 2014 x86_64 x86_64 x86_64 GNU/Linux   |  
|  Build tool   |  maven   |  
|  Personality   |  /testptch/hadoop/patchprocess/precommit/personality/provided.sh   |  
|  git revision   |  trunk / 6243eab   |  
|  Default Java   |  1.7.0_95   |  
|  Multi-JDK versions   |  /usr/lib/jvm/java-8-oracle:1.8.0_91 /usr/lib/jvm/java-7-openjdk-amd64:1.7.0_95   |  
|  findbugs   |  v3.0.0   |  
|  checkstyle   |  <https://builds.apache.org/job/PreCommit-YARN-Build/11277/artifact/patchprocess/diff-checkstyle-hadoop-yarn-project_hadoop-yarn.txt>  |  
|  JDK v1.7.0_95 Test Results   |  <https://builds.apache.org/job/PreCommit-YARN-Build/11277/testReport/>  |  
|  modules   |  C: hadoop-yarn-project/hadoop-yarn/hadoop-yarn-api hadoop-yarn-project/hadoop-yarn/hadoop-yarn-server/hadoop-yarn-server-nodemanager U: hadoop-yarn-project/hadoop-yarn   |  
|  Console output   |  <https://builds.apache.org/job/PreCommit-YARN-Build/11277/console>  |  
|  Powered by   |  Apache Yetus 0.2.0 <http://yetus.apache.org>  |  
This message was automatically generated.
[![hadoopqa](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Hadoop QA](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=hadoopqa) added a comment - [29/Apr/16 04:36](https://issues.apache.org/jira/browse/YARN-4577?focusedCommentId=15263524&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15263524) -1 overall Vote Subsystem Runtime Comment 0 reexec 0m 27s Docker mode activated. +1 @author 0m 0s The patch does not contain any @author tags. -1 test4tests 0m 0s The patch doesn't appear to include any new or modified tests. Please justify why no new tests are needed for this patch. Also please list what manual steps were performed to verify this patch. 0 mvndep 0m 15s Maven dependency ordering for branch +1 mvninstall 6m 31s trunk passed +1 compile 1m 45s trunk passed with JDK v1.8.0_91 +1 compile 2m 4s trunk passed with JDK v1.7.0_95 +1 checkstyle 0m 35s trunk passed +1 mvnsite 0m 54s trunk passed +1 mvneclipse 0m 25s trunk passed +1 findbugs 2m 0s trunk passed +1 javadoc 0m 54s trunk passed with JDK v1.8.0_91 +1 javadoc 3m 13s trunk passed with JDK v1.7.0_95 0 mvndep 0m 10s Maven dependency ordering for patch +1 mvninstall 0m 47s the patch passed +1 compile 1m 43s the patch passed with JDK v1.8.0_91 +1 javac 1m 43s the patch passed +1 compile 2m 2s the patch passed with JDK v1.7.0_95 +1 javac 2m 2s the patch passed -1 checkstyle 0m 34s hadoop-yarn-project/hadoop-yarn: patch generated 1 new + 263 unchanged - 0 fixed = 264 total (was 263) +1 mvnsite 0m 51s the patch passed +1 mvneclipse 0m 21s the patch passed +1 whitespace 0m 0s Patch has no whitespace issues. +1 findbugs 2m 21s the patch passed +1 javadoc 0m 50s the patch passed with JDK v1.8.0_91 +1 javadoc 3m 13s the patch passed with JDK v1.7.0_95 +1 unit 0m 20s hadoop-yarn-api in the patch passed with JDK v1.8.0_91. +1 unit 11m 6s hadoop-yarn-server-nodemanager in the patch passed with JDK v1.8.0_91. +1 unit 0m 22s hadoop-yarn-api in the patch passed with JDK v1.7.0_95. +1 unit 11m 44s hadoop-yarn-server-nodemanager in the patch passed with JDK v1.7.0_95. +1 asflicense 0m 20s Patch does not generate ASF License warnings. 57m 2s Subsystem Report/Notes Docker Image:yetus/hadoop:cf2ee45 JIRA Patch URL https://issues.apache.org/jira/secure/attachment/12801375/YARN-4577.20160428.patch JIRA Issue YARN-4577 Optional Tests asflicense compile javac javadoc mvninstall mvnsite unit findbugs checkstyle uname Linux f6d325834bde 3.13.0-36-lowlatency #63-Ubuntu SMP PREEMPT Wed Sep 3 21:56:12 UTC 2014 x86_64 x86_64 x86_64 GNU/Linux Build tool maven Personality /testptch/hadoop/patchprocess/precommit/personality/provided.sh git revision trunk / 6243eab Default Java 1.7.0_95 Multi-JDK versions /usr/lib/jvm/java-8-oracle:1.8.0_91 /usr/lib/jvm/java-7-openjdk-amd64:1.7.0_95 findbugs v3.0.0 checkstyle https://builds.apache.org/job/PreCommit-YARN-Build/11277/artifact/patchprocess/diff-checkstyle-hadoop-yarn-project_hadoop-yarn.txt JDK v1.7.0_95 Test Results https://builds.apache.org/job/PreCommit-YARN-Build/11277/testReport/ modules C: hadoop-yarn-project/hadoop-yarn/hadoop-yarn-api hadoop-yarn-project/hadoop-yarn/hadoop-yarn-server/hadoop-yarn-server-nodemanager U: hadoop-yarn-project/hadoop-yarn Console output https://builds.apache.org/job/PreCommit-YARN-Build/11277/console Powered by Apache Yetus 0.2.0 http://yetus.apache.org This message was automatically generated. 
[![vinodkv](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Vinod Kumar Vavilapalli](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=vinodkv) added a comment - [29/Apr/16 17:02](https://issues.apache.org/jira/browse/YARN-4577?focusedCommentId=15264338&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15264338)
Tx for taking care of this, [xgong](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=xgong) and [sjlee0](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=sjlee0)!
Few comments on the patch
  * YarnConfiguration: 
    * class.classpath -> classpath
    * classloader.system.classes -> system-classes
    * Similarly rename the corresponding constants
    * Add the new configs to yarn-default.xml, if only commented out
  * Change definitions of NM_AUX_SERVICE_CLASS_CLASSPATH, NM_AUX_SERVICE_CLASSLOADER_SYSTEM_CLASSES to use the other constant NM_AUX_SERVICES.
  * AuxServices 
    * createJobClassLoader -> createAuxServiceClassLoader()
    * systemClass -> systemClasses
  * The validation code to check the aux-service names so that ServiceData can be read and written properly should be done for aux-services loaded from a different classpath too.
  * AuxiliaryServiceWithCustomClassLoader 
    * Add a code comment as to why we are create new Configuration objects (a summary of what we discussed above).
    * Can we change the code such that AuxiliaryServiceWithCustomClassLoader simply takes in the class-name, classpath and system-classpath and does everything internally? This will keep the AuxServices class code cleaner.
  * We should definitely add a test-case. I think the simpler way to do this is to dynamically generate classes. Let me think about a bit while you address the remaining comments.


[![vinodkv](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Vinod Kumar Vavilapalli](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=vinodkv) added a comment - [29/Apr/16 17:02](https://issues.apache.org/jira/browse/YARN-4577?focusedCommentId=15264338&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15264338) Tx for taking care of this, xgong and sjlee0 ! Few comments on the patch YarnConfiguration: class.classpath -> classpath classloader.system.classes -> system-classes Similarly rename the corresponding constants Add the new configs to yarn-default.xml, if only commented out Change definitions of NM_AUX_SERVICE_CLASS_CLASSPATH, NM_AUX_SERVICE_CLASSLOADER_SYSTEM_CLASSES to use the other constant NM_AUX_SERVICES. AuxServices createJobClassLoader -> createAuxServiceClassLoader() systemClass -> systemClasses The validation code to check the aux-service names so that ServiceData can be read and written properly should be done for aux-services loaded from a different classpath too. AuxiliaryServiceWithCustomClassLoader Add a code comment as to why we are create new Configuration objects (a summary of what we discussed above). Can we change the code such that AuxiliaryServiceWithCustomClassLoader simply takes in the class-name, classpath and system-classpath and does everything internally? This will keep the AuxServices class code cleaner. We should definitely add a test-case. I think the simpler way to do this is to dynamically generate classes. Let me think about a bit while you address the remaining comments. 
[![sjlee0](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Sangjin Lee](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=sjlee0) added a comment - [29/Apr/16 17:37](https://issues.apache.org/jira/browse/YARN-4577?focusedCommentId=15264399&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15264399)
If you push more into `AuxiliaryServiceWithCustomClassLoader` from `AuxServices`, it may give you more opportunities to do targeted unit tests.
Just FYI, in case of `TestRunJar`, I created a few test classes (`ClassLoaderCheckMain`, etc.), created a jar on the fly (`makeClassLoaderTestJar()`), changed the system classes to include/exclude some of these test classes using the override, and test scenarios. Your mileage may vary.
[![sjlee0](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Sangjin Lee](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=sjlee0) added a comment - [29/Apr/16 17:37](https://issues.apache.org/jira/browse/YARN-4577?focusedCommentId=15264399&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15264399) If you push more into AuxiliaryServiceWithCustomClassLoader from AuxServices , it may give you more opportunities to do targeted unit tests. Just FYI, in case of TestRunJar , I created a few test classes ( ClassLoaderCheckMain , etc.), created a jar on the fly ( makeClassLoaderTestJar() ), changed the system classes to include/exclude some of these test classes using the override, and test scenarios. Your mileage may vary. 
[![xgong](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10443) Xuan Gong](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=xgong) added a comment - [10/May/16 03:44](https://issues.apache.org/jira/browse/YARN-4577?focusedCommentId=15277556&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15277556)
Attached a new patch with a test case.
[![xgong](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10443) Xuan Gong](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=xgong) added a comment - [10/May/16 03:44](https://issues.apache.org/jira/browse/YARN-4577?focusedCommentId=15277556&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15277556) Attached a new patch with a test case. 
[![hadoopqa](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Hadoop QA](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=hadoopqa) added a comment - [10/May/16 11:39](https://issues.apache.org/jira/browse/YARN-4577?focusedCommentId=15277972&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15277972)  
|  ![](https://issues.apache.org/jira/images/icons/emoticons/check.png) **+1 overall**  |  
| --- |  
  
  
  
|  Vote   |  Subsystem   |  Runtime   |  Comment   |  
| --- | --- | --- | --- |  
|  0  |  reexec   |  0m 14s   |  Docker mode activated.   |  
|  +1  |  @author   |  0m 0s   |  The patch does not contain any @author tags.   |  
|  +1  |  test4tests   |  0m 0s   |  The patch appears to include 1 new or modified test files.   |  
|  0  |  mvndep   |  0m 10s   |  Maven dependency ordering for branch   |  
|  +1  |  mvninstall   |  6m 30s   |  trunk passed   |  
|  +1  |  compile   |  1m 45s   |  trunk passed with JDK v1.8.0_91   |  
|  +1  |  compile   |  2m 3s   |  trunk passed with JDK v1.7.0_95   |  
|  +1  |  checkstyle   |  0m 41s   |  trunk passed   |  
|  +1  |  mvnsite   |  0m 54s   |  trunk passed   |  
|  +1  |  mvneclipse   |  0m 24s   |  trunk passed   |  
|  +1  |  findbugs   |  2m 1s   |  trunk passed   |  
|  +1  |  javadoc   |  0m 56s   |  trunk passed with JDK v1.8.0_91   |  
|  +1  |  javadoc   |  3m 20s   |  trunk passed with JDK v1.7.0_95   |  
|  0  |  mvndep   |  0m 11s   |  Maven dependency ordering for patch   |  
|  +1  |  mvninstall   |  0m 47s   |  the patch passed   |  
|  +1  |  compile   |  1m 53s   |  the patch passed with JDK v1.8.0_91   |  
|  +1  |  javac   |  1m 53s   |  the patch passed   |  
|  +1  |  compile   |  2m 8s   |  the patch passed with JDK v1.7.0_95   |  
|  +1  |  javac   |  2m 8s   |  the patch passed   |  
|  +1  |  checkstyle   |  0m 39s   |  hadoop-yarn-project/hadoop-yarn: patch generated 0 new + 304 unchanged - 2 fixed = 304 total (was 306)   |  
|  +1  |  mvnsite   |  0m 51s   |  the patch passed   |  
|  +1  |  mvneclipse   |  0m 22s   |  the patch passed   |  
|  +1  |  whitespace   |  0m 0s   |  Patch has no whitespace issues.   |  
|  +1  |  findbugs   |  2m 23s   |  the patch passed   |  
|  +1  |  javadoc   |  0m 52s   |  the patch passed with JDK v1.8.0_91   |  
|  +1  |  javadoc   |  3m 22s   |  the patch passed with JDK v1.7.0_95   |  
|  +1  |  unit   |  0m 22s   |  hadoop-yarn-api in the patch passed with JDK v1.8.0_91.   |  
|  +1  |  unit   |  11m 7s   |  hadoop-yarn-server-nodemanager in the patch passed with JDK v1.8.0_91.   |  
|  +1  |  unit   |  0m 22s   |  hadoop-yarn-api in the patch passed with JDK v1.7.0_95.   |  
|  +1  |  unit   |  11m 33s   |  hadoop-yarn-server-nodemanager in the patch passed with JDK v1.7.0_95.   |  
|  +1  |  asflicense   |  0m 20s   |  Patch does not generate ASF License warnings.   |  
|   |   |  57m 21s   |   |  
  
  
  
|  Subsystem   |  Report/Notes   |  
| --- | --- |  
|  Docker   |  Image:yetus/hadoop:cf2ee45   |  
|  JIRA Patch URL   |  <https://issues.apache.org/jira/secure/attachment/12803148/YARN-4577.20160509.patch>  |  
|  JIRA Issue   |  [~~YARN-4577~~](https://issues.apache.org/jira/browse/YARN-4577 "Enable aux services to have their own custom classpath/jar file")  |  
|  Optional Tests   |  asflicense compile javac javadoc mvninstall mvnsite unit findbugs checkstyle   |  
|  uname   |  Linux 85cb2a13c3c3 3.13.0-36-lowlatency #63-Ubuntu SMP PREEMPT Wed Sep 3 21:56:12 UTC 2014 x86_64 x86_64 x86_64 GNU/Linux   |  
|  Build tool   |  maven   |  
|  Personality   |  /testptch/hadoop/patchprocess/precommit/personality/provided.sh   |  
|  git revision   |  trunk / 87f5e35   |  
|  Default Java   |  1.7.0_95   |  
|  Multi-JDK versions   |  /usr/lib/jvm/java-8-oracle:1.8.0_91 /usr/lib/jvm/java-7-openjdk-amd64:1.7.0_95   |  
|  findbugs   |  v3.0.0   |  
|  JDK v1.7.0_95 Test Results   |  <https://builds.apache.org/job/PreCommit-YARN-Build/11396/testReport/>  |  
|  modules   |  C: hadoop-yarn-project/hadoop-yarn/hadoop-yarn-api hadoop-yarn-project/hadoop-yarn/hadoop-yarn-server/hadoop-yarn-server-nodemanager U: hadoop-yarn-project/hadoop-yarn   |  
|  Console output   |  <https://builds.apache.org/job/PreCommit-YARN-Build/11396/console>  |  
|  Powered by   |  Apache Yetus 0.2.0 <http://yetus.apache.org>  |  
This message was automatically generated.
[![hadoopqa](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Hadoop QA](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=hadoopqa) added a comment - [10/May/16 11:39](https://issues.apache.org/jira/browse/YARN-4577?focusedCommentId=15277972&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15277972) +1 overall Vote Subsystem Runtime Comment 0 reexec 0m 14s Docker mode activated. +1 @author 0m 0s The patch does not contain any @author tags. +1 test4tests 0m 0s The patch appears to include 1 new or modified test files. 0 mvndep 0m 10s Maven dependency ordering for branch +1 mvninstall 6m 30s trunk passed +1 compile 1m 45s trunk passed with JDK v1.8.0_91 +1 compile 2m 3s trunk passed with JDK v1.7.0_95 +1 checkstyle 0m 41s trunk passed +1 mvnsite 0m 54s trunk passed +1 mvneclipse 0m 24s trunk passed +1 findbugs 2m 1s trunk passed +1 javadoc 0m 56s trunk passed with JDK v1.8.0_91 +1 javadoc 3m 20s trunk passed with JDK v1.7.0_95 0 mvndep 0m 11s Maven dependency ordering for patch +1 mvninstall 0m 47s the patch passed +1 compile 1m 53s the patch passed with JDK v1.8.0_91 +1 javac 1m 53s the patch passed +1 compile 2m 8s the patch passed with JDK v1.7.0_95 +1 javac 2m 8s the patch passed +1 checkstyle 0m 39s hadoop-yarn-project/hadoop-yarn: patch generated 0 new + 304 unchanged - 2 fixed = 304 total (was 306) +1 mvnsite 0m 51s the patch passed +1 mvneclipse 0m 22s the patch passed +1 whitespace 0m 0s Patch has no whitespace issues. +1 findbugs 2m 23s the patch passed +1 javadoc 0m 52s the patch passed with JDK v1.8.0_91 +1 javadoc 3m 22s the patch passed with JDK v1.7.0_95 +1 unit 0m 22s hadoop-yarn-api in the patch passed with JDK v1.8.0_91. +1 unit 11m 7s hadoop-yarn-server-nodemanager in the patch passed with JDK v1.8.0_91. +1 unit 0m 22s hadoop-yarn-api in the patch passed with JDK v1.7.0_95. +1 unit 11m 33s hadoop-yarn-server-nodemanager in the patch passed with JDK v1.7.0_95. +1 asflicense 0m 20s Patch does not generate ASF License warnings. 57m 21s Subsystem Report/Notes Docker Image:yetus/hadoop:cf2ee45 JIRA Patch URL https://issues.apache.org/jira/secure/attachment/12803148/YARN-4577.20160509.patch JIRA Issue YARN-4577 Optional Tests asflicense compile javac javadoc mvninstall mvnsite unit findbugs checkstyle uname Linux 85cb2a13c3c3 3.13.0-36-lowlatency #63-Ubuntu SMP PREEMPT Wed Sep 3 21:56:12 UTC 2014 x86_64 x86_64 x86_64 GNU/Linux Build tool maven Personality /testptch/hadoop/patchprocess/precommit/personality/provided.sh git revision trunk / 87f5e35 Default Java 1.7.0_95 Multi-JDK versions /usr/lib/jvm/java-8-oracle:1.8.0_91 /usr/lib/jvm/java-7-openjdk-amd64:1.7.0_95 findbugs v3.0.0 JDK v1.7.0_95 Test Results https://builds.apache.org/job/PreCommit-YARN-Build/11396/testReport/ modules C: hadoop-yarn-project/hadoop-yarn/hadoop-yarn-api hadoop-yarn-project/hadoop-yarn/hadoop-yarn-server/hadoop-yarn-server-nodemanager U: hadoop-yarn-project/hadoop-yarn Console output https://builds.apache.org/job/PreCommit-YARN-Build/11396/console Powered by Apache Yetus 0.2.0 http://yetus.apache.org This message was automatically generated. 
[![vvasudev](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Varun Vasudev](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=vvasudev) added a comment - [10/May/16 14:05](https://issues.apache.org/jira/browse/YARN-4577?focusedCommentId=15278138&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15278138) - edited
[xgong](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=xgong) - TestAuxServices#makeClassLoaderTestJar and TestRunJar#makeClassLoaderTestJar seem to be the same with minor differences - can you refactor the code to use the same underlying logic? And can you also add a comment explaining the test logic? Thanks!
[![vvasudev](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Varun Vasudev](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=vvasudev) added a comment - [10/May/16 14:05](https://issues.apache.org/jira/browse/YARN-4577?focusedCommentId=15278138&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15278138) - edited xgong - TestAuxServices#makeClassLoaderTestJar and TestRunJar#makeClassLoaderTestJar seem to be the same with minor differences - can you refactor the code to use the same underlying logic? And can you also add a comment explaining the test logic? Thanks! 
[![xgong](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10443) Xuan Gong](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=xgong) added a comment - [10/May/16 22:07](https://issues.apache.org/jira/browse/YARN-4577?focusedCommentId=15279080&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15279080)
Thanks for the review. [vvasudev](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=vvasudev)  
I have uploaded a new patch to address all your comments.
[![xgong](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10443) Xuan Gong](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=xgong) added a comment - [10/May/16 22:07](https://issues.apache.org/jira/browse/YARN-4577?focusedCommentId=15279080&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15279080) Thanks for the review. vvasudev I have uploaded a new patch to address all your comments. 
[![sjlee0](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Sangjin Lee](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=sjlee0) added a comment - [10/May/16 22:26](https://issues.apache.org/jira/browse/YARN-4577?focusedCommentId=15279123&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15279123)
It appears the latest patch is missing `AuxiliaryServiceWithCustomClassLoader.java`?
[![sjlee0](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Sangjin Lee](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=sjlee0) added a comment - [10/May/16 22:26](https://issues.apache.org/jira/browse/YARN-4577?focusedCommentId=15279123&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15279123) It appears the latest patch is missing AuxiliaryServiceWithCustomClassLoader.java ? 
[![sjlee0](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Sangjin Lee](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=sjlee0) added a comment - [10/May/16 22:42](https://issues.apache.org/jira/browse/YARN-4577?focusedCommentId=15279138&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15279138)
One minor nit on `AuxiliaryServiceWithCustomClassLoader.java`:
  * l.45: now that we have a static factory method, it would be better to make the constructor private


[![sjlee0](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Sangjin Lee](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=sjlee0) added a comment - [10/May/16 22:42](https://issues.apache.org/jira/browse/YARN-4577?focusedCommentId=15279138&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15279138) One minor nit on AuxiliaryServiceWithCustomClassLoader.java : l.45: now that we have a static factory method, it would be better to make the constructor private 
[![hadoopqa](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Hadoop QA](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=hadoopqa) added a comment - [11/May/16 03:19](https://issues.apache.org/jira/browse/YARN-4577?focusedCommentId=15279430&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15279430)  
|  ![](https://issues.apache.org/jira/images/icons/emoticons/error.png) **-1 overall**  |  
| --- |  
  
  
  
|  Vote   |  Subsystem   |  Runtime   |  Comment   |  
| --- | --- | --- | --- |  
|  0  |  reexec   |  0m 15s   |  Docker mode activated.   |  
|  +1  |  @author   |  0m 0s   |  The patch does not contain any @author tags.   |  
|  +1  |  test4tests   |  0m 0s   |  The patch appears to include 3 new or modified test files.   |  
|  0  |  mvndep   |  0m 36s   |  Maven dependency ordering for branch   |  
|  +1  |  mvninstall   |  9m 27s   |  trunk passed   |  
|  +1  |  compile   |  11m 47s   |  trunk passed with JDK v1.8.0_91   |  
|  +1  |  compile   |  8m 50s   |  trunk passed with JDK v1.7.0_95   |  
|  +1  |  checkstyle   |  1m 45s   |  trunk passed   |  
|  +1  |  mvnsite   |  2m 20s   |  trunk passed   |  
|  +1  |  mvneclipse   |  0m 46s   |  trunk passed   |  
|  +1  |  findbugs   |  4m 17s   |  trunk passed   |  
|  +1  |  javadoc   |  2m 24s   |  trunk passed with JDK v1.8.0_91   |  
|  +1  |  javadoc   |  5m 4s   |  trunk passed with JDK v1.7.0_95   |  
|  0  |  mvndep   |  0m 18s   |  Maven dependency ordering for patch   |  
|  -1  |  mvninstall   |  0m 19s   |  hadoop-yarn-server-nodemanager in the patch failed.   |  
|  -1  |  compile   |  4m 7s   |  root in the patch failed with JDK v1.8.0_91.   |  
|  -1  |  javac   |  4m 7s   |  root in the patch failed with JDK v1.8.0_91.   |  
|  -1  |  compile   |  3m 49s   |  root in the patch failed with JDK v1.7.0_95.   |  
|  -1  |  javac   |  3m 49s   |  root in the patch failed with JDK v1.7.0_95.   |  
|  +1  |  checkstyle   |  1m 43s   |  root: patch generated 0 new + 316 unchanged - 2 fixed = 316 total (was 318)   |  
|  -1  |  mvnsite   |  0m 21s   |  hadoop-yarn-server-nodemanager in the patch failed.   |  
|  +1  |  mvneclipse   |  0m 43s   |  the patch passed   |  
|  +1  |  whitespace   |  0m 0s   |  Patch has no whitespace issues.   |  
|  -1  |  findbugs   |  0m 16s   |  hadoop-yarn-server-nodemanager in the patch failed.   |  
|  +1  |  javadoc   |  2m 23s   |  the patch passed with JDK v1.8.0_91   |  
|  +1  |  javadoc   |  5m 4s   |  the patch passed with JDK v1.7.0_95   |  
|  +1  |  unit   |  10m 24s   |  hadoop-common in the patch passed with JDK v1.8.0_91.   |  
|  +1  |  unit   |  0m 31s   |  hadoop-yarn-api in the patch passed with JDK v1.8.0_91.   |  
|  -1  |  unit   |  0m 20s   |  hadoop-yarn-server-nodemanager in the patch failed with JDK v1.8.0_91.   |  
|  +1  |  unit   |  10m 0s   |  hadoop-common in the patch passed with JDK v1.7.0_95.   |  
|  +1  |  unit   |  0m 30s   |  hadoop-yarn-api in the patch passed with JDK v1.7.0_95.   |  
|  -1  |  unit   |  0m 21s   |  hadoop-yarn-server-nodemanager in the patch failed with JDK v1.7.0_95.   |  
|  +1  |  asflicense   |  0m 25s   |  Patch does not generate ASF License warnings.   |  
|   |   |  97m 37s   |   |  
  
  
  
|  Subsystem   |  Report/Notes   |  
| --- | --- |  
|  Docker   |  Image:yetus/hadoop:cf2ee45   |  
|  JIRA Patch URL   |  <https://issues.apache.org/jira/secure/attachment/12803326/YARN-4577.20160510.patch>  |  
|  JIRA Issue   |  [~~YARN-4577~~](https://issues.apache.org/jira/browse/YARN-4577 "Enable aux services to have their own custom classpath/jar file")  |  
|  Optional Tests   |  asflicense compile javac javadoc mvninstall mvnsite unit findbugs checkstyle   |  
|  uname   |  Linux e92da668fdd3 3.13.0-36-lowlatency #63-Ubuntu SMP PREEMPT Wed Sep 3 21:56:12 UTC 2014 x86_64 x86_64 x86_64 GNU/Linux   |  
|  Build tool   |  maven   |  
|  Personality   |  /testptch/hadoop/patchprocess/precommit/personality/provided.sh   |  
|  git revision   |  trunk / 6e56578   |  
|  Default Java   |  1.7.0_95   |  
|  Multi-JDK versions   |  /usr/lib/jvm/java-8-oracle:1.8.0_91 /usr/lib/jvm/java-7-openjdk-amd64:1.7.0_95   |  
|  findbugs   |  v3.0.0   |  
|  mvninstall   |  <https://builds.apache.org/job/PreCommit-YARN-Build/11404/artifact/patchprocess/patch-mvninstall-hadoop-yarn-project_hadoop-yarn_hadoop-yarn-server_hadoop-yarn-server-nodemanager.txt>  |  
|  compile   |  <https://builds.apache.org/job/PreCommit-YARN-Build/11404/artifact/patchprocess/patch-compile-root-jdk1.8.0_91.txt>  |  
|  javac   |  <https://builds.apache.org/job/PreCommit-YARN-Build/11404/artifact/patchprocess/patch-compile-root-jdk1.8.0_91.txt>  |  
|  compile   |  <https://builds.apache.org/job/PreCommit-YARN-Build/11404/artifact/patchprocess/patch-compile-root-jdk1.7.0_95.txt>  |  
|  javac   |  <https://builds.apache.org/job/PreCommit-YARN-Build/11404/artifact/patchprocess/patch-compile-root-jdk1.7.0_95.txt>  |  
|  mvnsite   |  <https://builds.apache.org/job/PreCommit-YARN-Build/11404/artifact/patchprocess/patch-mvnsite-hadoop-yarn-project_hadoop-yarn_hadoop-yarn-server_hadoop-yarn-server-nodemanager.txt>  |  
|  findbugs   |  <https://builds.apache.org/job/PreCommit-YARN-Build/11404/artifact/patchprocess/patch-findbugs-hadoop-yarn-project_hadoop-yarn_hadoop-yarn-server_hadoop-yarn-server-nodemanager.txt>  |  
|  unit   |  <https://builds.apache.org/job/PreCommit-YARN-Build/11404/artifact/patchprocess/patch-unit-hadoop-yarn-project_hadoop-yarn_hadoop-yarn-server_hadoop-yarn-server-nodemanager-jdk1.8.0_91.txt>  |  
|  unit   |  <https://builds.apache.org/job/PreCommit-YARN-Build/11404/artifact/patchprocess/patch-unit-hadoop-yarn-project_hadoop-yarn_hadoop-yarn-server_hadoop-yarn-server-nodemanager-jdk1.7.0_95.txt>  |  
|  JDK v1.7.0_95 Test Results   |  <https://builds.apache.org/job/PreCommit-YARN-Build/11404/testReport/>  |  
|  modules   |  C: hadoop-common-project/hadoop-common hadoop-yarn-project/hadoop-yarn/hadoop-yarn-api hadoop-yarn-project/hadoop-yarn/hadoop-yarn-server/hadoop-yarn-server-nodemanager U: .   |  
|  Console output   |  <https://builds.apache.org/job/PreCommit-YARN-Build/11404/console>  |  
|  Powered by   |  Apache Yetus 0.2.0 <http://yetus.apache.org>  |  
This message was automatically generated.
[![hadoopqa](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Hadoop QA](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=hadoopqa) added a comment - [11/May/16 03:19](https://issues.apache.org/jira/browse/YARN-4577?focusedCommentId=15279430&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15279430) -1 overall Vote Subsystem Runtime Comment 0 reexec 0m 15s Docker mode activated. +1 @author 0m 0s The patch does not contain any @author tags. +1 test4tests 0m 0s The patch appears to include 3 new or modified test files. 0 mvndep 0m 36s Maven dependency ordering for branch +1 mvninstall 9m 27s trunk passed +1 compile 11m 47s trunk passed with JDK v1.8.0_91 +1 compile 8m 50s trunk passed with JDK v1.7.0_95 +1 checkstyle 1m 45s trunk passed +1 mvnsite 2m 20s trunk passed +1 mvneclipse 0m 46s trunk passed +1 findbugs 4m 17s trunk passed +1 javadoc 2m 24s trunk passed with JDK v1.8.0_91 +1 javadoc 5m 4s trunk passed with JDK v1.7.0_95 0 mvndep 0m 18s Maven dependency ordering for patch -1 mvninstall 0m 19s hadoop-yarn-server-nodemanager in the patch failed. -1 compile 4m 7s root in the patch failed with JDK v1.8.0_91. -1 javac 4m 7s root in the patch failed with JDK v1.8.0_91. -1 compile 3m 49s root in the patch failed with JDK v1.7.0_95. -1 javac 3m 49s root in the patch failed with JDK v1.7.0_95. +1 checkstyle 1m 43s root: patch generated 0 new + 316 unchanged - 2 fixed = 316 total (was 318) -1 mvnsite 0m 21s hadoop-yarn-server-nodemanager in the patch failed. +1 mvneclipse 0m 43s the patch passed +1 whitespace 0m 0s Patch has no whitespace issues. -1 findbugs 0m 16s hadoop-yarn-server-nodemanager in the patch failed. +1 javadoc 2m 23s the patch passed with JDK v1.8.0_91 +1 javadoc 5m 4s the patch passed with JDK v1.7.0_95 +1 unit 10m 24s hadoop-common in the patch passed with JDK v1.8.0_91. +1 unit 0m 31s hadoop-yarn-api in the patch passed with JDK v1.8.0_91. -1 unit 0m 20s hadoop-yarn-server-nodemanager in the patch failed with JDK v1.8.0_91. +1 unit 10m 0s hadoop-common in the patch passed with JDK v1.7.0_95. +1 unit 0m 30s hadoop-yarn-api in the patch passed with JDK v1.7.0_95. -1 unit 0m 21s hadoop-yarn-server-nodemanager in the patch failed with JDK v1.7.0_95. +1 asflicense 0m 25s Patch does not generate ASF License warnings. 97m 37s Subsystem Report/Notes Docker Image:yetus/hadoop:cf2ee45 JIRA Patch URL https://issues.apache.org/jira/secure/attachment/12803326/YARN-4577.20160510.patch JIRA Issue YARN-4577 Optional Tests asflicense compile javac javadoc mvninstall mvnsite unit findbugs checkstyle uname Linux e92da668fdd3 3.13.0-36-lowlatency #63-Ubuntu SMP PREEMPT Wed Sep 3 21:56:12 UTC 2014 x86_64 x86_64 x86_64 GNU/Linux Build tool maven Personality /testptch/hadoop/patchprocess/precommit/personality/provided.sh git revision trunk / 6e56578 Default Java 1.7.0_95 Multi-JDK versions /usr/lib/jvm/java-8-oracle:1.8.0_91 /usr/lib/jvm/java-7-openjdk-amd64:1.7.0_95 findbugs v3.0.0 mvninstall https://builds.apache.org/job/PreCommit-YARN-Build/11404/artifact/patchprocess/patch-mvninstall-hadoop-yarn-project_hadoop-yarn_hadoop-yarn-server_hadoop-yarn-server-nodemanager.txt compile https://builds.apache.org/job/PreCommit-YARN-Build/11404/artifact/patchprocess/patch-compile-root-jdk1.8.0_91.txt javac https://builds.apache.org/job/PreCommit-YARN-Build/11404/artifact/patchprocess/patch-compile-root-jdk1.8.0_91.txt compile https://builds.apache.org/job/PreCommit-YARN-Build/11404/artifact/patchprocess/patch-compile-root-jdk1.7.0_95.txt javac https://builds.apache.org/job/PreCommit-YARN-Build/11404/artifact/patchprocess/patch-compile-root-jdk1.7.0_95.txt mvnsite https://builds.apache.org/job/PreCommit-YARN-Build/11404/artifact/patchprocess/patch-mvnsite-hadoop-yarn-project_hadoop-yarn_hadoop-yarn-server_hadoop-yarn-server-nodemanager.txt findbugs https://builds.apache.org/job/PreCommit-YARN-Build/11404/artifact/patchprocess/patch-findbugs-hadoop-yarn-project_hadoop-yarn_hadoop-yarn-server_hadoop-yarn-server-nodemanager.txt unit https://builds.apache.org/job/PreCommit-YARN-Build/11404/artifact/patchprocess/patch-unit-hadoop-yarn-project_hadoop-yarn_hadoop-yarn-server_hadoop-yarn-server-nodemanager-jdk1.8.0_91.txt unit https://builds.apache.org/job/PreCommit-YARN-Build/11404/artifact/patchprocess/patch-unit-hadoop-yarn-project_hadoop-yarn_hadoop-yarn-server_hadoop-yarn-server-nodemanager-jdk1.7.0_95.txt JDK v1.7.0_95 Test Results https://builds.apache.org/job/PreCommit-YARN-Build/11404/testReport/ modules C: hadoop-common-project/hadoop-common hadoop-yarn-project/hadoop-yarn/hadoop-yarn-api hadoop-yarn-project/hadoop-yarn/hadoop-yarn-server/hadoop-yarn-server-nodemanager U: . Console output https://builds.apache.org/job/PreCommit-YARN-Build/11404/console Powered by Apache Yetus 0.2.0 http://yetus.apache.org This message was automatically generated. 
[![vvasudev](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Varun Vasudev](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=vvasudev) added a comment - [11/May/16 08:30](https://issues.apache.org/jira/browse/YARN-4577?focusedCommentId=15279782&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15279782)
[xgong](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=xgong) - as [sjlee0](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=sjlee0) mentioned the latest patch is missing AuxiliaryServiceWithCustomClassLoader.java.
[![vvasudev](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Varun Vasudev](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=vvasudev) added a comment - [11/May/16 08:30](https://issues.apache.org/jira/browse/YARN-4577?focusedCommentId=15279782&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15279782) xgong - as sjlee0 mentioned the latest patch is missing AuxiliaryServiceWithCustomClassLoader.java. 
[![xgong](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10443) Xuan Gong](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=xgong) added a comment - [11/May/16 17:21](https://issues.apache.org/jira/browse/YARN-4577?focusedCommentId=15280472&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15280472)
[vvasudev](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=vvasudev), [sjlee0](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=sjlee0)  
Sorry about that. I have uploaded a new patch for this
[![xgong](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10443) Xuan Gong](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=xgong) added a comment - [11/May/16 17:21](https://issues.apache.org/jira/browse/YARN-4577?focusedCommentId=15280472&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15280472) vvasudev , sjlee0 Sorry about that. I have uploaded a new patch for this 
[![hadoopqa](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Hadoop QA](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=hadoopqa) added a comment - [11/May/16 23:34](https://issues.apache.org/jira/browse/YARN-4577?focusedCommentId=15280993&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15280993)  
|  ![](https://issues.apache.org/jira/images/icons/emoticons/error.png) **-1 overall**  |  
| --- |  
  
  
  
|  Vote   |  Subsystem   |  Runtime   |  Comment   |  
| --- | --- | --- | --- |  
|  0  |  reexec   |  0m 13s   |  Docker mode activated.   |  
|  +1  |  @author   |  0m 0s   |  The patch does not contain any @author tags.   |  
|  +1  |  test4tests   |  0m 0s   |  The patch appears to include 3 new or modified test files.   |  
|  0  |  mvndep   |  0m 16s   |  Maven dependency ordering for branch   |  
|  +1  |  mvninstall   |  7m 14s   |  trunk passed   |  
|  +1  |  compile   |  6m 52s   |  trunk passed with JDK v1.8.0_91   |  
|  +1  |  compile   |  7m 2s   |  trunk passed with JDK v1.7.0_95   |  
|  +1  |  checkstyle   |  1m 31s   |  trunk passed   |  
|  +1  |  mvnsite   |  1m 52s   |  trunk passed   |  
|  +1  |  mvneclipse   |  0m 39s   |  trunk passed   |  
|  +1  |  findbugs   |  3m 37s   |  trunk passed   |  
|  +1  |  javadoc   |  1m 54s   |  trunk passed with JDK v1.8.0_91   |  
|  +1  |  javadoc   |  4m 24s   |  trunk passed with JDK v1.7.0_95   |  
|  0  |  mvndep   |  0m 14s   |  Maven dependency ordering for patch   |  
|  +1  |  mvninstall   |  1m 31s   |  the patch passed   |  
|  +1  |  compile   |  5m 50s   |  the patch passed with JDK v1.8.0_91   |  
|  +1  |  javac   |  5m 50s   |  the patch passed   |  
|  +1  |  compile   |  6m 47s   |  the patch passed with JDK v1.7.0_95   |  
|  +1  |  javac   |  6m 47s   |  the patch passed   |  
|  -1  |  checkstyle   |  1m 29s   |  root: patch generated 1 new + 316 unchanged - 2 fixed = 317 total (was 318)   |  
|  +1  |  mvnsite   |  1m 54s   |  the patch passed   |  
|  +1  |  mvneclipse   |  0m 39s   |  the patch passed   |  
|  +1  |  whitespace   |  0m 0s   |  Patch has no whitespace issues.   |  
|  +1  |  findbugs   |  4m 19s   |  the patch passed   |  
|  +1  |  javadoc   |  1m 52s   |  the patch passed with JDK v1.8.0_91   |  
|  +1  |  javadoc   |  4m 21s   |  the patch passed with JDK v1.7.0_95   |  
|  -1  |  unit   |  7m 21s   |  hadoop-common in the patch failed with JDK v1.8.0_91.   |  
|  +1  |  unit   |  0m 22s   |  hadoop-yarn-api in the patch passed with JDK v1.8.0_91.   |  
|  +1  |  unit   |  11m 4s   |  hadoop-yarn-server-nodemanager in the patch passed with JDK v1.8.0_91.   |  
|  +1  |  unit   |  7m 56s   |  hadoop-common in the patch passed with JDK v1.7.0_95.   |  
|  +1  |  unit   |  0m 26s   |  hadoop-yarn-api in the patch passed with JDK v1.7.0_95.   |  
|  +1  |  unit   |  11m 45s   |  hadoop-yarn-server-nodemanager in the patch passed with JDK v1.7.0_95.   |  
|  +1  |  asflicense   |  0m 23s   |  Patch does not generate ASF License warnings.   |  
|   |   |  105m 21s   |   |  
  
  
  
|  Reason   |  Tests   |  
| --- | --- |  
|  JDK v1.8.0_91 Failed junit tests   |  hadoop.net.TestDNS   |  
  
  
  
|  Subsystem   |  Report/Notes   |  
| --- | --- |  
|  Docker   |  Image:yetus/hadoop:cf2ee45   |  
|  JIRA Patch URL   |  <https://issues.apache.org/jira/secure/attachment/12803459/YARN-4577.20160511.patch>  |  
|  JIRA Issue   |  [~~YARN-4577~~](https://issues.apache.org/jira/browse/YARN-4577 "Enable aux services to have their own custom classpath/jar file")  |  
|  Optional Tests   |  asflicense compile javac javadoc mvninstall mvnsite unit findbugs checkstyle   |  
|  uname   |  Linux c9bed34a7662 3.13.0-36-lowlatency #63-Ubuntu SMP PREEMPT Wed Sep 3 21:56:12 UTC 2014 x86_64 x86_64 x86_64 GNU/Linux   |  
|  Build tool   |  maven   |  
|  Personality   |  /testptch/hadoop/patchprocess/precommit/personality/provided.sh   |  
|  git revision   |  trunk / 687233f   |  
|  Default Java   |  1.7.0_95   |  
|  Multi-JDK versions   |  /usr/lib/jvm/java-8-oracle:1.8.0_91 /usr/lib/jvm/java-7-openjdk-amd64:1.7.0_95   |  
|  findbugs   |  v3.0.0   |  
|  checkstyle   |  <https://builds.apache.org/job/PreCommit-YARN-Build/11420/artifact/patchprocess/diff-checkstyle-root.txt>  |  
|  unit   |  <https://builds.apache.org/job/PreCommit-YARN-Build/11420/artifact/patchprocess/patch-unit-hadoop-common-project_hadoop-common-jdk1.8.0_91.txt>  |  
|  unit test logs   |  <https://builds.apache.org/job/PreCommit-YARN-Build/11420/artifact/patchprocess/patch-unit-hadoop-common-project_hadoop-common-jdk1.8.0_91.txt>  |  
|  JDK v1.7.0_95 Test Results   |  <https://builds.apache.org/job/PreCommit-YARN-Build/11420/testReport/>  |  
|  modules   |  C: hadoop-common-project/hadoop-common hadoop-yarn-project/hadoop-yarn/hadoop-yarn-api hadoop-yarn-project/hadoop-yarn/hadoop-yarn-server/hadoop-yarn-server-nodemanager U: .   |  
|  Console output   |  <https://builds.apache.org/job/PreCommit-YARN-Build/11420/console>  |  
|  Powered by   |  Apache Yetus 0.2.0 <http://yetus.apache.org>  |  
This message was automatically generated.
[![hadoopqa](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Hadoop QA](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=hadoopqa) added a comment - [11/May/16 23:34](https://issues.apache.org/jira/browse/YARN-4577?focusedCommentId=15280993&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15280993) -1 overall Vote Subsystem Runtime Comment 0 reexec 0m 13s Docker mode activated. +1 @author 0m 0s The patch does not contain any @author tags. +1 test4tests 0m 0s The patch appears to include 3 new or modified test files. 0 mvndep 0m 16s Maven dependency ordering for branch +1 mvninstall 7m 14s trunk passed +1 compile 6m 52s trunk passed with JDK v1.8.0_91 +1 compile 7m 2s trunk passed with JDK v1.7.0_95 +1 checkstyle 1m 31s trunk passed +1 mvnsite 1m 52s trunk passed +1 mvneclipse 0m 39s trunk passed +1 findbugs 3m 37s trunk passed +1 javadoc 1m 54s trunk passed with JDK v1.8.0_91 +1 javadoc 4m 24s trunk passed with JDK v1.7.0_95 0 mvndep 0m 14s Maven dependency ordering for patch +1 mvninstall 1m 31s the patch passed +1 compile 5m 50s the patch passed with JDK v1.8.0_91 +1 javac 5m 50s the patch passed +1 compile 6m 47s the patch passed with JDK v1.7.0_95 +1 javac 6m 47s the patch passed -1 checkstyle 1m 29s root: patch generated 1 new + 316 unchanged - 2 fixed = 317 total (was 318) +1 mvnsite 1m 54s the patch passed +1 mvneclipse 0m 39s the patch passed +1 whitespace 0m 0s Patch has no whitespace issues. +1 findbugs 4m 19s the patch passed +1 javadoc 1m 52s the patch passed with JDK v1.8.0_91 +1 javadoc 4m 21s the patch passed with JDK v1.7.0_95 -1 unit 7m 21s hadoop-common in the patch failed with JDK v1.8.0_91. +1 unit 0m 22s hadoop-yarn-api in the patch passed with JDK v1.8.0_91. +1 unit 11m 4s hadoop-yarn-server-nodemanager in the patch passed with JDK v1.8.0_91. +1 unit 7m 56s hadoop-common in the patch passed with JDK v1.7.0_95. +1 unit 0m 26s hadoop-yarn-api in the patch passed with JDK v1.7.0_95. +1 unit 11m 45s hadoop-yarn-server-nodemanager in the patch passed with JDK v1.7.0_95. +1 asflicense 0m 23s Patch does not generate ASF License warnings. 105m 21s Reason Tests JDK v1.8.0_91 Failed junit tests hadoop.net.TestDNS Subsystem Report/Notes Docker Image:yetus/hadoop:cf2ee45 JIRA Patch URL https://issues.apache.org/jira/secure/attachment/12803459/YARN-4577.20160511.patch JIRA Issue YARN-4577 Optional Tests asflicense compile javac javadoc mvninstall mvnsite unit findbugs checkstyle uname Linux c9bed34a7662 3.13.0-36-lowlatency #63-Ubuntu SMP PREEMPT Wed Sep 3 21:56:12 UTC 2014 x86_64 x86_64 x86_64 GNU/Linux Build tool maven Personality /testptch/hadoop/patchprocess/precommit/personality/provided.sh git revision trunk / 687233f Default Java 1.7.0_95 Multi-JDK versions /usr/lib/jvm/java-8-oracle:1.8.0_91 /usr/lib/jvm/java-7-openjdk-amd64:1.7.0_95 findbugs v3.0.0 checkstyle https://builds.apache.org/job/PreCommit-YARN-Build/11420/artifact/patchprocess/diff-checkstyle-root.txt unit https://builds.apache.org/job/PreCommit-YARN-Build/11420/artifact/patchprocess/patch-unit-hadoop-common-project_hadoop-common-jdk1.8.0_91.txt unit test logs https://builds.apache.org/job/PreCommit-YARN-Build/11420/artifact/patchprocess/patch-unit-hadoop-common-project_hadoop-common-jdk1.8.0_91.txt JDK v1.7.0_95 Test Results https://builds.apache.org/job/PreCommit-YARN-Build/11420/testReport/ modules C: hadoop-common-project/hadoop-common hadoop-yarn-project/hadoop-yarn/hadoop-yarn-api hadoop-yarn-project/hadoop-yarn/hadoop-yarn-server/hadoop-yarn-server-nodemanager U: . Console output https://builds.apache.org/job/PreCommit-YARN-Build/11420/console Powered by Apache Yetus 0.2.0 http://yetus.apache.org This message was automatically generated. 
[![sjlee0](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Sangjin Lee](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=sjlee0) added a comment - [11/May/16 23:43](https://issues.apache.org/jira/browse/YARN-4577?focusedCommentId=15281003&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15281003)
I think it's quite close. The hadoop-common test failure is unrelated. The checkstyle issue should be trivial to fix. Hi [xgong](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=xgong), could you please fix the checkstyle issue? Then I think it's good to go.
[vvasudev](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=vvasudev), let me know if you're OK with that.
[![sjlee0](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Sangjin Lee](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=sjlee0) added a comment - [11/May/16 23:43](https://issues.apache.org/jira/browse/YARN-4577?focusedCommentId=15281003&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15281003) I think it's quite close. The hadoop-common test failure is unrelated. The checkstyle issue should be trivial to fix. Hi xgong , could you please fix the checkstyle issue? Then I think it's good to go. vvasudev , let me know if you're OK with that. 
[![vvasudev](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Varun Vasudev](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=vvasudev) added a comment - [12/May/16 02:40](https://issues.apache.org/jira/browse/YARN-4577?focusedCommentId=15281133&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15281133)
Agree with [sjlee0](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=sjlee0); [xgong](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=xgong) - can you please fix the checkstyle issue and we can commit it.
[![vvasudev](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Varun Vasudev](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=vvasudev) added a comment - [12/May/16 02:40](https://issues.apache.org/jira/browse/YARN-4577?focusedCommentId=15281133&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15281133) Agree with sjlee0 ; xgong - can you please fix the checkstyle issue and we can commit it. 
[![xgong](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10443) Xuan Gong](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=xgong) added a comment - [12/May/16 02:58](https://issues.apache.org/jira/browse/YARN-4577?focusedCommentId=15281140&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15281140)
Thanks for the review. Uploaded a new patch which made the AuxiliaryServiceWithCustomClassLoader as final
[![xgong](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10443) Xuan Gong](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=xgong) added a comment - [12/May/16 02:58](https://issues.apache.org/jira/browse/YARN-4577?focusedCommentId=15281140&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15281140) Thanks for the review. Uploaded a new patch which made the AuxiliaryServiceWithCustomClassLoader as final 
[![hadoopqa](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Hadoop QA](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=hadoopqa) added a comment - [12/May/16 06:13](https://issues.apache.org/jira/browse/YARN-4577?focusedCommentId=15281239&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15281239)  
|  ![](https://issues.apache.org/jira/images/icons/emoticons/check.png) **+1 overall**  |  
| --- |  
  
  
  
|  Vote   |  Subsystem   |  Runtime   |  Comment   |  
| --- | --- | --- | --- |  
|  0  |  reexec   |  0m 12s   |  Docker mode activated.   |  
|  +1  |  @author   |  0m 0s   |  The patch does not contain any @author tags.   |  
|  +1  |  test4tests   |  0m 0s   |  The patch appears to include 3 new or modified test files.   |  
|  0  |  mvndep   |  0m 15s   |  Maven dependency ordering for branch   |  
|  +1  |  mvninstall   |  6m 41s   |  trunk passed   |  
|  +1  |  compile   |  6m 3s   |  trunk passed with JDK v1.8.0_91   |  
|  +1  |  compile   |  6m 53s   |  trunk passed with JDK v1.7.0_95   |  
|  +1  |  checkstyle   |  1m 30s   |  trunk passed   |  
|  +1  |  mvnsite   |  1m 52s   |  trunk passed   |  
|  +1  |  mvneclipse   |  0m 40s   |  trunk passed   |  
|  +1  |  findbugs   |  3m 43s   |  trunk passed   |  
|  +1  |  javadoc   |  2m 31s   |  trunk passed with JDK v1.8.0_91   |  
|  +1  |  javadoc   |  5m 25s   |  trunk passed with JDK v1.7.0_95   |  
|  0  |  mvndep   |  0m 15s   |  Maven dependency ordering for patch   |  
|  +1  |  mvninstall   |  1m 31s   |  the patch passed   |  
|  +1  |  compile   |  6m 4s   |  the patch passed with JDK v1.8.0_91   |  
|  +1  |  javac   |  6m 4s   |  the patch passed   |  
|  +1  |  compile   |  6m 50s   |  the patch passed with JDK v1.7.0_95   |  
|  +1  |  javac   |  6m 50s   |  the patch passed   |  
|  +1  |  checkstyle   |  1m 30s   |  root: patch generated 0 new + 316 unchanged - 2 fixed = 316 total (was 318)   |  
|  +1  |  mvnsite   |  1m 53s   |  the patch passed   |  
|  +1  |  mvneclipse   |  0m 38s   |  the patch passed   |  
|  +1  |  whitespace   |  0m 0s   |  Patch has no whitespace issues.   |  
|  +1  |  findbugs   |  4m 18s   |  the patch passed   |  
|  +1  |  javadoc   |  1m 52s   |  the patch passed with JDK v1.8.0_91   |  
|  +1  |  javadoc   |  4m 24s   |  the patch passed with JDK v1.7.0_95   |  
|  +1  |  unit   |  7m 50s   |  hadoop-common in the patch passed with JDK v1.8.0_91.   |  
|  +1  |  unit   |  0m 22s   |  hadoop-yarn-api in the patch passed with JDK v1.8.0_91.   |  
|  +1  |  unit   |  11m 6s   |  hadoop-yarn-server-nodemanager in the patch passed with JDK v1.8.0_91.   |  
|  +1  |  unit   |  7m 48s   |  hadoop-common in the patch passed with JDK v1.7.0_95.   |  
|  +1  |  unit   |  0m 24s   |  hadoop-yarn-api in the patch passed with JDK v1.7.0_95.   |  
|  +1  |  unit   |  11m 36s   |  hadoop-yarn-server-nodemanager in the patch passed with JDK v1.7.0_95.   |  
|  +1  |  asflicense   |  0m 23s   |  Patch does not generate ASF License warnings.   |  
|   |   |  106m 1s   |   |  
  
  
  
|  Subsystem   |  Report/Notes   |  
| --- | --- |  
|  Docker   |  Image:yetus/hadoop:cf2ee45   |  
|  JIRA Patch URL   |  <https://issues.apache.org/jira/secure/attachment/12803562/YARN-4577.20160511.1.patch>  |  
|  JIRA Issue   |  [~~YARN-4577~~](https://issues.apache.org/jira/browse/YARN-4577 "Enable aux services to have their own custom classpath/jar file")  |  
|  Optional Tests   |  asflicense compile javac javadoc mvninstall mvnsite unit findbugs checkstyle   |  
|  uname   |  Linux e71cd162ac8f 3.13.0-36-lowlatency #63-Ubuntu SMP PREEMPT Wed Sep 3 21:56:12 UTC 2014 x86_64 x86_64 x86_64 GNU/Linux   |  
|  Build tool   |  maven   |  
|  Personality   |  /testptch/hadoop/patchprocess/precommit/personality/provided.sh   |  
|  git revision   |  trunk / d464f4d   |  
|  Default Java   |  1.7.0_95   |  
|  Multi-JDK versions   |  /usr/lib/jvm/java-8-oracle:1.8.0_91 /usr/lib/jvm/java-7-openjdk-amd64:1.7.0_95   |  
|  findbugs   |  v3.0.0   |  
|  JDK v1.7.0_95 Test Results   |  <https://builds.apache.org/job/PreCommit-YARN-Build/11426/testReport/>  |  
|  modules   |  C: hadoop-common-project/hadoop-common hadoop-yarn-project/hadoop-yarn/hadoop-yarn-api hadoop-yarn-project/hadoop-yarn/hadoop-yarn-server/hadoop-yarn-server-nodemanager U: .   |  
|  Console output   |  <https://builds.apache.org/job/PreCommit-YARN-Build/11426/console>  |  
|  Powered by   |  Apache Yetus 0.2.0 <http://yetus.apache.org>  |  
This message was automatically generated.
[![hadoopqa](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Hadoop QA](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=hadoopqa) added a comment - [12/May/16 06:13](https://issues.apache.org/jira/browse/YARN-4577?focusedCommentId=15281239&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15281239) +1 overall Vote Subsystem Runtime Comment 0 reexec 0m 12s Docker mode activated. +1 @author 0m 0s The patch does not contain any @author tags. +1 test4tests 0m 0s The patch appears to include 3 new or modified test files. 0 mvndep 0m 15s Maven dependency ordering for branch +1 mvninstall 6m 41s trunk passed +1 compile 6m 3s trunk passed with JDK v1.8.0_91 +1 compile 6m 53s trunk passed with JDK v1.7.0_95 +1 checkstyle 1m 30s trunk passed +1 mvnsite 1m 52s trunk passed +1 mvneclipse 0m 40s trunk passed +1 findbugs 3m 43s trunk passed +1 javadoc 2m 31s trunk passed with JDK v1.8.0_91 +1 javadoc 5m 25s trunk passed with JDK v1.7.0_95 0 mvndep 0m 15s Maven dependency ordering for patch +1 mvninstall 1m 31s the patch passed +1 compile 6m 4s the patch passed with JDK v1.8.0_91 +1 javac 6m 4s the patch passed +1 compile 6m 50s the patch passed with JDK v1.7.0_95 +1 javac 6m 50s the patch passed +1 checkstyle 1m 30s root: patch generated 0 new + 316 unchanged - 2 fixed = 316 total (was 318) +1 mvnsite 1m 53s the patch passed +1 mvneclipse 0m 38s the patch passed +1 whitespace 0m 0s Patch has no whitespace issues. +1 findbugs 4m 18s the patch passed +1 javadoc 1m 52s the patch passed with JDK v1.8.0_91 +1 javadoc 4m 24s the patch passed with JDK v1.7.0_95 +1 unit 7m 50s hadoop-common in the patch passed with JDK v1.8.0_91. +1 unit 0m 22s hadoop-yarn-api in the patch passed with JDK v1.8.0_91. +1 unit 11m 6s hadoop-yarn-server-nodemanager in the patch passed with JDK v1.8.0_91. +1 unit 7m 48s hadoop-common in the patch passed with JDK v1.7.0_95. +1 unit 0m 24s hadoop-yarn-api in the patch passed with JDK v1.7.0_95. +1 unit 11m 36s hadoop-yarn-server-nodemanager in the patch passed with JDK v1.7.0_95. +1 asflicense 0m 23s Patch does not generate ASF License warnings. 106m 1s Subsystem Report/Notes Docker Image:yetus/hadoop:cf2ee45 JIRA Patch URL https://issues.apache.org/jira/secure/attachment/12803562/YARN-4577.20160511.1.patch JIRA Issue YARN-4577 Optional Tests asflicense compile javac javadoc mvninstall mvnsite unit findbugs checkstyle uname Linux e71cd162ac8f 3.13.0-36-lowlatency #63-Ubuntu SMP PREEMPT Wed Sep 3 21:56:12 UTC 2014 x86_64 x86_64 x86_64 GNU/Linux Build tool maven Personality /testptch/hadoop/patchprocess/precommit/personality/provided.sh git revision trunk / d464f4d Default Java 1.7.0_95 Multi-JDK versions /usr/lib/jvm/java-8-oracle:1.8.0_91 /usr/lib/jvm/java-7-openjdk-amd64:1.7.0_95 findbugs v3.0.0 JDK v1.7.0_95 Test Results https://builds.apache.org/job/PreCommit-YARN-Build/11426/testReport/ modules C: hadoop-common-project/hadoop-common hadoop-yarn-project/hadoop-yarn/hadoop-yarn-api hadoop-yarn-project/hadoop-yarn/hadoop-yarn-server/hadoop-yarn-server-nodemanager U: . Console output https://builds.apache.org/job/PreCommit-YARN-Build/11426/console Powered by Apache Yetus 0.2.0 http://yetus.apache.org This message was automatically generated. 
[![vvasudev](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Varun Vasudev](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=vvasudev) added a comment - [12/May/16 14:25](https://issues.apache.org/jira/browse/YARN-4577?focusedCommentId=15281551&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15281551)
Latest patch looks good to me. [sjlee0](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=sjlee0) what do you think?
[![vvasudev](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Varun Vasudev](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=vvasudev) added a comment - [12/May/16 14:25](https://issues.apache.org/jira/browse/YARN-4577?focusedCommentId=15281551&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15281551) Latest patch looks good to me. sjlee0 what do you think? 
[![sjlee0](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Sangjin Lee](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=sjlee0) added a comment - [12/May/16 17:07](https://issues.apache.org/jira/browse/YARN-4577?focusedCommentId=15281757&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15281757)
+1. Committing shortly. I'm going to commit to trunk and branch-2 (2.9). Do we need/want this for 2.8.0 as well?
[![sjlee0](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Sangjin Lee](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=sjlee0) added a comment - [12/May/16 17:07](https://issues.apache.org/jira/browse/YARN-4577?focusedCommentId=15281757&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15281757) +1. Committing shortly. I'm going to commit to trunk and branch-2 (2.9). Do we need/want this for 2.8.0 as well? 
[![xgong](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10443) Xuan Gong](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=xgong) added a comment - [12/May/16 17:14](https://issues.apache.org/jira/browse/YARN-4577?focusedCommentId=15281771&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15281771)
[sjlee0](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=sjlee0)  
Please commit into trunk and branch-2. Thanks
[![xgong](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10443) Xuan Gong](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=xgong) added a comment - [12/May/16 17:14](https://issues.apache.org/jira/browse/YARN-4577?focusedCommentId=15281771&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15281771) sjlee0 Please commit into trunk and branch-2. Thanks 
[![sjlee0](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Sangjin Lee](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=sjlee0) added a comment - [12/May/16 17:20](https://issues.apache.org/jira/browse/YARN-4577?focusedCommentId=15281780&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15281780)
Committed the patch to trunk and branch-2. Thanks [xgong](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=xgong) for your contribution! Thanks [steve_l](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=steve_l), [gtCarrera9](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=gtCarrera9), [vinodkv](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=vinodkv), and [vvasudev](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=vvasudev) for your reviews.
[xgong](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=xgong), do you think this warrants some release notes? If so, do you mind adding a little?
[![sjlee0](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Sangjin Lee](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=sjlee0) added a comment - [12/May/16 17:20](https://issues.apache.org/jira/browse/YARN-4577?focusedCommentId=15281780&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15281780) Committed the patch to trunk and branch-2. Thanks xgong for your contribution! Thanks steve_l , gtCarrera9 , vinodkv , and vvasudev for your reviews. xgong , do you think this warrants some release notes? If so, do you mind adding a little? 
[![hudson](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Hudson](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=hudson) added a comment - [12/May/16 18:50](https://issues.apache.org/jira/browse/YARN-4577?focusedCommentId=15281911&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15281911)
SUCCESS: Integrated in Hadoop-trunk-Commit #9753 (See <https://builds.apache.org/job/Hadoop-trunk-Commit/9753/>)  
[~~YARN-4577~~](https://issues.apache.org/jira/browse/YARN-4577 "Enable aux services to have their own custom classpath/jar file"). Enable aux services to have their own custom classpath/jar (sjlee: rev 0bbe01f8d56191edfba3b50fb9f8859a0b3f826f)
  * hadoop-yarn-project/hadoop-yarn/hadoop-yarn-server/hadoop-yarn-server-nodemanager/src/main/java/org/apache/hadoop/yarn/server/nodemanager/containermanager/AuxServices.java
  * hadoop-yarn-project/hadoop-yarn/hadoop-yarn-server/hadoop-yarn-server-nodemanager/src/test/java/org/apache/hadoop/yarn/server/nodemanager/containermanager/TestAuxServices.java
  * hadoop-yarn-project/hadoop-yarn/hadoop-yarn-api/src/main/java/org/apache/hadoop/yarn/conf/YarnConfiguration.java
  * hadoop-common-project/hadoop-common/src/test/java/org/apache/hadoop/util/JarFinder.java
  * hadoop-common-project/hadoop-common/src/test/java/org/apache/hadoop/util/TestRunJar.java
  * hadoop-yarn-project/hadoop-yarn/hadoop-yarn-server/hadoop-yarn-server-nodemanager/src/main/java/org/apache/hadoop/yarn/server/nodemanager/containermanager/AuxiliaryServiceWithCustomClassLoader.java


[![hudson](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Hudson](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=hudson) added a comment - [12/May/16 18:50](https://issues.apache.org/jira/browse/YARN-4577?focusedCommentId=15281911&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15281911) SUCCESS: Integrated in Hadoop-trunk-Commit #9753 (See https://builds.apache.org/job/Hadoop-trunk-Commit/9753/ ) YARN-4577 . Enable aux services to have their own custom classpath/jar (sjlee: rev 0bbe01f8d56191edfba3b50fb9f8859a0b3f826f) hadoop-yarn-project/hadoop-yarn/hadoop-yarn-server/hadoop-yarn-server-nodemanager/src/main/java/org/apache/hadoop/yarn/server/nodemanager/containermanager/AuxServices.java hadoop-yarn-project/hadoop-yarn/hadoop-yarn-server/hadoop-yarn-server-nodemanager/src/test/java/org/apache/hadoop/yarn/server/nodemanager/containermanager/TestAuxServices.java hadoop-yarn-project/hadoop-yarn/hadoop-yarn-api/src/main/java/org/apache/hadoop/yarn/conf/YarnConfiguration.java hadoop-common-project/hadoop-common/src/test/java/org/apache/hadoop/util/JarFinder.java hadoop-common-project/hadoop-common/src/test/java/org/apache/hadoop/util/TestRunJar.java hadoop-yarn-project/hadoop-yarn/hadoop-yarn-server/hadoop-yarn-server-nodemanager/src/main/java/org/apache/hadoop/yarn/server/nodemanager/containermanager/AuxiliaryServiceWithCustomClassLoader.java 
[![tonydoen](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=34045) tonydoen](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=tonydoen) added a comment - [17/Feb/22 03:14](https://issues.apache.org/jira/browse/YARN-4577?focusedCommentId=17493624&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-17493624) - edited
Thanks [xgong](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=xgong) , xkrogen@apache.org ![](https://issues.apache.org/jira/images/icons/mail_small.gif)for your contribution!
we have tried to run multiple versions of the Spark Shuffle Service according <https://github.com/apache/spark/blob/master/docs/running-on-yarn.md>
but, it wont work. any suggestion, we would appreciate it.
[yarn-site.xml] configuration

```
...
  <property>
    <name>yarn.nodemanager.aux-services</name>
    <value>mapreduce_shuffle,spark_shuffle_1_6,spark_shuffle_3_2</value>
  </property>
  <property>
    <name>yarn.nodemanager.aux-services.mapreduce_shuffle.class&lt;/name>
    <value>org.apache.hadoop.mapred.ShuffleHandler</value>
  </property>
  <property>
    <name>yarn.nodemanager.aux-services.spark_shuffle_1_6.class&lt;/name>
    <value>org.apache.spark.network.yarn.YarnShuffleService</value>
  </property>
  <property>
    <name>yarn.nodemanager.aux-services.spark_shuffle_1_6.classpath</name>
    <value>/app/yarn/c4prc-cluster/nodemanager/spark-yarn-shuffle-lib/spark-1-6-yarn-shuffle-lib,/app/yarn/c4prc-cluster/nodemanager/spark-yarn-shuffle-lib/spark-1-6-yarn-shuffle-config</value>
  </property>
  <property>
    <name>yarn.nodemanager.aux-services.spark_shuffle_3_2.class&lt;/name>
    <value>org.apache.spark.network.yarn.YarnShuffleService</value>
  </property>
  <property>
    <name>yarn.nodemanager.aux-services.spark_shuffle_3_2.classpath</name>
    <value>/app/yarn/c4prc-cluster/nodemanager/spark-yarn-shuffle-lib/spark-3-2-yarn-shuffle-lib,/app/yarn/c4prc-cluster/nodemanager/spark-yarn-shuffle-lib/spark-3-2-yarn-shuffle-config</value>
  </property>
...


```

/app/yarn/c4prc-cluster/nodemanager/spark-yarn-shuffle-lib/spark-3-2-yarn-shuffle-lib
is spark-yarn-shuffle lib location
/app/yarn/c4prc-cluster/nodemanager/spark-yarn-shuffle-lib/spark-3-2-yarn-shuffle-config
is spark-yarn-shuffle config, just one file named [spark-shuffle-site.xml] is in the above path.
[spark-shuffle-site.xml] content is

```
<configuration>
  <property>
    <name>spark.shuffle.service.port</name>
    <value>20811</value>
  </property>
  <property>
    <name>spark.yarn.shuffle.service.metrics.namespace</name>
    <value>sparkShuffleService1</value>
  </property>
</configuration> 
```

[![tonydoen](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=34045) tonydoen](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=tonydoen) added a comment - [17/Feb/22 03:14](https://issues.apache.org/jira/browse/YARN-4577?focusedCommentId=17493624&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-17493624) - edited Thanks xgong , xkrogen@apache.org for your contribution! we have tried to run multiple versions of the Spark Shuffle Service according https://github.com/apache/spark/blob/master/docs/running-on-yarn.md but, it wont work. any suggestion, we would appreciate it. [yarn-site.xml] configuration ... <property> <name>yarn.nodemanager.aux-services</name> <value>mapreduce_shuffle,spark_shuffle_1_6,spark_shuffle_3_2</value> </property> <property> <name>yarn.nodemanager.aux-services.mapreduce_shuffle. class& lt;/name> <value>org.apache.hadoop.mapred.ShuffleHandler</value> </property> <property> <name>yarn.nodemanager.aux-services.spark_shuffle_1_6. class& lt;/name> <value>org.apache.spark.network.yarn.YarnShuffleService</value> </property> <property> <name>yarn.nodemanager.aux-services.spark_shuffle_1_6.classpath</name> <value>/app/yarn/c4prc-cluster/nodemanager/spark-yarn-shuffle-lib/spark-1-6-yarn-shuffle-lib,/app/yarn/c4prc-cluster/nodemanager/spark-yarn-shuffle-lib/spark-1-6-yarn-shuffle-config</value> </property> <property> <name>yarn.nodemanager.aux-services.spark_shuffle_3_2. class& lt;/name> <value>org.apache.spark.network.yarn.YarnShuffleService</value> </property> <property> <name>yarn.nodemanager.aux-services.spark_shuffle_3_2.classpath</name> <value>/app/yarn/c4prc-cluster/nodemanager/spark-yarn-shuffle-lib/spark-3-2-yarn-shuffle-lib,/app/yarn/c4prc-cluster/nodemanager/spark-yarn-shuffle-lib/spark-3-2-yarn-shuffle-config</value> </property> ... /app/yarn/c4prc-cluster/nodemanager/spark-yarn-shuffle-lib/spark-3-2-yarn-shuffle-lib is spark-yarn-shuffle lib location /app/yarn/c4prc-cluster/nodemanager/spark-yarn-shuffle-lib/spark-3-2-yarn-shuffle-config is spark-yarn-shuffle config, just one file named [spark-shuffle-site.xml] is in the above path. [spark-shuffle-site.xml] content is <configuration> <property> <name>spark.shuffle.service.port</name> <value>20811</value> </property> <property> <name>spark.yarn.shuffle.service.metrics.namespace</name> <value>sparkShuffleService1</value> </property> </configuration>
[![tonydoen](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=34045) tonydoen](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=tonydoen) added a comment - [28/Feb/22 08:57](https://issues.apache.org/jira/browse/YARN-4577?focusedCommentId=17498775&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-17498775)
Thanks, I have solved the problem
[![tonydoen](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=34045) tonydoen](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=tonydoen) added a comment - [28/Feb/22 08:57](https://issues.apache.org/jira/browse/YARN-4577?focusedCommentId=17498775&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-17498775) Thanks, I have solved the problem 
[![Deegue](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Deegue](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=Deegue) added a comment - [28/Feb/22 12:27](https://issues.apache.org/jira/browse/YARN-4577?focusedCommentId=17498873&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-17498873)
Hi [tonydoen](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=tonydoen), am meeting the same problem via spark 3.2, can you share your solution? 
[![Deegue](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Deegue](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=Deegue) added a comment - [28/Feb/22 12:27](https://issues.apache.org/jira/browse/YARN-4577?focusedCommentId=17498873&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-17498873) Hi tonydoen , am meeting the same problem via spark 3.2, can you share your solution? 
[![koodin9](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=34044) SeongHoon Ku](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=koodin9) added a comment - [15/Mar/22 04:20](https://issues.apache.org/jira/browse/YARN-4577?focusedCommentId=17506685&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-17506685)
[Deegue](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=Deegue) In my case I solved it by using colon when writing %s.classpath instead of commas. 
[![koodin9](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=34044) SeongHoon Ku](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=koodin9) added a comment - [15/Mar/22 04:20](https://issues.apache.org/jira/browse/YARN-4577?focusedCommentId=17506685&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-17506685) Deegue In my case I solved it by using colon when writing %s.classpath instead of commas. 
[![tonydoen](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=34045) tonydoen](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=tonydoen) added a comment - [20/Mar/22 10:25](https://issues.apache.org/jira/browse/YARN-4577?focusedCommentId=17509421&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-17509421) - edited
[Deegue](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=Deegue) In my case I solved it by the same way like [koodin9](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=koodin9)

```
  yarn.nodemanager.aux-services = spark_shuffle_x,spark_shuffle_y
  yarn.nodemanager.aux-services.spark_shuffle_x.classpath = /path/to/spark-x-yarn-shuffle.jar:/path/to/spark-x-config
  yarn.nodemanager.aux-services.spark_shuffle_y.classpath = /path/to/spark-y-yarn-shuffle.jar:/path/to/spark-y-config 
```

[![tonydoen](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=34045) tonydoen](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=tonydoen) added a comment - [20/Mar/22 10:25](https://issues.apache.org/jira/browse/YARN-4577?focusedCommentId=17509421&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-17509421) - edited Deegue In my case I solved it by the same way like koodin9 yarn.nodemanager.aux-services = spark_shuffle_x,spark_shuffle_y yarn.nodemanager.aux-services.spark_shuffle_x.classpath = /path/to/spark-x-yarn-shuffle.jar:/path/to/spark-x-config yarn.nodemanager.aux-services.spark_shuffle_y.classpath = /path/to/spark-y-yarn-shuffle.jar:/path/to/spark-y-config 
#### People 

Assignee: 
     ![xgong](https://issues.apache.org/jira/secure/useravatar?size=small&avatarId=10443) Xuan Gong  

Reporter: 
     ![xgong](https://issues.apache.org/jira/secure/useravatar?size=small&avatarId=10443) Xuan Gong  

Votes:
     0 Vote for this issue 

Watchers:
     18 Start watching this issue
#### Dates 

Created: 
     11/Jan/16 17:35 

Updated: 
     20/Mar/22 10:26 

Resolved: 
     12/May/16 17:20
  * Atlassian Jira [Project Management Software](https://www.atlassian.com/software/jira)
  * [About Jira](https://issues.apache.org/jira/secure/AboutPage.jspa/secure/AboutPage.jspa)
  * [Report a problem](https://issues.apache.org/jira/secure/CreateIssue!default.jspa)


Powered by a free Atlassian [Jira](http://www.atlassian.com/software/jira) open source license for Apache Software Foundation. Try Jira - [bug tracking software](http://www.atlassian.com/software/jira) for _your_ team. 
[Atlassian](http://www.atlassian.com/)
[](javascript:;)[](javascript:;)

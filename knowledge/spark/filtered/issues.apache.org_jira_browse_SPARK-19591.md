[Log in](https://issues.apache.org/jira/login.jsp?os_destination=%2Fbrowse%2FSPARK-19591)[Skip to main content](https://issues.apache.org/jira/browse/SPARK-19591#main)[Skip to sidebar](https://issues.apache.org/jira/browse/SPARK-19591#sidebar)
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
  * [Log In](https://issues.apache.org/jira/login.jsp?os_destination=%2Fbrowse%2FSPARK-19591)


Public signup for this instance is **disabled**. Go to our [Self serve sign up page](https://selfserve.apache.org/jira-account.html) to request an account. Report potential security issues [privately](https://apache.org/security/#reporting-a-vulnerability)
[![Spark](https://issues.apache.org/jira/secure/projectavatar?pid=12315420&avatarId=27346)![Project Type: software](https://issues.apache.org/jira/browse/SPARK-19591)](https://issues.apache.org/jira/projects/SPARK/summary "Spark")
# 
[Spark](https://issues.apache.org/jira/projects/SPARK/summary "Spark")
  * [Issues](https://issues.apache.org/jira/projects/SPARK/issues)
  * [Reports](https://issues.apache.org/jira/projects/SPARK?selectedItem=com.atlassian.jira.jira-projects-plugin:report-page)
  * [Components](https://issues.apache.org/jira/projects/SPARK?selectedItem=com.atlassian.jira.jira-projects-plugin:components-page)
  * [Roadmap](https://issues.apache.org/jira/projects/SPARK?selectedItem=biz.everit.jira.epic-roadmap:erfj-sidebar-roadmap)


![Uploaded image for project: 'Spark'](https://issues.apache.org/jira/secure/projectavatar?pid=12315420&avatarId=27346)
  1. [Spark](https://issues.apache.org/jira/browse/SPARK)
  2. [SPARK-19591](https://issues.apache.org/jira/browse/SPARK-19591)


# Add sample weights to decision trees
[Log In](https://issues.apache.org/jira/login.jsp?os_destination=%2Fbrowse%2FSPARK-19591 "Log In")
[ Export](https://issues.apache.org/jira/browse/SPARK-19591)
[XML](https://issues.apache.org/jira/si/jira.issueviews:issue-xml/SPARK-19591/SPARK-19591.xml)[Word](https://issues.apache.org/jira/si/jira.issueviews:issue-word/SPARK-19591/SPARK-19591.doc)[Printable](https://issues.apache.org/jira/si/jira.issueviews:issue-html/SPARK-19591/SPARK-19591.html)[JSON](https://issues.apache.org/jira/si/com.atlassian.jira.plugins.jira-importers-plugin:issue-json/SPARK-19591/SPARK-19591.json) 

#### Details
  * ** Type: ** ![](https://issues.apache.org/jira/secure/viewavatar?size=xsmall&avatarId=21141&avatarType=issuetype) New Feature 
  * **Status:** Closed
  * ** Priority: ** ![](https://issues.apache.org/jira/images/icons/priorities/major.svg) Major 
  * **Resolution:** Fixed 
  * ** Affects Version/s: ** 2.1.0
  * ** Fix Version/s:  ** [3.0.0](https://issues.apache.org/jira/issues/?jql=project+%3D+SPARK+AND+fixVersion+%3D+3.0.0 "3.0.0 ")
  * ** Component/s: ** [ML](https://issues.apache.org/jira/issues/?jql=project+%3D+SPARK+AND+component+%3D+ML "ML Features under the spark.ml package")
  * ** Labels: **
None


#### Description
Add sample weights to decision trees. See [~~SPARK-9478~~](https://issues.apache.org/jira/browse/SPARK-9478 "Add sample weights to Random Forest") for details on the design.
#### Attachments
#### Issue Links 

blocks
    
![New Feature - A new feature of the product, which has yet to be developed.](https://issues.apache.org/jira/secure/viewavatar?size=xsmall&avatarId=21141&avatarType=issuetype) [SPARK-9612](https://issues.apache.org/jira/browse/SPARK-9612) Add instance weight support for GBTs
  * ![Minor - Minor loss of function, or other problem where easy workaround is present.](https://issues.apache.org/jira/images/icons/priorities/minor.svg)
  * Resolved

    
![Improvement - An improvement or enhancement to an existing feature or task.](https://issues.apache.org/jira/secure/viewavatar?size=xsmall&avatarId=21140&avatarType=issuetype) [SPARK-9478](https://issues.apache.org/jira/browse/SPARK-9478) Add sample weights to Random Forest
  * ![Major - Major loss of function.](https://issues.apache.org/jira/images/icons/priorities/major.svg)
  * Closed



Is contained by
    
![Umbrella - An overarching type made of sub-tasks](https://issues.apache.org/jira/secure/viewavatar?size=xsmall&avatarId=21130&avatarType=issuetype) [SPARK-14045](https://issues.apache.org/jira/browse/SPARK-14045) DecisionTree improvement umbrella
  * ![Major - Major loss of function.](https://issues.apache.org/jira/images/icons/priorities/major.svg)
  * Resolved



is duplicated by
    
![Improvement - An improvement or enhancement to an existing feature or task.](https://issues.apache.org/jira/secure/viewavatar?size=xsmall&avatarId=21140&avatarType=issuetype) [SPARK-14599](https://issues.apache.org/jira/browse/SPARK-14599) BaggedPoint should support weighted instances.
  * ![Major - Major loss of function.](https://issues.apache.org/jira/images/icons/priorities/major.svg)
  * Resolved

    
![Improvement - An improvement or enhancement to an existing feature or task.](https://issues.apache.org/jira/secure/viewavatar?size=xsmall&avatarId=21140&avatarType=issuetype) [SPARK-9478](https://issues.apache.org/jira/browse/SPARK-9478) Add sample weights to Random Forest
  * ![Major - Major loss of function.](https://issues.apache.org/jira/images/icons/priorities/major.svg)
  * Closed



links to
    
![Pull request #16722](https://assets-cdn.github.com/favicon.ico) [[Github] Pull Request #16722 (sethah)](https://github.com/apache/spark/pull/16722)     
![Pull request #21632](https://assets-cdn.github.com/favicon.ico) [[Github] Pull Request #21632 (imatiach-msft)](https://github.com/apache/spark/pull/21632)     
![Web Link](https://github.com/favicon.ico) [GitHub Pull Request #16722](https://github.com/apache/spark/pull/16722)     
![Web Link](https://github.com/favicon.ico) [GitHub Pull Request #21632](https://github.com/apache/spark/pull/21632)     
![Web Link](https://github.com/favicon.ico) [GitHub Pull Request #23682](https://github.com/apache/spark/pull/23682)     
![Web Link](https://github.com/favicon.ico) [GitHub Pull Request #23818](https://github.com/apache/spark/pull/23818)
Show 6 more links (6 links to)
#### Sub-Tasks
  * Options
    * [Show All](https://issues.apache.org/jira/browse/SPARK-19591?subTaskView=all#issuetable "Show All")
    * [Show Open](https://issues.apache.org/jira/browse/SPARK-19591?subTaskView=unresolved#issuetable "Show Open")
    * [Bulk operation](https://issues.apache.org/jira/issue/bulkedit/BulkEdit1!default.jspa?reset=true&searchParent=SPARK-19591 "Bulk operation")
    * [Open issue navigator](https://issues.apache.org/jira/issues/?jql=parent%3DSPARK-19591 "Open issue navigator")

  
|  1.  | [Add outlierRatio option to testOutliersWithSmallWeights](https://issues.apache.org/jira/browse/SPARK-20183)  |  [ ![Sub-task](https://issues.apache.org/jira/secure/viewavatar?size=xsmall&avatarId=21146&avatarType=issuetype) ](https://issues.apache.org/jira/browse/SPARK-20183)  |  Closed  |  [Seth Hendrickson](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=sethah)  |  
| --- | --- | --- | --- | --- |  
#### Activity
  * [All](https://issues.apache.org/jira/browse/SPARK-19591?page=com.atlassian.jira.plugin.system.issuetabpanels:all-tabpanel)
  * Comments
  * [Work Log](https://issues.apache.org/jira/browse/SPARK-19591?page=com.atlassian.jira.plugin.system.issuetabpanels:worklog-tabpanel)
  * [History](https://issues.apache.org/jira/browse/SPARK-19591?page=com.atlassian.jira.plugin.system.issuetabpanels:changehistory-tabpanel)
  * [Activity](https://issues.apache.org/jira/browse/SPARK-19591?page=com.atlassian.streams.streams-jira-plugin:activity-stream-issue-tab)
  * [Transitions](https://issues.apache.org/jira/browse/SPARK-19591?page=com.googlecode.jira-suite-utilities:transitions-summary-tabpanel)


[ Ascending order - Click to sort in descending order ](https://issues.apache.org/jira/browse/SPARK-19591?actionOrder=desc "Ascending order - Click to sort in descending order")
[![apachespark](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Apache Spark](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=apachespark) added a comment - [14/Feb/17 05:21](https://issues.apache.org/jira/browse/SPARK-19591?focusedCommentId=15865078&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15865078)
User 'sethah' has created a pull request for this issue:  
<https://github.com/apache/spark/pull/16722>
[![apachespark](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Apache Spark](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=apachespark) added a comment - [14/Feb/17 05:21](https://issues.apache.org/jira/browse/SPARK-19591?focusedCommentId=15865078&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15865078) User 'sethah' has created a pull request for this issue: https://github.com/apache/spark/pull/16722 
[![apachespark](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Apache Spark](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=apachespark) added a comment - [25/Jun/18 05:01](https://issues.apache.org/jira/browse/SPARK-19591?focusedCommentId=16521855&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16521855)
User 'imatiach-msft' has created a pull request for this issue:  
<https://github.com/apache/spark/pull/21632>
[![apachespark](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Apache Spark](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=apachespark) added a comment - [25/Jun/18 05:01](https://issues.apache.org/jira/browse/SPARK-19591?focusedCommentId=16521855&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16521855) User 'imatiach-msft' has created a pull request for this issue: https://github.com/apache/spark/pull/21632 
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [10/Dec/18 23:04](https://issues.apache.org/jira/browse/SPARK-19591?focusedCommentId=16715737&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16715737)
imatiach-msft commented on issue #21632: [~~SPARK-19591~~](https://issues.apache.org/jira/browse/SPARK-19591 "Add sample weights to decision trees")[ML][MLlib] Add sample weights to decision trees  
URL: <https://github.com/apache/spark/pull/21632#issuecomment-446008052>
jenkins retest this please (updated PR to latest)
----------------------------------------------------------------  
This is an automated message from the Apache Git Service.  
To respond to the message, please log on GitHub and use the  
URL above to go to the specific comment.
For queries about this service, please contact Infrastructure at:  
users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [10/Dec/18 23:04](https://issues.apache.org/jira/browse/SPARK-19591?focusedCommentId=16715737&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16715737) imatiach-msft commented on issue #21632: SPARK-19591 [ML] [MLlib] Add sample weights to decision trees URL: https://github.com/apache/spark/pull/21632#issuecomment-446008052 jenkins retest this please (updated PR to latest) ---------------------------------------------------------------- This is an automated message from the Apache Git Service. To respond to the message, please log on GitHub and use the URL above to go to the specific comment. For queries about this service, please contact Infrastructure at: users@infra.apache.org 
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [10/Dec/18 23:07](https://issues.apache.org/jira/browse/SPARK-19591?focusedCommentId=16715742&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16715742)
SparkQA commented on issue #21632: [~~SPARK-19591~~](https://issues.apache.org/jira/browse/SPARK-19591 "Add sample weights to decision trees")[ML][MLlib] Add sample weights to decision trees  
URL: <https://github.com/apache/spark/pull/21632#issuecomment-446008972>
**[Test build #99937 has started](https://issues.apache.org/jira/browse/SPARK-19591#99937%20has%20started)(<https://amplab.cs.berkeley.edu/jenkins/job/SparkPullRequestBuilder/99937/testReport)**> for PR 21632 at commit [`1d303c8`](<https://github.com/apache/spark/commit/1d303c83e5c8c15876726811634e5658d70e5b49>).
----------------------------------------------------------------  
This is an automated message from the Apache Git Service.  
To respond to the message, please log on GitHub and use the  
URL above to go to the specific comment.
For queries about this service, please contact Infrastructure at:  
users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [10/Dec/18 23:07](https://issues.apache.org/jira/browse/SPARK-19591?focusedCommentId=16715742&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16715742) SparkQA commented on issue #21632: SPARK-19591 [ML] [MLlib] Add sample weights to decision trees URL: https://github.com/apache/spark/pull/21632#issuecomment-446008972 ** Test build #99937 has started ( https://amplab.cs.berkeley.edu/jenkins/job/SparkPullRequestBuilder/99937/testReport)** for PR 21632 at commit [`1d303c8`] ( https://github.com/apache/spark/commit/1d303c83e5c8c15876726811634e5658d70e5b49 ). ---------------------------------------------------------------- This is an automated message from the Apache Git Service. To respond to the message, please log on GitHub and use the URL above to go to the specific comment. For queries about this service, please contact Infrastructure at: users@infra.apache.org 
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [10/Dec/18 23:08](https://issues.apache.org/jira/browse/SPARK-19591?focusedCommentId=16715743&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16715743)
AmplabJenkins commented on issue #21632: [~~SPARK-19591~~](https://issues.apache.org/jira/browse/SPARK-19591 "Add sample weights to decision trees")[ML][MLlib] Add sample weights to decision trees  
URL: <https://github.com/apache/spark/pull/21632#issuecomment-446009051>
Merged build finished. Test PASSed.
----------------------------------------------------------------  
This is an automated message from the Apache Git Service.  
To respond to the message, please log on GitHub and use the  
URL above to go to the specific comment.
For queries about this service, please contact Infrastructure at:  
users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [10/Dec/18 23:08](https://issues.apache.org/jira/browse/SPARK-19591?focusedCommentId=16715743&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16715743) AmplabJenkins commented on issue #21632: SPARK-19591 [ML] [MLlib] Add sample weights to decision trees URL: https://github.com/apache/spark/pull/21632#issuecomment-446009051 Merged build finished. Test PASSed. ---------------------------------------------------------------- This is an automated message from the Apache Git Service. To respond to the message, please log on GitHub and use the URL above to go to the specific comment. For queries about this service, please contact Infrastructure at: users@infra.apache.org 
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [10/Dec/18 23:08](https://issues.apache.org/jira/browse/SPARK-19591?focusedCommentId=16715744&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16715744)
AmplabJenkins commented on issue #21632: [~~SPARK-19591~~](https://issues.apache.org/jira/browse/SPARK-19591 "Add sample weights to decision trees")[ML][MLlib] Add sample weights to decision trees  
URL: <https://github.com/apache/spark/pull/21632#issuecomment-446009060>
Test PASSed.  
Refer to this link for build results (access rights to CI server needed):   
<https://amplab.cs.berkeley.edu/jenkins//job/testing-k8s-prb-make-spark-distribution-unified/5942/>  
Test PASSed.
----------------------------------------------------------------  
This is an automated message from the Apache Git Service.  
To respond to the message, please log on GitHub and use the  
URL above to go to the specific comment.
For queries about this service, please contact Infrastructure at:  
users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [10/Dec/18 23:08](https://issues.apache.org/jira/browse/SPARK-19591?focusedCommentId=16715744&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16715744) AmplabJenkins commented on issue #21632: SPARK-19591 [ML] [MLlib] Add sample weights to decision trees URL: https://github.com/apache/spark/pull/21632#issuecomment-446009060 Test PASSed. Refer to this link for build results (access rights to CI server needed): https://amplab.cs.berkeley.edu/jenkins//job/testing-k8s-prb-make-spark-distribution-unified/5942/ Test PASSed. ---------------------------------------------------------------- This is an automated message from the Apache Git Service. To respond to the message, please log on GitHub and use the URL above to go to the specific comment. For queries about this service, please contact Infrastructure at: users@infra.apache.org 
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [10/Dec/18 23:08](https://issues.apache.org/jira/browse/SPARK-19591?focusedCommentId=16715745&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16715745)
AmplabJenkins removed a comment on issue #21632: [~~SPARK-19591~~](https://issues.apache.org/jira/browse/SPARK-19591 "Add sample weights to decision trees")[ML][MLlib] Add sample weights to decision trees  
URL: <https://github.com/apache/spark/pull/21632#issuecomment-446009051>
Merged build finished. Test PASSed.
----------------------------------------------------------------  
This is an automated message from the Apache Git Service.  
To respond to the message, please log on GitHub and use the  
URL above to go to the specific comment.
For queries about this service, please contact Infrastructure at:  
users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [10/Dec/18 23:08](https://issues.apache.org/jira/browse/SPARK-19591?focusedCommentId=16715745&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16715745) AmplabJenkins removed a comment on issue #21632: SPARK-19591 [ML] [MLlib] Add sample weights to decision trees URL: https://github.com/apache/spark/pull/21632#issuecomment-446009051 Merged build finished. Test PASSed. ---------------------------------------------------------------- This is an automated message from the Apache Git Service. To respond to the message, please log on GitHub and use the URL above to go to the specific comment. For queries about this service, please contact Infrastructure at: users@infra.apache.org 
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [10/Dec/18 23:08](https://issues.apache.org/jira/browse/SPARK-19591?focusedCommentId=16715746&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16715746)
AmplabJenkins removed a comment on issue #21632: [~~SPARK-19591~~](https://issues.apache.org/jira/browse/SPARK-19591 "Add sample weights to decision trees")[ML][MLlib] Add sample weights to decision trees  
URL: <https://github.com/apache/spark/pull/21632#issuecomment-446009060>
Test PASSed.  
Refer to this link for build results (access rights to CI server needed):   
<https://amplab.cs.berkeley.edu/jenkins//job/testing-k8s-prb-make-spark-distribution-unified/5942/>  
Test PASSed.
----------------------------------------------------------------  
This is an automated message from the Apache Git Service.  
To respond to the message, please log on GitHub and use the  
URL above to go to the specific comment.
For queries about this service, please contact Infrastructure at:  
users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [10/Dec/18 23:08](https://issues.apache.org/jira/browse/SPARK-19591?focusedCommentId=16715746&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16715746) AmplabJenkins removed a comment on issue #21632: SPARK-19591 [ML] [MLlib] Add sample weights to decision trees URL: https://github.com/apache/spark/pull/21632#issuecomment-446009060 Test PASSed. Refer to this link for build results (access rights to CI server needed): https://amplab.cs.berkeley.edu/jenkins//job/testing-k8s-prb-make-spark-distribution-unified/5942/ Test PASSed. ---------------------------------------------------------------- This is an automated message from the Apache Git Service. To respond to the message, please log on GitHub and use the URL above to go to the specific comment. For queries about this service, please contact Infrastructure at: users@infra.apache.org 
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 03:26](https://issues.apache.org/jira/browse/SPARK-19591?focusedCommentId=16716072&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16716072)
SparkQA commented on issue #21632: [~~SPARK-19591~~](https://issues.apache.org/jira/browse/SPARK-19591 "Add sample weights to decision trees")[ML][MLlib] Add sample weights to decision trees  
URL: <https://github.com/apache/spark/pull/21632#issuecomment-446059275>
**[Test build #99937 has finished](https://issues.apache.org/jira/browse/SPARK-19591#99937%20has%20finished)(<https://amplab.cs.berkeley.edu/jenkins/job/SparkPullRequestBuilder/99937/testReport)**> for PR 21632 at commit [`1d303c8`](<https://github.com/apache/spark/commit/1d303c83e5c8c15876726811634e5658d70e5b49>).
  * This patch passes all tests.
  * This patch merges cleanly.
  * This patch adds no public classes.


----------------------------------------------------------------  
This is an automated message from the Apache Git Service.  
To respond to the message, please log on GitHub and use the  
URL above to go to the specific comment.
For queries about this service, please contact Infrastructure at:  
users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 03:26](https://issues.apache.org/jira/browse/SPARK-19591?focusedCommentId=16716072&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16716072) SparkQA commented on issue #21632: SPARK-19591 [ML] [MLlib] Add sample weights to decision trees URL: https://github.com/apache/spark/pull/21632#issuecomment-446059275 ** Test build #99937 has finished ( https://amplab.cs.berkeley.edu/jenkins/job/SparkPullRequestBuilder/99937/testReport)** for PR 21632 at commit [`1d303c8`] ( https://github.com/apache/spark/commit/1d303c83e5c8c15876726811634e5658d70e5b49 ). This patch passes all tests. This patch merges cleanly. This patch adds no public classes. ---------------------------------------------------------------- This is an automated message from the Apache Git Service. To respond to the message, please log on GitHub and use the URL above to go to the specific comment. For queries about this service, please contact Infrastructure at: users@infra.apache.org 
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 03:27](https://issues.apache.org/jira/browse/SPARK-19591?focusedCommentId=16716073&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16716073)
SparkQA removed a comment on issue #21632: [~~SPARK-19591~~](https://issues.apache.org/jira/browse/SPARK-19591 "Add sample weights to decision trees")[ML][MLlib] Add sample weights to decision trees  
URL: <https://github.com/apache/spark/pull/21632#issuecomment-446008972>
**[Test build #99937 has started](https://issues.apache.org/jira/browse/SPARK-19591#99937%20has%20started)(<https://amplab.cs.berkeley.edu/jenkins/job/SparkPullRequestBuilder/99937/testReport)**> for PR 21632 at commit [`1d303c8`](<https://github.com/apache/spark/commit/1d303c83e5c8c15876726811634e5658d70e5b49>).
----------------------------------------------------------------  
This is an automated message from the Apache Git Service.  
To respond to the message, please log on GitHub and use the  
URL above to go to the specific comment.
For queries about this service, please contact Infrastructure at:  
users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 03:27](https://issues.apache.org/jira/browse/SPARK-19591?focusedCommentId=16716073&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16716073) SparkQA removed a comment on issue #21632: SPARK-19591 [ML] [MLlib] Add sample weights to decision trees URL: https://github.com/apache/spark/pull/21632#issuecomment-446008972 ** Test build #99937 has started ( https://amplab.cs.berkeley.edu/jenkins/job/SparkPullRequestBuilder/99937/testReport)** for PR 21632 at commit [`1d303c8`] ( https://github.com/apache/spark/commit/1d303c83e5c8c15876726811634e5658d70e5b49 ). ---------------------------------------------------------------- This is an automated message from the Apache Git Service. To respond to the message, please log on GitHub and use the URL above to go to the specific comment. For queries about this service, please contact Infrastructure at: users@infra.apache.org 
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 03:28](https://issues.apache.org/jira/browse/SPARK-19591?focusedCommentId=16716075&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16716075)
AmplabJenkins commented on issue #21632: [~~SPARK-19591~~](https://issues.apache.org/jira/browse/SPARK-19591 "Add sample weights to decision trees")[ML][MLlib] Add sample weights to decision trees  
URL: <https://github.com/apache/spark/pull/21632#issuecomment-446059600>
Merged build finished. Test PASSed.
----------------------------------------------------------------  
This is an automated message from the Apache Git Service.  
To respond to the message, please log on GitHub and use the  
URL above to go to the specific comment.
For queries about this service, please contact Infrastructure at:  
users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 03:28](https://issues.apache.org/jira/browse/SPARK-19591?focusedCommentId=16716075&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16716075) AmplabJenkins commented on issue #21632: SPARK-19591 [ML] [MLlib] Add sample weights to decision trees URL: https://github.com/apache/spark/pull/21632#issuecomment-446059600 Merged build finished. Test PASSed. ---------------------------------------------------------------- This is an automated message from the Apache Git Service. To respond to the message, please log on GitHub and use the URL above to go to the specific comment. For queries about this service, please contact Infrastructure at: users@infra.apache.org 
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 03:28](https://issues.apache.org/jira/browse/SPARK-19591?focusedCommentId=16716076&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16716076)
AmplabJenkins commented on issue #21632: [~~SPARK-19591~~](https://issues.apache.org/jira/browse/SPARK-19591 "Add sample weights to decision trees")[ML][MLlib] Add sample weights to decision trees  
URL: <https://github.com/apache/spark/pull/21632#issuecomment-446059603>
Test PASSed.  
Refer to this link for build results (access rights to CI server needed):   
<https://amplab.cs.berkeley.edu/jenkins//job/SparkPullRequestBuilder/99937/>  
Test PASSed.
----------------------------------------------------------------  
This is an automated message from the Apache Git Service.  
To respond to the message, please log on GitHub and use the  
URL above to go to the specific comment.
For queries about this service, please contact Infrastructure at:  
users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 03:28](https://issues.apache.org/jira/browse/SPARK-19591?focusedCommentId=16716076&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16716076) AmplabJenkins commented on issue #21632: SPARK-19591 [ML] [MLlib] Add sample weights to decision trees URL: https://github.com/apache/spark/pull/21632#issuecomment-446059603 Test PASSed. Refer to this link for build results (access rights to CI server needed): https://amplab.cs.berkeley.edu/jenkins//job/SparkPullRequestBuilder/99937/ Test PASSed. ---------------------------------------------------------------- This is an automated message from the Apache Git Service. To respond to the message, please log on GitHub and use the URL above to go to the specific comment. For queries about this service, please contact Infrastructure at: users@infra.apache.org 
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 03:29](https://issues.apache.org/jira/browse/SPARK-19591?focusedCommentId=16716077&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16716077)
AmplabJenkins removed a comment on issue #21632: [~~SPARK-19591~~](https://issues.apache.org/jira/browse/SPARK-19591 "Add sample weights to decision trees")[ML][MLlib] Add sample weights to decision trees  
URL: <https://github.com/apache/spark/pull/21632#issuecomment-446059600>
Merged build finished. Test PASSed.
----------------------------------------------------------------  
This is an automated message from the Apache Git Service.  
To respond to the message, please log on GitHub and use the  
URL above to go to the specific comment.
For queries about this service, please contact Infrastructure at:  
users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 03:29](https://issues.apache.org/jira/browse/SPARK-19591?focusedCommentId=16716077&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16716077) AmplabJenkins removed a comment on issue #21632: SPARK-19591 [ML] [MLlib] Add sample weights to decision trees URL: https://github.com/apache/spark/pull/21632#issuecomment-446059600 Merged build finished. Test PASSed. ---------------------------------------------------------------- This is an automated message from the Apache Git Service. To respond to the message, please log on GitHub and use the URL above to go to the specific comment. For queries about this service, please contact Infrastructure at: users@infra.apache.org 
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 03:29](https://issues.apache.org/jira/browse/SPARK-19591?focusedCommentId=16716078&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16716078)
AmplabJenkins removed a comment on issue #21632: [~~SPARK-19591~~](https://issues.apache.org/jira/browse/SPARK-19591 "Add sample weights to decision trees")[ML][MLlib] Add sample weights to decision trees  
URL: <https://github.com/apache/spark/pull/21632#issuecomment-446059603>
Test PASSed.  
Refer to this link for build results (access rights to CI server needed):   
<https://amplab.cs.berkeley.edu/jenkins//job/SparkPullRequestBuilder/99937/>  
Test PASSed.
----------------------------------------------------------------  
This is an automated message from the Apache Git Service.  
To respond to the message, please log on GitHub and use the  
URL above to go to the specific comment.
For queries about this service, please contact Infrastructure at:  
users@infra.apache.org
[![githubbot](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) ASF GitHub Bot](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=githubbot) added a comment - [11/Dec/18 03:29](https://issues.apache.org/jira/browse/SPARK-19591?focusedCommentId=16716078&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16716078) AmplabJenkins removed a comment on issue #21632: SPARK-19591 [ML] [MLlib] Add sample weights to decision trees URL: https://github.com/apache/spark/pull/21632#issuecomment-446059603 Test PASSed. Refer to this link for build results (access rights to CI server needed): https://amplab.cs.berkeley.edu/jenkins//job/SparkPullRequestBuilder/99937/ Test PASSed. ---------------------------------------------------------------- This is an automated message from the Apache Git Service. To respond to the message, please log on GitHub and use the URL above to go to the specific comment. For queries about this service, please contact Infrastructure at: users@infra.apache.org 
[![srowen](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Sean R. Owen](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=srowen) added a comment - [25/Jan/19 01:20](https://issues.apache.org/jira/browse/SPARK-19591?focusedCommentId=16751774&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16751774)
Issue resolved by pull request 21632  
<https://github.com/apache/spark/pull/21632>
[![srowen](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Sean R. Owen](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=srowen) added a comment - [25/Jan/19 01:20](https://issues.apache.org/jira/browse/SPARK-19591?focusedCommentId=16751774&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16751774) Issue resolved by pull request 21632 https://github.com/apache/spark/pull/21632 
#### People 

Assignee: 
     ![sethah](https://issues.apache.org/jira/secure/useravatar?size=small&avatarId=10452) Seth Hendrickson  

Reporter: 
     ![sethah](https://issues.apache.org/jira/secure/useravatar?size=small&avatarId=10452) Seth Hendrickson  

Votes:
     4 Vote for this issue 

Watchers:
     8 Start watching this issue
#### Dates 

Created: 
     14/Feb/17 05:19 

Updated: 
     15/Feb/26 20:11 

Resolved: 
     25/Jan/19 01:20
  * Atlassian Jira [Project Management Software](https://www.atlassian.com/software/jira)
  * [About Jira](https://issues.apache.org/jira/secure/AboutPage.jspa/secure/AboutPage.jspa)
  * [Report a problem](https://issues.apache.org/jira/secure/CreateIssue!default.jspa)


Powered by a free Atlassian [Jira](http://www.atlassian.com/software/jira) open source license for Apache Software Foundation. Try Jira - [bug tracking software](http://www.atlassian.com/software/jira) for _your_ team. 
[Atlassian](http://www.atlassian.com/)
[](javascript:;)[](javascript:;)

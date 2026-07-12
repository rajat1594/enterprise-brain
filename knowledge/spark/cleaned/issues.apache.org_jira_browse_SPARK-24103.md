[Log in](https://issues.apache.org/jira/login.jsp?os_destination=%2Fbrowse%2FSPARK-24103)[Skip to main content](https://issues.apache.org/jira/browse/SPARK-24103#main)[Skip to sidebar](https://issues.apache.org/jira/browse/SPARK-24103#sidebar)
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
  * [Log In](https://issues.apache.org/jira/login.jsp?os_destination=%2Fbrowse%2FSPARK-24103)

Public signup for this instance is **disabled**. Go to our [Self serve sign up page](https://selfserve.apache.org/jira-account.html) to request an account. Report potential security issues [privately](https://apache.org/security/#reporting-a-vulnerability)
[![Spark](https://issues.apache.org/jira/secure/projectavatar?pid=12315420&avatarId=27346)![Project Type: software](https://issues.apache.org/jira/browse/SPARK-24103)](https://issues.apache.org/jira/projects/SPARK/summary "Spark")
#
[Spark](https://issues.apache.org/jira/projects/SPARK/summary "Spark")
  * [Issues](https://issues.apache.org/jira/projects/SPARK/issues)
  * [Reports](https://issues.apache.org/jira/projects/SPARK?selectedItem=com.atlassian.jira.jira-projects-plugin:report-page)
  * [Components](https://issues.apache.org/jira/projects/SPARK?selectedItem=com.atlassian.jira.jira-projects-plugin:components-page)
  * [Roadmap](https://issues.apache.org/jira/projects/SPARK?selectedItem=biz.everit.jira.epic-roadmap:erfj-sidebar-roadmap)

![Uploaded image for project: 'Spark'](https://issues.apache.org/jira/secure/projectavatar?pid=12315420&avatarId=27346)
  1. [Spark](https://issues.apache.org/jira/browse/SPARK)
  2. [SPARK-24103](https://issues.apache.org/jira/browse/SPARK-24103)

# BinaryClassificationEvaluator should use sample weight data
[Log In](https://issues.apache.org/jira/login.jsp?os_destination=%2Fbrowse%2FSPARK-24103 "Log In")
[ Export](https://issues.apache.org/jira/browse/SPARK-24103)
[XML](https://issues.apache.org/jira/si/jira.issueviews:issue-xml/SPARK-24103/SPARK-24103.xml)[Word](https://issues.apache.org/jira/si/jira.issueviews:issue-word/SPARK-24103/SPARK-24103.doc)[Printable](https://issues.apache.org/jira/si/jira.issueviews:issue-html/SPARK-24103/SPARK-24103.html)[JSON](https://issues.apache.org/jira/si/com.atlassian.jira.plugins.jira-importers-plugin:issue-json/SPARK-24103/SPARK-24103.json)

#### Details
  * ** Type: ** ![](https://issues.apache.org/jira/secure/viewavatar?size=xsmall&avatarId=21140&avatarType=issuetype) Improvement
  * **Status:** Closed
  * ** Priority: ** ![](https://issues.apache.org/jira/images/icons/priorities/major.svg) Major
  * **Resolution:** Fixed
  * ** Affects Version/s: ** 2.0.2
  * ** Fix Version/s:  ** [3.0.0](https://issues.apache.org/jira/issues/?jql=project+%3D+SPARK+AND+fixVersion+%3D+3.0.0 "3.0.0 ")
  * ** Component/s: ** [ML](https://issues.apache.org/jira/issues/?jql=project+%3D+SPARK+AND+component+%3D+ML "ML Features under the spark.ml package")
  * ** Labels: **
    * [starter](https://issues.apache.org/jira/issues/?jql=labels+%3D+starter "starter")

#### Description
The LogisticRegression and LinearRegression models support training with a weight column, but the corresponding evaluators do not support computing metrics using those weights. This breaks model selection using CrossValidator.
#### Attachments
#### Issue Links

is a child of

![Improvement - An improvement or enhancement to an existing feature or task.](https://issues.apache.org/jira/secure/viewavatar?size=xsmall&avatarId=21140&avatarType=issuetype) [SPARK-18693](https://issues.apache.org/jira/browse/SPARK-18693) BinaryClassificationEvaluator, RegressionEvaluator, and MulticlassClassificationEvaluator should use sample weight data
  * ![Major - Major loss of function.](https://issues.apache.org/jira/images/icons/priorities/major.svg)
  * Resolved

links to

![Pull request #17084](https://assets-cdn.github.com/favicon.ico) [[Github] Pull Request #17084 (imatiach-msft)](https://github.com/apache/spark/pull/17084)
![Web Link](https://github.com/favicon.ico) [GitHub Pull Request #17084](https://github.com/apache/spark/pull/17084)
#### Activity
  * [All](https://issues.apache.org/jira/browse/SPARK-24103?page=com.atlassian.jira.plugin.system.issuetabpanels:all-tabpanel)
  * Comments
  * [Work Log](https://issues.apache.org/jira/browse/SPARK-24103?page=com.atlassian.jira.plugin.system.issuetabpanels:worklog-tabpanel)
  * [History](https://issues.apache.org/jira/browse/SPARK-24103?page=com.atlassian.jira.plugin.system.issuetabpanels:changehistory-tabpanel)
  * [Activity](https://issues.apache.org/jira/browse/SPARK-24103?page=com.atlassian.streams.streams-jira-plugin:activity-stream-issue-tab)
  * [Transitions](https://issues.apache.org/jira/browse/SPARK-24103?page=com.googlecode.jira-suite-utilities:transitions-summary-tabpanel)

[ Ascending order - Click to sort in descending order ](https://issues.apache.org/jira/browse/SPARK-24103?actionOrder=desc "Ascending order - Click to sort in descending order")
[![imatiach](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Ilya Matiach](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=imatiach) added a comment - [14/May/18 20:24](https://issues.apache.org/jira/browse/SPARK-24103?focusedCommentId=16474754&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16474754)
This issue is fixed by this PR:
<https://github.com/apache/spark/pull/17084>
[![imatiach](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Ilya Matiach](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=imatiach) added a comment - [14/May/18 20:24](https://issues.apache.org/jira/browse/SPARK-24103?focusedCommentId=16474754&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16474754) This issue is fixed by this PR: https://github.com/apache/spark/pull/17084
[![apachespark](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Apache Spark](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=apachespark) added a comment - [14/May/18 20:25](https://issues.apache.org/jira/browse/SPARK-24103?focusedCommentId=16474755&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16474755)
User 'imatiach-msft' has created a pull request for this issue:
<https://github.com/apache/spark/pull/17084>
[![apachespark](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Apache Spark](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=apachespark) added a comment - [14/May/18 20:25](https://issues.apache.org/jira/browse/SPARK-24103?focusedCommentId=16474755&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16474755) User 'imatiach-msft' has created a pull request for this issue: https://github.com/apache/spark/pull/17084
[![srowen](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Sean R. Owen](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=srowen) added a comment - [25/Feb/19 23:17](https://issues.apache.org/jira/browse/SPARK-24103?focusedCommentId=16777380&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16777380)
Issue resolved by pull request 17084
<https://github.com/apache/spark/pull/17084>
[![srowen](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Sean R. Owen](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=srowen) added a comment - [25/Feb/19 23:17](https://issues.apache.org/jira/browse/SPARK-24103?focusedCommentId=16777380&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16777380) Issue resolved by pull request 17084 https://github.com/apache/spark/pull/17084
#### People

Assignee:
     ![imatiach](https://issues.apache.org/jira/secure/useravatar?size=small&avatarId=10452) Ilya Matiach

Reporter:
     ![imatiach](https://issues.apache.org/jira/secure/useravatar?size=small&avatarId=10452) Ilya Matiach

Votes:
     0 Vote for this issue

Watchers:
     5 Start watching this issue
#### Dates

Created:
     26/Apr/18 15:52

Updated:
     15/Feb/26 20:10

Resolved:
     25/Feb/19 23:17
  * Atlassian Jira [Project Management Software](https://www.atlassian.com/software/jira)
  * [About Jira](https://issues.apache.org/jira/secure/AboutPage.jspa/secure/AboutPage.jspa)
  * [Report a problem](https://issues.apache.org/jira/secure/CreateIssue!default.jspa)

Powered by a free Atlassian [Jira](http://www.atlassian.com/software/jira) open source license for Apache Software Foundation. Try Jira - [bug tracking software](http://www.atlassian.com/software/jira) for _your_ team.
[Atlassian](http://www.atlassian.com/)
[](javascript:;)[](javascript:;)

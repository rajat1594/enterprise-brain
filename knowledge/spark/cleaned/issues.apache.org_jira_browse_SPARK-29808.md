[Log in](https://issues.apache.org/jira/login.jsp?os_destination=%2Fbrowse%2FSPARK-29808)[Skip to main content](https://issues.apache.org/jira/browse/SPARK-29808#main)[Skip to sidebar](https://issues.apache.org/jira/browse/SPARK-29808#sidebar)
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
  * [Log In](https://issues.apache.org/jira/login.jsp?os_destination=%2Fbrowse%2FSPARK-29808)

Public signup for this instance is **disabled**. Go to our [Self serve sign up page](https://selfserve.apache.org/jira-account.html) to request an account. Report potential security issues [privately](https://apache.org/security/#reporting-a-vulnerability)
[![Spark](https://issues.apache.org/jira/secure/projectavatar?pid=12315420&avatarId=27346)![Project Type: software](https://issues.apache.org/jira/browse/SPARK-29808)](https://issues.apache.org/jira/projects/SPARK/summary "Spark")
#
[Spark](https://issues.apache.org/jira/projects/SPARK/summary "Spark")
  * [Issues](https://issues.apache.org/jira/projects/SPARK/issues)
  * [Reports](https://issues.apache.org/jira/projects/SPARK?selectedItem=com.atlassian.jira.jira-projects-plugin:report-page)
  * [Components](https://issues.apache.org/jira/projects/SPARK?selectedItem=com.atlassian.jira.jira-projects-plugin:components-page)
  * [Roadmap](https://issues.apache.org/jira/projects/SPARK?selectedItem=biz.everit.jira.epic-roadmap:erfj-sidebar-roadmap)

![Uploaded image for project: 'Spark'](https://issues.apache.org/jira/secure/projectavatar?pid=12315420&avatarId=27346)
  1. [Spark](https://issues.apache.org/jira/browse/SPARK)
  2. [SPARK-29808](https://issues.apache.org/jira/browse/SPARK-29808)

# StopWordsRemover should support multi-cols
[Log In](https://issues.apache.org/jira/login.jsp?os_destination=%2Fbrowse%2FSPARK-29808 "Log In")
[ Export](https://issues.apache.org/jira/browse/SPARK-29808)
[XML](https://issues.apache.org/jira/si/jira.issueviews:issue-xml/SPARK-29808/SPARK-29808.xml)[Word](https://issues.apache.org/jira/si/jira.issueviews:issue-word/SPARK-29808/SPARK-29808.doc)[Printable](https://issues.apache.org/jira/si/jira.issueviews:issue-html/SPARK-29808/SPARK-29808.html)[JSON](https://issues.apache.org/jira/si/com.atlassian.jira.plugins.jira-importers-plugin:issue-json/SPARK-29808/SPARK-29808.json)

#### Details
  * ** Type: ** ![](https://issues.apache.org/jira/secure/viewavatar?size=xsmall&avatarId=21140&avatarType=issuetype) Improvement
  * **Status:** Closed
  * ** Priority: ** ![](https://issues.apache.org/jira/images/icons/priorities/minor.svg) Minor
  * **Resolution:** Fixed
  * ** Affects Version/s: ** 3.0.0
  * ** Fix Version/s:  ** [3.0.0](https://issues.apache.org/jira/issues/?jql=project+%3D+SPARK+AND+fixVersion+%3D+3.0.0 "3.0.0 ")
  * ** Component/s: ** [ML](https://issues.apache.org/jira/issues/?jql=project+%3D+SPARK+AND+component+%3D+ML "ML Features under the spark.ml package"), [PySpark](https://issues.apache.org/jira/issues/?jql=project+%3D+SPARK+AND+component+%3D+PySpark "PySpark Spark Python API")
  * ** Labels: **
None

#### Description
As a basic Transformer, StopWordsRemover should support multi-cols.
Param stopWords can be applied across all columns.
#### Attachments
#### Issue Links

links to

![Web Link](https://github.com/favicon.ico) [GitHub Pull Request #26480](https://github.com/apache/spark/pull/26480)
#### Activity
  * [All](https://issues.apache.org/jira/browse/SPARK-29808?page=com.atlassian.jira.plugin.system.issuetabpanels:all-tabpanel)
  * Comments
  * [Work Log](https://issues.apache.org/jira/browse/SPARK-29808?page=com.atlassian.jira.plugin.system.issuetabpanels:worklog-tabpanel)
  * [History](https://issues.apache.org/jira/browse/SPARK-29808?page=com.atlassian.jira.plugin.system.issuetabpanels:changehistory-tabpanel)
  * [Activity](https://issues.apache.org/jira/browse/SPARK-29808?page=com.atlassian.streams.streams-jira-plugin:activity-stream-issue-tab)
  * [Transitions](https://issues.apache.org/jira/browse/SPARK-29808?page=com.googlecode.jira-suite-utilities:transitions-summary-tabpanel)

[ Ascending order - Click to sort in descending order ](https://issues.apache.org/jira/browse/SPARK-29808?actionOrder=desc "Ascending order - Click to sort in descending order")
[![huaxingao](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Huaxin Gao](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=huaxingao) added a comment - [11/Nov/19 17:49](https://issues.apache.org/jira/browse/SPARK-29808?focusedCommentId=16971757&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16971757)
I will work on this. [podongfeng](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=podongfeng)
[![huaxingao](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Huaxin Gao](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=huaxingao) added a comment - [11/Nov/19 17:49](https://issues.apache.org/jira/browse/SPARK-29808?focusedCommentId=16971757&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16971757) I will work on this. podongfeng
[![srowen](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Sean R. Owen](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=srowen) added a comment - [13/Nov/19 14:18](https://issues.apache.org/jira/browse/SPARK-29808?focusedCommentId=16973381&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16973381)
Issue resolved by pull request 26480
<https://github.com/apache/spark/pull/26480>
[![srowen](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Sean R. Owen](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=srowen) added a comment - [13/Nov/19 14:18](https://issues.apache.org/jira/browse/SPARK-29808?focusedCommentId=16973381&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16973381) Issue resolved by pull request 26480 https://github.com/apache/spark/pull/26480
#### People

Assignee:
     ![huaxingao](https://issues.apache.org/jira/secure/useravatar?size=small&avatarId=10452) Huaxin Gao

Reporter:
     ![podongfeng](https://issues.apache.org/jira/secure/useravatar?size=small&avatarId=10452) Ruifeng Zheng

Votes:
     0 Vote for this issue

Watchers:
     3 Start watching this issue
#### Dates

Created:
     09/Nov/19 07:31

Updated:
     15/Feb/26 20:00

Resolved:
     13/Nov/19 14:18
  * Atlassian Jira [Project Management Software](https://www.atlassian.com/software/jira)
  * [About Jira](https://issues.apache.org/jira/secure/AboutPage.jspa/secure/AboutPage.jspa)
  * [Report a problem](https://issues.apache.org/jira/secure/CreateIssue!default.jspa)

Powered by a free Atlassian [Jira](http://www.atlassian.com/software/jira) open source license for Apache Software Foundation. Try Jira - [bug tracking software](http://www.atlassian.com/software/jira) for _your_ team.
[Atlassian](http://www.atlassian.com/)
[](javascript:;)[](javascript:;)

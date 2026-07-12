[Log in](https://issues.apache.org/jira/login.jsp?os_destination=%2Fbrowse%2FSPARK-16692)[Skip to main content](https://issues.apache.org/jira/browse/SPARK-16692#main)[Skip to sidebar](https://issues.apache.org/jira/browse/SPARK-16692#sidebar)
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
  * [Log In](https://issues.apache.org/jira/login.jsp?os_destination=%2Fbrowse%2FSPARK-16692)

Public signup for this instance is **disabled**. Go to our [Self serve sign up page](https://selfserve.apache.org/jira-account.html) to request an account. Report potential security issues [privately](https://apache.org/security/#reporting-a-vulnerability)
[![Spark](https://issues.apache.org/jira/secure/projectavatar?pid=12315420&avatarId=27346)![Project Type: software](https://issues.apache.org/jira/browse/SPARK-16692)](https://issues.apache.org/jira/projects/SPARK/summary "Spark")
#
[Spark](https://issues.apache.org/jira/projects/SPARK/summary "Spark")
  * [Issues](https://issues.apache.org/jira/projects/SPARK/issues)
  * [Reports](https://issues.apache.org/jira/projects/SPARK?selectedItem=com.atlassian.jira.jira-projects-plugin:report-page)
  * [Components](https://issues.apache.org/jira/projects/SPARK?selectedItem=com.atlassian.jira.jira-projects-plugin:components-page)
  * [Roadmap](https://issues.apache.org/jira/projects/SPARK?selectedItem=biz.everit.jira.epic-roadmap:erfj-sidebar-roadmap)

![Uploaded image for project: 'Spark'](https://issues.apache.org/jira/secure/projectavatar?pid=12315420&avatarId=27346)
  1. [Spark](https://issues.apache.org/jira/browse/SPARK)
  2. [SPARK-16692](https://issues.apache.org/jira/browse/SPARK-16692)

#  multilabel classification to DataFrame, ML
[Log In](https://issues.apache.org/jira/login.jsp?os_destination=%2Fbrowse%2FSPARK-16692 "Log In")
[ Export](https://issues.apache.org/jira/browse/SPARK-16692)
[XML](https://issues.apache.org/jira/si/jira.issueviews:issue-xml/SPARK-16692/SPARK-16692.xml)[Word](https://issues.apache.org/jira/si/jira.issueviews:issue-word/SPARK-16692/SPARK-16692.doc)[Printable](https://issues.apache.org/jira/si/jira.issueviews:issue-html/SPARK-16692/SPARK-16692.html)[JSON](https://issues.apache.org/jira/si/com.atlassian.jira.plugins.jira-importers-plugin:issue-json/SPARK-16692/SPARK-16692.json)

#### Details
  * ** Type: ** ![](https://issues.apache.org/jira/secure/viewavatar?size=xsmall&avatarId=21140&avatarType=issuetype) Improvement
  * **Status:** Closed
  * ** Priority: ** ![](https://issues.apache.org/jira/images/icons/priorities/minor.svg) Minor
  * **Resolution:** Fixed
  * ** Affects Version/s: ** None
  * ** Fix Version/s:  ** [3.0.0](https://issues.apache.org/jira/issues/?jql=project+%3D+SPARK+AND+fixVersion+%3D+3.0.0 "3.0.0 ")
  * ** Component/s: ** [ML](https://issues.apache.org/jira/issues/?jql=project+%3D+SPARK+AND+component+%3D+ML "ML Features under the spark.ml package"), [MLlib](https://issues.apache.org/jira/issues/?jql=project+%3D+SPARK+AND+component+%3D+MLlib "MLlib Machine learning library")
  * ** Labels: **
None

#### Description
For the multi labels evaluations. There is a method to in MLlib named MultilabelMetrics: A multilabel classification problem involves mapping each sample in a dataset to a set of class labels. In this type of classification problem, the labels are not mutually exclusive. For example, when classifying a set of news articles into topics, a single article might be both science and politics.
Added this method to support DataFrame in ML.
#### Attachments
#### Issue Links

links to

![Pull request #14325](https://assets-cdn.github.com/favicon.ico) [[Github] Pull Request #14325 (liwzhi)](https://github.com/apache/spark/pull/14325)
![Web Link](https://github.com/favicon.ico) [GitHub Pull Request #14325](https://github.com/apache/spark/pull/14325)
![Web Link](https://github.com/favicon.ico) [GitHub Pull Request #24777](https://github.com/apache/spark/pull/24777)
#### Activity
  * [All](https://issues.apache.org/jira/browse/SPARK-16692?page=com.atlassian.jira.plugin.system.issuetabpanels:all-tabpanel)
  * Comments
  * [Work Log](https://issues.apache.org/jira/browse/SPARK-16692?page=com.atlassian.jira.plugin.system.issuetabpanels:worklog-tabpanel)
  * [History](https://issues.apache.org/jira/browse/SPARK-16692?page=com.atlassian.jira.plugin.system.issuetabpanels:changehistory-tabpanel)
  * [Activity](https://issues.apache.org/jira/browse/SPARK-16692?page=com.atlassian.streams.streams-jira-plugin:activity-stream-issue-tab)
  * [Transitions](https://issues.apache.org/jira/browse/SPARK-16692?page=com.googlecode.jira-suite-utilities:transitions-summary-tabpanel)

[ Ascending order - Click to sort in descending order ](https://issues.apache.org/jira/browse/SPARK-16692?actionOrder=desc "Ascending order - Click to sort in descending order")
[![apachespark](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Apache Spark](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=apachespark) added a comment - [23/Jul/16 06:39](https://issues.apache.org/jira/browse/SPARK-16692?focusedCommentId=15390576&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15390576)
User 'liwzhi' has created a pull request for this issue:
<https://github.com/apache/spark/pull/14325>
[![apachespark](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Apache Spark](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=apachespark) added a comment - [23/Jul/16 06:39](https://issues.apache.org/jira/browse/SPARK-16692?focusedCommentId=15390576&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15390576) User 'liwzhi' has created a pull request for this issue: https://github.com/apache/spark/pull/14325
[![srowen](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Sean R. Owen](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=srowen) added a comment - [13/Jun/19 13:01](https://issues.apache.org/jira/browse/SPARK-16692?focusedCommentId=16863057&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16863057)
Issue resolved by pull request 24777
<https://github.com/apache/spark/pull/24777>
[![srowen](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Sean R. Owen](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=srowen) added a comment - [13/Jun/19 13:01](https://issues.apache.org/jira/browse/SPARK-16692?focusedCommentId=16863057&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16863057) Issue resolved by pull request 24777 https://github.com/apache/spark/pull/24777
#### People

Assignee:
     ![podongfeng](https://issues.apache.org/jira/secure/useravatar?size=small&avatarId=10452) Ruifeng Zheng

Reporter:
     ![liwzhi](https://issues.apache.org/jira/secure/useravatar?size=small&avatarId=10452) Weizhi Li

Votes:
     0 Vote for this issue

Watchers:
     4 Start watching this issue
#### Dates

Created:
     23/Jul/16 05:40

Updated:
     15/Feb/26 20:10

Resolved:
     13/Jun/19 13:01
#### Time Tracking

Estimated:

|  ![Original Estimate - 1h](https://issues.apache.org/jira/images/border/spacer.gif)  |
| --- |      1h

Remaining:

|  ![Remaining Estimate - 1h](https://issues.apache.org/jira/images/border/spacer.gif)  |
| --- |      1h

Logged:

|  ![Time Spent - Not Specified](https://issues.apache.org/jira/images/border/spacer.gif)  |
| --- |      Not Specified
  * Atlassian Jira [Project Management Software](https://www.atlassian.com/software/jira)
  * [About Jira](https://issues.apache.org/jira/secure/AboutPage.jspa/secure/AboutPage.jspa)
  * [Report a problem](https://issues.apache.org/jira/secure/CreateIssue!default.jspa)

Powered by a free Atlassian [Jira](http://www.atlassian.com/software/jira) open source license for Apache Software Foundation. Try Jira - [bug tracking software](http://www.atlassian.com/software/jira) for _your_ team.
[Atlassian](http://www.atlassian.com/)
[](javascript:;)[](javascript:;)

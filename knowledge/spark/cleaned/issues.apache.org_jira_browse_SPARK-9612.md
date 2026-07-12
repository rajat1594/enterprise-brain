[Log in](https://issues.apache.org/jira/login.jsp?os_destination=%2Fbrowse%2FSPARK-9612)[Skip to main content](https://issues.apache.org/jira/browse/SPARK-9612#main)[Skip to sidebar](https://issues.apache.org/jira/browse/SPARK-9612#sidebar)
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
  * [Log In](https://issues.apache.org/jira/login.jsp?os_destination=%2Fbrowse%2FSPARK-9612)

Public signup for this instance is **disabled**. Go to our [Self serve sign up page](https://selfserve.apache.org/jira-account.html) to request an account. Report potential security issues [privately](https://apache.org/security/#reporting-a-vulnerability)
[![Spark](https://issues.apache.org/jira/secure/projectavatar?pid=12315420&avatarId=27346)![Project Type: software](https://issues.apache.org/jira/browse/SPARK-9612)](https://issues.apache.org/jira/projects/SPARK/summary "Spark")
#
[Spark](https://issues.apache.org/jira/projects/SPARK/summary "Spark")
  * [Issues](https://issues.apache.org/jira/projects/SPARK/issues)
  * [Reports](https://issues.apache.org/jira/projects/SPARK?selectedItem=com.atlassian.jira.jira-projects-plugin:report-page)
  * [Components](https://issues.apache.org/jira/projects/SPARK?selectedItem=com.atlassian.jira.jira-projects-plugin:components-page)
  * [Roadmap](https://issues.apache.org/jira/projects/SPARK?selectedItem=biz.everit.jira.epic-roadmap:erfj-sidebar-roadmap)

![Uploaded image for project: 'Spark'](https://issues.apache.org/jira/secure/projectavatar?pid=12315420&avatarId=27346)
  1. [Spark](https://issues.apache.org/jira/browse/SPARK)
  2. [SPARK-9612](https://issues.apache.org/jira/browse/SPARK-9612)

# Add instance weight support for GBTs
[Log In](https://issues.apache.org/jira/login.jsp?os_destination=%2Fbrowse%2FSPARK-9612 "Log In")
[ Export](https://issues.apache.org/jira/browse/SPARK-9612)
[XML](https://issues.apache.org/jira/si/jira.issueviews:issue-xml/SPARK-9612/SPARK-9612.xml)[Word](https://issues.apache.org/jira/si/jira.issueviews:issue-word/SPARK-9612/SPARK-9612.doc)[Printable](https://issues.apache.org/jira/si/jira.issueviews:issue-html/SPARK-9612/SPARK-9612.html)[JSON](https://issues.apache.org/jira/si/com.atlassian.jira.plugins.jira-importers-plugin:issue-json/SPARK-9612/SPARK-9612.json)

#### Details
  * ** Type: ** ![](https://issues.apache.org/jira/secure/viewavatar?size=xsmall&avatarId=21141&avatarType=issuetype) New Feature
  * **Status:** Resolved
  * ** Priority: ** ![](https://issues.apache.org/jira/images/icons/priorities/minor.svg) Minor
  * **Resolution:** Fixed
  * ** Affects Version/s: ** None
  * ** Fix Version/s:  ** None
  * ** Component/s: ** [ML](https://issues.apache.org/jira/issues/?jql=project+%3D+SPARK+AND+component+%3D+ML "ML Features under the spark.ml package")
  * ** Labels: **
    * [bulk-closed](https://issues.apache.org/jira/issues/?jql=labels+%3D+bulk-closed "bulk-closed")

#### Description
GBT support for instance weights could be handled by:
  * sampling data before passing it to trees
  * passing weights to trees (requiring weight support for trees first, but probably better in the end)

#### Attachments
#### Issue Links

is blocked by

![New Feature - A new feature of the product, which has yet to be developed.](https://issues.apache.org/jira/secure/viewavatar?size=xsmall&avatarId=21141&avatarType=issuetype) [SPARK-19591](https://issues.apache.org/jira/browse/SPARK-19591) Add sample weights to decision trees
  * ![Major - Major loss of function.](https://issues.apache.org/jira/images/icons/priorities/major.svg)
  * Closed

Is contained by

![Umbrella - An overarching type made of sub-tasks](https://issues.apache.org/jira/secure/viewavatar?size=xsmall&avatarId=21130&avatarType=issuetype) [SPARK-14047](https://issues.apache.org/jira/browse/SPARK-14047) GBT improvement umbrella
  * ![Major - Major loss of function.](https://issues.apache.org/jira/images/icons/priorities/major.svg)
  * Resolved

relates to

![Umbrella - An overarching type made of sub-tasks](https://issues.apache.org/jira/secure/viewavatar?size=xsmall&avatarId=21130&avatarType=issuetype) [SPARK-9610](https://issues.apache.org/jira/browse/SPARK-9610) Class and instance weighting for ML
  * ![Major - Major loss of function.](https://issues.apache.org/jira/images/icons/priorities/major.svg)
  * Resolved

links to

![Web Link](https://github.com/favicon.ico) [GitHub Pull Request #25926](https://github.com/apache/spark/pull/25926)
![Web Link](https://github.com/favicon.ico) [GitHub Pull Request #27070](https://github.com/apache/spark/pull/27070)
#### Activity
  * [All](https://issues.apache.org/jira/browse/SPARK-9612?page=com.atlassian.jira.plugin.system.issuetabpanels:all-tabpanel)
  * Comments
  * [Work Log](https://issues.apache.org/jira/browse/SPARK-9612?page=com.atlassian.jira.plugin.system.issuetabpanels:worklog-tabpanel)
  * [History](https://issues.apache.org/jira/browse/SPARK-9612?page=com.atlassian.jira.plugin.system.issuetabpanels:changehistory-tabpanel)
  * [Activity](https://issues.apache.org/jira/browse/SPARK-9612?page=com.atlassian.streams.streams-jira-plugin:activity-stream-issue-tab)
  * [Transitions](https://issues.apache.org/jira/browse/SPARK-9612?page=com.googlecode.jira-suite-utilities:transitions-summary-tabpanel)

[ Ascending order - Click to sort in descending order ](https://issues.apache.org/jira/browse/SPARK-9612?actionOrder=desc "Ascending order - Click to sort in descending order")
[![josephkb](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Joseph K. Bradley](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=josephkb) added a comment - [22/Apr/16 02:10](https://issues.apache.org/jira/browse/SPARK-9612?focusedCommentId=15253185&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15253185)
Removing target version, but please update as needed [dbtsai](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=dbtsai)
[![josephkb](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Joseph K. Bradley](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=josephkb) added a comment - [22/Apr/16 02:10](https://issues.apache.org/jira/browse/SPARK-9612?focusedCommentId=15253185&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15253185) Removing target version, but please update as needed dbtsai
[![podongfeng](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Ruifeng Zheng](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=podongfeng) added a comment - [06/Sep/19 09:41](https://issues.apache.org/jira/browse/SPARK-9612?focusedCommentId=16924090&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16924090)
<https://issues.apache.org/jira/browse/SPARK-19591> is now resolved by [imatiach](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=imatiach)
[dbtsai](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=dbtsai) Will you go on working on this?
[![podongfeng](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Ruifeng Zheng](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=podongfeng) added a comment - [06/Sep/19 09:41](https://issues.apache.org/jira/browse/SPARK-9612?focusedCommentId=16924090&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16924090) https://issues.apache.org/jira/browse/SPARK-19591 is now resolved by imatiach dbtsai Will you go on working on this?
#### People

Assignee:
     ![podongfeng](https://issues.apache.org/jira/secure/useravatar?size=small&avatarId=10452) Ruifeng Zheng

Reporter:
     ![josephkb](https://issues.apache.org/jira/secure/useravatar?size=small&avatarId=10452) Joseph K. Bradley

Votes:
     3 Vote for this issue

Watchers:
     6 Start watching this issue
#### Dates

Created:
     04/Aug/15 20:30

Updated:
     06/Jan/20 02:08

Resolved:
     25/Oct/19 08:52
  * Atlassian Jira [Project Management Software](https://www.atlassian.com/software/jira)
  * [About Jira](https://issues.apache.org/jira/secure/AboutPage.jspa/secure/AboutPage.jspa)
  * [Report a problem](https://issues.apache.org/jira/secure/CreateIssue!default.jspa)

Powered by a free Atlassian [Jira](http://www.atlassian.com/software/jira) open source license for Apache Software Foundation. Try Jira - [bug tracking software](http://www.atlassian.com/software/jira) for _your_ team.
[Atlassian](http://www.atlassian.com/)
[](javascript:;)[](javascript:;)

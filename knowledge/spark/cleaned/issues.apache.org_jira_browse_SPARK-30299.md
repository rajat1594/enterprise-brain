[Log in](https://issues.apache.org/jira/login.jsp?os_destination=%2Fbrowse%2FSPARK-30299)[Skip to main content](https://issues.apache.org/jira/browse/SPARK-30299#main)[Skip to sidebar](https://issues.apache.org/jira/browse/SPARK-30299#sidebar)
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
  * [Log In](https://issues.apache.org/jira/login.jsp?os_destination=%2Fbrowse%2FSPARK-30299)

Public signup for this instance is **disabled**. Go to our [Self serve sign up page](https://selfserve.apache.org/jira-account.html) to request an account. Report potential security issues [privately](https://apache.org/security/#reporting-a-vulnerability)
[![Spark](https://issues.apache.org/jira/secure/projectavatar?pid=12315420&avatarId=27346)![Project Type: software](https://issues.apache.org/jira/browse/SPARK-30299)](https://issues.apache.org/jira/projects/SPARK/summary "Spark")
#
[Spark](https://issues.apache.org/jira/projects/SPARK/summary "Spark")
  * [Issues](https://issues.apache.org/jira/projects/SPARK/issues)
  * [Reports](https://issues.apache.org/jira/projects/SPARK?selectedItem=com.atlassian.jira.jira-projects-plugin:report-page)
  * [Components](https://issues.apache.org/jira/projects/SPARK?selectedItem=com.atlassian.jira.jira-projects-plugin:components-page)
  * [Roadmap](https://issues.apache.org/jira/projects/SPARK?selectedItem=biz.everit.jira.epic-roadmap:erfj-sidebar-roadmap)

![Uploaded image for project: 'Spark'](https://issues.apache.org/jira/secure/projectavatar?pid=12315420&avatarId=27346)
  1. [Spark](https://issues.apache.org/jira/browse/SPARK)
  2. [SPARK-30299](https://issues.apache.org/jira/browse/SPARK-30299)

# Dynamic allocation with Standalone mode calculates to many executors needed
[Log In](https://issues.apache.org/jira/login.jsp?os_destination=%2Fbrowse%2FSPARK-30299 "Log In")
[ Export](https://issues.apache.org/jira/browse/SPARK-30299)
[XML](https://issues.apache.org/jira/si/jira.issueviews:issue-xml/SPARK-30299/SPARK-30299.xml)[Word](https://issues.apache.org/jira/si/jira.issueviews:issue-word/SPARK-30299/SPARK-30299.doc)[Printable](https://issues.apache.org/jira/si/jira.issueviews:issue-html/SPARK-30299/SPARK-30299.html)[JSON](https://issues.apache.org/jira/si/com.atlassian.jira.plugins.jira-importers-plugin:issue-json/SPARK-30299/SPARK-30299.json)

#### Details
  * ** Type: ** ![](https://issues.apache.org/jira/secure/viewavatar?size=xsmall&avatarId=21133&avatarType=issuetype) Bug
  * **Status:** Open
  * ** Priority: ** ![](https://issues.apache.org/jira/images/icons/priorities/major.svg) Major
  * **Resolution:** Unresolved
  * ** Affects Version/s: ** 2.4.4, 3.0.0
  * ** Fix Version/s:  ** None
  * ** Component/s: ** [Spark Core](https://issues.apache.org/jira/issues/?jql=project+%3D+SPARK+AND+component+%3D+%22Spark+Core%22 "Spark Core ")
  * ** Labels: **
None

#### Description
While I was doing some changes in the executor allocation manager, I realized there is a bug with dynamic allocation in standalone mode.
The issue is that if you run standalone mode with the default settings where the executor gets all the cores of the worker, spark core (allocation manager) doesn't know the number of cores per executor to be able to calculate how many tasks can fit on an executor.
It therefore defaults to the use the default EXECUTOR_CORES which is 1 and thus could calculate it needs way more containers there are actually does.
For instance, I have a worker with 12 cores. That means by default when I start an executor on it, it gets 12 cores and can fit 12 tasks. The allocation manager would use the default of 1 core per executor and say it needs 12 executors when it only needs 1.
The fix for this isn't trivial since it would need to know how many cores each one has and I assume it would also need to handle heterogenous nodes. I could start workers on nodes with different numbers of cores - one with 24 cores and one with 16 cores. How do we estimate the number of executors in this case. We could just choose the min of existing ones or something like that as an estimate and it would be closer, unless of course the next executor you got didn't actually have that.
#### Attachments
#### Activity
  * [All](https://issues.apache.org/jira/browse/SPARK-30299?page=com.atlassian.jira.plugin.system.issuetabpanels:all-tabpanel)
  * Comments
  * [Work Log](https://issues.apache.org/jira/browse/SPARK-30299?page=com.atlassian.jira.plugin.system.issuetabpanels:worklog-tabpanel)
  * [History](https://issues.apache.org/jira/browse/SPARK-30299?page=com.atlassian.jira.plugin.system.issuetabpanels:changehistory-tabpanel)
  * [Activity](https://issues.apache.org/jira/browse/SPARK-30299?page=com.atlassian.streams.streams-jira-plugin:activity-stream-issue-tab)
  * [Transitions](https://issues.apache.org/jira/browse/SPARK-30299?page=com.googlecode.jira-suite-utilities:transitions-summary-tabpanel)

[![tgraves](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Thomas Graves](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=tgraves) added a comment - [06/Apr/20 18:19](https://issues.apache.org/jira/browse/SPARK-30299?focusedCommentId=17076525&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-17076525)
Note that there are other places in the code that uses executor cores which could also be wrong in standalone mode. for instance PythonRunner is using it to split memory.
[![tgraves](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Thomas Graves](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=tgraves) added a comment - [06/Apr/20 18:19](https://issues.apache.org/jira/browse/SPARK-30299?focusedCommentId=17076525&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-17076525) Note that there are other places in the code that uses executor cores which could also be wrong in standalone mode. for instance PythonRunner is using it to split memory.
#### People

Assignee:
     ![Unassigned](https://issues.apache.org/jira/secure/useravatar?size=small&avatarId=10453) Unassigned

Reporter:
     ![tgraves](https://issues.apache.org/jira/secure/useravatar?size=small&avatarId=10452) Thomas Graves

Votes:
     0 Vote for this issue

Watchers:
     3 Start watching this issue
#### Dates

Created:
     18/Dec/19 14:14

Updated:
     06/Apr/20 18:19
  * Atlassian Jira [Project Management Software](https://www.atlassian.com/software/jira)
  * [About Jira](https://issues.apache.org/jira/secure/AboutPage.jspa/secure/AboutPage.jspa)
  * [Report a problem](https://issues.apache.org/jira/secure/CreateIssue!default.jspa)

Powered by a free Atlassian [Jira](http://www.atlassian.com/software/jira) open source license for Apache Software Foundation. Try Jira - [bug tracking software](http://www.atlassian.com/software/jira) for _your_ team.
[Atlassian](http://www.atlassian.com/)
[](javascript:;)[](javascript:;)

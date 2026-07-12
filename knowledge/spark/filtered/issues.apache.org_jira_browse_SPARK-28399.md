[Log in](https://issues.apache.org/jira/login.jsp?os_destination=%2Fbrowse%2FSPARK-28399)[Skip to main content](https://issues.apache.org/jira/browse/SPARK-28399#main)[Skip to sidebar](https://issues.apache.org/jira/browse/SPARK-28399#sidebar)
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
  * [Log In](https://issues.apache.org/jira/login.jsp?os_destination=%2Fbrowse%2FSPARK-28399)


Public signup for this instance is **disabled**. Go to our [Self serve sign up page](https://selfserve.apache.org/jira-account.html) to request an account. Report potential security issues [privately](https://apache.org/security/#reporting-a-vulnerability)
[![Spark](https://issues.apache.org/jira/secure/projectavatar?pid=12315420&avatarId=27346)![Project Type: software](https://issues.apache.org/jira/browse/SPARK-28399)](https://issues.apache.org/jira/projects/SPARK/summary "Spark")
# 
[Spark](https://issues.apache.org/jira/projects/SPARK/summary "Spark")
  * [Issues](https://issues.apache.org/jira/projects/SPARK/issues)
  * [Reports](https://issues.apache.org/jira/projects/SPARK?selectedItem=com.atlassian.jira.jira-projects-plugin:report-page)
  * [Components](https://issues.apache.org/jira/projects/SPARK?selectedItem=com.atlassian.jira.jira-projects-plugin:components-page)
  * [Roadmap](https://issues.apache.org/jira/projects/SPARK?selectedItem=biz.everit.jira.epic-roadmap:erfj-sidebar-roadmap)


![Uploaded image for project: 'Spark'](https://issues.apache.org/jira/secure/projectavatar?pid=12315420&avatarId=27346)
  1. [Spark](https://issues.apache.org/jira/browse/SPARK)
  2. [SPARK-28399](https://issues.apache.org/jira/browse/SPARK-28399)


# Impl RobustScaler
[Log In](https://issues.apache.org/jira/login.jsp?os_destination=%2Fbrowse%2FSPARK-28399 "Log In")
[ Export](https://issues.apache.org/jira/browse/SPARK-28399)
[XML](https://issues.apache.org/jira/si/jira.issueviews:issue-xml/SPARK-28399/SPARK-28399.xml)[Word](https://issues.apache.org/jira/si/jira.issueviews:issue-word/SPARK-28399/SPARK-28399.doc)[Printable](https://issues.apache.org/jira/si/jira.issueviews:issue-html/SPARK-28399/SPARK-28399.html)[JSON](https://issues.apache.org/jira/si/com.atlassian.jira.plugins.jira-importers-plugin:issue-json/SPARK-28399/SPARK-28399.json) 

#### Details
  * ** Type: ** ![](https://issues.apache.org/jira/secure/viewavatar?size=xsmall&avatarId=21141&avatarType=issuetype) New Feature 
  * **Status:** Closed
  * ** Priority: ** ![](https://issues.apache.org/jira/images/icons/priorities/major.svg) Major 
  * **Resolution:** Fixed 
  * ** Affects Version/s: ** 3.0.0
  * ** Fix Version/s:  ** [3.0.0](https://issues.apache.org/jira/issues/?jql=project+%3D+SPARK+AND+fixVersion+%3D+3.0.0 "3.0.0 ")
  * ** Component/s: ** [ML](https://issues.apache.org/jira/issues/?jql=project+%3D+SPARK+AND+component+%3D+ML "ML Features under the spark.ml package")
  * ** Labels: **
None


#### Description
RobustScaler is a kind of widely-used scaler, which use median/IQR to replace mean/std in StandardScaler. It can produce stable result that are much more robust to outliers. It is already a part of [Scikit-Learn](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.RobustScaler.html#sklearn.preprocessing.RobustScaler).
So far, it is now implemented in ML.
I encounter a practical case that need this feature, and notice that other users also wanted this function in [~~SPARK-17934~~](https://issues.apache.org/jira/browse/SPARK-17934 "Support percentile scale in ml.feature"), so I am to add it in ML.
#### Attachments
#### Issue Links 

Blocked
    
![New Feature - A new feature of the product, which has yet to be developed.](https://issues.apache.org/jira/secure/viewavatar?size=xsmall&avatarId=21141&avatarType=issuetype) [SPARK-17934](https://issues.apache.org/jira/browse/SPARK-17934) Support percentile scale in ml.feature
  * ![Major - Major loss of function.](https://issues.apache.org/jira/images/icons/priorities/major.svg)
  * Resolved



links to
    
![Web Link](https://github.com/favicon.ico) [GitHub Pull Request #25160](https://github.com/apache/spark/pull/25160)
#### Activity
  * [All](https://issues.apache.org/jira/browse/SPARK-28399?page=com.atlassian.jira.plugin.system.issuetabpanels:all-tabpanel)
  * Comments
  * [Work Log](https://issues.apache.org/jira/browse/SPARK-28399?page=com.atlassian.jira.plugin.system.issuetabpanels:worklog-tabpanel)
  * [History](https://issues.apache.org/jira/browse/SPARK-28399?page=com.atlassian.jira.plugin.system.issuetabpanels:changehistory-tabpanel)
  * [Activity](https://issues.apache.org/jira/browse/SPARK-28399?page=com.atlassian.streams.streams-jira-plugin:activity-stream-issue-tab)
  * [Transitions](https://issues.apache.org/jira/browse/SPARK-28399?page=com.googlecode.jira-suite-utilities:transitions-summary-tabpanel)


[![srowen](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Sean R. Owen](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=srowen) added a comment - [30/Jul/19 15:24](https://issues.apache.org/jira/browse/SPARK-28399?focusedCommentId=16896225&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16896225)
Issue resolved by pull request 25160  
<https://github.com/apache/spark/pull/25160>
[![srowen](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Sean R. Owen](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=srowen) added a comment - [30/Jul/19 15:24](https://issues.apache.org/jira/browse/SPARK-28399?focusedCommentId=16896225&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16896225) Issue resolved by pull request 25160 https://github.com/apache/spark/pull/25160 
#### People 

Assignee: 
     ![podongfeng](https://issues.apache.org/jira/secure/useravatar?size=small&avatarId=10452) Ruifeng Zheng  

Reporter: 
     ![podongfeng](https://issues.apache.org/jira/secure/useravatar?size=small&avatarId=10452) Ruifeng Zheng  

Votes:
     0 Vote for this issue 

Watchers:
     2 Start watching this issue
#### Dates 

Created: 
     15/Jul/19 11:13 

Updated: 
     15/Feb/26 20:04 

Resolved: 
     30/Jul/19 15:24
  * Atlassian Jira [Project Management Software](https://www.atlassian.com/software/jira)
  * [About Jira](https://issues.apache.org/jira/secure/AboutPage.jspa/secure/AboutPage.jspa)
  * [Report a problem](https://issues.apache.org/jira/secure/CreateIssue!default.jspa)


Powered by a free Atlassian [Jira](http://www.atlassian.com/software/jira) open source license for Apache Software Foundation. Try Jira - [bug tracking software](http://www.atlassian.com/software/jira) for _your_ team. 
[Atlassian](http://www.atlassian.com/)
[](javascript:;)[](javascript:;)

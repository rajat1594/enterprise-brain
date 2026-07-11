[Log in](https://issues.apache.org/jira/login.jsp?os_destination=%2Fbrowse%2FSPARK-11215)[Skip to main content](https://issues.apache.org/jira/browse/SPARK-11215#main)[Skip to sidebar](https://issues.apache.org/jira/browse/SPARK-11215#sidebar)
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
  * [Log In](https://issues.apache.org/jira/login.jsp?os_destination=%2Fbrowse%2FSPARK-11215)


Public signup for this instance is **disabled**. Go to our [Self serve sign up page](https://selfserve.apache.org/jira-account.html) to request an account. Report potential security issues [privately](https://apache.org/security/#reporting-a-vulnerability)
[![Spark](https://issues.apache.org/jira/secure/projectavatar?pid=12315420&avatarId=27346)![Project Type: software](https://issues.apache.org/jira/browse/SPARK-11215)](https://issues.apache.org/jira/projects/SPARK/summary "Spark")
# 
[Spark](https://issues.apache.org/jira/projects/SPARK/summary "Spark")
  * [Issues](https://issues.apache.org/jira/projects/SPARK/issues)
  * [Reports](https://issues.apache.org/jira/projects/SPARK?selectedItem=com.atlassian.jira.jira-projects-plugin:report-page)
  * [Components](https://issues.apache.org/jira/projects/SPARK?selectedItem=com.atlassian.jira.jira-projects-plugin:components-page)
  * [Roadmap](https://issues.apache.org/jira/projects/SPARK?selectedItem=biz.everit.jira.epic-roadmap:erfj-sidebar-roadmap)


![Uploaded image for project: 'Spark'](https://issues.apache.org/jira/secure/projectavatar?pid=12315420&avatarId=27346)
  1. [Spark](https://issues.apache.org/jira/browse/SPARK)
  2. [SPARK-11215](https://issues.apache.org/jira/browse/SPARK-11215)


# Add multiple columns support to StringIndexer
[Log In](https://issues.apache.org/jira/login.jsp?os_destination=%2Fbrowse%2FSPARK-11215 "Log In")
[ Export](https://issues.apache.org/jira/browse/SPARK-11215)
[XML](https://issues.apache.org/jira/si/jira.issueviews:issue-xml/SPARK-11215/SPARK-11215.xml)[Word](https://issues.apache.org/jira/si/jira.issueviews:issue-word/SPARK-11215/SPARK-11215.doc)[Printable](https://issues.apache.org/jira/si/jira.issueviews:issue-html/SPARK-11215/SPARK-11215.html)[JSON](https://issues.apache.org/jira/si/com.atlassian.jira.plugins.jira-importers-plugin:issue-json/SPARK-11215/SPARK-11215.json) 

#### Details
  * ** Type: ** ![](https://issues.apache.org/jira/secure/viewavatar?size=xsmall&avatarId=21140&avatarType=issuetype) Improvement 
  * **Status:** Closed
  * ** Priority: ** ![](https://issues.apache.org/jira/images/icons/priorities/major.svg) Major 
  * **Resolution:** Fixed 
  * ** Affects Version/s: ** 2.4.0
  * ** Fix Version/s:  ** [3.0.0](https://issues.apache.org/jira/issues/?jql=project+%3D+SPARK+AND+fixVersion+%3D+3.0.0 "3.0.0 ")
  * ** Component/s: ** [ML](https://issues.apache.org/jira/issues/?jql=project+%3D+SPARK+AND+component+%3D+ML "ML Features under the spark.ml package")
  * ** Labels: **
None


  * ** Docs Text: **
[Hide](https://issues.apache.org/jira/browse/SPARK-11215)
When specifying frequencyDesc or frequencyAsc as stringOrderType param in StringIndexer, in case of equal frequency, the order of strings was previously undefined. Since Spark 3.0, strings with equal frequency are further   
sorted lexicographically. 
[Show](https://issues.apache.org/jira/browse/SPARK-11215)
When specifying frequencyDesc or frequencyAsc as stringOrderType param in StringIndexer, in case of equal frequency, the order of strings was previously undefined. Since Spark 3.0, strings with equal frequency are further sorted lexicographically. 


#### Description
Add multiple columns support to StringIndexer, then users can transform multiple input columns to multiple output columns simultaneously. See discussion [~~SPARK-8418~~](https://issues.apache.org/jira/browse/SPARK-8418 "Add single- and multi-value support to ML Transformers").
#### Attachments
#### Issue Links 

Is contained by
    
![Sub-task - The sub-task of the issue](https://issues.apache.org/jira/secure/viewavatar?size=xsmall&avatarId=21146&avatarType=issuetype) [SPARK-8418](https://issues.apache.org/jira/browse/SPARK-8418) Add single- and multi-value support to ML Transformers
  * ![Major - Major loss of function.](https://issues.apache.org/jira/images/icons/priorities/major.svg)
  * Resolved



is related to
    
![Bug - A problem which impairs or prevents the functions of the product.](https://issues.apache.org/jira/secure/viewavatar?size=xsmall&avatarId=21133&avatarType=issuetype) [SPARK-30939](https://issues.apache.org/jira/browse/SPARK-30939) StringIndexer setOutputCols does not set output cols
  * ![Major - Major loss of function.](https://issues.apache.org/jira/images/icons/priorities/major.svg)
  * Closed



is required by
    
![New Feature - A new feature of the product, which has yet to be developed.](https://issues.apache.org/jira/secure/viewavatar?size=xsmall&avatarId=21141&avatarType=issuetype) [SPARK-22798](https://issues.apache.org/jira/browse/SPARK-22798) Add multiple column support to PySpark StringIndexer
  * ![Major - Major loss of function.](https://issues.apache.org/jira/images/icons/priorities/major.svg)
  * Closed



links to
    
![Pull request #9183](https://assets-cdn.github.com/favicon.ico) [[Github] Pull Request #9183 (yanboliang)](https://github.com/apache/spark/pull/9183)     
![Pull request #19621](https://assets-cdn.github.com/favicon.ico) [[Github] Pull Request #19621 (WeichenXu123)](https://github.com/apache/spark/pull/19621)     
![Pull request #20146](https://assets-cdn.github.com/favicon.ico) [[Github] Pull Request #20146 (viirya)](https://github.com/apache/spark/pull/20146)     
![Web Link](https://github.com/favicon.ico) [GitHub Pull Request #20146](https://github.com/apache/spark/pull/20146)     
![Web Link](https://github.com/favicon.ico) [GitHub Pull Request #25428](https://github.com/apache/spark/pull/25428)
Show 3 more links (3 links to)
#### Activity
  * [All](https://issues.apache.org/jira/browse/SPARK-11215?page=com.atlassian.jira.plugin.system.issuetabpanels:all-tabpanel)
  * Comments
  * [Work Log](https://issues.apache.org/jira/browse/SPARK-11215?page=com.atlassian.jira.plugin.system.issuetabpanels:worklog-tabpanel)
  * [History](https://issues.apache.org/jira/browse/SPARK-11215?page=com.atlassian.jira.plugin.system.issuetabpanels:changehistory-tabpanel)
  * [Activity](https://issues.apache.org/jira/browse/SPARK-11215?page=com.atlassian.streams.streams-jira-plugin:activity-stream-issue-tab)
  * [Transitions](https://issues.apache.org/jira/browse/SPARK-11215?page=com.googlecode.jira-suite-utilities:transitions-summary-tabpanel)


[ Ascending order - Click to sort in descending order ](https://issues.apache.org/jira/browse/SPARK-11215?actionOrder=desc "Ascending order - Click to sort in descending order")
[![apachespark](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Apache Spark](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=apachespark) added a comment - [20/Oct/15 15:31](https://issues.apache.org/jira/browse/SPARK-11215?focusedCommentId=14965261&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-14965261)
User 'yanboliang' has created a pull request for this issue:  
<https://github.com/apache/spark/pull/9183>
[![apachespark](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Apache Spark](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=apachespark) added a comment - [20/Oct/15 15:31](https://issues.apache.org/jira/browse/SPARK-11215?focusedCommentId=14965261&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-14965261) User 'yanboliang' has created a pull request for this issue: https://github.com/apache/spark/pull/9183 
[![barrybecker4](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Barry Becker](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=barrybecker4) added a comment - [05/Dec/16 16:39](https://issues.apache.org/jira/browse/SPARK-11215?focusedCommentId=15722696&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15722696)
This would be a good feature. It might be nice to add an optional parameter for "maxCategories" like VectorIndexer does. Any column found to have more than maxCategories would then be skipped. This would have the advantage of avoiding the work of indexing columns with huge numbers of distinct values.
[![barrybecker4](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Barry Becker](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=barrybecker4) added a comment - [05/Dec/16 16:39](https://issues.apache.org/jira/browse/SPARK-11215?focusedCommentId=15722696&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15722696) This would be a good feature. It might be nice to add an optional parameter for "maxCategories" like VectorIndexer does. Any column found to have more than maxCategories would then be skipped. This would have the advantage of avoiding the work of indexing columns with huge numbers of distinct values. 
[![weichenxu123](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Weichen Xu](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=weichenxu123) added a comment - [26/Jul/17 20:57](https://issues.apache.org/jira/browse/SPARK-11215?focusedCommentId=16102274&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16102274)
I will take over this feature and create a PR soon.
[![weichenxu123](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Weichen Xu](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=weichenxu123) added a comment - [26/Jul/17 20:57](https://issues.apache.org/jira/browse/SPARK-11215?focusedCommentId=16102274&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16102274) I will take over this feature and create a PR soon. 
[![viirya](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) L. C. Hsieh](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=viirya) added a comment - [30/Oct/17 13:41](https://issues.apache.org/jira/browse/SPARK-11215?focusedCommentId=16224975&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16224975)
Hi [WeichenXu123](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=WeichenXu123), I'd like to know if you are busy these days, if so, I could work on it. Please let me know. Thanks.
[![viirya](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) L. C. Hsieh](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=viirya) added a comment - [30/Oct/17 13:41](https://issues.apache.org/jira/browse/SPARK-11215?focusedCommentId=16224975&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16224975) Hi WeichenXu123 , I'd like to know if you are busy these days, if so, I could work on it. Please let me know. Thanks. 
[![weichenxu123](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Weichen Xu](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=weichenxu123) added a comment - [30/Oct/17 15:08](https://issues.apache.org/jira/browse/SPARK-11215?focusedCommentId=16225093&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16225093)
[viirya](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=viirya) Sorry for late! I already has partly written code and will try to submit tomorrow, thank you for attention!
[![weichenxu123](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Weichen Xu](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=weichenxu123) added a comment - [30/Oct/17 15:08](https://issues.apache.org/jira/browse/SPARK-11215?focusedCommentId=16225093&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16225093) viirya Sorry for late! I already has partly written code and will try to submit tomorrow, thank you for attention! 
[![apachespark](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Apache Spark](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=apachespark) added a comment - [31/Oct/17 14:48](https://issues.apache.org/jira/browse/SPARK-11215?focusedCommentId=16226915&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16226915)
User 'WeichenXu123' has created a pull request for this issue:  
<https://github.com/apache/spark/pull/19621>
[![apachespark](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Apache Spark](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=apachespark) added a comment - [31/Oct/17 14:48](https://issues.apache.org/jira/browse/SPARK-11215?focusedCommentId=16226915&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16226915) User 'WeichenXu123' has created a pull request for this issue: https://github.com/apache/spark/pull/19621 
[![apachespark](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Apache Spark](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=apachespark) added a comment - [04/Jan/18 03:58](https://issues.apache.org/jira/browse/SPARK-11215?focusedCommentId=16310690&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16310690)
User 'viirya' has created a pull request for this issue:  
<https://github.com/apache/spark/pull/20146>
[![apachespark](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Apache Spark](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=apachespark) added a comment - [04/Jan/18 03:58](https://issues.apache.org/jira/browse/SPARK-11215?focusedCommentId=16310690&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16310690) User 'viirya' has created a pull request for this issue: https://github.com/apache/spark/pull/20146 
[![barrybecker4](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Barry Becker](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=barrybecker4) added a comment - [24/Aug/18 13:41](https://issues.apache.org/jira/browse/SPARK-11215?focusedCommentId=16591667&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16591667)
Is the main motivation for this feature performance?
Can you give a rough estimate of how much performance might improve using this feature when you have a few hundred string valued columns that you apply it to?
[![barrybecker4](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Barry Becker](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=barrybecker4) added a comment - [24/Aug/18 13:41](https://issues.apache.org/jira/browse/SPARK-11215?focusedCommentId=16591667&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16591667) Is the main motivation for this feature performance? Can you give a rough estimate of how much performance might improve using this feature when you have a few hundred string valued columns that you apply it to? 
[![srowen](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Sean R. Owen](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=srowen) added a comment - [29/Jan/19 15:21](https://issues.apache.org/jira/browse/SPARK-11215?focusedCommentId=16755119&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16755119)
Issue resolved by pull request 20146  
<https://github.com/apache/spark/pull/20146>
[![srowen](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Sean R. Owen](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=srowen) added a comment - [29/Jan/19 15:21](https://issues.apache.org/jira/browse/SPARK-11215?focusedCommentId=16755119&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16755119) Issue resolved by pull request 20146 https://github.com/apache/spark/pull/20146 
#### People 

Assignee: 
     ![viirya](https://issues.apache.org/jira/secure/useravatar?size=small&avatarId=10452) L. C. Hsieh  

Reporter: 
     ![yanboliang](https://issues.apache.org/jira/secure/useravatar?size=small&avatarId=10452) Yanbo Liang  

Votes:
     6 Vote for this issue 

Watchers:
     11 Start watching this issue
#### Dates 

Created: 
     20/Oct/15 15:18 

Updated: 
     15/Feb/26 20:11 

Resolved: 
     29/Jan/19 15:21
  * Atlassian Jira [Project Management Software](https://www.atlassian.com/software/jira)
  * [About Jira](https://issues.apache.org/jira/secure/AboutPage.jspa/secure/AboutPage.jspa)
  * [Report a problem](https://issues.apache.org/jira/secure/CreateIssue!default.jspa)


Powered by a free Atlassian [Jira](http://www.atlassian.com/software/jira) open source license for Apache Software Foundation. Try Jira - [bug tracking software](http://www.atlassian.com/software/jira) for _your_ team. 
[Atlassian](http://www.atlassian.com/)
[](javascript:;)[](javascript:;)

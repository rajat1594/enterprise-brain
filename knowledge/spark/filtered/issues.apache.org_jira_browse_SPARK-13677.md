[Log in](https://issues.apache.org/jira/login.jsp?os_destination=%2Fbrowse%2FSPARK-13677)[Skip to main content](https://issues.apache.org/jira/browse/SPARK-13677#main)[Skip to sidebar](https://issues.apache.org/jira/browse/SPARK-13677#sidebar)
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
  * [Log In](https://issues.apache.org/jira/login.jsp?os_destination=%2Fbrowse%2FSPARK-13677)


Public signup for this instance is **disabled**. Go to our [Self serve sign up page](https://selfserve.apache.org/jira-account.html) to request an account. Report potential security issues [privately](https://apache.org/security/#reporting-a-vulnerability)
[![Spark](https://issues.apache.org/jira/secure/projectavatar?pid=12315420&avatarId=27346)![Project Type: software](https://issues.apache.org/jira/browse/SPARK-13677)](https://issues.apache.org/jira/projects/SPARK/summary "Spark")
# 
[Spark](https://issues.apache.org/jira/projects/SPARK/summary "Spark")
  * [Issues](https://issues.apache.org/jira/projects/SPARK/issues)
  * [Reports](https://issues.apache.org/jira/projects/SPARK?selectedItem=com.atlassian.jira.jira-projects-plugin:report-page)
  * [Components](https://issues.apache.org/jira/projects/SPARK?selectedItem=com.atlassian.jira.jira-projects-plugin:components-page)
  * [Roadmap](https://issues.apache.org/jira/projects/SPARK?selectedItem=biz.everit.jira.epic-roadmap:erfj-sidebar-roadmap)


![Uploaded image for project: 'Spark'](https://issues.apache.org/jira/secure/projectavatar?pid=12315420&avatarId=27346)
  1. [Spark](https://issues.apache.org/jira/browse/SPARK)
  2. [SPARK-13677](https://issues.apache.org/jira/browse/SPARK-13677)


# Support Tree-Based Feature Transformation for ML
[Log In](https://issues.apache.org/jira/login.jsp?os_destination=%2Fbrowse%2FSPARK-13677 "Log In")
[ Export](https://issues.apache.org/jira/browse/SPARK-13677)
[XML](https://issues.apache.org/jira/si/jira.issueviews:issue-xml/SPARK-13677/SPARK-13677.xml)[Word](https://issues.apache.org/jira/si/jira.issueviews:issue-word/SPARK-13677/SPARK-13677.doc)[Printable](https://issues.apache.org/jira/si/jira.issueviews:issue-html/SPARK-13677/SPARK-13677.html)[JSON](https://issues.apache.org/jira/si/com.atlassian.jira.plugins.jira-importers-plugin:issue-json/SPARK-13677/SPARK-13677.json) 

#### Details
  * ** Type: ** ![](https://issues.apache.org/jira/secure/viewavatar?size=xsmall&avatarId=21141&avatarType=issuetype) New Feature 
  * **Status:** Closed
  * ** Priority: ** ![](https://issues.apache.org/jira/images/icons/priorities/major.svg) Major 
  * **Resolution:** Fixed 
  * ** Affects Version/s: ** None 
  * ** Fix Version/s:  ** [3.0.0](https://issues.apache.org/jira/issues/?jql=project+%3D+SPARK+AND+fixVersion+%3D+3.0.0 "3.0.0 ")
  * ** Component/s: ** [ML](https://issues.apache.org/jira/issues/?jql=project+%3D+SPARK+AND+component+%3D+ML "ML Features under the spark.ml package")
  * ** Labels: **
None


#### Description
It would be nice to be able to use RF and GBT for feature transformation:  
First fit an ensemble of trees (like RF, GBT or other TreeEnsambleModels) on the training set. Then each leaf of each tree in the ensemble is assigned a fixed arbitrary feature index in a new feature space. These leaf indices are then encoded in a one-hot fashion.
This method was first introduced by facebook(<http://www.herbrich.me/papers/adclicksfacebook.pdf>), and is implemented in famous libraries:
sklearn [apply](https://issues.apache.org/jira/browse/SPARK-13677#example-ensemble-plot-feature-transformation-py\])
xgboost [predict_leaf_index|<https://github.com/dmlc/xgboost/blob/master/demo/guide-python/predict_leaf_indices.py>]
lightgbm [predict_leaf_index](https://lightgbm.readthedocs.io/en/latest/Parameters.html#predict_leaf_index)
catboost [calc_leaf_index](https://github.com/catboost/tutorials/tree/master/leaf_indexes_calculation)
Refering to the design of above impls, I propose following api:
val model1 : DecisionTreeClassificationModel= ...
model1.setLeafCol("leaves")  
model1.transform(df)
val model2 : GBTClassificationModel = ...
model2.getLeafCol  
model2.transform(df)
The detailed design doc: <https://docs.google.com/document/d/1d81qS0zfb6vqbt3dn6zFQUmWeh2ymoRALvhzPpTZqvo/edit?usp=sharing>
#### Attachments
#### Issue Links 

Is contained by
    
![Umbrella - An overarching type made of sub-tasks](https://issues.apache.org/jira/secure/viewavatar?size=xsmall&avatarId=21130&avatarType=issuetype) [SPARK-14047](https://issues.apache.org/jira/browse/SPARK-14047) GBT improvement umbrella
  * ![Major - Major loss of function.](https://issues.apache.org/jira/images/icons/priorities/major.svg)
  * Resolved



links to
    
![Pull request #11520](https://assets-cdn.github.com/favicon.ico) [[Github] Pull Request #11520 (zhengruifeng)](https://github.com/apache/spark/pull/11520)     
![Web Link](https://github.com/favicon.ico) [GitHub Pull Request #25383](https://github.com/apache/spark/pull/25383)
#### Activity
  * [All](https://issues.apache.org/jira/browse/SPARK-13677?page=com.atlassian.jira.plugin.system.issuetabpanels:all-tabpanel)
  * Comments
  * [Work Log](https://issues.apache.org/jira/browse/SPARK-13677?page=com.atlassian.jira.plugin.system.issuetabpanels:worklog-tabpanel)
  * [History](https://issues.apache.org/jira/browse/SPARK-13677?page=com.atlassian.jira.plugin.system.issuetabpanels:changehistory-tabpanel)
  * [Activity](https://issues.apache.org/jira/browse/SPARK-13677?page=com.atlassian.streams.streams-jira-plugin:activity-stream-issue-tab)
  * [Transitions](https://issues.apache.org/jira/browse/SPARK-13677?page=com.googlecode.jira-suite-utilities:transitions-summary-tabpanel)


[ Ascending order - Click to sort in descending order ](https://issues.apache.org/jira/browse/SPARK-13677?actionOrder=desc "Ascending order - Click to sort in descending order")
[![apachespark](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Apache Spark](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=apachespark) added a comment - [04/Mar/16 12:36](https://issues.apache.org/jira/browse/SPARK-13677?focusedCommentId=15179827&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15179827)
User 'zhengruifeng' has created a pull request for this issue:  
<https://github.com/apache/spark/pull/11520>
[![apachespark](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Apache Spark](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=apachespark) added a comment - [04/Mar/16 12:36](https://issues.apache.org/jira/browse/SPARK-13677?focusedCommentId=15179827&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15179827) User 'zhengruifeng' has created a pull request for this issue: https://github.com/apache/spark/pull/11520 
[![podongfeng](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Ruifeng Zheng](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=podongfeng) added a comment - [05/Nov/16 03:12](https://issues.apache.org/jira/browse/SPARK-13677?focusedCommentId=15638459&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15638459)
Since mllib is in maintenance status. If this feature will be included, the corresponding PR will be updated to focus on ML only.
[![podongfeng](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Ruifeng Zheng](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=podongfeng) added a comment - [05/Nov/16 03:12](https://issues.apache.org/jira/browse/SPARK-13677?focusedCommentId=15638459&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15638459) Since mllib is in maintenance status. If this feature will be included, the corresponding PR will be updated to focus on ML only. 
[![podongfeng](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Ruifeng Zheng](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=podongfeng) added a comment - [05/Nov/16 03:32](https://issues.apache.org/jira/browse/SPARK-13677?focusedCommentId=15638489&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15638489)
It is shown in sklearn's doc here (<http://scikit-learn.org/stable/auto_examples/ensemble/plot_feature_transformation.html> ) that GBDT+LiR often bring high score than GBDT.
[![podongfeng](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Ruifeng Zheng](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=podongfeng) added a comment - [05/Nov/16 03:32](https://issues.apache.org/jira/browse/SPARK-13677?focusedCommentId=15638489&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15638489) It is shown in sklearn's doc here ( http://scikit-learn.org/stable/auto_examples/ensemble/plot_feature_transformation.html ) that GBDT+LiR often bring high score than GBDT. 
[![josephkb](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Joseph K. Bradley](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=josephkb) added a comment - [04/Jan/17 00:53](https://issues.apache.org/jira/browse/SPARK-13677?focusedCommentId=15796748&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15796748)
[podongfeng](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=podongfeng) Apologies for the inaction on this, but I agree with you about redoing this for the DataFrame-based API. Could you please propose an API here before implementing it? Thanks!
[![josephkb](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Joseph K. Bradley](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=josephkb) added a comment - [04/Jan/17 00:53](https://issues.apache.org/jira/browse/SPARK-13677?focusedCommentId=15796748&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15796748) podongfeng Apologies for the inaction on this, but I agree with you about redoing this for the DataFrame-based API. Could you please propose an API here before implementing it? Thanks! 
[![podongfeng](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Ruifeng Zheng](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=podongfeng) added a comment - [04/Jan/17 02:50](https://issues.apache.org/jira/browse/SPARK-13677?focusedCommentId=15796968&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15796968)
Not at all. I know you commetters are busy. I will add an API here.
[![podongfeng](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Ruifeng Zheng](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=podongfeng) added a comment - [04/Jan/17 02:50](https://issues.apache.org/jira/browse/SPARK-13677?focusedCommentId=15796968&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-15796968) Not at all. I know you commetters are busy. I will add an API here. 
[![podongfeng](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Ruifeng Zheng](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=podongfeng) added a comment - [19/Jun/19 11:17](https://issues.apache.org/jira/browse/SPARK-13677?focusedCommentId=16867507&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16867507)
I closed this ticket since the old pr was based on mllib-api, and at that time the impl of trees were being refactored and impled directly in ml.
I reopen it now since I re-design it on the ml side.
[![podongfeng](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Ruifeng Zheng](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=podongfeng) added a comment - [19/Jun/19 11:17](https://issues.apache.org/jira/browse/SPARK-13677?focusedCommentId=16867507&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16867507) I closed this ticket since the old pr was based on mllib-api, and at that time the impl of trees were being refactored and impled directly in ml. I reopen it now since I re-design it on the ml side. 
[![podongfeng](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Ruifeng Zheng](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=podongfeng) added a comment - [19/Jun/19 11:17](https://issues.apache.org/jira/browse/SPARK-13677?focusedCommentId=16867508&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16867508)
update the design
[![podongfeng](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Ruifeng Zheng](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=podongfeng) added a comment - [19/Jun/19 11:17](https://issues.apache.org/jira/browse/SPARK-13677?focusedCommentId=16867508&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16867508) update the design 
[![srowen](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Sean R. Owen](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=srowen) added a comment - [22/Aug/19 14:37](https://issues.apache.org/jira/browse/SPARK-13677?focusedCommentId=16913377&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16913377)
Issue resolved by pull request 25383  
<https://github.com/apache/spark/pull/25383>
[![srowen](https://issues.apache.org/jira/secure/useravatar?size=xsmall&avatarId=10452) Sean R. Owen](https://issues.apache.org/jira/secure/ViewProfile.jspa?name=srowen) added a comment - [22/Aug/19 14:37](https://issues.apache.org/jira/browse/SPARK-13677?focusedCommentId=16913377&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-16913377) Issue resolved by pull request 25383 https://github.com/apache/spark/pull/25383 
#### People 

Assignee: 
     ![podongfeng](https://issues.apache.org/jira/secure/useravatar?size=small&avatarId=10452) Ruifeng Zheng  

Reporter: 
     ![podongfeng](https://issues.apache.org/jira/secure/useravatar?size=small&avatarId=10452) Ruifeng Zheng  

Votes:
     1 Vote for this issue 

Watchers:
     7 Start watching this issue
#### Dates 

Created: 
     04/Mar/16 12:25 

Updated: 
     15/Feb/26 20:10 

Resolved: 
     22/Aug/19 14:37
  * Atlassian Jira [Project Management Software](https://www.atlassian.com/software/jira)
  * [About Jira](https://issues.apache.org/jira/secure/AboutPage.jspa/secure/AboutPage.jspa)
  * [Report a problem](https://issues.apache.org/jira/secure/CreateIssue!default.jspa)


Powered by a free Atlassian [Jira](http://www.atlassian.com/software/jira) open source license for Apache Software Foundation. Try Jira - [bug tracking software](http://www.atlassian.com/software/jira) for _your_ team. 
[Atlassian](http://www.atlassian.com/)
[](javascript:;)[](javascript:;)

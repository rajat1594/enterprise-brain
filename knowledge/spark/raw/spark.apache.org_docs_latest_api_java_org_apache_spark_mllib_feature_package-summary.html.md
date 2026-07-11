[Skip navigation links](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/feature/package-summary.html#skip-navbar-top "Skip navigation links")
  * [Overview](https://spark.apache.org/docs/latest/api/java/index.html)
  * Package
  * Class
  * [Deprecated](https://spark.apache.org/docs/latest/api/java/deprecated-list.html)
  * [Index](https://spark.apache.org/docs/latest/api/java/index-all.html)
  * [Help](https://spark.apache.org/docs/latest/api/java/help-doc.html#package)


  * Package: 
  * Description | 
  * [Related Packages](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/feature/package-summary.html#related-package-summary) | 
  * [Classes and Interfaces](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/feature/package-summary.html#class-summary)


SEARCH:
# Package org.apache.spark.mllib.feature
* * *
package org.apache.spark.mllib.feature
  * Related Packages
Package
Description
[org.apache.spark.mllib](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/package-summary.html)
RDD-based machine learning APIs (in maintenance mode).
  * All Classes and InterfacesInterfacesClasses
Class
Description
[ChiSqSelector](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/feature/ChiSqSelector.html "class in org.apache.spark.mllib.feature")
Creates a ChiSquared feature selector.
[ChiSqSelectorModel](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/feature/ChiSqSelectorModel.html "class in org.apache.spark.mllib.feature")
Chi Squared selector model.
[ChiSqSelectorModel.SaveLoadV1_0$](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/feature/ChiSqSelectorModel.SaveLoadV1_0$.html "class in org.apache.spark.mllib.feature")
[ElementwiseProduct](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/feature/ElementwiseProduct.html "class in org.apache.spark.mllib.feature")
Outputs the Hadamard product (i.e., the element-wise product) of each input vector with a provided "weight" vector.
[HashingTF](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/feature/HashingTF.html "class in org.apache.spark.mllib.feature")
Maps a sequence of terms to their term frequencies using the hashing trick.
[IDF](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/feature/IDF.html "class in org.apache.spark.mllib.feature")
Inverse document frequency (IDF).
[IDF.DocumentFrequencyAggregator](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/feature/IDF.DocumentFrequencyAggregator.html "class in org.apache.spark.mllib.feature")
Document frequency aggregator.
[IDFModel](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/feature/IDFModel.html "class in org.apache.spark.mllib.feature")
Represents an IDF model that can transform term frequency vectors.
[Normalizer](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/feature/Normalizer.html "class in org.apache.spark.mllib.feature")
Normalizes samples individually to unit L^p^ norm
[PCA](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/feature/PCA.html "class in org.apache.spark.mllib.feature")
A feature transformer that projects vectors to a low-dimensional space using PCA.
[PCAModel](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/feature/PCAModel.html "class in org.apache.spark.mllib.feature")
Model fitted by [`PCA`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/feature/PCA.html "class in org.apache.spark.mllib.feature") that can project vectors to a low-dimensional space using PCA.
[PCAUtil](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/feature/PCAUtil.html "class in org.apache.spark.mllib.feature")
[StandardScaler](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/feature/StandardScaler.html "class in org.apache.spark.mllib.feature")
Standardizes features by removing the mean and scaling to unit std using column summary statistics on the samples in the training set.
[StandardScalerModel](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/feature/StandardScalerModel.html "class in org.apache.spark.mllib.feature")
Represents a StandardScaler model that can transform vectors.
[VectorTransformer](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/feature/VectorTransformer.html "interface in org.apache.spark.mllib.feature")
Trait for transformation of a vector
[VocabWord](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/feature/VocabWord.html "class in org.apache.spark.mllib.feature")
Entry in vocabulary
[Word2Vec](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/feature/Word2Vec.html "class in org.apache.spark.mllib.feature")
Word2Vec creates vector representation of words in a text corpus.
[Word2VecModel](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/feature/Word2VecModel.html "class in org.apache.spark.mllib.feature")
Word2Vec model param: wordIndex maps each word to an index, which can retrieve the corresponding vector from wordVectors param: wordVectors array of length numWords * vectorSize, vector corresponding to the word mapped with index i can be retrieved by the slice (i * vectorSize, i * vectorSize + vectorSize)



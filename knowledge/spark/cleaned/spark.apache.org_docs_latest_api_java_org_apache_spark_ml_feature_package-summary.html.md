[Skip navigation links](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/package-summary.html#skip-navbar-top "Skip navigation links")
  * [Overview](https://spark.apache.org/docs/latest/api/java/index.html)
  * Package
  * Class
  * [Deprecated](https://spark.apache.org/docs/latest/api/java/deprecated-list.html)
  * [Index](https://spark.apache.org/docs/latest/api/java/index-all.html)
  * [Help](https://spark.apache.org/docs/latest/api/java/help-doc.html#package)

  * Package:
  * [Description](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/package-summary.html#package-description) |
  * [Related Packages](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/package-summary.html#related-package-summary) |
  * [Classes and Interfaces](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/package-summary.html#class-summary)

SEARCH:
# Package org.apache.spark.ml.feature
* * *
package org.apache.spark.ml.feature
Feature transformers The `ml.feature` package provides common feature transformers that help convert raw data or features into more suitable forms for model fitting. Most feature transformers are implemented as [`Transformer`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/Transformer.html "class in org.apache.spark.ml")s, which transforms one [`Dataset`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/Dataset.html "class in org.apache.spark.sql") into another, e.g., [`HashingTF`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/HashingTF.html "class in org.apache.spark.ml.feature"). Some feature transformers are implemented as [`Estimator`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/Estimator.html "class in org.apache.spark.ml")}s, because the transformation requires some aggregated information of the dataset, e.g., document frequencies in [`IDF`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/IDF.html "class in org.apache.spark.ml.feature"). For those feature transformers, calling [`Estimator.fit(org.apache.spark.sql.Dataset<?>, org.apache.spark.ml.param.ParamPair<?>, org.apache.spark.ml.param.ParamPair<?>...)`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/Estimator.html#fit\(org.apache.spark.sql.Dataset,org.apache.spark.ml.param.ParamPair,org.apache.spark.ml.param.ParamPair...\)) is required to obtain the model first, e.g., [`IDFModel`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/IDFModel.html "class in org.apache.spark.ml.feature"), in order to apply transformation. The transformation is usually done by appending new columns to the input [`Dataset`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/Dataset.html "class in org.apache.spark.sql"), so all input columns are carried over. We try to make each transformer minimal, so it becomes flexible to assemble feature transformation pipelines. [`Pipeline`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/Pipeline.html "class in org.apache.spark.ml") can be used to chain feature transformers, and [`VectorAssembler`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/VectorAssembler.html "class in org.apache.spark.ml.feature") can be used to combine multiple feature transformations, for example:
```

   import java.util.Arrays;

   import org.apache.spark.api.java.JavaRDD;
   import static org.apache.spark.sql.types.DataTypes.*;
   import org.apache.spark.sql.types.StructType;
   import org.apache.spark.sql.Dataset;
   import org.apache.spark.sql.RowFactory;
   import org.apache.spark.sql.Row;

   import org.apache.spark.ml.feature.*;
   import org.apache.spark.ml.Pipeline;
   import org.apache.spark.ml.PipelineStage;
   import org.apache.spark.ml.PipelineModel;

  // a DataFrame with three columns: id (integer), text (string), and rating (double).
  StructType schema = createStructType(
    Arrays.asList(
      createStructField("id", IntegerType, false),
      createStructField("text", StringType, false),
      createStructField("rating", DoubleType, false)));
  JavaRDD<Row> rowRDD = jsc.parallelize(
    Arrays.asList(
      RowFactory.create(0, "Hi I heard about Spark", 3.0),
      RowFactory.create(1, "I wish Java could use case classes", 4.0),
      RowFactory.create(2, "Logistic regression models are neat", 4.0)));
  Dataset<Row> dataset = jsql.createDataFrame(rowRDD, schema);
  // define feature transformers
  RegexTokenizer tok = new RegexTokenizer()
    .setInputCol("text")
    .setOutputCol("words");
  StopWordsRemover sw = new StopWordsRemover()
    .setInputCol("words")
    .setOutputCol("filtered_words");
  HashingTF tf = new HashingTF()
    .setInputCol("filtered_words")
    .setOutputCol("tf")
    .setNumFeatures(10000);
  IDF idf = new IDF()
    .setInputCol("tf")
    .setOutputCol("tf_idf");
  VectorAssembler assembler = new VectorAssembler()
    .setInputCols(new String[] {"tf_idf", "rating"})
    .setOutputCol("features");

  // assemble and fit the feature transformation pipeline
  Pipeline pipeline = new Pipeline()
    .setStages(new PipelineStage[] {tok, sw, tf, idf, assembler});
  PipelineModel model = pipeline.fit(dataset);

  // save transformed features with raw data
  model.transform(dataset)
    .select("id", "text", "rating", "features")
    .write().format("parquet").save("/output/path");

```
Some feature transformers implemented in MLlib are inspired by those implemented in scikit-learn. The major difference is that most scikit-learn feature transformers operate eagerly on the entire input dataset, while MLlib's feature transformers operate lazily on individual columns, which is more efficient and flexible to handle large and complex datasets.

See Also:

  * [ scikit-learn.preprocessing](http://scikit-learn.org/stable/modules/preprocessing.html)

  * Related Packages
Package
Description
[org.apache.spark.ml](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/package-summary.html)
DataFrame-based machine learning APIs to let users quickly assemble and configure practical machine learning pipelines.
  * All Classes and InterfacesInterfacesClasses
Class
Description
[Binarizer](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/Binarizer.html "class in org.apache.spark.ml.feature")
Binarize a column of continuous features given a threshold.
[BucketedRandomProjectionLSH](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/BucketedRandomProjectionLSH.html "class in org.apache.spark.ml.feature")
This [`BucketedRandomProjectionLSH`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/BucketedRandomProjectionLSH.html "class in org.apache.spark.ml.feature") implements Locality Sensitive Hashing functions for Euclidean distance metrics.
[BucketedRandomProjectionLSHModel](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/BucketedRandomProjectionLSHModel.html "class in org.apache.spark.ml.feature")
Model produced by [`BucketedRandomProjectionLSH`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/BucketedRandomProjectionLSH.html "class in org.apache.spark.ml.feature"), where multiple random vectors are stored.
[BucketedRandomProjectionLSHModel.Data$](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/BucketedRandomProjectionLSHModel.Data$.html "class in org.apache.spark.ml.feature")
[BucketedRandomProjectionLSHParams](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/BucketedRandomProjectionLSHParams.html "interface in org.apache.spark.ml.feature")
Params for [`BucketedRandomProjectionLSH`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/BucketedRandomProjectionLSH.html "class in org.apache.spark.ml.feature").
[Bucketizer](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/Bucketizer.html "class in org.apache.spark.ml.feature")
`Bucketizer` maps a column of continuous features to a column of feature buckets.
[ChiSqSelector](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/ChiSqSelector.html "class in org.apache.spark.ml.feature")
Deprecated.
use UnivariateFeatureSelector instead.
[ChiSqSelectorModel](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/ChiSqSelectorModel.html "class in org.apache.spark.ml.feature")
Model fitted by [`ChiSqSelector`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/ChiSqSelector.html "class in org.apache.spark.ml.feature").
[ChiSqSelectorModel.ChiSqSelectorModelWriter](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/ChiSqSelectorModel.ChiSqSelectorModelWriter.html "class in org.apache.spark.ml.feature")
[ChiSqSelectorModel.Data$](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/ChiSqSelectorModel.Data$.html "class in org.apache.spark.ml.feature")
[ColumnPruner](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/ColumnPruner.html "class in org.apache.spark.ml.feature")
Utility transformer for removing temporary columns from a DataFrame.
[ColumnPruner.Data$](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/ColumnPruner.Data$.html "class in org.apache.spark.ml.feature")
[CountVectorizer](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/CountVectorizer.html "class in org.apache.spark.ml.feature")
Extracts a vocabulary from document collections and generates a [`CountVectorizerModel`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/CountVectorizerModel.html "class in org.apache.spark.ml.feature").
[CountVectorizerModel](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/CountVectorizerModel.html "class in org.apache.spark.ml.feature")
Converts a text document to a sparse vector of token counts.
[CountVectorizerModel.Data$](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/CountVectorizerModel.Data$.html "class in org.apache.spark.ml.feature")
[CountVectorizerParams](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/CountVectorizerParams.html "interface in org.apache.spark.ml.feature")
Params for [`CountVectorizer`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/CountVectorizer.html "class in org.apache.spark.ml.feature") and [`CountVectorizerModel`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/CountVectorizerModel.html "class in org.apache.spark.ml.feature").
[DCT](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/DCT.html "class in org.apache.spark.ml.feature")
A feature transformer that takes the 1D discrete cosine transform of a real vector.
[Dot](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/Dot.html "class in org.apache.spark.ml.feature")
[ElementwiseProduct](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/ElementwiseProduct.html "class in org.apache.spark.ml.feature")
Outputs the Hadamard product (i.e., the element-wise product) of each input vector with a provided "weight" vector.
[EmptyTerm](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/EmptyTerm.html "class in org.apache.spark.ml.feature")
Placeholder term for the result of undefined interactions, e.g.
[FeatureHasher](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/FeatureHasher.html "class in org.apache.spark.ml.feature")
Feature hashing projects a set of categorical or numerical features into a feature vector of specified dimension (typically substantially smaller than that of the original feature space).
[HashingTF](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/HashingTF.html "class in org.apache.spark.ml.feature")
Maps a sequence of terms to their term frequencies using the hashing trick.
[IDF](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/IDF.html "class in org.apache.spark.ml.feature")
Compute the Inverse Document Frequency (IDF) given a collection of documents.
[IDFBase](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/IDFBase.html "interface in org.apache.spark.ml.feature")
Params for [`IDF`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/IDF.html "class in org.apache.spark.ml.feature") and [`IDFModel`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/IDFModel.html "class in org.apache.spark.ml.feature").
[IDFModel](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/IDFModel.html "class in org.apache.spark.ml.feature")
Model fitted by [`IDF`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/IDF.html "class in org.apache.spark.ml.feature").
[IDFModel.Data$](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/IDFModel.Data$.html "class in org.apache.spark.ml.feature")
[Imputer](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/Imputer.html "class in org.apache.spark.ml.feature")
Imputation estimator for completing missing values, using the mean, median or mode of the columns in which the missing values are located.
[ImputerModel](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/ImputerModel.html "class in org.apache.spark.ml.feature")
Model fitted by [`Imputer`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/Imputer.html "class in org.apache.spark.ml.feature").
[ImputerParams](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/ImputerParams.html "interface in org.apache.spark.ml.feature")
Params for [`Imputer`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/Imputer.html "class in org.apache.spark.ml.feature") and [`ImputerModel`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/ImputerModel.html "class in org.apache.spark.ml.feature").
[IndexToString](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/IndexToString.html "class in org.apache.spark.ml.feature")
A `Transformer` that maps a column of indices back to a new column of corresponding string values.
[InteractableTerm](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/InteractableTerm.html "interface in org.apache.spark.ml.feature")
A term that may be part of an interaction, e.g.
[Interaction](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/Interaction.html "class in org.apache.spark.ml.feature")
Implements the feature interaction transform.
[LabeledPoint](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/LabeledPoint.html "class in org.apache.spark.ml.feature")
Class that represents the features and label of a data point.
[LSHParams](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/LSHParams.html "interface in org.apache.spark.ml.feature")
Params for `LSH`.
[MaxAbsScaler](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/MaxAbsScaler.html "class in org.apache.spark.ml.feature")
Rescale each feature individually to range [-1, 1] by dividing through the largest maximum absolute value in each feature.
[MaxAbsScalerModel](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/MaxAbsScalerModel.html "class in org.apache.spark.ml.feature")
Model fitted by [`MaxAbsScaler`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/MaxAbsScaler.html "class in org.apache.spark.ml.feature").
[MaxAbsScalerModel.Data$](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/MaxAbsScalerModel.Data$.html "class in org.apache.spark.ml.feature")
[MaxAbsScalerParams](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/MaxAbsScalerParams.html "interface in org.apache.spark.ml.feature")
Params for [`MaxAbsScaler`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/MaxAbsScaler.html "class in org.apache.spark.ml.feature") and [`MaxAbsScalerModel`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/MaxAbsScalerModel.html "class in org.apache.spark.ml.feature").
[MinHashLSH](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/MinHashLSH.html "class in org.apache.spark.ml.feature")
LSH class for Jaccard distance.
[MinHashLSHModel](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/MinHashLSHModel.html "class in org.apache.spark.ml.feature")
Model produced by [`MinHashLSH`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/MinHashLSH.html "class in org.apache.spark.ml.feature"), where multiple hash functions are stored.
[MinHashLSHModel.Data$](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/MinHashLSHModel.Data$.html "class in org.apache.spark.ml.feature")
[MinMaxScaler](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/MinMaxScaler.html "class in org.apache.spark.ml.feature")
Rescale each feature individually to a common range [min, max] linearly using column summary statistics, which is also known as min-max normalization or Rescaling.
[MinMaxScalerModel](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/MinMaxScalerModel.html "class in org.apache.spark.ml.feature")
Model fitted by [`MinMaxScaler`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/MinMaxScaler.html "class in org.apache.spark.ml.feature").
[MinMaxScalerModel.Data$](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/MinMaxScalerModel.Data$.html "class in org.apache.spark.ml.feature")
[MinMaxScalerParams](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/MinMaxScalerParams.html "interface in org.apache.spark.ml.feature")
Params for [`MinMaxScaler`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/MinMaxScaler.html "class in org.apache.spark.ml.feature") and [`MinMaxScalerModel`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/MinMaxScalerModel.html "class in org.apache.spark.ml.feature").
[NGram](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/NGram.html "class in org.apache.spark.ml.feature")
A feature transformer that converts the input array of strings into an array of n-grams.
[Normalizer](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/Normalizer.html "class in org.apache.spark.ml.feature")
Normalize a vector to have unit norm using the given p-norm.
[OneHotEncoder](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/OneHotEncoder.html "class in org.apache.spark.ml.feature")
A one-hot encoder that maps a column of category indices to a column of binary vectors, with at most a single one-value per row that indicates the input category index.
[OneHotEncoderBase](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/OneHotEncoderBase.html "interface in org.apache.spark.ml.feature")
Private trait for params and common methods for OneHotEncoder and OneHotEncoderModel
[OneHotEncoderCommon](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/OneHotEncoderCommon.html "class in org.apache.spark.ml.feature")
Provides some helper methods used by `OneHotEncoder`.
[OneHotEncoderModel](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/OneHotEncoderModel.html "class in org.apache.spark.ml.feature")
param: categorySizes Original number of categories for each feature being encoded.
[OneHotEncoderModel.Data$](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/OneHotEncoderModel.Data$.html "class in org.apache.spark.ml.feature")
[PCA](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/PCA.html "class in org.apache.spark.ml.feature")
PCA trains a model to project vectors to a lower dimensional space of the top `PCA!.k` principal components.
[PCAModel](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/PCAModel.html "class in org.apache.spark.ml.feature")
Model fitted by [`PCA`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/PCA.html "class in org.apache.spark.ml.feature").
[PCAModel.Data$](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/PCAModel.Data$.html "class in org.apache.spark.ml.feature")
[PCAParams](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/PCAParams.html "interface in org.apache.spark.ml.feature")
Params for [`PCA`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/PCA.html "class in org.apache.spark.ml.feature") and [`PCAModel`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/PCAModel.html "class in org.apache.spark.ml.feature").
[PolynomialExpansion](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/PolynomialExpansion.html "class in org.apache.spark.ml.feature")
Perform feature expansion in a polynomial space.
[QuantileDiscretizer](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/QuantileDiscretizer.html "class in org.apache.spark.ml.feature")
`QuantileDiscretizer` takes a column with continuous features and outputs a column with binned categorical features.
[QuantileDiscretizerBase](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/QuantileDiscretizerBase.html "interface in org.apache.spark.ml.feature")
Params for [`QuantileDiscretizer`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/QuantileDiscretizer.html "class in org.apache.spark.ml.feature").
[RegexTokenizer](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/RegexTokenizer.html "class in org.apache.spark.ml.feature")
A regex based tokenizer that extracts tokens either by using the provided regex pattern to split the text (default) or repeatedly matching the regex (if `gaps` is false).
[RFormula](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/RFormula.html "class in org.apache.spark.ml.feature")
Implements the transforms required for fitting a dataset against an R model formula.
[RFormulaBase](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/RFormulaBase.html "interface in org.apache.spark.ml.feature")
Base trait for [`RFormula`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/RFormula.html "class in org.apache.spark.ml.feature") and [`RFormulaModel`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/RFormulaModel.html "class in org.apache.spark.ml.feature").
[RFormulaModel](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/RFormulaModel.html "class in org.apache.spark.ml.feature")
Model fitted by [`RFormula`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/RFormula.html "class in org.apache.spark.ml.feature").
[RFormulaParser](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/RFormulaParser.html "class in org.apache.spark.ml.feature")
Limited implementation of R formula parsing.
[RobustScaler](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/RobustScaler.html "class in org.apache.spark.ml.feature")
Scale features using statistics that are robust to outliers.
[RobustScalerModel](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/RobustScalerModel.html "class in org.apache.spark.ml.feature")
Model fitted by [`RobustScaler`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/RobustScaler.html "class in org.apache.spark.ml.feature").
[RobustScalerModel.Data$](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/RobustScalerModel.Data$.html "class in org.apache.spark.ml.feature")
[RobustScalerParams](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/RobustScalerParams.html "interface in org.apache.spark.ml.feature")
Params for [`RobustScaler`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/RobustScaler.html "class in org.apache.spark.ml.feature") and [`RobustScalerModel`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/RobustScalerModel.html "class in org.apache.spark.ml.feature").
[SelectorParams](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/SelectorParams.html "interface in org.apache.spark.ml.feature")
Params for `Selector` and `SelectorModel`.
[SQLTransformer](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/SQLTransformer.html "class in org.apache.spark.ml.feature")
Implements the transformations which are defined by SQL statement.
[StandardScaler](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/StandardScaler.html "class in org.apache.spark.ml.feature")
Standardizes features by removing the mean and scaling to unit variance using column summary statistics on the samples in the training set.
[StandardScalerModel](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/StandardScalerModel.html "class in org.apache.spark.ml.feature")
Model fitted by [`StandardScaler`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/StandardScaler.html "class in org.apache.spark.ml.feature").
[StandardScalerModel.Data$](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/StandardScalerModel.Data$.html "class in org.apache.spark.ml.feature")
[StandardScalerParams](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/StandardScalerParams.html "interface in org.apache.spark.ml.feature")
Params for [`StandardScaler`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/StandardScaler.html "class in org.apache.spark.ml.feature") and [`StandardScalerModel`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/StandardScalerModel.html "class in org.apache.spark.ml.feature").
[StopWordsRemover](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/StopWordsRemover.html "class in org.apache.spark.ml.feature")
A feature transformer that filters out stop words from input.
[StringIndexer](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/StringIndexer.html "class in org.apache.spark.ml.feature")
A label indexer that maps string column(s) of labels to ML column(s) of label indices.
[StringIndexerBase](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/StringIndexerBase.html "interface in org.apache.spark.ml.feature")
Base trait for [`StringIndexer`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/StringIndexer.html "class in org.apache.spark.ml.feature") and [`StringIndexerModel`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/StringIndexerModel.html "class in org.apache.spark.ml.feature").
[StringIndexerModel](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/StringIndexerModel.html "class in org.apache.spark.ml.feature")
Model fitted by [`StringIndexer`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/StringIndexer.html "class in org.apache.spark.ml.feature").
[StringIndexerModel.Data$](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/StringIndexerModel.Data$.html "class in org.apache.spark.ml.feature")
[TargetEncoder](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/TargetEncoder.html "class in org.apache.spark.ml.feature")
Target Encoding maps a column of categorical indices into a numerical feature derived from the target.
[TargetEncoderBase](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/TargetEncoderBase.html "interface in org.apache.spark.ml.feature")
Private trait for params and common methods for TargetEncoder and TargetEncoderModel
[TargetEncoderModel](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/TargetEncoderModel.html "class in org.apache.spark.ml.feature")
param: stats Array of statistics for each input feature.
[TargetEncoderModel.Data$](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/TargetEncoderModel.Data$.html "class in org.apache.spark.ml.feature")
[Term](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/Term.html "interface in org.apache.spark.ml.feature")
R formula terms.
[Tokenizer](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/Tokenizer.html "class in org.apache.spark.ml.feature")
A tokenizer that converts the input string to lowercase and then splits it by white spaces.
[UnivariateFeatureSelector](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/UnivariateFeatureSelector.html "class in org.apache.spark.ml.feature")
Feature selector based on univariate statistical tests against labels.
[UnivariateFeatureSelectorModel](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/UnivariateFeatureSelectorModel.html "class in org.apache.spark.ml.feature")
Model fitted by [`UnivariateFeatureSelectorModel`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/UnivariateFeatureSelectorModel.html "class in org.apache.spark.ml.feature").
[UnivariateFeatureSelectorModel.Data$](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/UnivariateFeatureSelectorModel.Data$.html "class in org.apache.spark.ml.feature")
[UnivariateFeatureSelectorParams](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/UnivariateFeatureSelectorParams.html "interface in org.apache.spark.ml.feature")
Params for [`UnivariateFeatureSelector`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/UnivariateFeatureSelector.html "class in org.apache.spark.ml.feature") and [`UnivariateFeatureSelectorModel`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/UnivariateFeatureSelectorModel.html "class in org.apache.spark.ml.feature").
[VarianceThresholdSelector](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/VarianceThresholdSelector.html "class in org.apache.spark.ml.feature")
Feature selector that removes all low-variance features.
[VarianceThresholdSelectorModel](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/VarianceThresholdSelectorModel.html "class in org.apache.spark.ml.feature")
Model fitted by [`VarianceThresholdSelector`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/VarianceThresholdSelector.html "class in org.apache.spark.ml.feature").
[VarianceThresholdSelectorModel.Data$](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/VarianceThresholdSelectorModel.Data$.html "class in org.apache.spark.ml.feature")
[VarianceThresholdSelectorParams](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/VarianceThresholdSelectorParams.html "interface in org.apache.spark.ml.feature")
Params for [`VarianceThresholdSelector`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/VarianceThresholdSelector.html "class in org.apache.spark.ml.feature") and [`VarianceThresholdSelectorModel`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/VarianceThresholdSelectorModel.html "class in org.apache.spark.ml.feature").
[VectorAssembler](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/VectorAssembler.html "class in org.apache.spark.ml.feature")
A feature transformer that merges multiple columns into a vector column.
[VectorAttributeRewriter](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/VectorAttributeRewriter.html "class in org.apache.spark.ml.feature")
Utility transformer that rewrites Vector attribute names via prefix replacement.
[VectorAttributeRewriter.Data$](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/VectorAttributeRewriter.Data$.html "class in org.apache.spark.ml.feature")
[VectorIndexer](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/VectorIndexer.html "class in org.apache.spark.ml.feature")
Class for indexing categorical feature columns in a dataset of `Vector`.
[VectorIndexerModel](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/VectorIndexerModel.html "class in org.apache.spark.ml.feature")
Model fitted by [`VectorIndexer`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/VectorIndexer.html "class in org.apache.spark.ml.feature").
[VectorIndexerModel.Data$](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/VectorIndexerModel.Data$.html "class in org.apache.spark.ml.feature")
[VectorIndexerParams](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/VectorIndexerParams.html "interface in org.apache.spark.ml.feature")
Private trait for params for VectorIndexer and VectorIndexerModel
[VectorSizeHint](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/VectorSizeHint.html "class in org.apache.spark.ml.feature")
A feature transformer that adds size information to the metadata of a vector column.
[VectorSlicer](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/VectorSlicer.html "class in org.apache.spark.ml.feature")
This class takes a feature vector and outputs a new feature vector with a subarray of the original features.
[Word2Vec](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/Word2Vec.html "class in org.apache.spark.ml.feature")
Word2Vec trains a model of `Map(String, Vector)`, i.e.
[Word2VecBase](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/Word2VecBase.html "interface in org.apache.spark.ml.feature")
Params for [`Word2Vec`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/Word2Vec.html "class in org.apache.spark.ml.feature") and [`Word2VecModel`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/Word2VecModel.html "class in org.apache.spark.ml.feature").
[Word2VecModel](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/Word2VecModel.html "class in org.apache.spark.ml.feature")
Model fitted by [`Word2Vec`](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/Word2Vec.html "class in org.apache.spark.ml.feature").
[Word2VecModel.Data$](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/Word2VecModel.Data$.html "class in org.apache.spark.ml.feature")
[Word2VecModel.Word2VecModelWriter$](https://spark.apache.org/docs/latest/api/java/org/apache/spark/ml/feature/Word2VecModel.Word2VecModelWriter$.html "class in org.apache.spark.ml.feature")

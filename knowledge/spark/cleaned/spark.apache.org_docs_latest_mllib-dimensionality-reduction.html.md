[ ![](https://spark.apache.org/images/spark-logo-rev.svg)](https://spark.apache.org/docs/latest/index.html)4.1.2
  * [Overview](https://spark.apache.org/docs/latest/index.html)
  * [Programming Guides](https://spark.apache.org/docs/latest/mllib-dimensionality-reduction.html)
[Quick Start](https://spark.apache.org/docs/latest/quick-start.html) [RDDs, Accumulators, Broadcasts Vars](https://spark.apache.org/docs/latest/rdd-programming-guide.html) [SQL, DataFrames, and Datasets](https://spark.apache.org/docs/latest/sql-programming-guide.html) [Structured Streaming](https://spark.apache.org/docs/latest/streaming/index.html) [Spark Streaming (DStreams)](https://spark.apache.org/docs/latest/streaming-programming-guide.html) [MLlib (Machine Learning)](https://spark.apache.org/docs/latest/ml-guide.html) [GraphX (Graph Processing)](https://spark.apache.org/docs/latest/graphx-programming-guide.html) [SparkR (R on Spark)](https://spark.apache.org/docs/latest/sparkr.html) [PySpark (Python on Spark)](https://spark.apache.org/docs/latest/api/python/getting_started/index.html) [Declarative Pipelines](https://spark.apache.org/docs/latest/declarative-pipelines-programming-guide.html)
  * [API Docs](https://spark.apache.org/docs/latest/mllib-dimensionality-reduction.html)
[Python](https://spark.apache.org/docs/latest/api/python/index.html) [Scala](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html) [Java](https://spark.apache.org/docs/latest/api/java/index.html) [R](https://spark.apache.org/docs/latest/api/R/index.html) [SQL, Built-in Functions](https://spark.apache.org/docs/latest/api/sql/index.html)
  * [Deploying](https://spark.apache.org/docs/latest/mllib-dimensionality-reduction.html)
[Overview](https://spark.apache.org/docs/latest/cluster-overview.html) [Submitting Applications](https://spark.apache.org/docs/latest/submitting-applications.html) [Spark Standalone](https://spark.apache.org/docs/latest/spark-standalone.html) [YARN](https://spark.apache.org/docs/latest/running-on-yarn.html) [Kubernetes](https://spark.apache.org/docs/latest/running-on-kubernetes.html)
  * [More](https://spark.apache.org/docs/latest/mllib-dimensionality-reduction.html)
[Configuration](https://spark.apache.org/docs/latest/configuration.html) [Monitoring](https://spark.apache.org/docs/latest/monitoring.html) [Tuning Guide](https://spark.apache.org/docs/latest/tuning.html) [Job Scheduling](https://spark.apache.org/docs/latest/job-scheduling.html) [Security](https://spark.apache.org/docs/latest/security.html) [Hardware Provisioning](https://spark.apache.org/docs/latest/hardware-provisioning.html) [Migration Guide](https://spark.apache.org/docs/latest/migration-guide.html) [Building Spark](https://spark.apache.org/docs/latest/building-spark.html) [Contributing to Spark](https://spark.apache.org/contributing.html) [Third Party Projects](https://spark.apache.org/third-party-projects.html)
  *

###  [MLlib: Main Guide](https://spark.apache.org/docs/latest/ml-guide.html)[](https://spark.apache.org/docs/latest/mllib-dimensionality-reduction.html#mllib-main-guide)
  * [ Basic statistics ](https://spark.apache.org/docs/latest/ml-statistics.html)
  * [ Data sources ](https://spark.apache.org/docs/latest/ml-datasource.html)
  * [ Pipelines ](https://spark.apache.org/docs/latest/ml-pipeline.html)
  * [ Extracting, transforming and selecting features ](https://spark.apache.org/docs/latest/ml-features.html)
  * [ Classification and Regression ](https://spark.apache.org/docs/latest/ml-classification-regression.html)
  * [ Clustering ](https://spark.apache.org/docs/latest/ml-clustering.html)
  * [ Collaborative filtering ](https://spark.apache.org/docs/latest/ml-collaborative-filtering.html)
  * [ Frequent Pattern Mining ](https://spark.apache.org/docs/latest/ml-frequent-pattern-mining.html)
  * [ Model selection and tuning ](https://spark.apache.org/docs/latest/ml-tuning.html)
  * [ Advanced topics ](https://spark.apache.org/docs/latest/ml-advanced.html)

###  [MLlib: RDD-based API Guide](https://spark.apache.org/docs/latest/mllib-guide.html)[](https://spark.apache.org/docs/latest/mllib-dimensionality-reduction.html#mllib-rdd-based-api-guide)
  * [ Data types ](https://spark.apache.org/docs/latest/mllib-data-types.html)
  * [ Basic statistics ](https://spark.apache.org/docs/latest/mllib-statistics.html)
  * [ Classification and regression ](https://spark.apache.org/docs/latest/mllib-classification-regression.html)
  * [ Collaborative filtering ](https://spark.apache.org/docs/latest/mllib-collaborative-filtering.html)
  * [ Clustering ](https://spark.apache.org/docs/latest/mllib-clustering.html)
  * [ Dimensionality reduction ](https://spark.apache.org/docs/latest/mllib-dimensionality-reduction.html)
    * [ singular value decomposition (SVD) ](https://spark.apache.org/docs/latest/mllib-dimensionality-reduction.html#singular-value-decomposition-svd)
    * [ principal component analysis (PCA) ](https://spark.apache.org/docs/latest/mllib-dimensionality-reduction.html#principal-component-analysis-pca)
  * [ Feature extraction and transformation ](https://spark.apache.org/docs/latest/mllib-feature-extraction.html)
  * [ Frequent pattern mining ](https://spark.apache.org/docs/latest/mllib-frequent-pattern-mining.html)
  * [ Evaluation metrics ](https://spark.apache.org/docs/latest/mllib-evaluation-metrics.html)
  * [ PMML model export ](https://spark.apache.org/docs/latest/mllib-pmml-model-export.html)
  * [ Optimization (developer) ](https://spark.apache.org/docs/latest/mllib-optimization.html)

# Dimensionality Reduction - RDD-based API[](https://spark.apache.org/docs/latest/mllib-dimensionality-reduction.html#dimensionality-reduction-rdd-based-api)
  * [Singular value decomposition (SVD)](https://spark.apache.org/docs/latest/mllib-dimensionality-reduction.html#singular-value-decomposition-svd)
    * [Performance](https://spark.apache.org/docs/latest/mllib-dimensionality-reduction.html#performance)
    * [SVD Example](https://spark.apache.org/docs/latest/mllib-dimensionality-reduction.html#svd-example)
  * [Principal component analysis (PCA)](https://spark.apache.org/docs/latest/mllib-dimensionality-reduction.html#principal-component-analysis-pca)

[Dimensionality reduction](http://en.wikipedia.org/wiki/Dimensionality_reduction) is the process of reducing the number of variables under consideration. It can be used to extract latent features from raw and noisy features or compress data while maintaining the structure. `spark.mllib` provides support for dimensionality reduction on the [RowMatrix](https://spark.apache.org/docs/latest/mllib-data-types.html#rowmatrix) class.
## Singular value decomposition (SVD)[](https://spark.apache.org/docs/latest/mllib-dimensionality-reduction.html#singular-value-decomposition-svd)
[Singular value decomposition (SVD)](http://en.wikipedia.org/wiki/Singular_value_decomposition) factorizes a matrix into three matrices: $U$, $\Sigma$, and $V$ such that
`\[ A = U \Sigma V^T, \]`
where
  * $U$ is an orthonormal matrix, whose columns are called left singular vectors,
  * $\Sigma$ is a diagonal matrix with non-negative diagonals in descending order, whose diagonals are called singular values,
  * $V$ is an orthonormal matrix, whose columns are called right singular vectors.

For large matrices, usually we don’t need the complete factorization but only the top singular values and its associated singular vectors. This can save storage, de-noise and recover the low-rank structure of the matrix.
If we keep the top $k$ singular values, then the dimensions of the resulting low-rank matrix will be:
  * `$U$`: `$m \times k$`,
  * `$\Sigma$`: `$k \times k$`,
  * `$V$`: `$n \times k$`.

### Performance[](https://spark.apache.org/docs/latest/mllib-dimensionality-reduction.html#performance)
We assume $n$ is smaller than $m$. The singular values and the right singular vectors are derived from the eigenvalues and the eigenvectors of the Gramian matrix $A^T A$. The matrix storing the left singular vectors $U$, is computed via matrix multiplication as $U = A (V S^{-1})$, if requested by the user via the computeU parameter. The actual method to use is determined automatically based on the computational cost:
  * If $n$ is small ($n < 100$) or $k$ is large compared with $n$ ($k > n / 2$), we compute the Gramian matrix first and then compute its top eigenvalues and eigenvectors locally on the driver. This requires a single pass with $O(n^2)$ storage on each executor and on the driver, and $O(n^2 k)$ time on the driver.
  * Otherwise, we compute $(A^T A) v$ in a distributive way and send it to [ARPACK](https://web.archive.org/web/20210503024933/http://www.caam.rice.edu/software/ARPACK) to compute $(A^T A)$’s top eigenvalues and eigenvectors on the driver node. This requires $O(k)$ passes, $O(n)$ storage on each executor, and $O(n k)$ storage on the driver.

### SVD Example[](https://spark.apache.org/docs/latest/mllib-dimensionality-reduction.html#svd-example)
`spark.mllib` provides SVD functionality to row-oriented matrices, provided in the [RowMatrix](https://spark.apache.org/docs/latest/mllib-data-types.html#rowmatrix) class.
  * **Python**
  * **Scala**
  * **Java**

Refer to the [`SingularValueDecomposition` Python docs](https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.mllib.linalg.distributed.SingularValueDecomposition.html) for details on the API.

```
from pyspark.mllib.linalg import Vectors
from pyspark.mllib.linalg.distributed import RowMatrix

rows = sc.parallelize([
    Vectors.sparse(5, {1: 1.0, 3: 7.0}),
    Vectors.dense(2.0, 0.0, 3.0, 4.0, 5.0),
    Vectors.dense(4.0, 0.0, 0.0, 6.0, 7.0)
])

mat = RowMatrix(rows)

# Compute the top 5 singular values and corresponding singular vectors.
svd = mat.computeSVD(5, computeU=True)
U = svd.U       # The U factor is a RowMatrix.
s = svd.s       # The singular values are stored in a local dense vector.
V = svd.V       # The V factor is a local dense matrix.
```

Find full example code at "examples/src/main/python/mllib/svd_example.py" in the Spark repo.
The same code applies to `IndexedRowMatrix` if `U` is defined as an `IndexedRowMatrix`.
Refer to the [`SingularValueDecomposition` Scala docs](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/mllib/linalg/SingularValueDecomposition.html) for details on the API.

```
import org.apache.spark.mllib.linalg.Matrix
import org.apache.spark.mllib.linalg.SingularValueDecomposition
import org.apache.spark.mllib.linalg.Vector
import org.apache.spark.mllib.linalg.Vectors
import org.apache.spark.mllib.linalg.distributed.RowMatrix

val data = Array(
  Vectors.sparse(5, Seq((1, 1.0), (3, 7.0))),
  Vectors.dense(2.0, 0.0, 3.0, 4.0, 5.0),
  Vectors.dense(4.0, 0.0, 0.0, 6.0, 7.0))

val rows = sc.parallelize(immutable.ArraySeq.unsafeWrapArray(data))

val mat: RowMatrix = new RowMatrix(rows)

// Compute the top 5 singular values and corresponding singular vectors.
val svd: SingularValueDecomposition[RowMatrix, Matrix] = mat.computeSVD(5, computeU = true)
val U: RowMatrix = svd.U  // The U factor is a RowMatrix.
val s: Vector = svd.s     // The singular values are stored in a local dense vector.
val V: Matrix = svd.V     // The V factor is a local dense matrix.
```

Find full example code at "examples/src/main/scala/org/apache/spark/examples/mllib/SVDExample.scala" in the Spark repo.
The same code applies to `IndexedRowMatrix` if `U` is defined as an `IndexedRowMatrix`.
Refer to the [`SingularValueDecomposition` Java docs](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/linalg/SingularValueDecomposition.html) for details on the API.

```
import java.util.Arrays;
import java.util.List;

import org.apache.spark.api.java.JavaRDD;
import org.apache.spark.api.java.JavaSparkContext;
import org.apache.spark.mllib.linalg.Matrix;
import org.apache.spark.mllib.linalg.SingularValueDecomposition;
import org.apache.spark.mllib.linalg.Vector;
import org.apache.spark.mllib.linalg.Vectors;
import org.apache.spark.mllib.linalg.distributed.RowMatrix;

List<Vector> data = Arrays.asList(
        Vectors.sparse(5, new int[] {1, 3}, new double[] {1.0, 7.0}),
        Vectors.dense(2.0, 0.0, 3.0, 4.0, 5.0),
        Vectors.dense(4.0, 0.0, 0.0, 6.0, 7.0)
);

JavaRDD<Vector> rows = jsc.parallelize(data);

// Create a RowMatrix from JavaRDD<Vector>.
RowMatrix mat = new RowMatrix(rows.rdd());

// Compute the top 5 singular values and corresponding singular vectors.
SingularValueDecomposition<RowMatrix, Matrix> svd = mat.computeSVD(5, true, 1.0E-9d);
RowMatrix U = svd.U();  // The U factor is a RowMatrix.
Vector s = svd.s();     // The singular values are stored in a local dense vector.
Matrix V = svd.V();     // The V factor is a local dense matrix.
```

Find full example code at "examples/src/main/java/org/apache/spark/examples/mllib/JavaSVDExample.java" in the Spark repo.
The same code applies to `IndexedRowMatrix` if `U` is defined as an `IndexedRowMatrix`.
## Principal component analysis (PCA)[](https://spark.apache.org/docs/latest/mllib-dimensionality-reduction.html#principal-component-analysis-pca)
[Principal component analysis (PCA)](http://en.wikipedia.org/wiki/Principal_component_analysis) is a statistical method to find a rotation such that the first coordinate has the largest variance possible, and each succeeding coordinate, in turn, has the largest variance possible. The columns of the rotation matrix are called principal components. PCA is used widely in dimensionality reduction.
`spark.mllib` supports PCA for tall-and-skinny matrices stored in row-oriented format and any Vectors.
  * **Python**
  * **Scala**
  * **Java**

The following code demonstrates how to compute principal components on a `RowMatrix` and use them to project the vectors into a low-dimensional space.
Refer to the [`RowMatrix` Python docs](https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.mllib.linalg.distributed.RowMatrix.html) for details on the API.

```
from pyspark.mllib.linalg import Vectors
from pyspark.mllib.linalg.distributed import RowMatrix

rows = sc.parallelize([
    Vectors.sparse(5, {1: 1.0, 3: 7.0}),
    Vectors.dense(2.0, 0.0, 3.0, 4.0, 5.0),
    Vectors.dense(4.0, 0.0, 0.0, 6.0, 7.0)
])

mat = RowMatrix(rows)
# Compute the top 4 principal components.
# Principal components are stored in a local dense matrix.
pc = mat.computePrincipalComponents(4)

# Project the rows to the linear space spanned by the top 4 principal components.
projected = mat.multiply(pc)
```

Find full example code at "examples/src/main/python/mllib/pca_rowmatrix_example.py" in the Spark repo.
The following code demonstrates how to compute principal components on a `RowMatrix` and use them to project the vectors into a low-dimensional space.
Refer to the [`RowMatrix` Scala docs](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/mllib/linalg/distributed/RowMatrix.html) for details on the API.

```
import org.apache.spark.mllib.linalg.Matrix
import org.apache.spark.mllib.linalg.Vectors
import org.apache.spark.mllib.linalg.distributed.RowMatrix

val data = Array(
  Vectors.sparse(5, Seq((1, 1.0), (3, 7.0))),
  Vectors.dense(2.0, 0.0, 3.0, 4.0, 5.0),
  Vectors.dense(4.0, 0.0, 0.0, 6.0, 7.0))

val rows = sc.parallelize(immutable.ArraySeq.unsafeWrapArray(data))

val mat: RowMatrix = new RowMatrix(rows)

// Compute the top 4 principal components.
// Principal components are stored in a local dense matrix.
val pc: Matrix = mat.computePrincipalComponents(4)

// Project the rows to the linear space spanned by the top 4 principal components.
val projected: RowMatrix = mat.multiply(pc)
```

Find full example code at "examples/src/main/scala/org/apache/spark/examples/mllib/PCAOnRowMatrixExample.scala" in the Spark repo.
The following code demonstrates how to compute principal components on source vectors and use them to project the vectors into a low-dimensional space while keeping associated labels:
Refer to the [`PCA` Scala docs](https://spark.apache.org/docs/latest/api/scala/org/apache/spark/mllib/feature/PCA.html) for details on the API.

```
import org.apache.spark.mllib.feature.PCA
import org.apache.spark.mllib.linalg.Vectors
import org.apache.spark.mllib.regression.LabeledPoint
import org.apache.spark.rdd.RDD

val data: RDD[LabeledPoint] = sc.parallelize(Seq(
  new LabeledPoint(0, Vectors.dense(1, 0, 0, 0, 1)),
  new LabeledPoint(1, Vectors.dense(1, 1, 0, 1, 0)),
  new LabeledPoint(1, Vectors.dense(1, 1, 0, 0, 0)),
  new LabeledPoint(0, Vectors.dense(1, 0, 0, 0, 0)),
  new LabeledPoint(1, Vectors.dense(1, 1, 0, 0, 0))))

// Compute the top 5 principal components.
val pca = new PCA(5).fit(data.map(_.features))

// Project vectors to the linear space spanned by the top 5 principal
// components, keeping the label
val projected = data.map(p => p.copy(features = pca.transform(p.features)))
```

Find full example code at "examples/src/main/scala/org/apache/spark/examples/mllib/PCAOnSourceVectorExample.scala" in the Spark repo.
The following code demonstrates how to compute principal components on a `RowMatrix` and use them to project the vectors into a low-dimensional space.
Refer to the [`RowMatrix` Java docs](https://spark.apache.org/docs/latest/api/java/org/apache/spark/mllib/linalg/distributed/RowMatrix.html) for details on the API.

```
import java.util.Arrays;
import java.util.List;

import org.apache.spark.api.java.JavaRDD;
import org.apache.spark.api.java.JavaSparkContext;
import org.apache.spark.mllib.linalg.Matrix;
import org.apache.spark.mllib.linalg.Vector;
import org.apache.spark.mllib.linalg.Vectors;
import org.apache.spark.mllib.linalg.distributed.RowMatrix;

List<Vector> data = Arrays.asList(
        Vectors.sparse(5, new int[] {1, 3}, new double[] {1.0, 7.0}),
        Vectors.dense(2.0, 0.0, 3.0, 4.0, 5.0),
        Vectors.dense(4.0, 0.0, 0.0, 6.0, 7.0)
);

JavaRDD<Vector> rows = jsc.parallelize(data);

// Create a RowMatrix from JavaRDD<Vector>.
RowMatrix mat = new RowMatrix(rows.rdd());

// Compute the top 4 principal components.
// Principal components are stored in a local dense matrix.
Matrix pc = mat.computePrincipalComponents(4);

// Project the rows to the linear space spanned by the top 4 principal components.
RowMatrix projected = mat.multiply(pc);
```

Find full example code at "examples/src/main/java/org/apache/spark/examples/mllib/JavaPCAExample.java" in the Spark repo.

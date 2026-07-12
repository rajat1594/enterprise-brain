[Skip to contents](https://arrow.apache.org/docs/r/#main)
[Arrow R Package](https://arrow.apache.org/docs/r/index.html) 24.0.0
  * [Get started](https://arrow.apache.org/docs/r/articles/arrow.html)
  * [Reference](https://arrow.apache.org/docs/r/reference/index.html)
  * Articles
    * * * *
    * ###### Using the package
    * [Reading and writing data files](https://arrow.apache.org/docs/r/articles/read_write.html)
    * [Data analysis with dplyr syntax](https://arrow.apache.org/docs/r/articles/data_wrangling.html)
    * [Working with multi-file data sets](https://arrow.apache.org/docs/r/articles/dataset.html)
    * [Integrating Arrow, Python, and R](https://arrow.apache.org/docs/r/articles/python.html)
    * [Using cloud storage (S3, GCS)](https://arrow.apache.org/docs/r/articles/fs.html)
    * [Connecting to a Flight server](https://arrow.apache.org/docs/r/articles/flight.html)
    * * * *
    * ###### Arrow concepts
    * [Data objects](https://arrow.apache.org/docs/r/articles/data_objects.html)
    * [Data types](https://arrow.apache.org/docs/r/articles/data_types.html)
    * [Metadata](https://arrow.apache.org/docs/r/articles/metadata.html)
    * * * *
    * ###### Installation
    * [Installing on Linux](https://arrow.apache.org/docs/r/articles/install.html)
    * [Installing development versions](https://arrow.apache.org/docs/r/articles/install_nightly.html)
    * * * *
    * [More articles...](https://arrow.apache.org/docs/r/articles/index.html)
  * [Changelog](https://arrow.apache.org/docs/r/news/index.html)


  * [](https://github.com/apache/arrow/)


# arrow ![](https://arrow.apache.org/img/arrow-logo_hex_black-txt_white-bg.png)[](https://arrow.apache.org/docs/r/#arrow-)
## Overview[](https://arrow.apache.org/docs/r/#overview)
The R [arrow](https://github.com/apache/arrow/) package provides access to many of the features of the [Apache Arrow C++ library](https://arrow.apache.org/docs/cpp/index.html) for R users. The goal of arrow is to provide an Arrow C++ backend to [dplyr](https://dplyr.tidyverse.org), and access to the Arrow C++ library through familiar base R and tidyverse functions, or [R6](https://r6.r-lib.org) classes. The dedicated R package website is located [here](https://arrow.apache.org/docs/r/index.html).
To learn more about the Apache Arrow project, see the documentation of the parent [Arrow Project](https://arrow.apache.org/). The Arrow project provides functionality for a wide range of data analysis tasks to store, process and move data fast. See the [read/write article](https://arrow.apache.org/docs/r/articles/read_write.html) to learn about reading and writing data files, [data wrangling](https://arrow.apache.org/docs/r/articles/data_wrangling.html) to learn how to use dplyr syntax with arrow objects, and the [function documentation](https://arrow.apache.org/docs/r/reference/acero.html) for a full list of supported functions within dplyr queries.
## Installation[](https://arrow.apache.org/docs/r/#installation)
The latest release of arrow can be installed from CRAN. In most cases installing the latest release should work without requiring any additional system dependencies, especially if you are using Windows or macOS.

```
install.packages[](https://rdrr.io/r/utils/install.packages.html)("arrow")
```

If you are having trouble installing from CRAN, then we offer two alternative install options for grabbing the latest arrow release. First, [R-universe](https://r-universe.dev/) provides pre-compiled binaries for the most commonly used operating systems.1

```
install.packages[](https://rdrr.io/r/utils/install.packages.html)("arrow", repos = c[](https://rdrr.io/r/base/c.html)("https://apache.r-universe.dev", "https://cloud.r-project.org"))
```

Second, if you are using conda then you can install arrow from conda-forge.

```
[](https://arrow.apache.org/docs/r/#cb3-1)conda install -c conda-forge --strict-channel-priority r-arrow
```

There are some special cases to note:
  * On macOS, the R you use with Arrow should match the architecture of the machine you are using. If you’re using an ARM (aka M1, M2, etc.) processor use R compiled for arm64. If you’re using an Intel based mac, use R compiled for x86. Using R and Arrow compiled for Intel based macs on an ARM based mac will result in segfaults and crashes.
  * On Linux the installation process can sometimes be more involved because CRAN does not host binaries for Linux. For more information please see the [installation guide](https://arrow.apache.org/docs/r/articles/install.html).
  * If you are compiling arrow from source, please note that as of version 23.0.0, arrow requires C++20 to build. This has implications on Windows and CentOS 7. For Windows users it means you need to be running an R version of 4.3 or later (though R 4.2 has incomplete support and might work with special configuration). See the [installation details article](https://arrow.apache.org/docs/r/articles/developers/install_details.html) for guidance.
  * Development versions of arrow are released nightly. For information on how to install nightly builds please see the [installing nightly builds](https://arrow.apache.org/docs/r/articles/install_nightly.html) article.


## What can the arrow package do?[](https://arrow.apache.org/docs/r/#what-can-the-arrow-package-do)
The Arrow C++ library is comprised of different parts, each of which serves a specific purpose. The arrow package provides bindings to the C++ functionality for a wide range of data analysis tasks.
It allows users to read and write data in a variety of formats:
  * Read and write Parquet files, an efficient and widely used columnar format
  * Read and write Arrow (formerly known as Feather) files, a format optimized for speed and interoperability
  * Read and write CSV files with excellent speed and efficiency
  * Read and write multi-file and larger-than-memory datasets
  * Read JSON files


It provides access to remote filesystems and servers:
  * Read and write files in Amazon S3 and Google Cloud Storage buckets (note: CRAN builds include S3 support but not GCS which require an alternative installation method; see the [cloud storage article](https://arrow.apache.org/docs/r/articles/fs.html) for details)
  * Connect to Arrow Flight servers to transport large datasets over networks


Additional features include:
  * Manipulate and analyze Arrow data with dplyr verbs
  * Zero-copy data sharing between R and Python
  * Fine control over column types to work seamlessly with databases and data warehouses
  * Toolkit for building connectors to other applications and services that use Arrow


## What is Apache Arrow?[](https://arrow.apache.org/docs/r/#what-is-apache-arrow)
Apache Arrow is a cross-language development platform for in-memory and larger-than-memory data. It specifies a standardized language-independent columnar memory format for flat and hierarchical data, organized for efficient analytic operations on modern hardware. It also provides computational libraries and zero-copy streaming, messaging, and interprocess communication.
This package exposes an interface to the Arrow C++ library, enabling access to many of its features in R. It provides low-level access to the Arrow C++ library API and higher-level access through a dplyr backend and familiar R functions.
## Arrow resources[](https://arrow.apache.org/docs/r/#arrow-resources)
There are a few additional resources that you may find useful for getting started with arrow:
  * The official [Arrow R package documentation](https://arrow.apache.org/docs/r/)
  * [Scaling Up With R and Arrow](https://arrowrbook.com)
  * [Arrow for R cheatsheet](https://github.com/apache/arrow/blob/-/r/cheatsheet/arrow-cheatsheet.pdf)
  * [Apache Arrow R Cookbook](https://arrow.apache.org/cookbook/r/index.html)
  * R for Data Science [Chapter on Arrow](https://r4ds.hadley.nz/arrow)
  * [Awesome Arrow R](https://github.com/thisisnic/awesome-arrow-r)


## Getting help[](https://arrow.apache.org/docs/r/#getting-help)
We welcome questions, discussion, and contributions from users of the arrow package. For information about mailing lists and other venues for engaging with the Arrow developer and user communities, please see the [Apache Arrow Community](https://arrow.apache.org/community/) page.
If you encounter a bug, please file an issue with a minimal reproducible example on [GitHub issues](https://github.com/apache/arrow/issues). Log in to your GitHub account, click on **New issue** and select the type of issue you want to create. Add a meaningful title prefixed with **`[R]`**followed by a space, the issue summary and select component**R** from the dropdown list. For more information, see the **Report bugs and propose features** section of the [Contributing to Apache Arrow](https://arrow.apache.org/docs/developers/#contributing) page in the Arrow developer documentation.
## Code of Conduct[](https://arrow.apache.org/docs/r/#code-of-conduct)
Please note that all participation in the Apache Arrow project is governed by the Apache Software Foundation’s [code of conduct](https://www.apache.org/foundation/policies/conduct.html).
## Arrow Project
  * [Homepage](https://arrow.apache.org/)   
[Specifications](https://arrow.apache.org/docs/format/Columnar.html)


## Links
  * [View on CRAN](https://cloud.r-project.org/package=arrow)
  * [Browse source code](https://github.com/apache/arrow/)
  * [Report a bug](https://github.com/apache/arrow/issues)


## License
  * Apache License (>= 2.0)


## Community
  * [Code of conduct](https://www.apache.org/foundation/policies/conduct.html)


## Implementations
  * [.NET](https://arrow.apache.org/dotnet/)   
[C GLib](https://arrow.apache.org/docs/c_glib)   
[C++](https://arrow.apache.org/docs/cpp)   
[Go](https://arrow.apache.org/go/)   
[JavaScript](https://arrow.apache.org/js/)   
[Java](https://arrow.apache.org/docs/java)   
[Julia](https://github.com/apache/arrow-julia/blob/main/README.md)   
[MATLAB](https://github.com/apache/arrow/blob/main/matlab/README.md)   
[Python](https://arrow.apache.org/docs/python)   
[R](https://arrow.apache.org/docs/r/index.html)   
[Ruby](https://github.com/apache/arrow/blob/main/ruby/README.md)   
[Rust](https://docs.rs/crate/arrow/latest)   
[Swift](https://arrow.apache.org/swift/)


## Citation
  * [Citing arrow](https://arrow.apache.org/docs/r/authors.html#citation)


## Developers
  * Neal Richardson   
Author 
  * Ian Cook   
Author 
  * Nic Crane   
Author 
  * Dewey Dunnington   
Author  [](https://orcid.org/0000-0002-9415-4582)
  * Romain François   
Author  [](https://orcid.org/0000-0002-2444-4226)
  * Jonathan Keane   
Author, maintainer 
  * Bryce Mecum   
Author 
  * Dragoș Moldovan-Grünfeld   
Author 
  * Jeroen Ooms   
Author 
  * Jacob Wujciak-Jens   
Author 
  * Apache Arrow   
Author, copyright holder 
  * [More about authors...](https://arrow.apache.org/docs/r/authors.html)


## Dev status
  * [![cran](https://www.r-pkg.org/badges/version-last-release/arrow)](https://cran.r-project.org/package=arrow)
  * [![CI](https://github.com/apache/arrow/actions/workflows/r.yml/badge.svg?branch=main&event=push)](https://github.com/apache/arrow/actions/workflows/r.yml?query=branch%3Amain+event%3Apush)
  * [![R-universe status badge](https://apache.r-universe.dev/badges/arrow)](https://apache.r-universe.dev)
  * [![conda-forge](https://img.shields.io/conda/vn/conda-forge/r-arrow.svg)](https://anaconda.org/conda-forge/r-arrow)


[Older versions of these docs](https://arrow.apache.org/docs/r/versions.html)
Site built with [pkgdown](https://pkgdown.r-lib.org/) 2.2.0. Apache Arrow, Arrow, Apache, the Apache logo, and the Apache Arrow project logo are either registered trademarks or trademarks of The Apache Software Foundation in the United States and other countries.

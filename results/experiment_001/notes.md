# Experiment 001 - Spark Documentation Baseline

## Goal

Build the initial knowledge acquisition pipeline for the Spark Brain.

## Corpus

- Source: Apache Spark Documentation
- Raw Documents: 590
- Filtered Documents: 585

## Filtering

Removed:
- 3 tiny documents
- 1 archive/checksum file
- 1 huge API index

## Analysis

Raw:
- Words: 2,188,770

Filtered:
- Words: 1,795,028

Duplicate Documents:
- 3

## Conclusion

The crawler and filtering pipeline work correctly.
The filtered corpus will be used for chunking and embedding generation.


## Filtering Summary

Accepted Documents: 585

Rejected Documents: 5

Reasons:
- Tiny documents: 3
- Huge API index: 1
- Archive: 1

Detailed report:
knowledge/spark/filter_report.json
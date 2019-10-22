# Getting Started

## Installation

# Using Command Line Tool

This tool summarizes genomic alterations for the set of TCGA GBM patients.

Each parameter is a gene name i.e. `TP53` or `BRCA1`

```
./gbm_summarize.sh TP53
TP53 is mutated in 29% of all cases.
TP53 is copy number altered in 2% of all cases.
Total % of cases where TP53 is altered by either mutation or copy number alteration: 30% of all
cases.
```

The user can also be able to execute the program with up to three
genes. For example:

```
./gbm_summarize.sh TP53 MDM2 MDM4
TP53 is altered in 30% of cases. MDM2 is altered in 10% of cases. MDM4 is altered in 10% of
cases.
The gene set is altered in 47% of all cases.
```

# Cancer Mutation Finder CLI

This Python 3 CLI app retrieves data from the [cancer bio portal](https://www.cbioportal.org/)
and does a rudimentary analysis of mutation frequency of the supplied gene symbols. Gene symbols
are limited to the 1000 common genes listed in `app/data/gene_id_symbol_map.csv`. Currently the study ID
is firm-coded to `"gbm_tcga_gistic"`.

## Getting Started

Dependencies:

- Internet access
- Python 3
- pip

## Installation

```
cd DFCI
virtualenv venv  # Recommended
source venv/bin/activate # Recommended
pip install -r requirements.txt
```

Note the shebang line in `app/main.py` may not work for all systems. In that case run
`main.py` as a script. I.E. `$ python3.6 main.py TP53`.

# Using Command Line Tool

Each parameter is a gene name i.e. `TP53` or `BRCA1`.

```
$ ./main.py TP53
TP53 is mutated in 22.34% of all cases.
TP53 is copy number altered in 1.83% of all cases.
```

The user can also be able to execute the program with as many genes as desired
genes. For example:

```
$ ./main.py TP53 MDM2 MDM4 MXA XPA
TP53 is mutated in 22.34% of all cases.
TP53 is copy number altered in 1.83% of all cases.
MDM2 is mutated in 23.81% of all cases.
MDM2 is copy number altered in 9.16% of all cases.
MDM4 is mutated in 30.40% of all cases.
MDM4 is copy number altered in 9.52% of all cases.
XPA is mutated in 26.74% of all cases.
XPA is copy number altered in 0.37% of all cases.
The gene set is altered in 61.54% of all cases.
```

And finally, because life is short, the --toJSON flag results in JSON
being sent to standard out. Note I used `jq` to format the output for
legibility in this example.

```
$ ./main.py TP53 MDM2 MDM4 XPA --toJSON | jq
{
  "geneset": {
    "mutated": 168,
    "totalCount": 273
  },
  "TP53": {
    "NA": 0,
    "singleCopy": 56,
    "noCopy": 5,
    "multiCopy": 0,
    "noChange": 212
  },
  "MDM2": {
    "NA": 0,
    "singleCopy": 40,
    "noCopy": 0,
    "multiCopy": 25,
    "noChange": 208
  },
  "MDM4": {
    "NA": 0,
    "singleCopy": 57,
    "noCopy": 0,
    "multiCopy": 26,
    "noChange": 190
  },
  "XPA": {
    "NA": 0,
    "singleCopy": 72,
    "noCopy": 0,
    "multiCopy": 1,
    "noChange": 200
  }
}
```

# Known Issues

- There are (almost) no test. Unit test and at least one integration test would be
  awesome and wouldn't take very long.
- Executing the script from outside of `/app` resulting in incorrect path to `/data`. This could be fixed
  pretty easily with:
  ```
  import os
  dirname = os.path.dirname(__file__)
  filename = os.path.join(dirname, 'relative/path/to/file/you/want')
  ```
- Single genes should also return the total % of mutations. I.E. `"Total % of cases where TP53 is altered by either mutation or copy number alteration: 30% of all cases."` for `./main.py TP53`
- The error messages are uninformative and should tell a user why the app is failing. Usually this is because the gene symbol isn't recognized.
- None of the functions have doc string. Might not be that big of a deal since they're not designed for export but it would help with maintenance.

# Future Features

- Specifying a study ID could add a lot of value and is trivial.
- Dockerizing the whole app while definitely overkill would solve shebang line issues and
  negate the need to install requirements.txt.
- If a gene symbol isn't found in `app/data/gene_id_symbol_map.csv` the app should look for it online.
- Gene results should be cached. (I.E. `app/data/<study_id>/<gene_id>`)

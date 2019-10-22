import argparse


def parse():
    parser = argparse.ArgumentParser(
        description='Retrieve metadata about a gene in The Cancer Genome Atlas.')
    parser.add_argument('GeneSymbols',
                        metavar='GeneSymbols',
                        type=str,
                        nargs='+',
                        help='Gene Symbol names as found in NCBI website. If the symbol cannot be unambiguously matched\
                            no data will be retrieved. If NO symbol can be unambiguously matched an error is raised.')

    args = parser.parse_args()
    return args.GeneSymbols

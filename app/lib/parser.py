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

    parser.add_argument("--toJSON",
                        action='store_true',
                        help="toJSON is a flag which tells the program to send the data to STDOUT as json file\
                        rather than printing it for legibility.")

    args = parser.parse_args()
    return args.GeneSymbols, args.toJSON

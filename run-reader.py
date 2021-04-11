import argparse
from reader import Reader

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Reader of MongoDB documents.')

    parser.add_argument('--start', action='store', type=int, default=0,
                    help='The document number to start with (default 0)')
    parser.add_argument('--end', action='store', type=int,
                    help='The document number to end with (default last)')
    parser.add_argument('--size', action='store', type=int, default=10,
                    help='The document count to handle (default 10)')
    parser.add_argument('--config', action='store', type=str,
                    help='The configuration file to use.')
    args = parser.parse_args()
    reader = Reader(args.start, args.end, args.size, args.config)
    reader.run()

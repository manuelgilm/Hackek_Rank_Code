import random
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-s", help="Strings separated by ' '")
parser.add_argument("-q", help="queries separated by ' '")


def matching_strings(strings, queries):
    return [strings.count(q) for q in queries]

if __name__ == '__main__':
    
    args = parser.parse_args()

    strings = args.s.split("-")
    queries = args.q.split("-")

    result = matching_strings(strings,queries)
    print(result)
    

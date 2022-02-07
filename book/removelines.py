import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--file', type=str, required=True)
parser.add_argument('--line', type=int, required=True)

args = parser.parse_args()

filename = args.file
line = args.line

with open(filename, 'rt') as f:
    lines = f.readlines()

newcontent =  [l for i, l in enumerate(lines) if i != line -1]

with open(filename, 'wt') as f:
    f.writelines(newcontent)

import argparse
parser = argparse.ArgumentParser("xuliang test..")
parser.add_argument("--act1",action="store_false")
args = parser.parse_args("--act1".split())
print(args)
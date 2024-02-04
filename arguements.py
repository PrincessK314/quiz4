import argparse

parser = argparse.ArgumentParser()
parser.add_argument(type=str, dest="input_str", help="String")
parser.add_argument(type=int, dest="input_int", help="Integer")
parser.add_argument(type=float, dest="input_float", help="Decimal")

args = parser.parse_args()

print("String: " + args.input_str)
print("Int: " + str(args.input_int))
print("Float: " + str(args.input_float))

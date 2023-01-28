import sys
import ast 

input = ast.literal_eval(sys.argv[1])
for i in input:
    print(i)
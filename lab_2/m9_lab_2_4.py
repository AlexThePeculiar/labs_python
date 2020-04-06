# A test array for CMD: [[[[2,3],3],2,[2,'hello']],2,'there']

import sys
import ast

def flatten_it(iterable):
    try:
        for item in iterable:
            if type(item) != list:
                yield item
            else:
                try:
                    yield from flatten_it(item)
                except TypeError:
                    yield item
    except RecursionError:
        print("RecursionError: An infinite nesting was encountered.")
        
if len(sys.argv) == 1:
    arr = [[[1, 2, 'hello'], ["there", 5]], 'hon',[5,[3]], 2, [34,[[2]]]]
else:
    arr = ast.literal_eval(sys.argv[1])
    
result = [el for el in flatten_it(arr)]
print("The original list: ", arr)
print("The flattened list:", result)
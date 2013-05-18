import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    key = record[0]
    if key == "a":
        for i in range(0,5):
            mr.emit_intermediate((record[1], i), (record[2], record[3]))
    else:
        for i in range(0,5):
            mr.emit_intermediate((i, record[2]), (record[1], record[3]))
    
def reducer(key, list_of_values):
    total = 0
    cache = {}
    for (j, value) in list_of_values:
        if j not in cache:
            cache[j] = value
        else:
            total += cache[j]*value
        
    mr.emit((key[0], key[1], total))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)

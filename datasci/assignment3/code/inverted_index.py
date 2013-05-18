import MapReduce
import sys

# Part 1
mr = MapReduce.MapReduce()

# Part 2
def mapper(record):
    # key: document identifier
    # value: document contents
    key = record[0]
    value = record[1]
    words = value.split()
    for w in words:
        mr.emit_intermediate(w, key)

# Part 3
def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    #total = 0
    docset = []
    for v in list_of_values:
        if not v in docset:
            docset.append(v)
    mr.emit((key, docset))

# Part 4
inputdata = open(sys.argv[1])
mr.execute(inputdata, mapper, reducer)

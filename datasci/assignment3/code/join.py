import MapReduce
import sys

# Part 1
mr = MapReduce.MapReduce()

# Part 2
def mapper(record):
    relation = record[0]
    key = record[1]
    mr.emit_intermediate(key, (relation, record))
    

# Part 3
def reducer(key, list_of_values):
    order_values = []
    item_values = []
    for (relation, value) in list_of_values:
        if relation == "order":
            order_values.append(value)
        else:
            item_values.append(value)
    for order in order_values:
        for item in item_values:
            value = order + item
            mr.emit(value)

# Part 4
inputdata = open(sys.argv[1])
mr.execute(inputdata, mapper, reducer)

import MapReduce
import sys

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    #hash is a numerical value, so (a,b) and (b,a) will give same result
    key = hash(record[0]) + hash(record[1])
    mr.emit_intermediate(key, record)

def reducer(key, values):
    if len(values) == 1:
        mr.emit((values[0][0], values[0][1]))
        mr.emit((values[0][1], values[0][0]))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)

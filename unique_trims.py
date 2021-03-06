import MapReduce
import sys

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    trimmed = record[1][:-10]
    mr.emit_intermediate(trimmed, None)

def reducer(key, values):
    mr.emit(key)
# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)

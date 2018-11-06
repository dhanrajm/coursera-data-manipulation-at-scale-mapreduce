import MapReduce
import sys

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    personA = record[0]
    personB = record[1]
    mr.emit_intermediate(personA, personB)

def reducer(key, values):
    count = len(set(values))
    mr.emit((key, count))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)

import MapReduce
import sys

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    mr.emit_intermediate(record[1], record)

def reducer(key, values):
    output = []
    for order in values:
        if order[0] == 'order':
            for line in values:
                if line[0] == 'line_item':
                    mr.emit(order + line)



    #output = list(set(output))
    #print(len(output))


# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)

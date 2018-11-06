import MapReduce
import sys

mr = MapReduce.MapReduce()

DIM_ROW_A = 5
DIM_COL_A = 5
DIM_COL_B = 5

# =============================
# Do not modify above this line

def mapper(record):
    matrix = record[0];
    if matrix == 'a':
        for i in range(DIM_COL_B):
            mr.emit_intermediate((record[1], i), (record[0], record[2], record[3]))
    else:
        for i in range(DIM_ROW_A):
            mr.emit_intermediate((i, record[2]), (record[0], record[1], record[3]))

def reducer(key, values):
    arow = [0]*DIM_COL_A;
    brow = [0]*DIM_COL_A;
    for value in values:
        if value[0] == 'a':
            arow[value[1]] = value[2]
        else:
            brow[value[1]] = value[2]

    sum = 0;
    for i in range(DIM_COL_A):
        sum = sum + arow[i]*brow[i]

    mr.emit((key[0], key[1], sum))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)

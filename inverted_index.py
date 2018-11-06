import MapReduce
import sys

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    doc_id = record[0]
    doc_text = record[1]
    words = doc_text.split()
    for w in words:
        mr.emit_intermediate(w, doc_id)

def reducer(key, values):
    mr.emit((key, list(set(values))))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)

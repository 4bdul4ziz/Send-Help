cols = 0
rows = 0

def num_columns(input_listA):
    cols = len(list(input_listA[0]))
    return cols
def num_rows(input_listB):
    rows = len(list(input_listB))
    return rows

def multiply_matrice(num_columns, num_rows):
    if cols == rows:
        return True
    else:
        return False

input_listA = [1,2,3,4,5]
input_listB = [6,7,8,9,10]

num_columns(input_listA)
num_rows(input_listB)

multiply_matrice(num_columns(input_listA), num_rows(input_listB))
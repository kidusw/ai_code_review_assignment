from typing import List

def average_valid_measurements(values:List):
    total = 0
    valid_count = 0

    if len(values) == 0:
        return 'the list is empty!'

    for v in values:
        if not isinstance(v,(int,float)):
            continue
        total += float(v)
        valid_count +=1
    
    return total / valid_count

values = ["str",None,"str2",1.2,2]

print(average_valid_measurements(values))

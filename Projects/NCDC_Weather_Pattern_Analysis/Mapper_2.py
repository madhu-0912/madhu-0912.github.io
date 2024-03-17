import sys

vh_dict = {}

for line in sys.stdin:
    line = line.strip()
    (key, v_dist, q) = (line[4:10], line[78:84], line[84:85])
    if(key != '999999' and v_dist != '999999' and q in ['0','1','4','5','9']):
        vh_dict[key] = str(vh_dict.get(key,''))+str(v_dist)+','

for k in vh_dict:
    output = str(k)+','+str(vh_dict[k])
    if output[-1] == ',':
        output = output[:-1]
        
    print(output)
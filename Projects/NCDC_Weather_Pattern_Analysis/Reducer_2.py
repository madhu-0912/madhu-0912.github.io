import sys

output_dict = {}

for line in sys.stdin:
    line = line.strip()
    line = line.split(',')
    s = line[0]
    d = line[1:]
    c = output_dict.get(s,'')
    output_dict[s] = list(c)+d

for key in output_dict:
    d_line = output_dict[key]
    r = len(d_line)
    s = 0
    for r in d_line:
        s = s+int(r)
    a = s/r
    
    print '%s\t%s' % (key, a)


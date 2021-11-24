import re
with open('sample-table.txt', 'r') as f:
    with open('newtable.txt' ,'w') as w:
        for line in f:
            line = re.sub('\t', '&',line)
            line = line.replace('\n','')
            line+="\\\\"
            # print(line)
            w.write(line+'\n')
            w.write('\hline\n')


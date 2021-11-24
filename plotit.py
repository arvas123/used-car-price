import re
with open('cool.txt', 'r') as f:
    with open('cool1.txt','w') as g:
        for line in f:
            g.write("\hline\n")
            line=re.sub('\t','&',line)
            line=line.strip()
            g.write(line+'\\'+'\\'+'\n')
        g.write("\hline")

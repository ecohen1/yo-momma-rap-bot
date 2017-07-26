with open('insults.txt','r') as f:
    outlines = []
    lines = f.readlines()
    for line in lines:
        if line[0] == 'Y':
            outlines.append(line.rstrip())
        else:
            outlines[-1] += line.rstrip()
    with open('insults2.txt','w') as out:
        for outline in outlines:
            out.write(outline + '\n')

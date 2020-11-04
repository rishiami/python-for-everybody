fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
a=list()

for i in fh:
    if i.startswith('From') and len(i.split())>2:
        a.append(i)
        z=i.split()
        print(z[1])

print("There were",len(a),"lines in the file with From as the first word") 
        

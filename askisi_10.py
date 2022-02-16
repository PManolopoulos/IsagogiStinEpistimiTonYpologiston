#sinartisi metatropis ascii se diadiko
def toBinary(a):
  l,m=[],[]
  for i in a:
    l.append(ord(i))
  for i in l:
    m.append(int(bin(i)[2:]))
  return m

#sinartisi metatropis tuple se int
def magic(number):
    return int(''.join(str(i) for i in number))





keimeno =  input("Enter ASCII charcters:")
binary =  toBinary(keimeno)
y=[]
for i in range(len(binary)):
    x = [int(d) for d in str(binary[i])]
    while len(x)<7  :
      x.insert(0,0)
    y.append(x)
for i in range(len(y)):
  y[i]=y[i][0],y[i][1],y[i][5],y[i][6]
for i in range(len(y)//4 ) :
  y[i]=y[2*i+1] + y[2*i+2] + y[2*i+3] + y[2*i]
upoloipa=len(y)-4*i
if upoloipa>0  :
    y[i]=y[i*4+1]
    upoloipa=upoloipa-1
    if upoloipa>0   :
        for z in range(upoloipa)    :
            y[i]=y[i]+y[i*4+1+z]
for k in range(i,len(y)-1)  :
    del y[i+1]
zygoi=0
dia3=0
dia5=0
dia7=0
for w in range(len(y))  :
    ok=magic(y[w])
    if (ok/3)==(ok//3)  :
        dia3=dia3+1
    if (ok/7)==(ok//7)  :
        dia7=dia7+1
    if (ok/5)==(ok//5)  :
        dia5=dia5+1
    if y[w][-1]==0  :
        zygoi=zygoi+1
zygoi=zygoi*100/len(y)
dia7=dia7*100/len(y)
dia3=dia3*100/len(y)
dia5=dia5*100/len(y)
print("POSOSTO ZYGON:",zygoi,"POSOSTO POLLAPLASION TON 3,5,7 ANTISTOIXA:",dia3,",",dia5,",",dia7)





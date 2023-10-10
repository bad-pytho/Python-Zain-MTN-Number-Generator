sudanall = ('0909','0906','0902','0904','0901','0930','0931','0932','0933','0934','0935','0936','0937','0938','0939','0940','0941')
num1 =(1,10)
num2 =(0,10)
num3 =(0,10)
num4 =(0,10)
num5 =(0,10)
num6 =(0,10)
#num7 =(0,10)
for sudannum in sudanall:
    for a in range(1,10):
        for b in range(0,10):
            for c in range(0,10):
                for d in range(0,10):
                    for e in range(0,10):
                        for t in range(0,10):
                            #for g in range(0,10): # print(7m)-str(g)+
                                hm=(str(sudannum+str(a)+str(b)+str(c)+str(d)+str(e)+str(t)+'\n'))
                                if hm[0:4]== '0909':
                                        f=open('0909nums.txt','a')
                                        f.write(hm)
                                if hm[0:4]== '0906':
                                        f=open('0906nums.txt','a')
                                        f.write(hm)
                                if hm[0:4]== '0902':
                                        f=open('0902nums.txt','a')
                                        f.write(hm)
                                if hm[0:4]== '0904':
                                        f=open('2904nums.txt','a')
                                        f.write(hm)
                                if hm[0:4]== '0901':
                                        f=open('0901nums.txt','a')
                                        f.write(hm)
                                if hm[0:4]== '0930':
                                        f=open('0930nums.txt','a')
                                        f.write(hm)
                                if hm[0:4]== '0931':
                                        f=open('0931nums.txt','a')
                                        f.write(hm)
                                if hm[0:4]== '0932':
                                        f=open('0932nums.txt','a')
                                        f.write(hm)
                                if hm[0:4]== '0933':
                                        f=open('0933nums.txt','a')
                                        f.write(hm)
                                if hm[0:4]== '0934':
                                        f=open('0934nums.txt','a')
                                        f.write(hm)
                                if hm[0:4]== '0935':
                                        f=open('2935nums.txt','a')
                                        f.write(hm)
                                if hm[0:4]== '0936':
                                        f=open('0936nums.txt','a')
                                        f.write(hm)
                                if hm[0:4]== '0937':
                                        f=open('09037nums.txt','a')
                                        f.write(hm)
                                if hm[0:4]== '0938':
                                        f=open('0938nums.txt','a')
                                        f.write(hm)
                                if hm[0:4]== '0939':
                                        f=open('0939nums.txt','a')
                                        f.write(hm)
                                if hm[0:4]== '0940':
                                        f=open('0940nums.txt','a')
                                        f.write(hm)
                                if hm[0:4]== '0941':
                                        f=open('0941nums.txt','a')
                                        f.write(hm)
f.close()

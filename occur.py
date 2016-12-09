def tables(n,limit):
    for i in range(1,limit+1):
        print ("{:2} x {:2} = {:2}".format(n, i, n*i))


def mult(num):
     for i in range (1,num+1):
           for j in range(1,num+1):
                  print('{:2}'.format(i*j)),
           print("\n")



def disp(num):
     for i in xrange(1,num+1):
             if (i%15)==0:
                         print("FizzBizz")
             elif i%3==0:
                         print("Fizz")
             elif i%5==0:
                         print("Bizz")
             else:
                         print(i)

                         

def occur(p):
    c = 0
    p = p.lower()
    symbol = 'abcdefghijklmnopqrstuvwxyz'
    for key in symbol:
            if p.count(key) > 0:
             continue
            else:
             c = 1
             print key,"is missing"   
    if c==0:
        print "True"
        print " Panagram"
    else:
        print "False"



def change(money):
    for i in [1000,500,100,50,20,10,1]:
        denom = money/i
        if denom > 0:
         print i,"*",denom,"=",i*denom
         money = money - (i * denom )


def freq(strings):
   d = {}
   for i in strings:
       a = strings.count(i)
       d.update({i: a})
   print(str(d))


if __name__ == '__main__':
    tables(6,12) 
    mult(5)                   
    disp(15)
    occur("the Quick brown fox jumps over the lazy dog")
    change(1574)
    freq("jubinnnn")

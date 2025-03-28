## 解答例



以下はPythonプログラムですが、私はコードを短くまとめ、読みやすいようにします。
以下のプログラムでは、メモリ使用量と計算コストの問題がありました。(2017年3月)

# 以下に解答例があります。



#import numpy as np
#def area--------------------------#
#ryouno syokiti
class ryou:
    def flinit(self):
        room=list()
        for i in range(4):
            room+=[0]
        return room
#----------------------------------#
def kaijo(x):
    print "",
    for i in x:
    	if i!=x[len(x)-1]:
        	print str(i) + "," ,
    	else:
    	    print str(i)
    	    
   
floor_1=ryou().flinit()
floor_2=ryou().flinit()
floor_3=ryou().flinit()
floor_4=ryou().flinit()


fldic={"1":floor_1,
       "2":floor_2,
       "3":floor_3,
       "4":floor_4
       }
#----------------------------------#



#1kaime yomikomi
n=int(raw_input())

#nkaime syusyori

for l in range(n):
    list_mojiretsu=raw_input().split(" ")
    henka=map(int,list_mojiretsu)
    fldic[str(henka[0])][henka[1]-1]+=henka[2]

kaijo(floor_1)
print "####################"
kaijo(floor_2)
print "####################"
kaijo(floor_3)
print "####################"
kaijo(floor_4)
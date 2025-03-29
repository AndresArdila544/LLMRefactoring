#import numpy as np

def kaijo(x):
	print "",
	for i in range(len(x)-1):
		print str(x[i]),
	print str(x[len(x)-1])

def area():
	fldic={"11":ryou().flinit(),
       "12":ryou().flinit(),
       "13":ryou().flinit(),
       "21":ryou().flinit(),
       "22":ryou().flinit(),
       "23":ryou().flinit(),
       "31":ryou().flinit(),
       "32":ryou().flinit(),
       "33":ryou().flinit(),
       "41":ryou().flinit(),
       "42":ryou().flinit(),
       "43":ryou().flinit()
       }
	n=int(raw_input())
	for l in range(n):
		list_mojiretsu=raw_input().split(" ")
		henka=map(int,list_mojiretsu)
		fldic[str(henka[0])+str(henka[1])][henka[2]-1]+=henka[3]

	kaijo(fldic["11"])
	kaijo(fldic["12"])
	kaijo(fldic["13"])
	print "####################"
	kaijo(fldic["21"])
	kaijo(fldic["22"])
	kaijo(fldic["23"])
	print "####################"
	kaijo(fldic["31"])
	kaijo(fldic["32"])
	kaijo(fldic["33"])
	print "####################"
	kaijo(fldic["41"])
	kaijo(fldic["42"])
	kaijo(fldic["43"])
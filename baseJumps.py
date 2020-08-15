#python3
#program to search base address jumps


import os
import sys
import subprocess


if not os.path.isfile('baseAddress.txt'):
	print ('please place "baseAddress.txt" in the same folder and try again')
	sys.exit()
if open('baseAddress.txt').read().count("decrement!")>0:
	print ('The base GOT is not valid please add 16 to the base GOT, until you see decrement! in the dumpped text')
	sys.exit()	
		
jumps= []
unSortedArray=[]
sortedArray=[]
skipFlag=True

for ln in open('baseAddress.txt').read().strip().split("\n"):
	if skipFlag:
		if ln.startswith("ptr_3"):
			skipFlag=False
		continue
	unSortedArray.append(ln.strip())
	sortedArray.append(ln.strip())
sortedArray.sort()

jumps.append([sortedArray[0],unSortedArray.index(sortedArray[0])+1])

for k,address in enumerate(sortedArray):
	Currentn16=int(sortedArray[k],16)
	Nextn16=int(sortedArray[k+1],16)

	if Nextn16-Currentn16>10000000:
		jumps.append([sortedArray[k+1],unSortedArray.index(sortedArray[k+1])+1])
	if address.startswith("effffffe"):
		break;

jumps = sorted(jumps, key=lambda element: (element[1]))
for j,rec in enumerate(jumps):
	print ("{} Jump {} @ {}".format(rec[0],j+1,rec[1]))

### VM page replacement victim choice algorithm simulations ###

import sys
from sys import exit
import copy
from copy import deepcopy
import random

### Functions ###

#Input interaction functions#
def my_input(prompt=None):
	"Prompts for input on the stderr channel"

	if prompt:							#if there is a prompt
		sys.stderr.write(str(prompt))		#display it on the error channel

	return input()						#return the user response

def getInt(prompt,message):
	"Get an integer"

	while True:							#keep trying until no problem
		try:
			value = int(my_input(prompt))		#get user response and convert it to integer
		except ValueError:						#if response not an integer
			sys.stderr.write(message+"\n")			#inform user
			continue								#and try again
		break							#otherwise skip to end

	return value							#and return the integer

#sorting key functions for process list elements 
def getFirst(item):
	return(item[0])

def getSecond(item):
	return(item[1])

def getThird(item):
	return(item[2])
	
def getFourth(item):
	return(item[3])
	
def getFifth(item):
	return(item[4])
	
def getSixth(item):
	return(item[5])
	
def initialise(pageNames, frameData, usePattern, pagesInRAM, numRefs, numFrames):
	"Initialise RAM with randomly generated page names and 30 references to any of the pages named"
	
	pageIndex=0			#index of page name in RAM data
	refIndex=2			#index of page's reference bit in RAM data
	refCountIndex=4		#index of page's reference counter in RAM data
	refByteIndex=5		#index of decaying or ageing reference count for LFUDC and LRUA
	
	#make page names
	i=0								#no page names generated yet
	while i < numFrames:			#while number of page names generated < frames available
		random.seed()
		pName=random.randint(1, 99)		#generate a random number as page name
		if pName not in pageNames:	#if it is not already generated
			pageNames.append(pName)		#add it to the list
			i += 1						#count one more page name generated
			
	#generate initial page references, install referenced page in RAM and count references
	for clock in range(numRefs):
		random.seed()
		page = random.randint(0, len(pageNames)-1)    #Pick a random page name index
		if pageNames[page] not in pagesInRAM:	#if it has not already been installed in RAM
			pagesInRAM.append(pageNames[page])		#Add to pagesInRAM
			arriveTime=clock						#record arrival time
			ref = 1									#clear reference bit (for older pages)
			random.seed()
			mod = random.randint(0, 1)				#Randomly assign modify bit = 0 or 1
			refCount = 1							#initialise reference counter
			refByte = refCount						#used in LFUDC and LRUA as decaying or aging counter
			frameData.append([pageNames[page], arriveTime, ref, mod, refCount, refByte])		#Add to frameData
		else:
			pageIndex=pagesInRAM.index(pageNames[page])		#Get its index in pagesInRAM
			frameData[pageIndex][refCountIndex] += 1 		#increment its reference count
			frameData[pageIndex][refByteIndex] += 1 		#increment its decay/aged count
			frameData[pageIndex][refIndex] = 1			 	#set or clear its reference bit

		if clock<numRefs-5:						#if this is not a later reference
#			ref = 1									#set reference bit
#		else:
#			ref = 0									#clear reference bit
			frameData[pageIndex][refIndex] = 0 	#set or clear its reference bit

		usePattern.append(pageNames[page])			#Add this page reference to the usePattern record (oldest first)

	return frameData, usePattern, pagesInRAM, clock
	
def shiftRight(x,bit):
	"Shift integer to right filling with 1 or 0 bit"
		
	x=x>>1
	if bit == 1:
		x=x+128
	
	return x
	
#Output display functions#

def decToBin(dec):
	"Convert decimal to 8-bit binary string"

	bits=8			#number of bits to generate
	bin=""			#binary string to generate
	while dec > 0:	#while bits to generate
		r=dec % 2		#calculate bit
		dec = dec // 2	#reduce number by bits generated
		bin=str(r)+bin	#add bit to binary string
		bits=bits-1		#record another bit generated

	while bits>0:		#while fill bits needed
		bin="0"+bin			#fill string with 0
		bits=bits-1			#record another bit generated

	return bin
		
def outputResults(pageIn, data, newFrameData, victim, usePattern, algorithm, vFrame):
	"Display all results"

	page=0							#page name index in frameData
	arrive=1						#page arrival time index
	ref=2							#page reference bit index in frameData
	mod=3							#page modify bit index in frameData
	refcount=4						#page reference counter index in frameData
	refByteIndex=5					#index of decaying or ageing reference count for LFUDC and LRUA

	numRefs = len(usePattern)		#number of page references so far
	numPages = len(data)			#number of pages in RAM

	print("\nReference recency summary, most recent page referenced is shown last: ",end='')
	output=[pageIn]		#incoming page number is most recent reference
	i=numRefs-1			#start at end of references pattern with most recent reference
	while i >=0:			#while references to add to the reference history
		if usePattern[i] not in output:	#if have not already added this reference
			output.append(usePattern[i])	#add it
		thisPage=usePattern[i]			#record which page reference added
		i=i-1							#record one more reference dealt with
		while i > numRefs and usePattern[i] == thisPage:	#skip over repetitions of this page reference
			i-=1
	
	output.reverse()	#get into most recent last order
	print(output,"\n")	#display

	if algorithm == "clock":	#generate description of RAM display order
		order = "clock"
	else:
		order = "oldest first"
		
	print("List of page numbers referenced before new page entered is as follows (most recent reference last): ")
	usePattern.append(pageIn)
	print(usePattern)
	usePattern.remove(pageIn)
	print("\nThere are", numPages, "pages in RAM (assume RAM is now full)")
	print("\nFrames in memory are shown in", order, "order.")
	print("\nFrames in memory before victim replacement were:")
	print("Frame\tPage\tarrival time\treference bit\tmodify bit\treference counter",end='')
	if algorithm == "LRUA" or algorithm == "LFUDC":		#only have reference history byte for these
		print("\treference history")
	else:
		print()
		
	for i in range(len(data)):		#for each page in RAM print its data summary
		print(i,"\t",data[i][page],"\t",data[i][arrive],"\t\t",data[i][ref],"\t\t",\
		data[i][mod],"\t\t",data[i][refcount],"\t= ",decToBin(data[i][refcount]),end='')
		if algorithm == "LRUA" or algorithm == "LFUDC":		#only have reference history byte for these
			print("\t",decToBin(data[i][refByteIndex])," = ",data[i][refByteIndex])
		else:
			print()
		
	if len(victim)>0:	#if a victim was successfully chosen
		print("\nVictim chosen was: page ",victim[page])
		print("\nPage",pageIn,"was inserted instead, so:")
		print("\nFrames in memory are now:")
	else:	#algorithm failed to choose a victim
		print("\nNo victim chosen.")
		print("There were many candidates as follows but this algorithm cannot choose between them.")
		print("As a tiebreaker, the oldest candidate could be chosen. This is done in the other \
algorithms where needed.")

	print("Frame\tPage\tarrival time\treference bit\tmodify bit\treference counter",end='')
	if algorithm == "LRUA" or algorithm == "LFUDC":		#only have reference history byte for these
		print("\treference history")
	else:
		print()

	for i in range(len(newFrameData)):	#for each page in RAM now print its data summary
		if algorithm=="NRU":			#if NRU there are several victims with frame numbers in vFrame
			frame=vFrame[i]				#let frame be the frame number of the candidate victim
		elif algorithm=="FIFO":			#if FIFO the victim frame is always frame 0
			if i<len(newFrameData)-1:	#this is not the last frame
				frame=i+1				#so make frame number 1 more than item number
			else:						#this is the last frame to show
				frame=0					#which is frame 0
		elif algorithm=="clock":			#for clock 
			frame=i						#the victim frame is always frame i
		else:							#for all other algorithms
			if i>=vFrame[0] and i!=len(newFrameData)-1:	#if at or beyond the victim frame and not at last frame 
				frame=i+1								#add one to get frame number
			elif i==len(newFrameData)-1:				#otherwise if at last
				frame=vFrame[0]							#frame is victim frame number
			else:										#otherwise if before victim frame
				frame=i									#the victim frame is always frame i

		print(frame,"\t",newFrameData[i][page],"\t",newFrameData[i][arrive],"\t\t",newFrameData[i][ref],"\t\t",\
		newFrameData[i][mod],"\t\t",newFrameData[i][refcount],"\t= ",decToBin(newFrameData[i][refcount]),end='')
	
		if algorithm == "LRUA" or algorithm == "LFUDC":		#only have reference history byte for these
			print("\t",decToBin(newFrameData[i][refByteIndex])," = ",newFrameData[i][refByteIndex])
		else:
			print()
			
	return

def showData(label, d1,d2,d3):
	"for debug"
	
	print(label,len(d1),len(d2),len(d3))
	if d2==[] and d3==[]:
		for i in range(len(d1)):
			print(d1[i])
	else:
		if d3==[]:
			for i in range(len(d1)):
				print(d1[i],"\t",d2[i])
		else:
			for i in range(len(d1)):
				print(d1[i],"\t",d2[i],"\t",d3[i])
	return
	

#Simulation functions
def FIFO(data, pageIn, clock):
	"Simulate FIFO algorithm"
	
	print("\n\n ************** First in First out **************\n")

	head=0							#index head of queue (sorted in order of arrival in RAM)
	vFrame=[head	]					#victim frame will be first frame
	victim=data[head]					#choose this victim [page, arrive, ref, mod, refcount]
	data.remove(victim)				#remove it from the sorted list
	data.append([pageIn,clock,1,0,1,1])	#replace victim page with incoming page with ref=1 and modify=0
		
	return data, victim, vFrame			#return modified frame data, victim's data, and victim frame#
	
def clockSim(data, pageIn, clock, pointer, usePattern):
	"Simulate Clock algorithm"

	print("\n\n ************** Clock **************\n")

	page=0			#index of candidate page number
	arrive=1		#index of candidate arrival time
	ref=2			#index of candidate reference bit
	mod=3			#index of candidate modify bit
	refcount=4		#index of candidate reference counter
	refbyte=5		#index of candidate reference byte
	
#	newUsePattern=[]				#to hold updated use pattern to illustrate clock
	oldData=copy.deepcopy(data)	#take a copy of the data for later display as data will change when victim replaced
#	for i in range(len(oldData)):		#alter the original data to generate some pages with clear reference bits
#		random.seed()
#		oldData[i][ref] = random.randint(0,1)		#randomly choose a reference bit for this page
#		data[i][ref] = oldData[i][ref]				#alter new data to echo the changes

#	for i in range(len(oldData)):		#alter the usePattern to only have pages with set reference bits
#		if oldData[i][ref] == 1:
#			newUsePattern.append(oldData[i][page])
#	newUsePattern=newUsePattern+usePattern		#append original reference list for later display

#	print("NOTE: Old reference bits have been cleared and new references added to help illustrate the clock algorithm.")
#	my_input("Press <ENTER> to continue")
	ptrStart = pointer 	#record clock pointer starting position so can recognise full circuit completed
	victim = []				#assume no victim found

	candidate=data[pointer]			#choose first page at pointer as candidate victim
	if candidate[ref] == 0 and candidate[mod] == 0:			#if its reference and modify bits are clear
		victim=candidate[:]				#then choose this victim ([:] to ensure to take COPY of the data)
		victimIndex=pointer				#record where it is in RAM
		pointer=(pointer+1) % len(data)	#move clock pointer 1 place around clock for next run
	else:							#this candidate unsuitable
		data[pointer][ref]=0			#clear its reference bit to give a second chance
		pointer=(pointer+1) % len(data)	#move clock pointer 1 place around clock to try for another candidate
	#now continue through the other candidates if no victim chosen yet
	while len(victim) == 0 and pointer != ptrStart:		#repeat until victim found or done full circuit without finding victim
		candidate=data[pointer]			#choose page at pointer as candidate victim
		if candidate[ref] == 0 and candidate[mod] == 0:			#if its reference and modify bits are clear
			victim=candidate[:]				#then choose this victim ([:] to ensure to take COPY of the data)
			victimIndex=pointer				#record where it is in RAM
			pointer=(pointer+1) % len(data)	#move clock pointer 1 place around clock for next run
		else:							#this candidate unsuitable
			data[pointer][ref]=0			#clear its reference bit to give a second chance
			pointer=(pointer+1) % len(data)	#move clock pointer 1 place around clock to try for another candidate

#here either victim was chosen or pointer back to start
	if len(victim) == 0:		#if no victim chosen
	#so go around again - this time those given a second chance will have 0 ref bit and are examined for a non-modified page
		candidate=data[pointer]			#choose first page at pointer as candidate victim
		if candidate[mod] == 0:			#if its modify bits is clear
			victim=candidate[:]				#then choose this victim ([:] to ensure to take COPY of the data)
			victimIndex=pointer				#record where it is in RAM
			pointer=(pointer+1) % len(data)	#move clock pointer 1 place around clock for next run
		else:							#this candidate unsuitable
			pointer=(pointer+1) % len(data)	#move clock pointer 1 place around clock to try for another candidate
		#now continue through the other candidates if no victim chosen yet
		while len(victim) == 0 and pointer != ptrStart:		#repeat until victim found or done full circuit without finding victim
			candidate=data[pointer]			#choose page at pointer as candidate victim
			if candidate[mod] == 0:			#if its modify bits is clear
				victim=candidate[:]				#then choose this victim ([:] to ensure to take COPY of the data)
				victimIndex=pointer				#record where it is in RAM
				pointer=(pointer+1) % len(data)	#move clock pointer 1 place around clock for next run
			else:							#this candidate unsuitable
				pointer=(pointer+1) % len(data)	#move clock pointer 1 place around clock to try for another candidate
	if len(victim) == 0:		#if still no victim chosen
	#so must take a modified page
	
		victim=data[pointer][:]		#select the page at the start as victim ([:] to ensure to take COPY of the data)
		victimIndex=pointer			#record where it is in RAM
		pointer=(pointer+1) % len(data)	#move clock pointer 1 place around clock for next run
		
	data[victimIndex][page]=pageIn		#replace victim page with incoming page
	data[victimIndex][arrive]=clock		#set new page's arrival time
	data[victimIndex][ref]=1			#set new page's reference bit
	data[victimIndex][mod]=0			#clear new page's modify bit (arbitrary but why not?)
	data[victimIndex][refcount]=1		#set new page's reference counter		
	data[victimIndex][refbyte]=1		#set new page's reference byte		
	
	vFrame=[victimIndex]			#get victim's frame number
	#return old frame data, modified frame data, victim, new pointer value & full use pattern of references, and victim frame#
#	return oldData, data, victim, pointer, newUsePattern, vFrame
	return oldData, data, victim, pointer, usePattern, vFrame

def NRU(data):
	"Simulate NRU algorithm"

	print("\n\n ************** Not recently Used **************\n")

	refIndex = 2	#index of the reference bits
	page = 0		#index of the page number
	ref=2			#index of candidate reference bit

#	newUsePattern=[]					#to hold updated use pattern to illustrate NRU
	oldData=copy.deepcopy(data)			#take a copy of the datafor later display as data will change if victim replaced
#	for i in range(len(oldData)):		#alter the original data to generate some pages with clear reference bits
#		random.seed()
#		oldData[i][refIndex] = random.randint(0,1)		#randomly choose a reference bit for this page
#		data[i][ref] = oldData[i][ref]		#alter new data to echo the changes
		
#	for i in range(len(oldData)):		#alter the usePattern to only have pages with set reference bits
#		if oldData[i][refIndex] == 1:
#			newUsePattern.append(oldData[i][page])
#	newUsePattern=newUsePattern+usePattern		#append original reference list for later display
	
#	print("NOTE: Old reference bits have been cleared and new references added to help illustrate the NRU algorithm.")
#	my_input("Press <ENTER> to continue")
	candidates=[]				#no candidates identified yet
	vFrame=[]				#no candidate frame numbers yet
	for i in range(len(oldData)):	#check each page in RAM
		if oldData[i][refIndex]==0:	#if its reference bit is clear
			candidates.append(oldData[i])		#add it to list of possible candidates
			vFrame.append(i)					#add its frame number to list of possible candidates

#	return oldData, candidates, newUsePattern, vFrame	#return original data, possible candidate list& full use pattern of references, 
												#and candidate victim frame numbers
	return oldData, candidates, usePattern, vFrame	#return original data, possible candidate list & use pattern of references, 
													#and candidate victim frame numbers

def getRefHistory(usePattern):
	"Generate reference history in LRU order"
	
#find LRU page in the use pattern that is ordered with least recent reference last
	head=0					#index of head of list
	page=0					#index of page number in RAM
	numRefs=len(usePattern)	#number of references in the use pattern of references
	referenceOrder=[]		#to hold indexes of pages in 'most recent reference first' order
	thisPage=[]				#no page dealt with yet
	
	i=numRefs-1				#start at end of use pattern list with most recent reference
	while i >=0:									#while not finished looking
		if usePattern[i] not in referenceOrder:			#if this reference not in list of references already
			referenceOrder.append(usePattern[i])			#add it to the list
			thisPage=usePattern[i]							#record which page has just been added
		i=i-1										#move to next page in use pattern
		while i > numRefs and usePattern[i] == thisPage:	#while not finished and current page is the page last added 
			i-=1												#move to next page in use pattern
	referenceOrder.reverse()			#sort reference history into 'most recent first'
	
	return referenceOrder	#return LRU reference history in 'least first' order

def LRU(data, pageIn, clock, usePattern):
	"Simulate LRU algorithm"

	print("\n\n ************** Least Recently Used **************\n")

	head=0					#index of head of list
	page=0					#index of page number in RAM

#find LRU page in the use pattern that is ordered with least recent reference first
	referenceOrder=getRefHistory(usePattern)	#Generate reference history in LRU order
	victimPage=referenceOrder[head]				#choose this victim 

#find that victim page in the data to get victim data
	i=head								#start at the beginning
	victim=[]								#victim data not found yet
	while i < len(data) and len(victim)==0:	#while still data to search and have not found victim data
		if victimPage == data[i][page]:			#if this is the victim page
			victim=data[i][:]						#store its data ([:] gets a COPY)
			vFrame=[i]							#record victim frame #
			data.remove(victim)					#remove it from memory
			data.append([pageIn,clock,1,0,1,1])		#place the incoming page in memory
		i+=1									#try next page in the data
	
	return data, victim, vFrame			#return new frame data, and victim chosen, and victim frame#

def LFU(data, pageIn, clock, usePattern):
	"Simulate LFU algorithm"

	print("\n\n ************** Least Frequently Used **************\n")

	head=0								#LFU page will be at top of sorted list

	data.sort(key=getFifth)				#sort in order of reference counter
	victim=data[head][:]				#take a copy of the LFU page details
	data.sort(key=getSecond)			#put the RAM data back in order of page arrival
	vFrame=[data.index(victim)]			#record victim' frame number
	data.remove(victim)				#remove it from RAM
	data.append([pageIn,clock,1,0,1,1])	#place the incoming page in RAM
	data.sort(key=getSecond)			#put the RAM data back in order of page arrival
		
	return data, victim, vFrame			#return the modified RAM data and the victim page details, and victim frame#

def generateCounters(data, usePattern, period, type):
	"generate reference decaying or ageing counter bytes"
	
	#period is number of refs before counter decay/ageing
	
	page=0					#index of page name in RAM data
	refCountIndex=4			#index of page's reference counter in RAM data
	refByteIndex=5			#index of page's counter Byte
	refIndex=2				#index of reference bit in RAM data
	numRefs=len(usePattern)	#number of page references
	numPages=len(data)		#number of pages in RAM
			
#initialise all reference counters to 0
	for i in range(numPages):		#for every page
		data[i][refCountIndex]=0		#set its counter to 0
		data[i][refByteIndex]=0			#set its ageing counter to 0
		
	refPattern=[]				#to hold use pattern in sets of 'period' references
	tick=0						#time passed
	while tick < numRefs:		#while references to process
		refd=[]						#no references in this period yet
		start=tick					#start at current time
		while tick<(start+period) and tick<numRefs:	#while references to process in this time period and not at end of reference list
			refd.append(usePattern[tick])				#record this reference in this reference period
			tick+=1										#move time on
		refPattern.append(refd)					#add this reference period data to the record

	print("Reference counter",type,"history")
	
	#first count up the reference counts and (for decay only) reference history byte 
	for r in range(len(refPattern)):	#for every period of n references (n == period (or less at the end))
		for p in range(len(data)):		#for every page in RAM
			for pr in range(len(refPattern[r])):		#for every reference in that period
				if data[p][page] == refPattern[r][pr]:	#if this reference was to the current page
					data[p][refIndex]=1						#set the current page reference bit
					data[p][refCountIndex]+=1 				#increment the current page ref counter
					if type == "decay":						#if it is a decaying counter
						data[p][refByteIndex]+=1 				#increment the current page ref byte
				if data[p][page] not in refPattern[r]:	#if the current page was not referenced in that period
					data[p][refIndex]=0						#clear its reference bit
		
		#now either age or decay the counters
		for p in range(len(data)):
			if type == "ageing":			#if ageing is needed then age the ref byte 
				data[p][refByteIndex]=shiftRight(data[p][refByteIndex],data[p][refIndex]) #by shifting in ref bit

			if data[p][page] not in refPattern[r]:	#for decay, if this page was not referenced in this period
				if data[p][refByteIndex] > 0 and type == "decay":			#if its decay reference byte is not already 0
						data[p][refByteIndex]=shiftRight(data[p][refByteIndex],0)	#Decay the ref counter shifting in 0
				
		endTime = ((r+1) * period) % numRefs	 #get end time of this period
		
		if endTime == 0 or (((r+1) * period) > numRefs):	#if end time of this period == 0 then we have wrapped around OR refs all dealt with so
			endTime = numRefs	#set it to the number of references for output later

		#display the data after this period starting with this period's references and then all references so far
		print("In", period, "references up to time", endTime, "the pages referenced pages were: ", refPattern[r])
		print("And all references so far are: ", end='')
		for j in range(0,r+1):				#for each reference period's pattern gathered so far
			print(refPattern[j]," ",end='')		#print it
		print("\n\nAfter",r+1,type,"(s) the current reference history is:")	
		print("Frame\tPage\tReference count\tReference History Byte\tReference bit")
		for p in range(len(data)):	#for every page in RAM display its data at this stage
			print(p,"\t",data[p][page],"\t",data[p][refCountIndex],"\t\t",decToBin(data[p][refByteIndex]),"=",end='')
			print('{:<4}'.format(data[p][refByteIndex]),"\t",data[p][refIndex])
			
		my_input("Press <ENTER> to continue")

	return data	

def LFUDC(data, pageIn, usePattern, clock, period):
	"Simulate LFU with decaying count algorithm"

	print("\n\n ************** Least Frequently Used with Decaying Count**************\n")

	head=0		#index of head of list
	page=0		#index of page number in RAM data

	oldData = copy.deepcopy(data)		#keep a copy of the data as it will change
	oldData = generateCounters(oldData, usePattern, period, "decay")	#generate refernce history counter byte for decay
	newData=copy.deepcopy(oldData)		#keep copy
#find the victim page in the data as the page with the lowest reference counter
	newData.sort(key=getSixth)				#sort data in reference history byte order (lowest first)
	victim=newData[head][:]				#choose victim from head of sorted list
	newData.sort(key=getSecond)			#put data back in oldest page first order
	vFrame=[newData.index(victim)]			#record victim's frame number
	newData.remove(victim)				#remove it from memory
	newData.append([pageIn,clock,1,0,1,1])	#place the incoming page in memory
	newData.sort(key=getSecond)			#put data back in oldest page first order
	
	return oldData, newData, victim, vFrame	#return old frame data, new frame data, and victim chosen, and victim frame#

def LRUA(data, pageIn, usePattern, clock, period):
	"Simulate LRUA algorithm"

	print("\n\n ************** Least Recently Used with Ageing**************\n")

	head=0		#index of head of list
	page=0		#index of page number in RAM data

	oldData = copy.deepcopy(data)		#keep a copy of the data as it will change
	oldData = generateCounters(oldData, usePattern, period, "ageing")	#generate refernce history counter byte for ageing
	newData=copy.deepcopy(oldData)		#keep a copy

#find the victim page in the data as the page with the lowest reference counter
	newData.sort(key=getSixth)				#sort data in reference byte order (lowest first)
	victim=newData[head][:]					#choose victim from head of sorted list 
	newData.sort(key=getSecond)				#put data back in oldest page first order
	vFrame=[newData.index(victim)]				#record victim's frame number
	newData.remove(victim)					#remove it from memory
	newData.append([pageIn,clock,1,0,1,128])	#place the incoming page in memory with ref bit shifted in (i.e. 10000000)
	newData.sort(key=getSecond)				#put data back in oldest page first order

	return oldData, newData, victim, vFrame		#return old frame data, new frame data, and victim chosen, and victim frame#

def showMainMenu():
	"Display menu"
	
	print("\n\n1:    Run First In, First Out (FIFO) Frame Victim Replacement Algorithm")
	print("2:    Run Not Recently Used (NRU) Frame Victim Replacement Algorithm")
	print("3:    Run Least Recently Used (LRU) Frame Victim Replacement Algorithm")
	print("4:    Run Least Frequently Used (LFU) Frame Victim Replacement Algorithm")
	print("5:    Run Least Frequently Used with Decaying Counter (LFUDC) Frame Victim Replacement Algorithm")
	print("6:    Run Least Recently Used with Ageing Counter (LRUA) Frame Victim Replacement Algorithm")
	print("7:    Run Clock (aka Second Chance) Frame Victim Replacement Algorithm")
	print("8:    Generate New Random Data")
	print("0:    Quit")

	return

#### Main Program ####

#initialise data
pageNames = []		#list of pages that may enter RAM at start
pageIn = 100		#page to bring in to full RAM
frameData = []		#data on pages in RAM as [page, arrival time, reference bit, modify bit, reference counter]
usePattern = []		#list of references to pages so far
pagesInRAM = []		#list of pages that have entered RAM at start
numRefs = 30		#number of initial memory references to generate at start
numFrames = 10		#number of page frames in RAM
#initialise and fill RAM
frameData, usePattern, pagesInRAM, clock = initialise(pageNames, frameData, usePattern, pagesInRAM, numRefs, numFrames)

initialData=copy.deepcopy(frameData)	#take copy of frame data
clock += 1								#move to next time unit

print("\nRAM is now full and stores",len(frameData),"pages as follows:")
print("Frame\tPage\tArrival Time")
for i in range(len(frameData)):		#for each page in RAM print its data summary
	print(i,"\t",frameData[i][0],"\t",frameData[i][1])
print("\n\nA reference to page", pageIn, "generates a page fault at time", clock,"so must be installed in RAM.")
print("RAM is full. Therefore a victim page must be chosen from the frames in RAM.")
	
victim=[]	#no victim chosen yet

ans=-1				#guarantee menu loop runs
while ans!=0:
	ans=-1		#guarantee menu loop runs
	maxOption=8				#8 menu items

	while ans<0 or ans>maxOption:	#while no valid choice made
		showMainMenu()		#show the appropriate menu
		ans=getInt("Which action (0 to "+str(maxOption)+")?" ,"Choose an option between 0 and "+str(maxOption))

	if ans==1:	#FIFO
		newFrameData, victim, vFrame = FIFO(frameData, pageIn, clock)		#run FIFO
		outputResults(pageIn, initialData, newFrameData, victim, usePattern, "FIFO", vFrame)	#show results	
		my_input("Press <ENTER> to continue")
	elif ans==7:	#Clock
		maxPointer=len(frameData) - 1		#set maximum clock pointer value as number of pages in RAM
		pointer=-1							#start pointer at incorrect value to force input
		while pointer < 0 or pointer > maxPointer:	#while user has not given a valid pointer value
			pointer=getInt("Current clock pointer? (0 - "+str(maxPointer)+"): ", \
			"Please enter an integer between 0 and "+str(maxPointer))	#get pointer value in range
		
		oldData, newFrameData, victim, pointer, newUsePattern, vFrame = \
		clockSim(frameData, pageIn, clock, pointer, usePattern)	#run Clock
		outputResults(pageIn, oldData, newFrameData, victim, newUsePattern, "clock", vFrame)	#show results
		print("Now the current pointer is ",pointer," pointing to page",initialData[pointer][0],"\n")
		my_input("Press <ENTER> to continue")
	elif ans==2:	#NRU
		oldData, newFrameData, newUsePattern, vFrame = NRU(frameData)		#run NRU
		outputResults(pageIn, oldData, newFrameData, victim, newUsePattern, "NRU", vFrame)	#show results
		my_input("Press <ENTER> to continue")
	elif ans==3:	#LRU
		newFrameData, victim, vFrame = LRU(frameData, pageIn, clock, usePattern)		#run LRU
		outputResults(pageIn, initialData, newFrameData, victim, usePattern, "LRU", vFrame)	#show results
		my_input("Press <ENTER> to continue")
	elif ans==4:	#LFU
		newFrameData, victim, vFrame = LFU(frameData, pageIn, clock, usePattern)		#run LFU
		outputResults(pageIn, initialData, newFrameData, victim, usePattern, "LFU", vFrame)	#show results
		my_input("Press <ENTER> to continue")
	elif ans==5:	#LFUDC
		period=5	#set number of references between decays of counters
		oldFrameData, newFrameData, victim, vFrame = LFUDC(frameData, pageIn, usePattern, clock, period)		#run LFUDC
		outputResults(pageIn, oldFrameData, newFrameData, victim, usePattern, "LFUDC", vFrame)	#show results
		my_input("Press <ENTER> to continue")
	elif ans==6:	#LRUA
		period=5	#set number of references between ageing of counters
		oldFrameData, newFrameData, victim, vFrame = LRUA(frameData, pageIn, usePattern, clock, period)		#run LRUA
		outputResults(pageIn, oldFrameData, newFrameData, victim, usePattern, "LRUA", vFrame)	#show results
		my_input("Press <ENTER> to continue")
	elif ans==8: #New random data
		sure="n"
		sure=my_input("\nThis will quit and lose all the old data. Are you sure? y/[n]")
		if sure=="y":
			pageNames = []		#list of pages that may enter RAM at start
			pageIn = 100		#page to bring in to full RAM
			frameData = []		#data on pages in RAM as [page, arrival time, reference bit, modify bit, reference counter]
			usePattern = []		#list of references to pages so far
			pagesInRAM = []		#list of pages that have entered RAM at start
			numRefs = 30		#number of initial memory references to generate at start
			numFrames = 10		#number of page frames in RAM
			#initialise and fill RAM
			frameData, usePattern, pagesInRAM, clock = initialise(pageNames, frameData, usePattern, pagesInRAM, numRefs, numFrames)

			initialData=copy.deepcopy(frameData)	#take copy of frame data
			clock += 1								#move to next time unit

			print("\nRAM is now full and stores",len(frameData),"pages as follows:")
			print("Frame\tPage\tArrival Time")
			for i in range(len(frameData)):		#for each page in RAM print its data summary
				print(i,"\t",frameData[i][0],"\t",frameData[i][1])
			print("\n\nA reference to page", pageIn, "generates a page fault at time", clock,"so must be installed in RAM.")
			print("RAM is full. Therefore a victim page must be chosen from the frames in RAM.")
				
		my_input("Press <ENTER> to continue")
	elif ans==0: #quit
		sure="n"
		sure=my_input("\nThis will quit and lose all the old data. Are you sure? y/[n]")
		if sure!="y":
			ans=-1
		else:
			print("OK, Bye")
	
	if ans!=0:
		frameData=copy.deepcopy(initialData)	#re-instate original data
		victim=[]	#no victim chosen yet






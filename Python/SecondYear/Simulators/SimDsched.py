### Disk scheduling algorithm simulations ###

import sys
import random

### Functions ###

#Input interaction functions#
def my_input(prompt=None):
	"Prompts for input on the stderr channel"

	if prompt:						#if there is a prompt
		sys.stderr.write(str(prompt))			#display it on the error channel

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

def makeData(top, bottom):
	"Generate random data for simulation"

	random.seed()
	numberOfRequests = random.randint(8,10)	#generate a number of requests
	trackNums = []							#initially no requests
	for i in range(numberOfRequests):			#generate a set of track requests
		random.seed()
		trackNums.append(random.randint(bottom, top))	#append random request to the list of requests.
		random.seed()
		start=random.randint(bottom, top)	#get random starting track number

	return trackNums, start	 	#return the data to main program

def getData(top, bottom, start):
	"Gather the data for simulation"

	numberOfRequests = 0				#initially no requests
	while numberOfRequests < 1 or numberOfRequests > 10:		#continue to ask user for number of track requests while the response unsatisfactory
		numberOfRequests = getInt("How many new Disk Track Requests (Max 10)? ", "Please enter a positive integer up to 10.")

	trackNums = []						#initially no requests
	for i in range(numberOfRequests):		#generate a number for each request
		request=-1
		while (request<bottom or request>top):
			request=getInt("Disk Track Requested (integer "+str(bottom)+"-"+str(top)+")? ", "Please enter an integer "+str(bottom)+"-"+str(top)+").")
		trackNums.append(request)		#append it to the list of requests.

	if start<0:
		start=getInt("Starting Track of Disk R/W head (integer "+str(bottom)+"-"+str(top)+")? ", "Please enter an integer "+str(bottom)+"-"+str(top)+").")

	return trackNums,start	 	#return the data to main program

#Output display functions#
def outputResults(start, toDo, tracksCrossed, algType, requests):
	"Display all results"

	print("In the",algType,"algorithm simulation the following track requests were input (in order of arrival):",requests)
	print("and at the beginning of the simulation the r/w head was initially at track",start)
	print("Track requests were processed in the following order: ",group,toDo)
	print("Numbers of tracks crossed for each request: ")
	sum=0
	for i in range(len(tracksCrossed)):							#for every span of tracks crossed
		print("From",start,"to",toDo[i],":",tracksCrossed[i])	#display it from start to track: number crossed
		start=toDo[i]											#move start
		sum+=tracksCrossed[i]									#accumulate sum of tracks crossed

	print("\nTotal number of tracks crossed:",sum,group,"\n")			#total seek distance as measure of efficiency

	return

def showData(pending, start, top, bottom):
	"Show the data being used"
	
	print("\nAssuming the disk tracks are numbered from",bottom,"to",top,"and the disk arm is initially at track",start)
	print("\nAnd that CScan & CLook only process requests on the way up toward",top)
	print("\n",len(pending),"original disk track requests as follows:")
	print(pending)
		
	return

##### track processing tools ####
def processTrack(track, done, start, tracksCrossed):
	"process a track request, move to new position, add it to the list done and calculate & record distance travelled"

	done.append(track)			#record next track as visited
	cross=abs(start - track)	#count number of tracks traversed to get to it
	tracksCrossed.append(cross)	#record number of tracks traversed to get to it

	return done, track, tracksCrossed	 #return updated done list, new start position, & updated record of tracks crossed

######  First In First Out  ######
def FIFO(requests,start, top, bottom):
	"Simulate First In First Out algorithm"

	print("\n\n ************** First In, First Out **************\n")

	#will user want to add new data while tracks are being processed?
	addData="n"												#assume not
	addData = my_input("Will you want to add data while tracks are being processed (y/[n])? ")	#but ask 

	toDo = list(requests)		#generate a copy of the list of requests to deal with

	tracksCrossed=[]			#records numbers of tracks crossed for each request
	done=[]					#records tracks processed in order

	while len(toDo) > 0:			#while requests to do
		done, start, tracksCrossed=processTrack(toDo[0], done, start, tracksCrossed)	 #process the request and record changes
		del toDo[0]					#remove it from list of tracks to do

		if addData=="y":
			print("Have done",done)
			newData = my_input("New data for FIFO (y/[n])? ")	#does user want to add new data?
			if newData == "y":						#if so gather new data 
				newToDo, start = getData(top, bottom, start)	#get the new track requests
				toDo = toDo + newToDo					#append them to the existing list to do at the end
				requests = requests + newToDo				#keep list of all requests

	return tracksCrossed, done, requests

###### Shortest Seek Time First ######
def getSSTFOrder(order, where, top, bottom):

	newOrder=[]						#to hold the order of tracks in SSTF order
	while len(order)>0:					#while tracks to process
		min=top+1						#set minimum distance above all possible minima initially
		minIndex=-1						#set index of minimum element below all possible indexes initially
		for i in range(len(order)):			#for every request
			distance=abs(where - order[i])		#calculate distance from where we are to this track
			if distance < min:					#if distance < current minimum distance
				min=distance						#make it the new min
				minIndex=i						#record the index of the min

		newOrder.append(order[minIndex])	#add this track as next
		where=order[minIndex]				#move to that track
		del order[minIndex]				#remove it from those to do 

	return newOrder

def SSTF(requests,start, top, bottom):
	"Simulate Shortest Seek Time First algorithm"

	print("\n\n ************** Shortest Seek Time First **************\n")

	#will user want to add new data while tracks are being processed?
	addData="n"												#assume not
	addData = my_input("Will you want to add data while tracks are being processed (y/[n])? ")	#but ask 

	toDo = list(requests)		#generate a copy of the list of requests to deal with
	tracksCrossed=[]			#records number of tracks crossed in each step
	done=[]					#records tracks processed


	order=getSSTFOrder(toDo, start, top, bottom)	#get into correct order

	while len(order) > 0:			#while requests to process
		done, start, tracksCrossed=processTrack(order[0], done, start, tracksCrossed)	 #process the request and record changes
		del order[0]					#remove it from list of requests to do

		if addData=="y":
			print("Have done",done)
			newData = my_input("New data for SSTF (y/[n])? ")	#does user want to add new data?
			if newData == "y":						#if so gather new data 
				newToDo, start = getData(top, bottom, start)		#get new requests
				order = order + newToDo						#append them to the existing order
				order=getSSTFOrder(order, start, top, bottom)		#re-order into SSTF
				requests = requests + newToDo				#keep list of all requests

	return tracksCrossed, done, requests

#### Scanning Algorithm functions ####
def showDirMenu(top, bottom):
	"Display Scan direction menu"
	
	print("Choose Scan Direction")
	print("\n\n1:    From", bottom, "to", top)
	print("2:    From", top, "to", bottom)

	return
	
def getScanOrder(algType, toDo, low, high, start, top, bottom, direction, firsttime):
	"get into correct order for scanning"

	i=0
	if direction==1:
		while  i<len(toDo):			#distribute requests above and below current position
			if toDo[i]<start:			#if it is below current position
				low.append(toDo[i])			#put it in the low list
			else:						#if it is above or equal to current position
				high.append(toDo[i])		#put it in the high list
			i+=1						#move to next track to do
	elif direction==2:
		while  i<len(toDo):			#distribute requests above and below current position
			if toDo[i]<=start:			#if it is below current position
				low.append(toDo[i])			#put it in the low list
			else:						#if it is above or equal to current position
				high.append(toDo[i])		#put it in the high list
			i+=1						#move to next track to do

	if (algType=="scan" or algType=="cscan" or algType=="nstepscan" or algType=="fscan"):	#scans should process extremities first time
		if firsttime==1 and direction==1:
			if len(high)==0:
				high.append(top)
		if firsttime==1 and direction==2:
			if len(low)==0:
				low.append(bottom)		
		
	high.sort()					#sort the track requests above current position in increasing order
	low.sort()					#sort the track requests below current position in increasing order
	if algType=="look" or algType=="scan" or  algType=="nstepscan" or algType=="nsteplook"\
		or  algType=="fscan" or algType=="flook":	#looks and scans should process in both directions
		low.reverse()					#change to decreasing order so that they are dealt with on the return

	if direction==1:		#if scanning from bottom to top
		order=high+low		#do the requests above on the way up first then those below on the way back (or up if C)
#		print("Dir 1: hi-lo")
	else:					#if scanning from top to bottom
		order=low+high		#do the requests below on the way down (or up for C) first then those above
#		print("Dir 2: lo-hi")
	
	return order, low, high

def doScan(algType, order, done, start, tracksCrossed, low, high, top, bottom, direction, addData):
	"Do any type of scan"

	newToDo=[]
	addedExtras = newToDo 	#keep a copy of the added jobs
	dirChange=0	
	didFast=0
	while len(order) > 0:			#while requests to process
		#print(start, low, high)
		if direction==2 and (algType=="cscan" or algType=="clook"):	#is C and started in down direction
			if algType=="cscan" and order[0]!=bottom: #for cscan if not about to visit bottom track
				done, start, tracksCrossed=processTrack(bottom, done, start, tracksCrossed)	 #fast return to bottom and record changes
#				print("Did bottom for first time cscan that started going down")
				didFast=1	#record bottom done on fast return
			elif algType=="cscan" and order[0]==bottom: #for cscan if already going to visit bottom track
				didFast=1	#record bottom done on fast return
			direction = 1			#then reverse the direction to make it always up for both cscan and clook
#			print("Did fast return for first time c alg going down - now going up")
#			dirChange=1				#record change

		done, start, tracksCrossed=processTrack(order[0], done, start, tracksCrossed)	 #process the next request and record changes
		track=order[0]					#record track done
		del order[0]					#remove it from list of requests to do
			
		if track in low:		#if this done track is in the low list
			low.remove(track)		#remove it
		if track in high:		#if this done track is in the high list
			high.remove(track)		#remove it
			

#at a turning point? 
#First Deal with scans (not looks) as they need to travel to disk extremities even if not requested
#then cscan dealt with separately (cscan's direction is fixed at start to upwards)
#then looks (except clook) to get them to change direction at right times (clook's direction is fixed at start to upwards)

#first is there more to do?
		if len(order)>0 and (algType=="fscan" or algType=="nstepscan" or algType=="scan"):	#more to do & just the non-C scans 
			if direction==1 and track>max(order) :	#going up, highest track is done
#				print("len(order)>0 and fscan, nstepscan, scan")
#				print("going up, just done highest and it was=",track)
				if track!=top:	#but top track not done
					done, start, tracksCrossed=processTrack(top, done, start, tracksCrossed)	#go to top and record changes
				direction = 2			#then reverse the direction to start traveling down
#				print("top done, changed to down")
#				dirChange=2				#record change
			elif direction==2 and track<min(order): #going down, lowest track is done
#				print("len(order)>0 and fscan, nstepscan, scan")
#				print("going down, just done lowest and it was=",track)
				if track!=bottom:	#but bottom track not done
					done, start, tracksCrossed=processTrack(bottom, done, start, tracksCrossed)	 #go to bottom and record changes
				direction = 1			#then reverse the direction to start traveling up
#				print("bottom done, changed to up")
#				dirChange=1				#record change	

#Or have we just finished a scan? There may be another for fscan and nstepscan so get ready
		if len(order)==0 and (algType=="fscan" or algType=="nstepscan" or algType=="scan"):	#finshed this scan for just the non-C scans 
			if direction==1:	#going up, all done 
				if track!=top: #but not reached top
					done, start, tracksCrossed=processTrack(top, done, start, tracksCrossed)	 #go to top and record changes
				direction=2	#then reverse the direction
#				print("finished a scan up so did top and turned")
			elif direction==2:	#going down, all done 
				if track!=bottom: 	#but not reached bottom
					done, start, tracksCrossed=processTrack(bottom, done, start, tracksCrossed)	 #go to top and record changes
				direction=1	#then reverse the direction
#				print("finished a scan down so did bottom and turned")

#now deal with cscan's limits		
		if direction==1 and didFast==0:	#going up and not dealing with first fast return having started downward 
			if algType=="cscan" and len(order)!=0 and track>max(order): #for cscan and some more tracks to do and highest track done 
				if track!=top:	#but top not done
					done, start, tracksCrossed=processTrack(top, done, start, tracksCrossed)	 #go to top and record changes
				if order[0]!=bottom:	#if bottom not next to be done
					done, start, tracksCrossed=processTrack(bottom, done, start, tracksCrossed)	 #fast return to bottom and record changes
#				print("cscan and more to do and just did highest track",track,"so did top and fast return to bottom")

		didFast=0	#reset record of first fast return for cscan
		
#now deal with looks
		if len(order)>0 and (algType=="look" or algType=="flook" or algType=="nsteplook"): #there's more to do and a looker (but not a 'C')
			if direction==1 and track>max(order): 	#have done highest and going up
				direction=2	#start going downward
			elif direction==2 and track<min(order):	#have done lowest and going down
				direction=1	#start going upwards
				
	
		if addData=="y":
			print("Have done",done)
			newData = my_input("New data for "+algType+" (y/[n])? ")	#does user want to add new data?
			if newData == "y":						#if so gather new data 
				if algType=="nstepscan" or algType=="nsteplook" or algType=="fscan" or algType=="flook":
					newToDoMore, start = getData(top, bottom, start)		#get more data for later (no new start)
					newToDo = newToDo + newToDoMore				#add it to the new to do list for later
					addedExtras = addedExtras + newToDo 	#keep a copy of the added jobs
				else:
					newToDo, start = getData(top, bottom, start) #get new requests
					addedExtras = addedExtras + newToDo 	#keep a copy of the added jobs
					#get into correct scan order by distributing new requests into current low and high as appropriate
					newToDo=newToDo+order	#put all requests together
					low=[]	#empty the low list
					high=[]	#empty high list 
					#now re-distribute according to new r/w head location
					order, low, high= getScanOrder(algType, newToDo, low, high, start, top, bottom, direction, 0)	#get into correct scan order

	return done, start, tracksCrossed, low, high, direction, addedExtras

#### Scanning Algorithms ####
def scanning(algType, requests, start, top, bottom, n, firsttime):
	"Simulate Scan/CScan/Look/CLook algorithm"

	if n>0:	#step algorithm
		print("\n\n ************** ",algType," Algorithm where N=",str(n),"**************\n")
	else:
		print("\n\n ************** ",algType," Algorithm **************\n")

	direction=-1
	while direction!=1 and direction!=2:	#while no valid choice made
		showDirMenu(top, bottom)		#show the direction menu
		direction=getInt("Which scanning direction (1 or 2)?" ,"Choose either 1 or 2")

	#will user want to add new data while tracks are being processed?
	addData="n"												#assume not
	addData = my_input("Will you want to add data while tracks are being processed (y/[n])? ")	#but ask 

	toDo = list(requests)	#generate a copy of the list of requests to deal with
	tracksCrossed=[]		#records number of tracks crossed in each step
	done=[]					#records tracks processed in order
	low=[]					#records tracks to be processed below current position in order
	high=[]					#records tracks processed above current position in order
	newToDo=[]				#keeps a copy of new requests generated during each pass for nsteps

	if algType=="nstepscan" or algType=="nsteplook":
		oldStart=start
		while len(toDo)>0:			#while there are requests to process
			order=[]					#order of processing in this scan
			i=0							#start at first request to do in this scan
			while i<n and len(toDo)>0:	#while have not gathered all the tracks for this scan there are tracks to process
				order.append(toDo[0])		#add next request to this scan order
				del toDo[0]					#remove it from to do list
				i+=1						#go on to next request for this scan 

			order, low, high = getScanOrder(algType, order, low, high, start, top, bottom, direction, firsttime)	#get into correct order
			done, start, tracksCrossed, low, high, direction, newToDo = doScan(algType, order, done, start, tracksCrossed, low, high, top, bottom, direction, addData)
			toDo = toDo + newToDo 				#add new requests to the end of the to do list for later
			requests = requests + newToDo		#keep list of all requests
			newToDo=[]							#empty the list of newly added tracks

		return tracksCrossed, done, requests

	elif algType=="fscan" or algType=="flook":
		allTracksCrossed=[]	#record of all tracks crossed in processing requests
		allDone=[]			#record of all tracks processed
		while len(toDo)>0: #while requests to process (either original list or later added requests)
			#process the current toDo list (while gathering possible new requests into newToDo
			order, low, high = getScanOrder(algType, toDo, low, high, start, top, bottom, direction, firsttime)	#get into correct order
			done, start, tracksCrossed, low, high, direction, newToDo = doScan(algType, order, done, start, tracksCrossed, low, high, top, bottom, direction, addData)
			allTracksCrossed = allTracksCrossed + tracksCrossed		#add the distances travelled for this batch to the record
			tracksCrossed=[]									#empty old tracks crossed list
			allDone = allDone + done							#add the tracks processed for this batch to the record
			done=[]												#empty old done list
			toDo=newToDo										#get the next batch
			requests = requests + newToDo						#keep list of all requests
			newToDo=[]							#empty the list of newly added tracks

		return allTracksCrossed, allDone, requests

	else: #cscan or clook or scan or look
		order, low, high = getScanOrder(algType, toDo, low, high, start, top, bottom, direction, firsttime)	#get into correct scan order
		done, start, tracksCrossed, low, high, direction, newToDo = doScan(algType, order, done, start, tracksCrossed, low, high, top, bottom, direction, addData)
		requests = requests + newToDo						#keep list of all requests
		newToDo=[]							#empty the list of newly added tracks

		return tracksCrossed, done, requests

def showMainMenu(data):
	"Display menu"
	
	print("\n\n1:    Generate Random Data")
	print("2:    Use Default Data")
	print("3:    Enter Your own Data")
	if (data>0):
		print("4:    Run First In, First Out (FIFO) Disk Scheduling Algorithm")
		print("5:    Run Shortest Seek Time First (SSTF) Disk Scheduling Algorithm")
		print("6:    Run Scan Disk Scheduling Algorithm")
		print("7:    Run Look Disk Scheduling Algorithm")
		print("8:    Run C-Scan Disk Scheduling Algorithm")
		print("9:    Run C-Look Disk Scheduling Algorithm")
		print("10:   Run N-Step-Scan Disk Scheduling Algorithm")
		print("11:   Run N-Step-Look Disk Scheduling Algorithm")
		print("12:   Run FScan Disk Scheduling Algorithm")
		print("13:   Run FLook Disk Scheduling Algorithm")
	print("0:    Quit")

	return

#### Main Program ####

#initialise data
trackNums=[]			#initially no data
tracksCrossed = []		#initially no tracks crossed
bottom=0				#min disk track number
top=199					#max disk track number - This can be changed to uniquely identify a particular simulator in the output
group=""	#This can be changed to uniquely identify a particular simulator in the output

ans=-1				#guarantee menu loop runs
while ans!=0:			#keep looking for a valid choice
	ans=-1				#remove last choice
	if (len(trackNums)>0):	#if there is data
		maxOption=13		#full menu: 14 menu items: 0-13
	else:
		maxOption=3			#just the data generation menu

	while ans<0 or ans>maxOption:	#while no valid choice made
		showMainMenu(len(trackNums))		#show the appropriate menu
		ans=getInt("Which action (0 to "+str(maxOption)+")?" ,"Choose an option between 0 and "+str(maxOption))

	if ans==1:	#generate random data
		trackNums, start=makeData(top, bottom)		#generate track request data 
		showData(trackNums, start, top, bottom)		#show data
		my_input("Press <ENTER> to continue")
	elif ans==2:	#Use Default data
		trackNums=[98, 183, 37, 122, 14, 124, 65, 67]	#default track request data
		start=53									#disk arm starts at track 53
		showData(trackNums, start, top, bottom)		#show data
		my_input("Press <ENTER> to continue")
	elif ans==3:	#Input user data
		trackNums, start=getData(top, bottom, -1)		#gather track request data (new start)
		showData(trackNums, start, top, bottom)		#show data
		my_input("Press <ENTER> to continue")
	elif ans==4:	#FIFO
		tracksCrossed, done, requests = FIFO(trackNums, start, top, bottom)	#run First In, First Out
		outputResults(start, done, tracksCrossed, "FIFO", requests)			#show results
		my_input("Press <ENTER> to continue")
	elif ans==5:	#SSTF
		tracksCrossed, done, requests = SSTF(trackNums, start, top, bottom)	#run SSTF
		outputResults(start, done, tracksCrossed, "SSTF", requests)			#show results
		my_input("Press <ENTER> to continue")
	elif ans==6:	#Scan
		tracksCrossed, done, requests = scanning("scan", trackNums, start, top, bottom, 0, 1)	#run Scan
		outputResults(start, done, tracksCrossed, "Scan", requests)						#show results
		my_input("Press <ENTER> to continue")
	elif ans==7:	#Look
		tracksCrossed, done, requests = scanning("look", trackNums, start, top, bottom, 0, 1)	#run Look
		outputResults(start, done, tracksCrossed, "Look", requests)						#show results
		my_input("Press <ENTER> to continue")
	elif ans==8:	#CScan
		tracksCrossed, done, requests = scanning("cscan", trackNums, start, top, bottom, 0, 1)	#run CScan
		outputResults(start, done, tracksCrossed, "CScan", requests)						#show results
		my_input("Press <ENTER> to continue")
	elif ans==9:	#CLook
		tracksCrossed, done, requests = scanning("clook", trackNums, start, top, bottom, 0, 1)	#run CLook
		outputResults(start, done, tracksCrossed, "CLook", requests)						#show results
		my_input("Press <ENTER> to continue")
	elif ans==10: #N-Step-Scan
		n=0			#assume 0step (invalid )
		while n<1:	#while no valid choice made
			n=getInt("What value of N (>1)?" ,"Choose an N >1")
		tracksCrossed, done, requests =scanning("nstepscan", trackNums, start, top, bottom, n, 1)		#run N-Step-Scan 
		outputResults(start, done, tracksCrossed, str(n)+"-Step-Scan", requests)						#show results
		my_input("Press <ENTER> to continue")
	elif ans==11: #N-Step-Look
		n=1
		while n<2:	#while no valid choice made
			n=getInt("What value of N (>1)?" ,"Choose an an N >1")
		tracksCrossed, done, requests = scanning("nsteplook", trackNums, start, top, bottom, n, 1)		#run N-Step-Look 
		outputResults(start, done, tracksCrossed, str(n)+"-Step-Look", requests)						#show results
		my_input("Press <ENTER> to continue")
	elif ans==12: #FScan
		tracksCrossed, done, requests = scanning("fscan", trackNums, start, top, bottom, 0, 1)	#run FScan
		outputResults(start, done, tracksCrossed, "FScan", requests)						#show results
		my_input("Press <ENTER> to continue")
	elif ans==13: #FLook
		tracksCrossed, done, requests = scanning("flook", trackNums, start, top, bottom, 0, 1)	#run FLook
		outputResults(start, done, tracksCrossed, "FLook", requests)						#show results
		my_input("Press <ENTER> to continue")
	elif ans==0: #quit
		sure="n"
		sure=my_input("\nThis will quit and lose all the old data. Are you sure? y/[n]")
		if sure!="y":
			ans=-1
		else:
			print("OK, Bye")

	if ans!=0 and (len(trackNums)>0):			#if not quitting and there is data
		showData(trackNums, start, top, bottom)		#re-display it

### CPU scheduling algorithm simulations ###

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

def makeData(clock, previousNumProcs):
	"Generate random data for simulation"
	
	random.seed()
	numberOfProcesses = random.randint(4,5)
	processNames = []						#initially no processes
	for i in range(numberOfProcesses):		#generate a name for each process and
		processNames.append("p"+str(previousNumProcs+i))	#append it to the list of process names p0, p1, etc.
	#processNames.sort()
	#print(processNames)
	arrivalTimes = []					#initially have no arrival times
	for p in processNames:				#for each process
		random.seed()
		a=random.randint(0,12)	 	#make arrival time
		while a in arrivalTimes:			#avoid duplicates
			a=random.randint(0,12)	 		#make an alternative arrival time
		arrivalTimes.append(a+clock)	#ensure it is at or after clock time and append it to the list of arrival times

	serviceTimes = []						#initially have no service times
	for p in processNames:					#for each process
		random.seed()
		s = random.randint(1,6)					#make service requirement
		serviceTimes.append(s)				#append it to the list of service times

	return numberOfProcesses, processNames, arrivalTimes, serviceTimes	#return the data to main program

def getData(clock, previousNumProcs):
	"Gather the data for simulation"

	numberOfProcesses = 0				#initially no processes
	while numberOfProcesses < 1:		#continue to ask user for number of processes while the response unsatisfactory
		numberOfProcesses = getInt("Number of processes (positive integer)? ", "Please enter a positive integer.")

	processNames = []						#initially no processes
	for i in range(numberOfProcesses):		#generate a name for each process and
		processNames.append("p"+str(previousNumProcs+i))	#append it to the list of process names p0, p1, etc.

	arrivalTimes = []						#initially have no arrival times
	for p in processNames:					#for each process
		a=getInt("Arrival time for "+p+" (positive integer or 0)? ", "Please enter a positive integer or 0.")	 #get arrival time
		arrivalTimes.append(a+clock)					#ensure it is at or after clock time and append it to the list of arrival times

	serviceTimes = []						#initially have no service times
	for p in processNames:					#for each process
		s = 0								#initially no service requirement
		while s < 1:						#continually prompt for valid service requirement
			s=getInt("Service time for "+p+" (positive integer)? ","Please enter a positive integer.")	 #get the service time
		serviceTimes.append(s)				#append it to the list of service times

	return numberOfProcesses, processNames, arrivalTimes, serviceTimes	#return the data to main program

def getQuantum():
	"get quantum value for RR algorithm"

	quantum = 0							#initially no quantum for Round Robin
	while quantum < 1:					#continually prompt for valid quantum
		quantum = getInt("Quantum for Round Robin (positive integer)? ","Please enter a positive integer.")	 #get quantum

	return quantum

def getNewData(clock, previousNumProcs, newProcNames, newArrTimes, newServTimes, toDo):
	"Gather new process data in middle of an algorithm run and update data"

	#let user know that arrival times are counted from current clock time
	print("\nArrival times are to be counted from current clock time: ",clock)
	print("E.g. '0' means arriving now at time: ",clock,"\n")

	#gather new data at time on clock
	numAddedProcs, addedProcNames, addedArrTimes, addedServTimes = getData(clock, previousNumProcs)
		
	newToDo=[]						#initialise new list of processes to deal with
	for i in range(numAddedProcs):		#new processes:1 entry each: (arrival time, service time, name)
		newToDo.append([addedArrTimes[i], addedServTimes[i], addedProcNames[i]])	
	
	newToDo.sort()						#sort by arrival time - in event of a tie FCFS operates

	for a,s,p in newToDo:					#for each new process
		toDo.append([a,s,p])					#add it to the list of processes to deal with
		newProcNames.append(p)				#update list of processes added during algorithm run
		newArrTimes.append(a)				#update list of arrival times added during algorithm run
		newServTimes.append(s)				#update list of service times added during algorithm run

	#return data on processes added and updated toDo list, and list of new processes added
	return numAddedProcs, newProcNames, newArrTimes, newServTimes, toDo, newToDo

#Output display functions#
def showExecutionHeaders(clock):
	"Start table headers for execution pattern"

	print("\nProc\t",end='')	#display heading for 'Process' column
	for c in range(clock):	#for each required time unit
		print(c,"",end='')	#display time unit header
	print()				#newline at end

	return

def showExecutionPattern(processNames, executionPattern, serviceTimes, arrivalTimes):
	"Display table of 'runs' and 'waits' by time unit for each process"

	pNumber=0				#start with first process
	for p in processNames:		#for each process generate a
		rtimes=[]					#list of time points when the process is running
		for endTime, process, duration in executionPattern:	#for each execution burst [end time, process name, duration]
			if p==process: 				#if the current process is running during this execution burst
				for j in range(endTime-duration,endTime):		#from start time of run burst [= end time - duration] to end time
					rtimes.append(j)		#record that time unit in the list of run times
		
		pline=[]								#initially no print line data for that process
		time=0								#start at time 0
		for i in range(arrivalTimes[pNumber]):		#need to avoid Ws and Rs in print line before arrival
			pline.append("  ")						#so insert spaces at the start of the process's record
			time+=1								#move time on

		while time<=max(rtimes):	#build the rest of the process's record up to the end of its runs
			if time in rtimes:			#if it is running at this time
				pline.append("R ")			#insert 'R' in its print line
			else:						#if not running then waiting
				pline.append("W ")		#insert a 'W' in its print line
			time+=1					#move time on

		print(p,"\t",end='')			#print process number as row label
		t=0						#initially deal with time unit 0 
		for c in pline:				#for each recorded activity description for this process
			if t<10:					#if single digit time unit
				print(c,end='')				#print its activity
			else:						#otherwise if more space needed
				print(c,"",end='')			#print the activity with more space
			t+=1						#move to next time unit
		print()					#move to next output line for next process
		pNumber+=1				#go to next process

	return

def outputResults(clock,processNames,executionPattern,serviceTimes,arrivalTimes):
	"Display all results"

	showExecutionHeaders(clock)												#display execution pattern table headers
	showExecutionPattern(processNames, executionPattern, serviceTimes, arrivalTimes)	#display execution pattern table data

	return

def showData(pending):
	"Show the data being used"
	
	name=2
	arrival=0
	service=1
	pending.sort(key=getName)
	print("\nProcess\tArrival Time\tService Time")
	for i in range(len(pending)):
		print(pending[i][name],"\t",pending[i][arrival],"\t\t",pending[i][service])
		
	return

#sorting key functions for process list elements with [arrival time, service time, process name, response ratio]#
def getArrival(item):
	return(item[0])

def getService(item):
	return(item[1])

def getName(item):
	return(item[2])

def getRatio(item):
	return(item[3])

###### First Come First Served ######
def FCFS(processes):
	"Simulate First Come First Served algorithm"

	print("\n\n ************** First Come First Served **************\n")

	#will user want to add new data on the fly?
	addData="n"												#assume not
	addData = my_input("Will you want to add data on the fly (y/[n])? ")	#but ask 

	numNewProcs	=0									#number of processes added during the run of FCFS
	newProcNames, newArrTimes, newServTimes=[],[],[]		#details of processes added during the run of FCFS

	toDo = list(processes)		#generate a copy of the list of processes to deal with
	numProcesses=len(toDo)	#record initial number of processes

	executionPattern=[]			#records pattern of execution as list of entries: [at time t, process, service received]
	clock = 0						#start the clock
	next=0						#next process will be at start of list when sorted by arrival times

	while len(toDo) > 0:			#while processes to run
		queue=[]						#current queue of processes arrived and competing for processor
		arrivalTimes=[]				#arrival times of queue processes
		for arrival, service, process in toDo:			#for each toDo process
			if arrival<=clock:							#if it has arrived
				arrivalTimes.append(arrival)				#record its arrival time
				queue.append([arrival, service, process])		#add it to the queue

		arrivalTimes.sort()										#sort arrival times
		queue.sort(key=getArrival)								#sort queue by arrival times

		if len(queue)>0:							#if there are waiting processes
			arrival,service,process=queue[next]				#get next process details
			clock += service								#count time passed for its execution
			executionPattern.append([clock, process, service])	#store execution info as [at time t, process name, time used]
			toDo.remove([arrival, service, process])			#remove it from list of processes to do
		else:										#if no processes waiting
			clock+=1										#move time on 

		if addData=="y":
			newData = my_input("New data for FCFS at time "+str(clock)+" (y/[n])? ")	#does user want to add new data?
			if newData == "y":						#if so gather new data at time on clock
				numNewProcs, newProcNames, newArrTimes, newServTimes, toDo, newToDo =\
					getNewData(clock, numProcesses, newProcNames, newArrTimes, newServTimes, toDo) 
				numProcesses+=numNewProcs	#update number of processes

	#return total time used, pattern of execution, and, for processes added, number, names, arrival times, and service times
	return clock, executionPattern, numNewProcs, newProcNames, newArrTimes, newServTimes

###### Shortest Process Next ######
def SPN(processes):
	"Simulate Shortest Process Next algorithm"

	print("\n\n ************** Shortest Process Next **************\n")

	#will user want to add new data on the fly?
	addData="n"												#assume not
	addData = my_input("Will you want to add data on the fly (y/[n])? ")	#but ask 

	numNewProcs	=0									#number of processes added during the run of SPN
	newProcNames, newArrTimes, newServTimes=[],[],[]		#details of processes added during the run of SPN

	toDo = list(processes)		#generate a copy of the list of processes to deal with
	numProcesses=len(toDo)	#record initial number of processes

	executionPattern=[]			#records pattern of execution as list of entries: [at time t, process, service received]
	clock = 0						#start the clock
	shortest=0					#shortest process will be at start of list when sorted by service times

	while len(toDo) > 0:			#while processes to deal with
		pool=[]							#current pool of processes arrived and competing for processor
		serviceNeeds=[]					#service needs of pool processes
		for arrival, service, process in toDo:			#for each toDo process
			if arrival<=clock:							#if it has arrived
				serviceNeeds.append(service)				#record its service need	
				pool.append([arrival, service, process])		#add it to the pool

		serviceNeeds.sort()										#sort service needs
		pool.sort(key=getService)								#sort pool by service times

		if len(pool)>0:						#process waiting
			arrival,service,process=pool[shortest]				#get shortest process details
			clock = clock + service							#count time passed for its execution
			executionPattern.append([clock, process, service])	#store execution info as [at time t, process name, time used]
			toDo.remove([arrival, service, process])			#remove it from list of processes to do
		else:								#no process waiting but more to do
			clock+=1							#move time on

		if addData=="y":
			newData = my_input("New data for SPN at time "+str(clock)+" (y/[n])? ")	#does user want to add new data?
			if newData == "y":						#if so gather new data at time on clock
				numNewProcs, newProcNames, newArrTimes, newServTimes, toDo, newToDo =\
					getNewData(clock, numProcesses, newProcNames, newArrTimes, newServTimes, toDo) 
				numProcesses+=numNewProcs	#update number of processes

	#return total time used, pattern of execution, and, for processes added, number, names, arrival times, and service times
	return clock, executionPattern, numNewProcs, newProcNames, newArrTimes, newServTimes
	
#### Round Robin ####
def RR(processes,quantum):
	"Simulate Round Robin algorithm"

	print("\n\n ************** Round robin with time slice = ", quantum," **************\n")

	#will user want to add new data on the fly?
	addData="n"												#assume not
	addData = my_input("Will you want to add data on the fly (y/[n])? ")	#but ask 

	numNewProcs	=0									#number of processes added during the run of RR
	newProcNames, newArrTimes, newServTimes=[],[],[]		#details of processes added during the run of RR

	allProcesses=processes		#keep copy of list of processes
	toDo = list(processes)		#generate a copy of the list of processes to deal with
	numProcesses=len(toDo)	#record initial number of processes

	toDo.sort(key=getArrival)		#sort list by arrival times to form a queue

	executionPattern=[]			#records pattern of execution as list of entries: [at time t, process, service received]
	clock = 0						#start the clock
	head=0						#next process will be at start of queue when sorted by arrival times

	queue=[]						#current queue of processes arrived and competing for processor
	arrivals=[]					#arrival and service times data of queue processes for display

	#initialise the queue
	for arr, serv, proc in toDo:			#for each toDo process' arrival time, service requirement, & process name
		if arr<=clock: 						#if it has arrived
			arrivals.append([arr, serv])			#record its arrival and service times
			queue.append([arr, serv, proc])		#add it to the queue

		arrivals.sort()										#sort arrival and service times
		queue.sort(key=getArrival)							#sort queue by arrival times

	for p in queue:		#for every process already in the queue
		toDo.remove(p)		#remove it from the toDo list

	while len(queue)>0 or len(toDo)>0:			#while processes waiting to run or still to join queue
		service=0						#assume no service require

		if len(queue)>0:							#if processes waiting
			arrival,service,process=queue[head]			#get next process details
			slice=quantum							#allocate slice
			while slice > 0 and service > 0:				#run process for slice or less
				slice=slice-1								#1 time unit used
				service = service - 1						#reduce remaining service time by 1

			clock = clock + (quantum-slice)		#update clock by time used
			executionPattern.append([clock, process, quantum-slice])	#store usage info as [at time t, process name, time used]
			del queue[head]					#remove it from queue of processes
			del arrivals[head]					#remove its data from arrivals list	
		else:							#no processes in queue but more to do
			clock+=1									#move time on

		if addData=="y":
			newData = my_input("New data for RR at time "+str(clock)+" (y/[n])? ")	#does user want to add new data?
			if newData == "y":						#if so gather new data at time on clock
				numNewProcs, newProcNames, newArrTimes, newServTimes, toDo, newToDo =\
					getNewData(clock, numProcesses, newProcNames, newArrTimes, newServTimes, toDo) 
				numProcesses+=numNewProcs		#update number of processes
				allProcesses=allProcesses+newToDo	#update list of all processes

		#add any new arrivals to the queue
		for arr, serv, proc in toDo:			#for each toDo process
			if arr<=clock: 						#if it has arrived
				arrivals.append([arr, serv])			#record its arrival and service remaining times
				queue.append([arr, serv, proc])			#add it to the queue

		#remove them from the toDo list
		for p in queue:			#for each process in the queue
			if p in toDo:				#if it is in the toDo list
				toDo.remove(p)			#remove it

		#put unfinished process at back of the queue 
		if service > 0:								#quantum used, more to do
			arrivals.append([arrival, service])				#add its data to the arrivals list
			queue.append([arrival,service,process])		#add it to the back of the queue
		
	#return total time used, pattern of execution, and, for processes added, number, names, arrival times, and service times
	return clock, executionPattern, numNewProcs, newProcNames, newArrTimes, newServTimes

####HRRN####
def HRRN(processes):
	"Simulate Highest Response Ratio Next algorithm"

	print("\n\n ************** Highest Response Ratio Next ************** \n")

	#will user want to add new data on the fly?
	addData="n"												#assume not
	addData = my_input("Will you want to add data on the fly (y/[n])? ")	#but ask 

	numNewProcs	=0									#number of processes added during the run of HRRN
	newProcNames, newArrTimes, newServTimes=[],[],[]		#details of processes added during the run of HRRN

	toDo = list(processes)		#generate a copy of the list of processes to deal with
	numProcesses=len(toDo)	#record initial number of processes

	clock = 0				#start the clock
	executionPattern=[]	#to hold information on sequence of execution as [at time t, process name, time used]
	initialRatio=1.0		#initial response ratio is always 1.0

	arrivalTime=0			#index of arrival time for a process in the pool
	serviceTime=1			#index of service time for a process in the pool
	name=2				#index of process name for a process in the pool
	ratioIndex=3			#index of current response ratio for a process in the pool
	HRRp=0				#index of HRRatio process when pool sorted by HRRatio

	#initialise the pool
	pool=[]				#list of processes waiting
	toRemove=[]			#processes to be removed from to Do list
	for arr, serv, proc in toDo:				#for each toDo process
		if arr<=clock:							#if it has arrived add it to the pool 
			pool.append([arr, serv, proc, initialRatio])	#as arrival time, service time, name  current response ratio
			toRemove.append([arr, serv, proc])		#record it for removal from toDo list

	for rp in toRemove:		#for each process to be removed from the toDo list
		toDo.remove(rp)			#remove it

	while len(pool)>0 or len(toDo)>0:		#while there are processes waiting in the pool or to do
		if len(pool)>0:						#there is a process waiting
			pool.sort(key=getRatio, reverse=True)		#sort list with highest response ratios first
			ratios=[]									#initialise list of ratios for display
			for i in range(len(pool)):					#for each process in pool
				ratios.append(pool[i][ratioIndex])			#record its ratio

			#process with highest response ratio will be first in the pool list
			process = pool[HRRp][name]			#get its process name
			arrival = pool[HRRp][arrivalTime]		#get its arrival time
			service = pool[HRRp][serviceTime]	#get its service time

			clock = clock + service							#count time passed for its execution
			del pool[HRRp]								#remove it from the pool
			executionPattern.append([clock, process, service])	#store execution info as [at time t, process name, time used]
		else:
			clock+=1				#move time on

		if addData=="y":
			newData = my_input("New data for HRRN at time "+str(clock)+" (y/[n])? ")	#does user want to add new data?
			if newData == "y":						#if so gather new data at time on clock
				numNewProcs, newProcNames, newArrTimes, newServTimes, toDo, newToDo =\
					getNewData(clock, numProcesses, newProcNames, newArrTimes, newServTimes, toDo) 
				numProcesses+=numNewProcs	#update number of processes

		toRemove=[]					#processes to be added to pool and removed from to Do list
		for arr, serv, proc in toDo:		#for each process left to do
			if arr<=clock:					#if it has arrived
				pool.append([arr, serv, proc, initialRatio])		#add it to the pool
				toRemove.append([arr, serv, proc])			#record it in the list of processes to remove from toDo list

		for rp in toRemove:		#for each process to remove from the toDo list
			toDo.remove(rp)			#remove it 

		for i in range(len(pool)):		#for each process in the pool
			ratio = round((pool[i][serviceTime] + (clock - pool[i][arrivalTime])) / pool[i][serviceTime],2)	#recalculate it ratio and
			pool[i][ratioIndex]=ratio														#update it in the pool entry

	#return total time used, pattern of execution, and, for processes added, number, names, arrival times, and service times
	return clock, executionPattern, numNewProcs, newProcNames, newArrTimes, newServTimes

####SRT####
def SRT(processes):
	"Shortest Remaining Time"
	print("\n\n ************** Shortest Remaining Time ************** \n")

	#will user want to add new data on the fly?
	addData="n"												#assume not
	addData = my_input("Will you want to add data on the fly (y/[n])? ")	#but ask 

	numNewProcs	=0									#number of processes added during the run of SRT
	newProcNames, newArrTimes, newServTimes=[],[],[]		#details of processes added during the run of SRT

	allProcesses=processes		#keep copy of list of processes
	toDo = list(processes)		#generate a copy of the list of processes to deal with
	numProcesses=len(toDo)	#record initial number of processes

	arrivalTime=0			#index of arrival time for a process in the pool
	serviceTime=1			#index of service time for a process in the pool
	name=2				#index of name of process in the pool
	SRTp=0				#index of SRT process when pool is sorted by remaining service time

	executionPattern=[]	#to hold information on sequence of execution as [at time t, process name, time used]
	clock = 0				#start the clock

	toRemove=[]			#processes to remove from the toDo list
	pool=[]				#processes in the waiting pool
	#populate initial pool
	for arrival, service, proc in toDo:				#for each toDo process
		if arrival<=clock:								#if it has arrived
			pool.append([arrival, service, proc])				#add it to the pool
			toRemove.append([arrival, service, proc])			#record it for removal from toDo list

	for rp in toRemove:		#for each process to be removed from the toDo list
		toDo.remove(rp)			#remove it

	while len(pool)>0 or len(toDo)>0:		#while there are processes waiting in the pool or to do later
		if len(pool)>0:						#if processes waiting
			pool.sort(key=getService)			#sort pool by service times remaining
			remaining=[]						#initialise remaining service times of processes in the pool
			for p in pool:						#copy processes' service times for display later
				remaining.append(p[serviceTime])	#one entry for each process in pool: [service remaining]

			process=pool[SRTp]		#get Shortest Remaining Time process

			time=0							#amount of time used by the SRT process this time around
			noNewArrival = True				#initially 'no new arrivals' in pool
			while noNewArrival and process[serviceTime] > 0:	#run process for service time or perhaps less if a new arrival
				time = time + 1								#1 time unit used
				clock = clock + 1								#update clock by time passed
				process[serviceTime] = process[serviceTime] - 1		#reduce remaining service time by 1

				if addData=="y":
					newData = my_input("New data for SRT at time "+str(clock)+" (y/[n])? ")	#does user want to add new data?
					if newData == "y":						#if so gather new data at time on clock
						numNewProcs, newProcNames, newArrTimes, newServTimes, toDo, newToDo =\
							getNewData(clock, numProcesses, newProcNames, newArrTimes, newServTimes, toDo) 
						numProcesses+=numNewProcs		#update number of processes
						allProcesses=allProcesses+newToDo	#update list of all processes

				#check for new arrivals during run of current process
				toRemove=[]					#processes to remove from toDo list
				for arrival, service, proc in toDo:				#for each process to do
					if arrival<=clock:							#if it has newly arrived
						pool.append([arrival, service, proc])			#add it to the pool
						noNewArrival = False						#record new arrival so that competition will be re-run
						toRemove.append([arrival, service, proc])		#record it for removal from toDo list

				for rp in toRemove:		#for each process to be removed from the toDo list
					toDo.remove(rp)			#remove it

			executionPattern.append([clock, process[name],time])	#store usage info as [at time t, process name, time used]
			if process[serviceTime] == 0:				#current process has no more to do
				pool.remove(process)									#remove process from pool			
		else:							#no process waiting
			clock+=1						#move time on

			if addData=="y":
				newData = my_input("New data for SRT at time "+str(clock)+" (y/[n])? ")	#does user want to add new data?
				if newData == "y":						#if so gather new data at time on clock
					numNewProcs, newProcNames, newArrTimes, newServTimes, toDo, newToDo =\
						getNewData(clock, numProcesses, newProcNames, newArrTimes, newServTimes, toDo) 
					numProcesses+=numNewProcs		#update number of processes
					allProcesses=allProcesses+newToDo	#update list of all processes

			#check for new arrivals as time has moved on 
			toRemove=[]					#processes to remove from toDo list
			for arrival, service, proc in toDo:				#for each process to do
				if arrival<=clock:							#if it has newly arrived
					pool.append([arrival, service, proc])			#add it to the pool
					toRemove.append([arrival, service, proc])		#record it for removal from toDo list

			for rp in toRemove:		#for each process to be removed from the toDo list
				toDo.remove(rp)			#remove it

	#return total time used, pattern of execution, and, for processes added, number, names, arrival times, and service times
	return clock, executionPattern, numNewProcs, newProcNames, newArrTimes, newServTimes

def showMainMenu(data):
	"Display menu"
	
	print("\n\n1:    Generate Random Data")
	print("2:    Use Default Data")
	print("3:    Enter Your own Data")
	if (data>0):
		print("4:    Run First Come, First Served (FCFS) Scheduling Algorithm")
		print("5:    Run Round Robin (RR) Scheduling Algorithm")
		print("6:    Run Shortest Process Next (SPN) Scheduling Algorithm")
		print("7:    Run Shortest Remaining Time (SRT) Scheduling Algorithm")
		print("8:    Run Highest Response Ratio Next (HRRN) Scheduling Algorithm")
	print("0:    Quit")

	return

#### Main Program ####

#initialise data
numberOfProcesses=0	#initially no data
ans=-1				#guarantee menu loop runs
while ans!=0:
	ans=-1		#guarantee menu loop runs
	if (numberOfProcesses>0):	#if there is data
		maxOption=8				#8 menu items
	else:
		maxOption=3				#just the data generation menu

	while ans<0 or ans>maxOption:	#while no valid choice made
		showMainMenu(numberOfProcesses)		#show the appropriate menu
		ans=getInt("Which action (0 to "+str(maxOption)+")?" ,"Choose an option between 0 and "+str(maxOption))

	if ans==1:	#generate random data
		numberOfProcesses, processNames, arrivalTimes, serviceTimes=makeData(0,0)	#gather data at time 0 where 0 previous processes
		random.seed()
		quantum = random.randint(1,4)		
		my_input("Press <ENTER> to continue")
	elif ans==2:	#Use Default data
		quantum = 2								#time slice for Round Robin
		numberOfProcesses = 5						#How many processes
		processNames = ["p0","p1","p2","p3","p4"]		#process names
		arrivalTimes = [0,2,4,6,8]					#times of arrival
		serviceTimes = [3,6,4,5,2]					#CPU service burst times
		my_input("Press <ENTER> to continue")
	elif ans==3:	#Input user data
		numberOfProcesses, processNames, arrivalTimes, serviceTimes=getData(0,0)	#gather data at time 0 where 0 previous processes
		quantum = getQuantum()
		my_input("Press <ENTER> to continue")
	elif ans==4:	#FCFS
		clock,executionPattern,numProcsAdded, addedProcNames, addedArrTimes, addedServTimes = \
												FCFS(pending)	#run First Come, First Served
		pNames=processNames+addedProcNames
		sTimes=serviceTimes+addedServTimes
		aTimes=arrivalTimes+addedArrTimes
		outputResults(clock,pNames,executionPattern,sTimes,aTimes)	#show results
		my_input("Press <ENTER> to continue")
	elif ans==5:	#RR
		print("Current quantum for Round Robin is: ",quantum)
		change=my_input("Do you want to change it? y/[n]: ")
		if change=="y":
			quantum = getQuantum()
		clock,executionPattern,numProcsAdded, addedProcNames, addedArrTimes, addedServTimes = \
												RR(pending, quantum)	#run Round Robin
		pNames=processNames+addedProcNames
		sTimes=serviceTimes+addedServTimes
		aTimes=arrivalTimes+addedArrTimes
		outputResults(clock,pNames,executionPattern,sTimes,aTimes)	#show results
		my_input("Press <ENTER> to continue")
	elif ans==6:	#SPN
		clock,executionPattern,numProcsAdded, addedProcNames, addedArrTimes, addedServTimes = \
												SPN(pending)	#run Shortest Process next
		pNames=processNames+addedProcNames
		sTimes=serviceTimes+addedServTimes
		aTimes=arrivalTimes+addedArrTimes
		outputResults(clock,pNames,executionPattern,sTimes,aTimes)	#show results
		my_input("Press <ENTER> to continue")
	elif ans==7:	#SRT
		clock,executionPattern,numProcsAdded, addedProcNames, addedArrTimes, addedServTimes = \
												SRT(pending)	#run Shortest remaining Time
		pNames=processNames+addedProcNames
		sTimes=serviceTimes+addedServTimes
		aTimes=arrivalTimes+addedArrTimes
		outputResults(clock,pNames,executionPattern,sTimes,aTimes)	#show results
		my_input("Press <ENTER> to continue")
	elif ans==8: #HRRN
		clock,executionPattern,numProcsAdded, addedProcNames, addedArrTimes, addedServTimes = \
												HRRN(pending)	#run Highest Response ratio next
		pNames=processNames+addedProcNames
		sTimes=serviceTimes+addedServTimes
		aTimes=arrivalTimes+addedArrTimes
		outputResults(clock,pNames,executionPattern,sTimes,aTimes)	#show results
		my_input("Press <ENTER> to continue")
	elif ans==0: #quit
		sure="n"
		sure=my_input("\nThis will quit and lose all the old data. Are you sure? y/[n]")
		if sure!="y":
			ans=-1
		else:
			print("OK, Bye")
			
	if ans!= 0 and (numberOfProcesses>0):
		pending=[]						#initial list of processes to run
		for i in range(numberOfProcesses):	#pending processes:1 entry each: (arrival time, service time, name)
			pending.append([arrivalTimes[i], serviceTimes[i], processNames[i]])	
		pending.sort()						#sort by arrival time - in event of a tie FCFS operates
		showData(pending)
		

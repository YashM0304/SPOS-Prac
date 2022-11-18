 
def findWaitingTime(processes, n, wt):            # Function to find the waiting time for all processes
	rt = [0] * n 
	for i in range(n):                     # Copy the burst time into rt[] 
		rt[i] = processes[i][1] 
	complete = 0
	t = 0
	minm = 999999999
	short = 0
	check = False
	while (complete != n):                                # Process until all processes gets completed
		
		for j in range(n):                             # Find process with minimum remaining time among the processes that arrives till the current time`
			if ((processes[j][2] <= t) and (rt[j] < minm) and rt[j] > 0): 
				minm = rt[j] 
				short = j 
				check = True
		if (check == False): 
			t += 1
			continue	
		rt[short] -= 1              # Reduce remaining time by one 
		minm = rt[short]                  # Update minimum
		if (minm == 0): 
			minm = 999999999
		if (rt[short] == 0):                        # If a process gets completely executed
			complete += 1                   # Increment complete 
			check = False 
			fint = t + 1            # Find finish time of current process 

			wt[short] = (fint - proc[short][1] - proc[short][2])              # Calculate waiting time   

			if (wt[short] < 0): 
				wt[short] = 0
		t += 1            # Increment time 

def findTurnAroundTime(processes, n, wt, tat):          # Function to calculate turn around time
	for i in range(n):                           # Calculating turnaround time 
		tat[i] = processes[i][1] + wt[i] 
 
def findavgTime(processes, n):                  # Function to calculate average waiting and turn-around times.
	wt = [0] * n  
	tat = [0] * n 
  
	findWaitingTime(processes, n, wt)                  # Function to find waiting time of all processes 
	findTurnAroundTime(processes, n, wt, tat)            # Function to find turn around time for all processes

	print("Processes Burst Time	 Waiting", "Time	 Turn-Around Time")                               # Display processes along with all details 
	total_wt = 0
	total_tat = 0
	for i in range(n): 

		total_wt = total_wt + wt[i] 
		total_tat = total_tat + tat[i] 
		print(" ", processes[i][0], "\t\t", processes[i][1], "\t\t", wt[i], "\t\t", tat[i]) 

	print("\nAverage waiting time = %.5f "%(total_wt /n) ) 
	print("Average turn around time = ", total_tat / n) 
	
if __name__ =="__main__":             # Driver code 
	
	proc = [[1, 6, 1], [2, 8, 1],[3, 7, 2], [4, 3, 3] ]       # Process id's 
	n = 4
	findavgTime(proc, n) 
	
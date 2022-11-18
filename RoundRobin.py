
def findWaitingTime(processes, n, bt, wt, quantum):            # Function to find the waiting time for all processes 
	rem_bt = [0] * n

	for i in range(n):            # Copy the burst time into rt[]
		rem_bt[i] = bt[i]
	t = 0                # Current time

	while(1):                     # Keep traversing processes in round robin manner until all of them are not done.
		done = True

		for i in range(n):           # Traverse all processes one by one repeatedly

			if (rem_bt[i] > 0) :               # If burst time of a process is greater than 0 then only need to process further
				done = False       # There is a pending process
				
				if (rem_bt[i] > quantum) :
					t += quantum              # Increase the value of t i.e. shows how much time a process has been processed
					rem_bt[i] -= quantum          # Decrease the burst_time of current process by quantum
				
				else:                       # If burst time is smaller than or equal to quantum. Last cycle for this process 
					t = t + rem_bt[i]                  # Increase the value of t i.e. shows how much time a process has been processed
					wt[i] = t - bt[i]          # Waiting time is current time minus time used by this process 
					rem_bt[i] = 0           # As the process gets fully executed make its remaining burst time = 0
				
		if (done == True):       # If all processes are done
			break
			
def findTurnAroundTime(processes, n, bt, wt, tat):           # Function to calculate turn around time
	for i in range(n):                   # Calculating turnaround time
		tat[i] = bt[i] + wt[i]

def findavgTime(processes, n, bt, quantum):              # Function to calculate average waiting and turn-around times.
	wt = [0] * n
	tat = [0] * n

	findWaitingTime(processes, n, bt, wt, quantum)            # Function to find waiting time of all processes
	findTurnAroundTime(processes, n, bt, wt, tat)         # Function to find turn around time for all processes

	print("Processes Burst Time	 Waiting","Time Turn-Around Time")         # Display processes along with all details
	total_wt = 0
	total_tat = 0
	for i in range(n):

		total_wt = total_wt + wt[i]
		total_tat = total_tat + tat[i]
		print(" ", i + 1, "\t\t", bt[i],
			"\t\t", wt[i], "\t\t", tat[i])

	print("\nAverage waiting time = %.5f "%(total_wt /n) )
	print("Average turn around time = %.5f "% (total_tat / n))
	
if __name__ =="__main__":                          # Driver code
	n = int(input("Enter number of processes : "))              
	proc = list(map(int,input("Enter process id's ").strip().split()))                 	# Process id's
	burst_time = list(map(int,input("Enter burst times of processes: ").strip().split()))     # Burst time of all processes
	quantum = int(input("Enter Quantum Time : "))    # Time quantum
	print(quantum)
	findavgTime(proc, n, burst_time, quantum)


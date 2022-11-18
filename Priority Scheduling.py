def findWaitingTime(bt, n, wt):
	wt[0] = 0
	for i in range(1, n):                              
		wt[i] = bt[i - 1][1]+ wt[i - 1]            # calculating waiting time

def findTurnAroundTime(bt, n, wt, tat):                  # Function to calculate turn around time
	for i in range(n):
		tat[i] = bt[i][1] + wt[i]        # Calculating turnaround time by adding bt[i] + wt[i]

def findavgTime(bt, n):                 # Function to calculate average waiting and average turn-around times.          
	wt = [0] * n
	tat = [0] * n

	findWaitingTime(bt, n, wt)             # call Function to find waiting time of all processes
	findTurnAroundTime(bt, n, wt, tat)          # Function to find turn around time for all processes

	print("\nProcesses   Burst Time   Waiting Time    Turn-Around Time")                     # Display processes along with all details 
	total_wt = 0
	total_tat = 0
	for i in range(n):
		total_wt = total_wt + wt[i]
		total_tat = total_tat + tat[i]
		print(" ", bt[i][0], "\t\t",bt[i][1], "\t\t",wt[i], "\t\t", tat[i])

	print("\nAverage waiting time = %.5f "%(total_wt /n))
	print("Average turn around time = ", total_tat / n)

def priorityScheduling(proc, n):
	proc = sorted(proc, key = lambda proc:proc[2],reverse = False)         # Sort processes by priority
	print("Order in which processes gets executed")
	for i in proc:
		print(i[0], end = " ")
	findavgTime(proc, n)
	
# Driver code
if __name__ =="__main__":
	proc = [[1, 10, 1],[2, 5, 2],[3, 8, 3]]   # process id's in the format [arrival time, burst time, priority]
	n = 3
	priorityScheduling(proc, n)
	
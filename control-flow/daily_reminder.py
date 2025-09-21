task = input("Enter your task: ")
priority = input("Enter the priority (high/medium/low): ")
time_bound = input("Is the task time-bound? (yes/no): ")

match priority:
    case "high":
        reminder = f"The task '{task}' is HIGH priority."
    case "medium":
        reminder = f"The task '{task}' is MEDIUM priority."
    case "low":
        reminder = f"The task '{task}' is LOW priority."
    

if time_bound == "yes":
    print (" this task requires immediate attention today!")
else:
    print ("this task you can Complete it at your convenience.")




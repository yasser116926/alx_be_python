task = input("Enter your task: ")
priority = input("Enter the priority :")
time_bound = input("Is the task time-bound?:")

match priority:
    case "high":
        print("The task '{task}' is HIGH priority.")
    case "medium":
        print("The task '{task}' is MEDIUM priority.")
    case "low":
        print("The task '{task}' is LOW priority.")
    

if time_bound == True:
    print (" this task requires immediate attention today!")
else:
    print ("this task you can Complete it at your convenience.")





task = input("Enter your task: ")
priority = input("Enter the priority (high/medium/low): ").lower()
time_bound = input("Is the task time-bound? (yes/no): ").lower()

match priority:
    case "high":
        reminder = f"The task '{task}' is HIGH priority."
    case "medium":
        reminder = f"The task '{task}' is MEDIUM priority."
    case "low":
        reminder = f"The task '{task}' is LOW priority."
    case _:
        reminder = f"The task '{task}' has an UNKNOWN priority."

if time_bound == "yes":
    reminder += " It requires immediate attention today!"
else:
    reminder += " Complete it at your convenience."

print(reminder)

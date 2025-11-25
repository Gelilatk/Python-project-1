


##############################################################################################



# Fixed class roadmap (you can edit these names)
course_roadmap = [
    "Intro to Python",
    "Intro to SQL",
    "Git & GitHub",
    "Power BI",
    "Advanced SQL",
    "Advanced python"
]

# Each task is stored as a dictionary:
# {"course": "Intro to Python", "status": "current"}
tasks = []

# --- Stage 1: Show the roadmap once at start ---
print("===== CLASS ROADMAP =====")
i = 1
for course in course_roadmap:
    print(str(i) + ") " + course)
    i = i + 1
print("=========================")
print()

# --- Stage 2: To-Do List tied to the roadmap ---
print("Welcome to the Class To-Do List App!")
print("Commands: add, view, delete, exit")
print("- When adding, choose from the course list above.")
print("- Enter course number and status in ONE line, e.g.: 2, current")
print("- Allowed status: done, current, upcoming")
print()

while True:
    command = input("What do you want to do? (add/view/delete/exit): ").strip().lower()

    if command == "add":
        if len(course_roadmap) == 0:
            print("No courses available to add tasks for.")
            print()
        else:
            # Show roadmap again for convenience
            print("Choose a course by number and a status (done/current/upcoming) on ONE line.")
            print("Example: 3, upcoming")
            print("Courses:")
            j = 1
            for course in course_roadmap:
                print(str(j) + ") " + course)
                j = j + 1

            line = input("Enter course#, status: ").strip()
            if "," in line:
                parts = line.split(",", 1)
                course_num_text = parts[0].strip()
                status = parts[1].strip().lower()
            else:
                course_num_text = line
                status = "current"

            if course_num_text.isdigit():
                n = int(course_num_text)
                if n >= 1 and n <= len(course_roadmap):
                    chosen_course = course_roadmap[n - 1]
                else:
                    print("That course number is not on the list.")
                    print()
                    continue
            else:
                print("Please type a valid course number (e.g., 1, 2, 3).")
                print()
                continue

            if status not in ["done", "current", "upcoming"]:
                status = "current"

            task = {"course": chosen_course, "status": status}
            tasks.append(task)
            print("Added task for:", chosen_course, "-", status)
            print()

    elif command == "view":
        if len(tasks) == 0:
            print("No tasks yet. Use 'add' to create one.")
            print()
        else:
            print("----- YOUR TASKS -----")
            k = 1
            for t in tasks:
                print(str(k) + ") [" + t["status"] + "] " + t["course"])
                k = k + 1
            print("----------------------")
            print()

    elif command == "delete":
        if len(tasks) == 0:
            print("Nothing to delete. No tasks yet.")
            print()
        else:
            k = 1
            for t in tasks:
                print(str(k) + ") [" + t["status"] + "] " + t["course"])
                k = k + 1

            choice = input("Type the task number to delete: ").strip()
            if choice.isdigit():
                n = int(choice)
                if n >= 1 and n <= len(tasks):
                    removed_course = tasks[n - 1]["course"]
                    removed_status = tasks[n - 1]["status"]
                    del tasks[n - 1]
                    print("Deleted task:", "[" + removed_status + "] " + removed_course)
                else:
                    print("That number is not on the list.")
            else:
                print("Please type a number like 1 or 2.")
            print()

    elif command == "exit":
        done_count = 0
        current_count = 0
        upcoming_count = 0

        m = 0
        while m < len(tasks):
            s = tasks[m]["status"]
            if s == "done":
                done_count = done_count + 1
            elif s == "current":
                current_count = current_count + 1
            elif s == "upcoming":
                upcoming_count = upcoming_count + 1
            m = m + 1

        print()
        print("Summary by status:")
        print("done:", done_count)
        print("current:", current_count)
        print("upcoming:", upcoming_count)
        print("Goodbye!")
        break

    else:
        print("I didn't understand that. Type: add, view, delete, or exit.")
        print()
















projects = [
    {
        "Project ID": 101,
        "Client Name": "John Doe",
        "Client Email": "john@example.com",
        "Start Time": "2024-02-10",
        "Deadline": "2024-02-15",
        "Payment": 800
    },
    {
        "Project ID": 102,
        "Client Name": "Jane Smith",
        "Client Email": "jane@example.com",
        "Start Time": "2024-02-12",
        "Deadline": "2024-02-18",
        "Payment": 1000
    },
    {
        "Project ID": 103,
        "Client Name": "Alice Johnson",
        "Client Email": "alice@example.com",
        "Start Time": "2024-02-14",
        "Deadline": "2024-02-20",
        "Payment": 1200
    },
    {
        "Project ID": 104,
        "Client Name": "Bob Brown",
        "Client Email": "bob@example.com",
        "Start Time": "2024-02-16",
        "Deadline": "2024-02-22",
        "Payment": 900
    }
]

def calculate_days(start_time, deadline):
    start_year, start_month, start_day = map(int, start_time.split('-'))
    end_year, end_month, end_day = map(int, deadline.split('-'))

    start_total_days = start_year * 365 + start_month * 30 + start_day
    end_total_days = end_year * 365 + end_month * 30 + end_day

    return end_total_days - start_total_days

def insertion_sort(projects):
    for i in range(1, len(projects)):
        key = projects[i]
        key_days = calculate_days(key["Start Time"], key["Deadline"])
        key_hours = key_days * 24
        key_payment_per_hour = key["Payment"] / key_hours
        j = i - 1
        while j >= 0:
            days = calculate_days(projects[j]["Start Time"], projects[j]["Deadline"])
            hours = days * 24
            payment_per_hour = projects[j]["Payment"] / hours
            if key_payment_per_hour < payment_per_hour:
                break
            projects[j+1] = projects[j]
            j -= 1
        projects[j+1] = key
    return projects

sortedProjects = insertion_sort(projects)

print("Sorted Project Requests:")
for project in sortedProjects:
    print(f"Project ID: {project['Project ID']}")

# Question 2 : binary search on the sorted list of projects

def sort_by_project_id(projects):
    return sorted(projects, key=lambda x: x["Project ID"])

def binary_search(projects, project_id):
    low = 0
    high = len(projects) - 1
    while low <= high:
        mid = (low + high) // 2
        # print(f"mid: {mid}")
        if projects[mid]["Project ID"] == project_id:
            # print(projects[mid]["Project ID"])
            return projects[mid]
        elif projects[mid]["Project ID"] < project_id:
            # print(projects[mid]["Project ID"])
            low = mid + 1
        else:
            high = mid - 1
    return None

project_id = 103
sortedProjectsByID = sort_by_project_id(sortedProjects)

project = binary_search(sortedProjectsByID, project_id)

if project:
    for i in project:
        print(f"{i}: {project[i]}")
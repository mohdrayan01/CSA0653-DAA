# 192424059 - Assignment CO5 - AT1

# Q1: Job Scheduling using Backtracking
# -------------------------------------
# Problem:
# Assign jobs to employees such that:
# 1. Every job is assigned to exactly one employee.
# 2. No employee handles more than one job.
# 3. All assignments satisfy the given constraints.
#
# Technique Used:
# Backtracking (Constraint Satisfaction Problem - CSP)
#
# Time Complexity:
# O(n!) in the worst case
#
# Space Complexity:
# O(n) for recursion stack and assignments

print("Question 1 Output:\n")
# Function to check whether assigning
# an employee to a job is valid
def is_safe(job, employee, assignment):
    # An employee cannot be assigned
    # more than one job
    if employee in assignment.values():
        return False
    return True
# Recursive Backtracking Function
def solve(job_index, jobs, employees, assignment):
    # Base Case:
    # All jobs have been assigned
    if job_index == len(jobs):
        return True
    # Current Job
    job = jobs[job_index]
    # Try assigning every employee
    for employee in employees:
        # Check if assignment is valid
        if is_safe(job, employee, assignment):
            # Assign employee to job
            assignment[job] = employee
            # Recursively assign next job
            if solve(job_index + 1, jobs, employees, assignment):
                return True
            # Backtrack if assignment fails
            del assignment[job]
    return False
# Sample Input
jobs = ["J1", "J2", "J3"]
employees = ["E1", "E2", "E3"]
assignment = {}
# Solve the scheduling problem
if solve(0, jobs, employees, assignment):
    print("Job Assignment:")
    for job, employee in assignment.items():
        print(job, "->", employee)
else:
    print("No feasible assignment found")
print("\n")


# Q2: Exam Timetabling using Graph Coloring
# -----------------------------------------
# Problem:
# Schedule exams into available time slots such that:
# 1. No two conflicting exams are scheduled
#    in the same time slot.
# 2. Minimize scheduling conflicts.
#
# Graph Representation:
# Each exam = Vertex
# Edge between exams = Student conflict
#
# Technique Used:
# Graph Coloring using Backtracking
#
# Time Complexity:
# O(m^n)
# where:
# n = number of exams
# m = number of available time slots
#
# Space Complexity:
# O(n)

print("Question 2 Output:\n")
# Function to check whether a color
# (time slot) can be assigned
def is_safe(v, graph, colors, c):
    # Check all adjacent vertices
    for i in range(len(graph)):
        # If adjacent exam already
        # has same time slot
        if graph[v][i] == 1 and colors[i] == c:
            return False
    return True
# Recursive Graph Coloring Function
def graph_coloring(graph, m, colors, v):
    # Base Case:
    # All exams have been assigned slots
    if v == len(graph):
        return True
    # Try each available time slot
    for c in range(1, m + 1):
        # Check if assignment is safe
        if is_safe(v, graph, colors, c):
            # Assign time slot
            colors[v] = c
            # Recur for next exam
            if graph_coloring(graph, m, colors, v + 1):
                return True
            # Backtrack if needed
            colors[v] = 0
    return False
# Number of Exams
n = 4
# Conflict Graph (Adjacency Matrix)
# 1 indicates conflict between exams
graph = [
    [0, 1, 1, 0],
    [1, 0, 1, 1],
    [1, 1, 0, 1],
    [0, 1, 1, 0]
]
# Number of available time slots
m = 3
# Store assigned slots
colors = [0] * n
# Solve Timetabling Problem
if graph_coloring(graph, m, colors, 0):
    print("Exam Timetable:")
    for i in range(n):
        print("Exam", i + 1, "-> Time Slot", colors[i])
else:
    print("No valid timetable possible")
print("\n")
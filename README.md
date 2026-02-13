# First Laboratory
Python Calculator
# Second Labaratory
1. Which approach demonstrates true parallelism in Python? Explain.

Ans: Multiprocessing shows the real essence of parallelism in Python coding. This is due to the fact that each process runs independently in its own space and can operate on another core at the same time. Unlike threads, processes do not risk suffering from the so-called Global Interpreter Lock prevalent in Python, and this enables our grade calculations to be performed concurrently when the system is viewed from a CPU perspective. 

2. Compare execution times between multithreading and multiprocessing. 

Ans: As indicated by the accessible results, the execution rate of multi-threading is significantly quicker than that of multi-processing when managing this activity. The execution time taken by multi-threading is merely 0.001 seconds, while that taken by multi-processing is 0.228 seconds, simply due to greater overheads existing in multi-processing, such as more memory usage, etc. The GWA calculation process is quite simple, so multi-threading advantages prevail.

3. Can Python handle true parallelism using threads? Why or why not? 

Ans: Python threads do not really provide a facility for parallel processing for CPU-intensive tasks due to the Global Interpreter Lock. Moreover, the lock ensures that no more than one thread executes Python bytecodes at any time; therefore, even if the underlying system has multiple processors or cores, due to the Global Interpreter Lock, the threads will be scheduled in round-robin fashion. This feature is beneficial for I/O operations but can prove to be very inefficient for CPU-intensive calculations.


4. What happens if you input a large number of grades (e.g., 1000)? Which method is faster and why? 

Ans: However, when dealing with a large set of values, like 1000, multiprocessing will make the program faster if it's CPU-bound. This is because, even if the creation of processes is costly in terms of execution speed, it's faster than dealing with a large set of values when it comes to the count of computations that can be run in parallel compared to the count of CPU cores available. Creating 1000 threads in the program might actually lead to degradation of its performance due to context switches and GIL restrictions.

5. Which method is better for CPU-bound tasks and which for I/O-bound tasks? 

Ans: Multiprocessing has an efficient handling mechanism for CPU-intensive tasks, as it makes better use of CPU performance and does not restrict performance through GIL. On the contrary, multithreading will perform much better in handling tasks that are associated with I/O operations, as the thread can execute when it is waiting for input or data.

6. How did your group apply creative coding or algorithmic solutions in this lab? 

Ans: Our group demonstrated creativity by designing the code in a way that the input, computation, and timing aspects are organized well, making the program easy to read and understand. We also enhanced the way the program displays the results by indicating whether the result was obtained from threads or processes, in addition to the use of loops and ability to dynamically create threads and processes instead of hardcoding the values, which would make the program easy to scale if handling more grades.

# Third Labaratory
1. Differentiate Task and Data Parallelism. Identify which part of the lab
demonstrates each and justify the workload division.

Ans: Data Parallelism:
Definition: The same task is applied to different pieces of data simultaneously.
Example in lab: 
with ProcessPoolExecutor() as executor:
    results = list(executor.map(compute_payroll, EMPLOYEES))

Justification of workload division:
Each employee’s payroll is computed independently. Each process takes one employee, calculates the deductions, and returns the result. The work is divided based on the dataset (employees).

Task Parallelism:
Definition: Different tasks are executed simultaneously, often on the same data.

Example in lab:
future_sss = executor.submit(compute_sss, salary)
future_philhealth = executor.submit(compute_philhealth, salary)
future_pagibig = executor.submit(compute_pagibig, salary)
future_tax = executor.submit(compute_tax, salary)

Justification of workload division:
Each deduction computation (SSS, PhilHealth, Pag-IBIG, Tax) is independent and can run concurrently. The work is divided based on tasks/functions, not the dataset.

2. Explain how concurrent.futures managed execution, including submit(),
map(), and Future objects. Discuss the purpose of with when creating an
Executor.

Ans: Executor Objects:
ProcessPoolExecutor() and ThreadPoolExecutor() manage a pool of worker processes or threads. They handle scheduling, execution, and returning results.

submit() Method:
Schedules a single task for execution.
Returns a Future object, which represents a pending result.
Example:
future_sss = executor.submit(compute_sss, salary)
sss = future_sss.result()

map() Method:
Schedules the same function on multiple data items at once.
Returns an iterator of results.
Example:
results = list(executor.map(compute_payroll, EMPLOYEES))

Future Objects:
Represent a task that may not be completed yet.
.result() blocks until the computation is finished and retrieves the result.

Purpose of with Statement:
Automatically manages resource allocation for the executor.
Ensures that all threads or processes are properly cleaned up after use.
Equivalent to:
executor = ThreadPoolExecutor()
try:
    # do work
finally:
    executor.shutdown()

3. Analyze ThreadPoolExecutor execution in relation to the GIL and CPU cores. Did
true parallelism occur?

Ans: GIL (Global Interpreter Lock):
Python threads cannot execute Python bytecode in true parallel on multiple CPU cores because of the GIL.
ThreadPoolExecutor is best for I/O-bound tasks (like network calls, file operations), not CPU-heavy tasks.

In task parallelism code:
Deduction computations are lightweight CPU-bound tasks.
Threads may run concurrently, but true CPU parallelism did not occur. They were interleaved by the Python interpreter, not executed simultaneously on multiple cores.

In contrast, ProcessPoolExecutor:
Uses separate processes, each with its own Python interpreter.
True parallelism occurs, fully utilizing multiple CPU cores for data parallel tasks like payroll computation.

4. Explain why ProcessPoolExecutor enables true parallelism, including memory
space separation and GIL behavior.

Ans:ProcessPoolExecutor enables true parallelism because it creates separate processes instead of threads. Each process runs in its own memory space and has its own Python interpreter, which means each one also has its own Global Interpreter Lock (GIL). Since the GIL only restricts threads within the same process, using multiple processes allows the program to fully utilize multiple CPU cores at the same time. In our Data_Parallelism.py file, each employee’s payroll computation runs independently in separate processes, which makes true parallel execution possible, especially for CPU-bound tasks like salary calculations.

5. Evaluate scalability if the system increases from 5 to 10,000 employees. Which
approach scales better and why?

Ans:If the system increases from 5 to 10,000 employees, Data Parallelism using ProcessPoolExecutor scales much better. This is because the payroll computation for each employee is independent, so the workload can be divided efficiently across multiple CPU cores. As the number of employees grows, processes can distribute the tasks and process them concurrently. In contrast, Task Parallelism only parallelizes deduction types for one employee at a time. That approach does not significantly improve performance when the dataset becomes very large, so it is not ideal for large-scale payroll systems.

6. Provide a real-world payroll system example. Indicate where Task Parallelism and
Data Parallelism would be applied, and which executor you would use.

Ans:In a real-world payroll system, Task Parallelism can be applied when computing different salary components for a single employee, such as government deductions, company benefits, bonuses, and taxes simultaneously. In this case, ThreadPoolExecutor may be used, especially if some computations involve database or API calls (I/O-bound tasks). On the other hand, Data Parallelism would be used when processing payroll for thousands of employees at once, since each employee’s payroll is independent. For this scenario, ProcessPoolExecutor is more appropriate because it allows true parallelism across CPU cores and handles large-scale computations more efficiently.

# python-calculator--act1
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

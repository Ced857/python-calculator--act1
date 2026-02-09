#Multiprocessing Snippet

from multiprocessing import Process
import time

def compute_gwa_mp(grades):

    gwa = sum(grades) / len(grades)
    
    print(f"[Process] Calculated GWA: {gwa}")

if __name__ == "__main__":
    grades_list = [] # Replace with user input

    for i in range(4):
        grades = int(input("Enter grades: "))
        grades_list.append(grades)

    time_start = time.perf_counter()
        
    processes = []

    for grade in grades_list:

        p = Process(target=compute_gwa_mp, args=([grade],))
        
        processes.append(p)
        
        p.start()

    for p in processes:
        p.join()

    time_end = time.perf_counter()

    execution_time = time_end - time_start

    print(f'Execution time {execution_time}')
#Multithreading Snippet
import threading
import time

def compute_gwa(grades):
    gwa = sum(grades) / len(grades)
    
    print(f"[Thread] Calculated GWA: {gwa}")

if __name__ == "__main__":
    grades_list = []

    for i in range(4):
        grades = int(input("Enter grades: "))
        
        grades_list.append(grades)

    time_start = time.perf_counter()

    threads = []

    for grade in grades_list:
        t = threading.Thread(target=compute_gwa, args=([grade],))
        
        threads.append(t)
        
        t.start()

    for t in threads:

        t.join()

    time_end = time.perf_counter()

    execution_time = time_end - time_start

    print(f'Execution time: {execution_time}')
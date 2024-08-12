import sys
import time
import concurrent.futures
from datetime import datetime

def thread_something():
    import os
    os.system(f'nc 127.0.0.1 4444 <<< "{datetime.now()}"')


def loading_bar(iterations, total):
    # Define the length of the loading bar
    bar_length = 50
    # Calculate the progress ratio
    progress = iterations / total
    # Calculate the number of characters to represent the progress
    bar = '=' * int(bar_length * progress)
    # Add spaces to fill the rest of the bar
    bar += ' ' * (bar_length - len(bar))
    # Print the loading bar
    sys.stdout.write(f'\r[{bar}] {int(progress * 100)}%')
    sys.stdout.flush()

# Example usage

pool = concurrent.futures.ThreadPoolExecutor(max_workers=10)
tasks = 22
current_url_index_pos = 0
while current_url_index_pos <= tasks-1:
    pool.submit(thread_something)
    loading_bar(current_url_index_pos, tasks)
    current_url_index_pos+=1

total_iterations = 3
for i in range(total_iterations + 1):
    loading_bar(i, total_iterations)
    # Simulate some work being done
    time.sleep(0.1)

print("\nLoading complete!")

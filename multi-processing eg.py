import multiprocessing

# Function to be executed by each core
def core_function(core_id):
   print("Executing task on core", core_id)

# Get the number of CPU cores
num_cores = multiprocessing.cpu_count()

# Create a process pool with all CPU cores
pool = multiprocessing.Pool(processes=num_cores)

# Submit tasks to the process pool
for core_id in range(num_cores):
   pool.apply_async(core_function, args=(core_id,))

# Close the pool and wait for all tasks to complete
pool.close()
pool.join()

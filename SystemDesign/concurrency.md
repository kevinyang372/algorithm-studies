# Concurrency

## Type of Problems
### I/O Bound
I/O Bound type problems are caused by slow input/output (I/O) from external resources. One example of it is downloading multiple contents
from internet: as the downloading is much smaller than CPU processes, this could cause the CPU to constantly wait for downloading tasks to
complete as described in the graph below:
![image](https://user-images.githubusercontent.com/30107576/93652006-5ac72f00-f9c8-11ea-8fd9-3be6b10642e8.png)

### CPU Bound
CPU Bound type problems are caused by slow CPU operations. This usually happens when the computational task is huge compared to the resources CPU has
![image](https://user-images.githubusercontent.com/30107576/93652136-d032ff80-f9c8-11ea-874c-5b492c9a902b.png)

## Type of Solutions
- Pre-emptive multitasking:
  - The operation system decides when to switch tasks
  - Only requires one CPU / core
- Cooperative multitasking:
  - The task decides when to give up on control
  - Only requires one CPU / core
- Multiprocessing:
  - The processes all run at the same time on different processors
  - Requires many CPUs / cores

## Pre-emptive Multitasking
In Python, the library that uses the pre-emptive multitasking is `threading`. It works by allowing users to create multiple threads for the tasks and 
allow the processors to switch between them
```Python
import concurrent.futures
import requests
import threading
import time

# threading.local makes sure that the data in process is thread-safe
thread_local = threading.local()

# create an individual session for each thread
def get_session():
  if not hasattr(thread_local, "session"):
    thread_local.session = requests.Session()
  return thread_local.session

def download_site(url):
  session = get_session()
  with session.get(url) as response:
    print(f"Read {len(response.content)} from {url}")

def download_all_sites(sites):
  # ThreadPoolExecutor = Thread + Pool + Executor
  # Pool: Create a pool of threads. Each of which can run concurrently
  # Executor: Controls how and when each of the threads in the pool will run
  with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    executor.map(download_site, sites)
```

Note that creating too many threads could slow down execution as creating and deleting threads also takes time.

**Race Conditions**\
When using the multitasking method, it is important to avoid the race conditions, which happens because:
- The operation system is in control of when a thread runs and when it gets swapped for another thread
- If the data you are modifying is not thread-safe, some threads that are modifying it could have stale data
- This will cause error as the state of the data is inconsistent on each thread

**Why it works?**\
The pre-emptive multitasking method works for I/O Bound problems as it allows the operator to switch between threads and thus overlap the waiting time of the 
I/O processes.

However, for CPU Bound problems, pre-emnptive Multitasking will not help as we are still one CPU and switching threads will not increase the computational power available

## Cooperative Multitasking
The library that adapts cooperative multitasking is `asyncio`. `asyncio` introduces event loop into the execution. \
The event loop has the following attributes: 
- Controls how and when each task gets run
- In the simplified version, events have two states: ready and waiting (for some external task to finish).
- A running task has full control until it hands the control back to the event loop.

The event loop is triggered when a function is marked with `async`. The `await` keyword is used to indicate that the task will take a long time and thus hands the control
back to the event loop

```Python
import asyncio
import time
import aiohttp

async def download_site(session, url):
  async with session.get(url) as response:
    print(f"Read {response.content_length} from {url}")

async def download_all_sites(sites):
  # since everything is running on the same thread, we could use one session safely
  async with aiohttp.ClientSession() as session:
    tasks = []
    for url in sites:
      # creates a list of tasks to run
      task = asyncio.ensure_future(download_site(session, url))
      tasks.append(task)
    # keeps session alive until all tasks are completed
    await asyncio.gather(*tasks, return_exception=True)

asyncio.get_event_loop().run_until_complete(download_all_sites(sites))
```
**Why it works?**
The cooperative multitasking method as it creates the event loop allowing tasks that will take a long time to give their control to run other tasks before they finish.

However, same with the pre-emptive multitasking, this will not work on CPU Bound problems.

## Multiprocessing
Multiprocessing works by simply allow Python to use multiple cores in the system and run each task on a separate computational resource.

```Python
import requests
import multiprocessing
import time

session = None

def set_global_session():
  global session
  if not session:
    session = requests.Session()
    
def download_site(url):
  with session.get(url) as response:
    name = multiprocessing.current_process().name
    print(f"{name}:Read {len(response.content)} from {url}")

def download_all_sites(sites):
  # each process has its own memory space
  # the initializer creates one session for each process
  with multiprocessing.Pool(initializer=set_global_session) as pool:
    pool.map(download_site, sites)
```

**Why it works?**
The multiprocessing method works for both I/O Bound and CPU Bound problems as it allows more computation resource to run each task in parallel.

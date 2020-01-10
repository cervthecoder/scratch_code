import concurrent.futures as cf
#import multiprocessing as mp
import time

start = time.perf_counter()


def do_something(seconds):
    print(f'Sleeping in {seconds} second(s)...')
    time.sleep(seconds)
    return('Done sleeping...')

def main():

    with cf.ProcessPoolExecutor() as executor:
        results = [executor.submit(do_something, 1) for _ in range(10)]

    for f in cf.as_completed(results):
        print(f.result())
        


    """start = time.perf_counter()

    p1 = mp.Process( target=do_something)
    p2 = mp.Process( target=do_something)

    p1.start()
    p2.start()

    p1.join()
    p2.join() # run processes and then the rest

    finish = time.perf_counter()
    print(f'finished in {round(finish - start, 2)} second(s)')"""
# this code contains easy example of multi processing
    """for _ in range(5):
        p = mp.Process(target=do_something)
        p.start()
    for process in processes:
        process.join()"""






if __name__ == '__main__':
        main()    


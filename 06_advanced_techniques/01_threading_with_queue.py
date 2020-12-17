import queue
import threading

"""
process
- 프로그램 처리 단위로 개별 메모리 영역을 가짐

thread
- 단일 프로세스에 작업 처리자. 동일 프로세스 내 쓰레드들은 동일 메모리 접근
- 멀티 쓰레딩 작업시 락을 회피하여야 함 -> 락 관리를 위해 Queue사용

"""



q = queue.Queue()

def worker(num):
    while True:
        item = q.get()
        if item is None:
            break
        print("thread {0} : completed {1}".format(num+1, item))
        q.task_done()

if __name__ == "__main__":
    num_worker_threads = 5
    threads = []
    for i in range(num_worker_threads):
        t = threading.Thread(target=worker, args=(i,))
        t.start()
        threads.append(t)

    for item in range(20):
        q.put(item)
    
    # block until all work ended
    q.join()

    for i in range(num_worker_threads):
        q.put(None)
    for t in threads:
        t.join()
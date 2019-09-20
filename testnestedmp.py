import multiprocessing as mp
import time
import numpy as np



def g(arr, i, j,q):
	
	arr[j,i] = i+j
	q.put(arr[j,i])
	
if __name__ == '__main__':
	q = mp.Queue()
	mps = []
	arr = np.zeros((8,8))
	lock = mp.Lock()
	for j in range(arr.shape[0]):
		lock.acquire()
		for i in range(arr.shape[1]):
			m_p = mp.Process(target = g, args = (arr, i, j,q))
			mps.append(m_p)
			m_p.start()
		lock.release()
	# for i in range(arr.shape[1]):
	# 	m_p = mp.Process(target = g, args = (arr, i, 1, q))
	# 	mps.append(m_p)
	# 	m_p.start()

	for m_p in mps:
		m_p.join()
	for j in range(arr.shape[0]):
		for i in range(arr.shape[1]):
			print(q.get())
	# print(arr)


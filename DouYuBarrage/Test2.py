from multiprocessing import Process, Queue

if __name__ == '__main__':
    q = Queue(2)
    from DouYuBarrage.Test import product
    from DouYuBarrage.Test import customer
    pw = Process(target=product, args=(q,))
    pr = Process(target=customer, args=(q,))
    pw.start()
    pr.start()
    pw.join()

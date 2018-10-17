#coding:utf-8

# 管道可以双向通信，队列只可以单向通信(一个进程只能发数据，另一个只能收数据)
import multiprocessing
import os


def func(conn):  # conn管道类型
    conn.send(["a", "b", "c", "d", "e"])  # 发送的数据
    print('child process', os.getpid(), conn.recv())  # 收到的数据
    conn.close()  # 关闭


if __name__ == "__main__":
    conn_a, conn_b = multiprocessing.Pipe()  # 创建一个管道，两个口
    # print(id(conn_a),id(conn_b))
    # print(type(conn_a), type(conn_b)) #multiprocessing.connection.PipeConnection类型
    p = multiprocessing.Process(target=func, args=(conn_a,))
    p.start()
    conn_b.send([1, 2, 3, 4, 5, 6, 7])
    print('main process', os.getpid(), conn_b.recv())
    p.join()

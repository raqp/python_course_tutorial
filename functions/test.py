import gevent


def my_func_1():
    while True:
        print("Hello")
        gevent.sleep(1)


def my_func_2():
    while True:
        print("John")
        gevent.sleep(3)


thread = [
    gevent.spawn(my_func_1),
    gevent.spawn(my_func_2)
]
gevent.joinall(thread)

import time


def tictoc(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        func(*args, **kwargs)
        t2 = time.time()-t1
        print(f"func {func.__name__} took {t2} seconds")
    return wrapper


@tictoc
def do_something(t):
    time.sleep(t) 


@tictoc
def do_1():
    time.sleep(1.5)


@tictoc
def do_2():
    time.sleep(0.5)


do_something(1.2)
do_something(2.11)


# do_1()
# do_2()


print("Finish")
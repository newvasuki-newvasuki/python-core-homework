from ex2 import fetcher
from timeit import default_timer


CALL_COUNT = 10


def benchmark(num):
    """
    Совершает num прогонов переданной функции и выводит в консоль время каждого прогона и среднее время всех прогонов

    :param num: число итераций
    :return: функцию обёртку
    """
	# поскольку декоратор принимает параметр
	# придётся делать декоратор в декораторе
    def wrapper(func):
        def inner(*args,**kwargs):
            cumulativeTime = 0
            for itaration in range(num):
                startTime = default_timer()
                func(*args, **kwargs)
                endTime = default_timer()
                timeOfExecution = endTime - startTime
                cumulativeTime += timeOfExecution
                print(timeOfExecution)
            print(cumulativeTime)
        return inner        
    return wrapper


@benchmark(CALL_COUNT)
def fetch_page(url):
    fetcher.get(url)

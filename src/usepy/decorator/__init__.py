from .singleton import singleton as useSingleton
from .timeit import time_it as useTimeIt
from .catch_error import catch_error as useCatchError
from .except_debug import except_debug as useExceptDebug
from .run_in_thread import run_in_thread as useRunInThread
from .listify import listify as useListify


class Decorator:
    singleton = useSingleton
    timeit = useTimeIt
    catch_error = useCatchError
    except_debug = useExceptDebug
    run_in_thread = useRunInThread
    listify = useListify


useDecorator = Decorator

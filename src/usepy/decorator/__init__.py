from .singleton import singleton as useSingleton
from .timeit import time_it as useTimeIt
from .catch_error import catch_error as useCatchError
from .except_debug import except_debug as useExceptDebug
from .run_in_thread import run_in_thread as useRunInThread
from .listify import listify as useListify
from .cache import cached_property as useCachedProperty
from .retry import Retry as useRetry


class Decorator:
    singleton = useSingleton
    timeit = useTimeIt
    catch_error = useCatchError
    except_debug = useExceptDebug
    run_in_thread = useRunInThread
    listify = useListify
    cached_property = useCachedProperty
    retry = useRetry


useDecorator = Decorator

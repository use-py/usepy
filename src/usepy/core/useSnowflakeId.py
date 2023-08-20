import time

WORKER_ID_BITS = 5
DATACENTER_ID_BITS = 5
SEQUENCE_BITS = 12

MAX_WORKER_ID = -1 ^ (-1 << WORKER_ID_BITS)
MAX_DATACENTER_ID = -1 ^ (-1 << DATACENTER_ID_BITS)

WORKER_ID_SHIFT = SEQUENCE_BITS
DATACENTER_ID_SHIFT = SEQUENCE_BITS + WORKER_ID_BITS
TIMESTAMP_LEFT_SHIFT = SEQUENCE_BITS + WORKER_ID_BITS + DATACENTER_ID_BITS
SEQUENCE_MASK = -1 ^ (-1 << SEQUENCE_BITS)
TWEPOCH = 1288834974657


def _generate_timestamp():
    return int(time.time() * 1000)


class useSnowflakeId:
    def __init__(self, datacenter_id=1, worker_id=1, sequence=0):
        if worker_id > MAX_WORKER_ID or worker_id < 0:
            raise ValueError('worker_id is out of range')

        if datacenter_id > MAX_DATACENTER_ID or datacenter_id < 0:
            raise ValueError('datacenter_id is out of range')

        self.worker_id = worker_id
        self.datacenter_id = datacenter_id
        self.sequence = sequence
        self.last_timestamp = -1

    def generate_id(self):
        timestamp = _generate_timestamp()

        if timestamp < self.last_timestamp:
            raise ValueError('Clock is moving backwards. Rejecting requests until {}'.format(self.last_timestamp))

        if timestamp == self.last_timestamp:
            self.sequence = (self.sequence + 1) & SEQUENCE_MASK
            if self.sequence == 0:
                timestamp = self._wait_next_millis(self.last_timestamp)
        else:
            self.sequence = 0

        self.last_timestamp = timestamp

        new_id = ((timestamp - TWEPOCH) << TIMESTAMP_LEFT_SHIFT) | (self.datacenter_id << DATACENTER_ID_SHIFT) | (
                self.worker_id << WORKER_ID_SHIFT) | self.sequence
        return new_id
    
    @staticmethod
    def _wait_next_millis(last_timestamp):
        timestamp = _generate_timestamp()
        while timestamp <= last_timestamp:
            timestamp = _generate_timestamp()
        return timestamp

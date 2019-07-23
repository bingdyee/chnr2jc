# -*- coding: utf-8 -*-
import time


class SnowFlake:

    def __init__(self, worker_id, data_center_id):
        self.epoch = 1420041600000
        self.id_bits = 5
        self.data_center_id_bits = 5
        self.max_id = -1 ^ (-1 << self.id_bits)
        self.max_data_center_id = -1 ^ (-1 << self.data_center_id_bits)
        self.sequence_bits = 12
        self.id_shift = self.sequence_bits
        self.data_center_id_shift = self.sequence_bits + self.id_bits
        self.time_stamp_left_shift = self.sequence_bits + self.id_bits + self.data_center_id_bits
        self.sequence_mask = -1 ^ (-1 << self.sequence_bits)
        self.sequence = 0
        self.last_time_stamp = -1
        self.worker_id = 0
        self.data_center_id = 0
        self._init(worker_id, data_center_id)

    def _init(self, worker_id, data_center_id):
        if worker_id > self.max_id or worker_id < 0:
            raise Exception("worker Id can't be greater than %d or less than 0" % self.max_id)
        if data_center_id > self.max_data_center_id or data_center_id < 0:
            raise Exception("datacenter Id can't be greater than %d or less than 0" % self.max_data_center_id)
        self.worker_id = worker_id
        self.data_center_id = data_center_id

    def next_id(self):
        now_stamp = SnowFlake.gen_time()
        if now_stamp < self.last_time_stamp:
            raise Exception("Clock moved backwards. Refusing to generate id for %d milliseconds"
                            % (now_stamp - self.last_time_stamp))
        if now_stamp == self.last_time_stamp:
            self.sequence = (self.sequence + 1) & self.sequence_mask
            # 毫秒内序列溢出
            if self.sequence == 0:
                # 阻塞到下一个毫秒, 获得新的时间戳
                now_stamp = self.next_mills(self.last_time_stamp)
        else:
            self.sequence = 0
        self.last_time_stamp = now_stamp
        return ((now_stamp - self.epoch) << self.time_stamp_left_shift) | \
               (self.data_center_id << self.data_center_id_shift) | \
               (self.worker_id << self.id_shift) | self.sequence

    def next_mills(self, last_time):
        timestamp = self.gen_time()
        while timestamp <= last_time:
            timestamp = self.gen_time()
        return timestamp

    @staticmethod
    def gen_time():
        return int(round(time.time() * 1000))


SnowFlake = SnowFlake(0, 0)
#!/usr/bin/python

from __future__ import print_function

import rosbag
import numpy as np
from tqdm.auto import tqdm

with rosbag.Bag('/home/tobias/bags_2020-08-07-09-06-59.bag') as bag:
    num_msgs = bag.get_message_count('/gps/fix')
    with tqdm(total=num_msgs) as pbar:
        latitudes, longitudes, altitudes, times = [], [], [], []
        valid_samples = 0
        all_samples = 0

        for topic, msg, t in bag.read_messages():
            if topic == '/gps/fix':
                if not np.isnan(msg.latitude) and not np.isnan(msg.longitude):
                    if msg.status.status != 0 or msg.status.service != 1:
                        print(msg.status.status, msg.status.service)
                    # print(msg.position_covariance)
                    if msg.position_covariance[0] < 15:
                        valid_samples = valid_samples + 1
                        latitudes.append(msg.latitude)
                        longitudes.append(msg.longitude)
                        altitudes.append(msg.altitude)
                        times.append(msg.header.stamp.to_sec())
                    all_samples = all_samples + 1
                    # print(msg.latitude)
                pbar.update(1)

        latitudes = np.array(latitudes)
        longitudes = np.array(longitudes)
        times = np.array(times)
        altitudes = np.array(altitudes)
        print('saved', valid_samples, 'valid samples out of', all_samples, 'total samples')

        np.savez('gps.npz', latitudes=latitudes, longitudes=longitudes, times=times, altitudes=altitudes)

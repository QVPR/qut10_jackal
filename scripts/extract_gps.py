#!/usr/bin/python

from __future__ import print_function

import rosbag
import numpy as np
from tqdm.auto import tqdm

with rosbag.Bag('/home/tobias/bags_2020-08-07-09-06-59.bag') as bag:
    num_msgs = bag.get_message_count('/gps/fix')
    with tqdm(total=num_msgs) as pbar:
        latitudes, longitudes = [], []

        for topic, msg, t in bag.read_messages():
            if topic == '/gps/fix':
                if not np.isnan(msg.latitude) and not np.isnan(msg.longitude):
                    latitudes.append(msg.latitude)
                    longitudes.append(msg.longitude)
                    # print(msg.latitude)
                pbar.update(1)

        latitudes = np.array(latitudes)
        longitudes = np.array(longitudes)
        print('saved', len(latitudes), 'samples')

        np.savez('gps.npz', latitudes=latitudes, longitudes=longitudes)

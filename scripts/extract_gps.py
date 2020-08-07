#!/usr/bin/python

import rosbag
import numpy as np
from tqdm.auto import tqdm

with rosbag.Bag('/home/tobias/bags_2020-08-07-09-06-59.bag') as bag:
    num_msgs = bag.get_message_count('/gps/fix')
    with tqdm(total=num_msgs) as pbar:
        for topic, msg, t in bag.read_messages():
            latitudes, longitudes = [], []
            if topic == '/gps/fix':
                latitudes.append(msg.latitude)
                longitudes.append(msg.longitude)
                pbar.update(1)

        latitudes = np.array(latitudes)
        longitudes = np.array(longitudes)

        np.savez('gps.npz', latitudes=latitudes, longitudes=longitudes)

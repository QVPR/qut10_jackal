import unittest
import os
import subprocess
import rospy
import rostopic
import yaml

test_results = {}

test_results["ROSWTFTest"] = "SUCCESS"
class ROSWTFTest(unittest.TestCase):
    def runTest(self):
        status = True
        result = subprocess.check_output(['roswtf'], shell=True)
        if "ERROR" in result:
            print result
            status = False
        if "WARNING" in result:
            print result

        self.assertTrue(status)
test_results["ARKIP_PingTest"] = "SUCCESS"
class ARKIP_PingTest(unittest.TestCase):
    def setUp(self):
        self.hostname = "192.168.132.111"
        self.latency = 100.0

    def runTest(self):
        loss, avg_time, max_time = self.getPingTimes()

        self.assertEqual(loss, 0) # Packets Lost
        self.assertEqual(self.latency, max(avg_time, self.latency)) # Average Ping Time
        self.assertEqual(self.latency, max(max_time, self.latency)) # Max Ping Time

    def getPingTimes(self):
        try:
            result = subprocess.check_output("ping -q -W 2 -c 5 " + self.hostname, shell=True)
            result = result.split()

            loss = int(result[17][:-1])
            speeds = result[25].split("/") #min/avg/max/mdev

            return loss, float(speeds[1]), float(speeds[2])
        except:
            return int(100), 99999.9, 99999.9

test_results["PCHostname_PingTest"] = "SUCCESS"
class PCHostname_PingTest(unittest.TestCase):
    def setUp(self):
        self.hostname = "cpr-qut10"
        self.latency = 100.0

    def runTest(self):
        loss, avg_time, max_time = self.getPingTimes()

        self.assertEqual(loss, 0) # Packets Lost
        self.assertEqual(self.latency, max(avg_time, self.latency)) # Average Ping Time
        self.assertEqual(self.latency, max(max_time, self.latency)) # Max Ping Time

    def getPingTimes(self):
        try:
            result = subprocess.check_output("ping -q -W 2 -c 5 " + self.hostname, shell=True)
            result = result.split()

            loss = int(result[17][:-1])
            speeds = result[25].split("/") #min/avg/max/mdev

            return loss, float(speeds[1]), float(speeds[2])
        except:
            return int(100), 99999.9, 99999.9

test_results["HokuyoUST10LX2IP_PingTest"] = "SUCCESS"
class HokuyoUST10LX2IP_PingTest(unittest.TestCase):
    def setUp(self):
        self.hostname = "192.168.131.21"
        self.latency = 100.0

    def runTest(self):
        loss, avg_time, max_time = self.getPingTimes()

        self.assertEqual(loss, 0) # Packets Lost
        self.assertEqual(self.latency, max(avg_time, self.latency)) # Average Ping Time
        self.assertEqual(self.latency, max(max_time, self.latency)) # Max Ping Time

    def getPingTimes(self):
        try:
            result = subprocess.check_output("ping -q -W 2 -c 5 " + self.hostname, shell=True)
            result = result.split()

            loss = int(result[17][:-1])
            speeds = result[25].split("/") #min/avg/max/mdev

            return loss, float(speeds[1]), float(speeds[2])
        except:
            return int(100), 99999.9, 99999.9

test_results["VelodyneVLP161IP_PingTest"] = "SUCCESS"
class VelodyneVLP161IP_PingTest(unittest.TestCase):
    def setUp(self):
        self.hostname = "192.168.131.23"
        self.latency = 100.0

    def runTest(self):
        loss, avg_time, max_time = self.getPingTimes()

        self.assertEqual(loss, 0) # Packets Lost
        self.assertEqual(self.latency, max(avg_time, self.latency)) # Average Ping Time
        self.assertEqual(self.latency, max(max_time, self.latency)) # Max Ping Time

    def getPingTimes(self):
        try:
            result = subprocess.check_output("ping -q -W 2 -c 5 " + self.hostname, shell=True)
            result = result.split()

            loss = int(result[17][:-1])
            speeds = result[25].split("/") #min/avg/max/mdev

            return loss, float(speeds[1]), float(speeds[2])
        except:
            return int(100), 99999.9, 99999.9

test_results["CustomerIP_PingTest"] = "SUCCESS"
class CustomerIP_PingTest(unittest.TestCase):
    def setUp(self):
        self.hostname = "192.168.131.1"
        self.latency = 100.0

    def runTest(self):
        loss, avg_time, max_time = self.getPingTimes()

        self.assertEqual(loss, 0) # Packets Lost
        self.assertEqual(self.latency, max(avg_time, self.latency)) # Average Ping Time
        self.assertEqual(self.latency, max(max_time, self.latency)) # Max Ping Time

    def getPingTimes(self):
        try:
            result = subprocess.check_output("ping -q -W 2 -c 5 " + self.hostname, shell=True)
            result = result.split()

            loss = int(result[17][:-1])
            speeds = result[25].split("/") #min/avg/max/mdev

            return loss, float(speeds[1]), float(speeds[2])
        except:
            return int(100), 99999.9, 99999.9

test_results["HokuyoUST10LX1IP_PingTest"] = "SUCCESS"
class HokuyoUST10LX1IP_PingTest(unittest.TestCase):
    def setUp(self):
        self.hostname = "192.168.131.20"
        self.latency = 100.0

    def runTest(self):
        loss, avg_time, max_time = self.getPingTimes()

        self.assertEqual(loss, 0) # Packets Lost
        self.assertEqual(self.latency, max(avg_time, self.latency)) # Average Ping Time
        self.assertEqual(self.latency, max(max_time, self.latency)) # Max Ping Time

    def getPingTimes(self):
        try:
            result = subprocess.check_output("ping -q -W 2 -c 5 " + self.hostname, shell=True)
            result = result.split()

            loss = int(result[17][:-1])
            speeds = result[25].split("/") #min/avg/max/mdev

            return loss, float(speeds[1]), float(speeds[2])
        except:
            return int(100), 99999.9, 99999.9

test_results["UM7_imu_um7data_AdvertiseTest"] = "SUCCESS"
class UM7_imu_um7data_AdvertiseTest(unittest.TestCase):
    def setUp(self):
        self.topic_name = "/imu_um7/data"

    def runTest(self):
        if not rospy.is_shutdown():
            msg_class, real_topic, _ = rostopic.get_topic_class(self.topic_name)

            self.assertIsNotNone(real_topic)

test_results["UM7_imu_um7data_RateTest"] = "SUCCESS"
class UM7_imu_um7data_RateTest(unittest.TestCase):
    def setUp(self):
        self.topic_name = "/imu_um7/data"
        self.min_freq = 20 * 0.95

    def runTest(self):
        if not rospy.is_shutdown():
            msg_class, real_topic, _ = rostopic.get_topic_class(self.topic_name)

            self.assertIsNotNone(real_topic)

            if real_topic:
                rt = rostopic.ROSTopicHz(-1, filter_expr=None, use_wtime=False)

                sub = rospy.Subscriber(real_topic, msg_class, rt.callback_hz)

                if not rospy.is_shutdown():
                    rospy.sleep(1.0)
                    hz = self.getHz(rt)

                    self.assertNotEqual(max(0.0, hz - self.min_freq), 0.0)

    def getHz(self, rt):
        rate = 0.0
        if not rt.times:
            return rate
        elif rt.msg_tn == rt.last_printed_tn:
            return rate
        with rt.lock:
            n = len(rt.times)
            mean = sum(rt.times) / n
            rate = 1.0/mean if mean > 0.0 else 0.0

        return rate

test_results["HokuyoUST10LX1_frontscan_AdvertiseTest"] = "SUCCESS"
class HokuyoUST10LX1_frontscan_AdvertiseTest(unittest.TestCase):
    def setUp(self):
        self.topic_name = "/front/scan"

    def runTest(self):
        if not rospy.is_shutdown():
            msg_class, real_topic, _ = rostopic.get_topic_class(self.topic_name)

            self.assertIsNotNone(real_topic)

test_results["HokuyoUST10LX1_frontscan_RateTest"] = "SUCCESS"
class HokuyoUST10LX1_frontscan_RateTest(unittest.TestCase):
    def setUp(self):
        self.topic_name = "/front/scan"
        self.min_freq = 40 * 0.95

    def runTest(self):
        if not rospy.is_shutdown():
            msg_class, real_topic, _ = rostopic.get_topic_class(self.topic_name)

            self.assertIsNotNone(real_topic)

            if real_topic:
                rt = rostopic.ROSTopicHz(-1, filter_expr=None, use_wtime=False)

                sub = rospy.Subscriber(real_topic, msg_class, rt.callback_hz)

                if not rospy.is_shutdown():
                    rospy.sleep(1.0)
                    hz = self.getHz(rt)

                    self.assertNotEqual(max(0.0, hz - self.min_freq), 0.0)

    def getHz(self, rt):
        rate = 0.0
        if not rt.times:
            return rate
        elif rt.msg_tn == rt.last_printed_tn:
            return rate
        with rt.lock:
            n = len(rt.times)
            mean = sum(rt.times) / n
            rate = 1.0/mean if mean > 0.0 else 0.0

        return rate

test_results["HokuyoUST10LX2_rearscan_AdvertiseTest"] = "SUCCESS"
class HokuyoUST10LX2_rearscan_AdvertiseTest(unittest.TestCase):
    def setUp(self):
        self.topic_name = "/rear/scan"

    def runTest(self):
        if not rospy.is_shutdown():
            msg_class, real_topic, _ = rostopic.get_topic_class(self.topic_name)

            self.assertIsNotNone(real_topic)

test_results["HokuyoUST10LX2_rearscan_RateTest"] = "SUCCESS"
class HokuyoUST10LX2_rearscan_RateTest(unittest.TestCase):
    def setUp(self):
        self.topic_name = "/rear/scan"
        self.min_freq = 40 * 0.95

    def runTest(self):
        if not rospy.is_shutdown():
            msg_class, real_topic, _ = rostopic.get_topic_class(self.topic_name)

            self.assertIsNotNone(real_topic)

            if real_topic:
                rt = rostopic.ROSTopicHz(-1, filter_expr=None, use_wtime=False)

                sub = rospy.Subscriber(real_topic, msg_class, rt.callback_hz)

                if not rospy.is_shutdown():
                    rospy.sleep(1.0)
                    hz = self.getHz(rt)

                    self.assertNotEqual(max(0.0, hz - self.min_freq), 0.0)

    def getHz(self, rt):
        rate = 0.0
        if not rt.times:
            return rate
        elif rt.msg_tn == rt.last_printed_tn:
            return rate
        with rt.lock:
            n = len(rt.times)
            mean = sum(rt.times) / n
            rate = 1.0/mean if mean > 0.0 else 0.0

        return rate

test_results["BuiltinIMU_imudata_AdvertiseTest"] = "SUCCESS"
class BuiltinIMU_imudata_AdvertiseTest(unittest.TestCase):
    def setUp(self):
        self.topic_name = "/imu/data"

    def runTest(self):
        if not rospy.is_shutdown():
            msg_class, real_topic, _ = rostopic.get_topic_class(self.topic_name)

            self.assertIsNotNone(real_topic)

test_results["BuiltinIMU_imudata_RateTest"] = "SUCCESS"
class BuiltinIMU_imudata_RateTest(unittest.TestCase):
    def setUp(self):
        self.topic_name = "/imu/data"
        self.min_freq = 75 * 0.95

    def runTest(self):
        if not rospy.is_shutdown():
            msg_class, real_topic, _ = rostopic.get_topic_class(self.topic_name)

            self.assertIsNotNone(real_topic)

            if real_topic:
                rt = rostopic.ROSTopicHz(-1, filter_expr=None, use_wtime=False)

                sub = rospy.Subscriber(real_topic, msg_class, rt.callback_hz)

                if not rospy.is_shutdown():
                    rospy.sleep(1.0)
                    hz = self.getHz(rt)

                    self.assertNotEqual(max(0.0, hz - self.min_freq), 0.0)

    def getHz(self, rt):
        rate = 0.0
        if not rt.times:
            return rate
        elif rt.msg_tn == rt.last_printed_tn:
            return rate
        with rt.lock:
            n = len(rt.times)
            mean = sum(rt.times) / n
            rate = 1.0/mean if mean > 0.0 else 0.0

        return rate

test_results["Novatel_gpsfix_AdvertiseTest"] = "SUCCESS"
class Novatel_gpsfix_AdvertiseTest(unittest.TestCase):
    def setUp(self):
        self.topic_name = "/gps/fix"

    def runTest(self):
        if not rospy.is_shutdown():
            msg_class, real_topic, _ = rostopic.get_topic_class(self.topic_name)

            self.assertIsNotNone(real_topic)

test_results["Novatel_gpsfix_RateTest"] = "SUCCESS"
class Novatel_gpsfix_RateTest(unittest.TestCase):
    def setUp(self):
        self.topic_name = "/gps/fix"
        self.min_freq = 5 * 0.95

    def runTest(self):
        if not rospy.is_shutdown():
            msg_class, real_topic, _ = rostopic.get_topic_class(self.topic_name)

            self.assertIsNotNone(real_topic)

            if real_topic:
                rt = rostopic.ROSTopicHz(-1, filter_expr=None, use_wtime=False)

                sub = rospy.Subscriber(real_topic, msg_class, rt.callback_hz)

                if not rospy.is_shutdown():
                    rospy.sleep(1.0)
                    hz = self.getHz(rt)

                    self.assertNotEqual(max(0.0, hz - self.min_freq), 0.0)

    def getHz(self, rt):
        rate = 0.0
        if not rt.times:
            return rate
        elif rt.msg_tn == rt.last_printed_tn:
            return rate
        with rt.lock:
            n = len(rt.times)
            mean = sum(rt.times) / n
            rate = 1.0/mean if mean > 0.0 else 0.0

        return rate

test_results["VelodyneVLP161_velodyne_points_AdvertiseTest"] = "SUCCESS"
class VelodyneVLP161_velodyne_points_AdvertiseTest(unittest.TestCase):
    def setUp(self):
        self.topic_name = "/velodyne_points"

    def runTest(self):
        if not rospy.is_shutdown():
            msg_class, real_topic, _ = rostopic.get_topic_class(self.topic_name)

            self.assertIsNotNone(real_topic)

test_results["VelodyneVLP161_velodyne_points_RateTest"] = "SUCCESS"
class VelodyneVLP161_velodyne_points_RateTest(unittest.TestCase):
    def setUp(self):
        self.topic_name = "/velodyne_points"
        self.min_freq = 10 * 0.95

    def runTest(self):
        if not rospy.is_shutdown():
            msg_class, real_topic, _ = rostopic.get_topic_class(self.topic_name)

            self.assertIsNotNone(real_topic)

            if real_topic:
                rt = rostopic.ROSTopicHz(-1, filter_expr=None, use_wtime=False)

                sub = rospy.Subscriber(real_topic, msg_class, rt.callback_hz)

                if not rospy.is_shutdown():
                    rospy.sleep(1.0)
                    hz = self.getHz(rt)

                    self.assertNotEqual(max(0.0, hz - self.min_freq), 0.0)

    def getHz(self, rt):
        rate = 0.0
        if not rt.times:
            return rate
        elif rt.msg_tn == rt.last_printed_tn:
            return rate
        with rt.lock:
            n = len(rt.times)
            mean = sum(rt.times) / n
            rate = 1.0/mean if mean > 0.0 else 0.0

        return rate


if __name__ == '__main__':
    rospy.init_node("system_test", anonymous=True)
    results = unittest.main(verbosity=2, exit=False)
    for t in results.result.failures:
        test_results[t[0].id().split(".")[1]] = "FAIL"
    for t in results.result.errors:
        test_results[t[0].id().split(".")[1]] = "ERROR"

    resultsFile = open("results.txt", 'w')
    yaml.dump(test_results, resultsFile)
    resultsFile.close()

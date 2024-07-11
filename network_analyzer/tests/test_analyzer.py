import unittest
from network_analyzer.analyzer import gather_network_info

class TestNetworkAnalyzer(unittest.TestCase):
    def test_gather_network_info(self):
        network_info = gather_network_info()
        self.assertIsInstance(network_info, list)
        if network_info:
            self.assertIn('local_address', network_info[0])
            self.assertIn('remote_address', network_info[0])

if __name__ == '__main__':
    unittest.main()

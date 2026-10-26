import unittest, statistics
class TestBasicStatistics(unittest.TestCase):
    def test_mean(self): self.assertAlmostEqual(statistics.mean([1,2,3]),2.0)
    def test_range(self): self.assertEqual(max([1,2,3])-min([1,2,3]),2)
if __name__ == '__main__': unittest.main()

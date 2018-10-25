import unittest
from coin_cal_fun import Coin_calculation

class test_coin_cal_fun(unittest.TestCase):

    def test_coin_cal_fun(self):
        packet_coin = [5, 5, 10, 10, 10, 50, 20, 1, 3, 100]
        object_price = 53
        result=Coin_calculation.coin_cal_fun(packet_coin,object_price)
        self.assertEqual(result,[50, 3])

        packet_coin = [5, 5, 10, 10, 10, 50, 20, 1]
        object_price = 83
        result=Coin_calculation.coin_cal_fun(packet_coin,object_price)
        self.assertEqual(result,[])

        packet_coin = [5, 5, 10, 10, 10, 50]
        object_price = 70
        result=Coin_calculation.coin_cal_fun(packet_coin,object_price)
        self.assertEqual(result,[50, 10, 10])







if __name__=='__main__':
    unittest.main()


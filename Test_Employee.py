import unittest
from Employee import Employee

class test_employee(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Set up class")

    @classmethod
    def tearDownClass(cls):
        print("Tear down class")

    def setUp(self):
        print('setUp \n')
        self.emp1=Employee("Amir", "Nematollahi", 5000)
        self.emp2=Employee("Ali", "Riazi", 400)

    def tearDown(self):
        print("Tear Down \n")


    def test_email(self):
        print("Test email method")

        self.assertEqual(self.emp1.email,"Amir.Nematollahi@email.com")
        self.assertEqual(self.emp2.email, "Ali.Riazi@email.com")

    def test_fullname(self):
        print("Test fullname method")
        self.assertEqual(self.emp1.fullname,"Amir Nematollahi")
        self.assertEqual(self.emp2.fullname, "Ali Riazi")

    def test_pay(self):
        print("Test apply raise method")
        self.emp1.apply_raise
        self.assertEqual(self.emp1.pay, 5250)



if __name__=='__main__':
    unittest.main()
import unittest
from tests import TestPISLogin, TestPISProduct, TestPISSuppliers, TestPISPurchaseOrders,TestPISBillingOrders
loader = unittest.TestLoader()
suite = unittest.TestSuite()

suite.addTest(loader.loadTestsFromModule(TestPISLogin))
suite.addTest(loader.loadTestsFromModule(TestPISProduct))
suite.addTest(loader.loadTestsFromModule(TestPISSuppliers))
suite.addTest(loader.loadTestsFromModule(TestPISPurchaseOrders))
suite.addTest(loader.loadTestsFromModule(TestPISBillingOrders))

runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)
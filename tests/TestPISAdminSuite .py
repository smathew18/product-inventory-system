import unittest
from tests import TestPISLoginAdmin, TestPISProductAdmin, TestPISSuppliersAdmin, TestPISPurchaseOrdersAdmin, TestPISBillingOrdersAdmin
loader = unittest.TestLoader()
suite = unittest.TestSuite()

suite.addTest(loader.loadTestsFromModule(TestPISLoginAdmin))
suite.addTest(loader.loadTestsFromModule(TestPISProductAdmin))
suite.addTest(loader.loadTestsFromModule(TestPISSuppliersAdmin))
suite.addTest(loader.loadTestsFromModule(TestPISPurchaseOrdersAdmin))
suite.addTest(loader.loadTestsFromModule(TestPISBillingOrdersAdmin))

runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)
from unittest import TestLoader, TestSuite, TextTestRunner
from structure2.Pages.test_TC01 import Home
from structure2.Pages.test_TC02 import Home2
from structure2.testUtility.ScreenShots import SS


import testtools as testtools

if __name__ == "__main__":
    loader = TestLoader()
    suite = TestSuite((
        loader.loadTestsFromTestCase(Home),
        loader.loadTestsFromTestCase(Home2),
        loader.loadTestsFromTestCase(SS),

    ))

    # run test sequentially using simple TextTestRunner
    runner = TextTestRunner(verbosity=2)
    runner.run(suite)

    # #run test parallel using concurrent_suite
    concurrent_suite = testtools.ConcurrentStreamTestSuite(lambda: ((case, None) for case in suite))
    concurrent_suite.run(testtools.StreamResult())

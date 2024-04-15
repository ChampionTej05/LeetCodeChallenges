import unittest
class CustomTestLoader(unittest.TestLoader):
    def loadTestsFromTestCase(self, testCaseClass, approach=1):
        if issubclass(testCaseClass, unittest.suite.TestSuite):
            raise TypeError("Test cases should not be derived from TestSuite. Maybe you meant to derive from TestCase?")
        testCaseNames = self.getTestCaseNames(testCaseClass)
        testCases = []
        for name in testCaseNames:
            testCases.append(testCaseClass(name, approach=approach))
        loaded_suite = self.suiteClass(testCases)
        return loaded_suite
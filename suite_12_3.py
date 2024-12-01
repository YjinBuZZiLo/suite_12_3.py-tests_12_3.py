import unittest
import tests_12_3

STrunner = unittest.TestSuite()
STrunner.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
STrunner.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(STrunner)
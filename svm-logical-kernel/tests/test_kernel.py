import unittest
from src.logical_kernel import logical_kernel

class TestLogicalKernel(unittest.TestCase):
    def test_similarita(self):
        X = [{"fatto1", "fatto2"}, {"fatto2", "fatto3"}]
        Y = [{"fatto1", "fatto2"}, {"fatto3", "fatto4"}]
        atteso = [[2, 0], [1, 1]]

        risultato = logical_kernel(X, Y)
        self.assertEqual(risultato.tolist(), atteso)

if __name__ == "__main__":
    unittest.main()

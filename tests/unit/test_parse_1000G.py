import unittest
import simple_example.parse_1000G as test_parse_1000G


class TestParse1000G(unittest.TestCase):

    def test_mean_allele_frequency_cal(self):
        test_dict = {
            'EAS_AF': '0.1',
            'AMR_AF': '0.2',
            'AFR_AF': '0.3',
            'EUR_AF': '0.4'
        }
        found = test_parse_1000G.cal_mean_allele_frequency(
            test_dict
        )
        expected = 0.25
        self.assertEqual(found, expected)


if __name__ == '__main__':
    unittest.main()

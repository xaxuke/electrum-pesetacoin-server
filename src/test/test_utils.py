import unittest
from utils import hash_160_to_address, ptc_address_to_hash_160


class UtilTest(unittest.TestCase):

    def test_hash_160_to_address(self):
        self.assertEqual(hash_160_to_address(None), None)
        self.assertEqual(hash_160_to_address('fffdf08d'.decode('hex')), None)
        self.assertEqual(hash_160_to_address('fffdf08d243d242b83aa42be4b95c735e595f19f'.decode('hex')), None)
        self.assertEqual(hash_160_to_address('e50d390d5a73508f08224156ed782317678f675d'.decode('hex')),
                         'LGmTrmr2cS9HD3YSbxtGGjhznabfnFba9a')


    def test_ptc_address_to_hash_160(self):
        self.assertEqual(ptc_address_to_hash_160(None), None)
        self.assertEqual(ptc_address_to_hash_160(''), None)
        self.assertEqual(ptc_address_to_hash_160('LGmTrmr2cS9HD3YSbxtGGjhznabfnFba9a1337'), None)
        self.assertEqual(ptc_address_to_hash_160('LGmTrmr2cS9HD3YSbxtGGjhznabfnFba9a').encode('hex'),
                                                'e50d390d5a73508f08224156ed782317678f675d')



if __name__ == '__main__':
    unittest.main()


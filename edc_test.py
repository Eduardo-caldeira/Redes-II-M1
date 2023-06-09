import unittest
from edc import (
    sender,
    receiver,
    CRC_16
)


class TestStringToBinaryParser(unittest.TestCase):

    def test_sender(self):
        self.assertEqual(sender('1101011011', '10011'), '11010110111110')
        self.assertEqual(sender('0010100101', '10011'), '00101001011011')
        self.assertEqual(sender('01110101001110100', '10011'),
                         '011101010011101000111')
        self.assertEqual(sender('01110101001110100111001011010110',
                         '10011'), '011101010011101001110010110101100010')

    def test_receiver(self):
        self.assertEqual(receiver('11010110111110', '10011'), '0000')
        self.assertEqual(receiver('00101001011011', '10011'), '0000')
        self.assertEqual(receiver('011101010011101000111', '10011'),
                         '0000')
        self.assertEqual(receiver('011101010011101001110010110101100010',
                         '10011'), '0000')

    def test_sender_polynomial_16_bits_arc(self):
        self.assertEqual(
            sender('01110101001110100111001011010110', CRC_16), '011101010011101001110010110101100010100110101101')

    def test_receiver_polynomial_16_bits_arc(self):
        self.assertEqual(
            receiver('011101010011101001110010110101100010100110101101', CRC_16), '0000000000000000')


if __name__ == "__main__":
    unittest.main()

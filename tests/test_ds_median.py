import unittest

from src.ds_median import (
    DataStreamMedian,
    NoDataOnStream,
    InvalidDataType
)


class DataStreamMedianTest(unittest.TestCase):

    def setUp(self):
        self.median = DataStreamMedian()

    def tearDown(self):
        self.median.clear()

    def test_data_stream_empty(self):

        with self.assertRaises(NoDataOnStream):
            self.median.compute()

    def test_data_stream_with_one_value(self):
        expected_median = 3
        self.median.add(3)

        self.assertEqual(self.median.compute(), expected_median)

    def test_data_stream_with_even_length(self):
        stream = [6, 10, 2, 6, 5, 0]
        expected_median = 5.5

        for value in stream:
            self.median.add(value)

        self.assertEqual(self.median.compute(), expected_median)

    def test_data_stream_with_odd_length(self):
        stream = [6, 10, 2, 6, 5]
        expected_median = 6

        for value in stream:
            self.median.add(value)

        self.assertEqual(self.median.compute(), expected_median)

    def test_data_stream_add_invalid_type(self):

        with self.assertRaises(InvalidDataType):
            self.median.add("string")

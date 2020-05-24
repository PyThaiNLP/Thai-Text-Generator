# -*- coding: utf-8 -*-

import unittest

from thaitextgenerator import *


class TestNgram(unittest.TestCase):

    def test_unigram(self):
        uni = Unigram()
        self.assertIsNotNone(uni.gen_sentence(N=10))
    def test_bigram(self):
        bi = Bigram()
        self.assertIsNotNone(bi.gen_sentence(N=10))
    def test_tigram(self):
        ti = Tigram()
        self.assertIsNotNone(ti.gen_sentence(N=10))
#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Copyright (C) 2015 - 2017 Martin Kauss (yo@bishoph.org)

Licensed under the Apache License, Version 2.0 (the "License"); you may
not use this file except in compliance with the License. You may obtain
a copy of the License at

 http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
License for the specific language governing permissions and limitations
under the License.
"""

import test.test_analyze as test_analyze
import test.test_filter as test_filter

class unit_tests():

    def __init__(self, debug, cfg):
        print ('starting analyze tests...')
        test_analyze.test_analyze(debug, cfg)
        test_filter.test_filter(debug, cfg)
        print ('unit_tests run successful!')

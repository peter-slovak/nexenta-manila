# Copyright 2016 Nexenta Systems, Inc.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from oslo_utils import units

from manila.share.drivers.nexenta import utils
from manila import test


class TestNexentaUtils(test.TestCase):

    def test_str2size(self):
        values_to_test = (
            # Test empty value
            (None, 0),
            ('', 0),
            ('0', 0),
            ('12', 12),
            # Test int values
            (10, 10),
            # Test bytes string
            ('1b', 1),
            ('1B', 1),
            ('1023b', 1023),
            ('0B', 0),
            # Test other units
            ('1M', units.Mi),
            ('1.0M', units.Mi),
        )

        for value, result in values_to_test:
            self.assertEqual(result, utils.str2size(value))

        # Invalid format value
        self.assertRaises(ValueError, utils.str2size, 'A')

# coding: utf-8

"""
    Allele Calling Service

    The Allele Calling  service provides an API for converting raw sequence data to GFE and HLA allele calls.  # noqa: E501

    OpenAPI spec version: 0.0.5
    Contact: mhalagan@nmdp.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import gfe_client
from gfe_client.api.type_align_api import TypeAlignApi  # noqa: E501
from gfe_client.rest import ApiException


class TestTypeAlignApi(unittest.TestCase):
    """TypeAlignApi unit test stubs"""

    def setUp(self):
        self.api = gfe_client.api.type_align_api.TypeAlignApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_typealign_get(self):
        """Test case for typealign_get

        """
        pass


if __name__ == '__main__':
    unittest.main()
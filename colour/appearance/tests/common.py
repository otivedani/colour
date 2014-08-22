# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Defines the common unit tests objects for :mod:`colour.appearance` package.
"""

from __future__ import division, unicode_literals

import csv
import numpy
import os
import unittest
from abc import abstractmethod
from collections import defaultdict
from numpy.testing import assert_allclose, assert_almost_equal

__author__ = 'Colour Developers'
__copyright__ = 'Copyright (C) 2013 - 2014 - Colour Developers'
__license__ = 'New BSD License - http://opensource.org/licenses/BSD-3-Clause'
__maintainer__ = 'Colour Developers'
__email__ = 'colour-science@googlegroups.com'
__status__ = 'Production'

__all__ = ['ColourAppearanceModelTest']


class ColourAppearanceModelTest(object):
    """
    Defines the base class for tests of: mod:`colour.appearance` package.

    Each colour appearance model is tested against a respective '.csv' file
    from which content has been generated from data of the following file by
    **Mark D. Fairchild**: http://rit-mcsl.org/fairchild//files/AppModEx.xls

    Methods
    -------
    load_fixtures
    get_output_specification_from_data
    check_specification_attribute
    check_model_consistency
    test_forward_examples
    """

    FIXTURE_BASENAME = None
    """
    '.csv' file fixture path for the colour appearance model being tested,
    must be reimplemented by each colour appearance model test sub-class.
    """

    LIMITED_FIXTURES = None
    """
    Limited list of fixtures to test the colour appearance model against.
    """

    OUTPUT_ATTRIBUTES = None
    """
    Binding the fixture attributes to the colour appearance model
    specification attributes, must be reimplemented by each colour appearance
    model test sub-class.
    """

    @staticmethod
    def load_fixtures(file_name, fixtures_directory='fixtures'):
        """
        Loads the fixtures data with given name.

        Parameters
        ----------
        file_name : unicode
            '.csv' fixture file name.
        fixtures_directory : unicode
            Relative directory path containing the '.csv' fixtures files.

        Returns
        -------
        list
            Fixtures data as a *list* of *dict* where each *dict* is a fixture
            case.
        """

        path = os.path.dirname(__file__)
        with open(os.path.join(path,
                               fixtures_directory,
                               file_name)) as in_file:
            result = []
            for case_data in csv.DictReader(in_file):
                for key in case_data:
                    try:
                        case_data[key] = float(case_data[key])
                    except ValueError:
                        pass
                result.append(case_data)
            return result

    @abstractmethod
    def get_output_specification_from_data(self, data):
        """
        Returns the colour appearance model output specification from given
        fixture data.

        Parameters
        ----------
        data : list
            Tested colour appearance model fixture data.

        Returns
        -------
        *_Specification
            Tested colour appearance model specification.
        """

        pass

    def check_specification_attribute(self, case, data, attribute, expected):
        """
        Tests given colour appearance model specification attribute value.

        Parameters
        ----------
        case : int
            Fixture case number.
        data : dict.
            Fixture case data.
        attribute : unicode.
            Tested attribute name.
        expected : numeric.
            Expected attribute value.

        Returns
        -------
        None
        """

        specification = self.get_output_specification_from_data(data)
        value = getattr(specification, attribute)

        error_message = (
            'Parameter "{0}" in test case "{1}" does not match target value.\n'
            'Expected: "{2}" \n'
            'Received "{3}"').format(attribute, case, expected, value)

        assert_allclose(value,
                        expected,
                        err_msg=error_message,
                        rtol=0.01,
                        atol=0.01,
                        verbose=False)

        assert_almost_equal(value,
                            expected,
                            decimal=1,
                            err_msg=error_message)

    def check_model_consistency(self, data, output_attributes):
        """
        Checks the colour appearance model consistency with the tested colour
        appearance model fixture case data.

        Parameters
        ----------
        data : list
            Tested model fixture case data.
        output_attributes : dict.
            Fixture case data parameters to the colour appearance model
            specification output binding.

        Returns
        -------
        tuple
        """

        for data_attr, specification_attr in sorted(output_attributes.items()):
            yield (self.check_specification_attribute,
                   data.get('Case'),
                   data,
                   specification_attr,
                   data[data_attr])


    def __get_fixtures(self):
        """
        Returns the fixtures case for tested colour appearance model and
        filter them accordingly with
        :attr:`ColourAppearanceModelTest.LIMITED_FIXTURES` value.

        Returns
        -------
        list
            Filtered fixtures case data.
        """

        fixtures = self.load_fixtures(self.FIXTURE_BASENAME)
        if self.LIMITED_FIXTURES is not None:
            fixtures = [fixtures[index] for index in self.LIMITED_FIXTURES]
        return fixtures

    def test_forward_examples(self):
        """
        Tests the forward colour appearance model implementation.

        Returns
        -------
        tuple
        """

        for data in self.__get_fixtures():
            for test in self.check_model_consistency(data,
                                                     self.OUTPUT_ATTRIBUTES):
                yield test

    @unittest.skip
    def test_parallel_forward_examples(self):
        """
        Not sure about this guy :)
        """

        # TODO: Check with Michael for this dead code path.
        data = defaultdict(list)
        for fixture in self.__get_fixtures():
            for key, value in fixture.items():
                data[key].append(value)

        for key in data:
            data[key] = numpy.array(data[key])

        for test in self.check_model_consistency(
                data, self.OUTPUT_ATTRIBUTES):
            yield test


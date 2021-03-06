"""
Tests for NitPycker
"""

import io
import os
import unittest


__author__ = "Benjamin Schubert, ben.c.schubert@gmail.com"


NUMBER_OF_PROCESS = 4
TEST_SAMPLES = os.path.join(os.path.dirname(os.path.abspath(__file__)), "test_samples")


def run_tests(test_pattern: str, test_runner=unittest.TextTestRunner, **kwargs) -> str:
    """
    Allows  to run tests with a given TestRunner (intended to compare against unittest's test runner)

    :param test_pattern: pattern for the tests to run
    :param test_runner: TestRunner to use
    :param kwargs: arguments to pass to the test runner on creation
    :return: whether the test was successful, output of the tests
    """
    output = io.StringIO()
    tests = unittest.defaultTestLoader.discover(start_dir=TEST_SAMPLES, pattern=test_pattern)
    result = test_runner(stream=output, **kwargs).run(test=tests)

    return result.wasSuccessful(), output.getvalue()

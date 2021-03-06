#!/usr/bin/python3

"""
Nitpycker's main program

This mimics as closely as possible the behavior of the main unittest program
"""


import sys
from unittest import TestProgram, signals

from . import runner


__author__ = "Benjamin Schubert <ben.c.schubert@gmail.com>"


class NitPyckerProgram(TestProgram):
    """
    A command-line program that runs a set of tests

    this is primarily for making test modules conveniently executable.
    """
    def runTests(self):
        if self.catchbreak:
            signals.installHandler()
        if self.testRunner is None:
            self.testRunner = runner.ParallelRunner
        if isinstance(self.testRunner, type):
            try:
                testRunner = self.testRunner(verbosity=self.verbosity,
                                             failfast=self.failfast,
                                             warnings=self.warnings)
            except TypeError:
                # didn't accept the verbosity, buffer or failfast arguments
                testRunner = self.testRunner()
        else:
            # it is assumed to be a TestRunner instance
            testRunner = self.testRunner
        result = testRunner.run(self.test)
        if self.exit:
            sys.exit(not result.wasSuccessful())


main = NitPyckerProgram

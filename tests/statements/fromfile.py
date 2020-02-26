#!/usr/bin/env python3

import os.path

from tests import Test
from parsers import Parser
from backends import Z3Backend

class FromFileTest(Test):
    testfile = "tests/statements/fromfile.lmod"

    @staticmethod
    def run():
        parser = Parser(pwd=os.path.dirname(os.path.realpath(__file__)))
        parser.parse_file(FromFileTest.testfile)

        backend = Z3Backend()
        backend.exec_statements(parser.statements)
        solver = backend.solver
        model = backend.model

        assert model, "Model unsat. Test failed"

        testcase = backend.generate_testcase(varname="file")
        assert(testcase[5:5+10] == b"1337133713")

        return True

if __name__ == "__main__":
    FromFileTest.run()
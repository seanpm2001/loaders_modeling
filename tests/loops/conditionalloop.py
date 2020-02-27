#!/usr/bin/env python3
import z3

from tests import Test
from parsers import Parser
from backends import Z3Backend

class ConditionalLoopTest(Test):
    testfile = "tests/loops/conditionalloop.lmod"

    @staticmethod
    def run():
        parser = Parser()
        parser.parse_file(ConditionalLoopTest.testfile)

        backend = Z3Backend()
        backend.exec_statements(parser.statements)
        solver = backend.solver
        model = backend.model

        assert model, "Model unsat. Test failed"

        testcase = backend.generate_testcase()
        expected = b'\x01' * 4
        assert(testcase[4:8] == expected)

if __name__ == "__main__":
    ConditionalLoopTest.run()

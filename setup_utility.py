
# TODO move to a separate setput utility project

from setuptools.command.test import test as TestCommand
from setuptools_behave import behave_test 
import sys
import os
from setuptools import Command
import glob

try:
    from setupext import janitor
    CleanCommand = janitor.CleanCommand
except ImportError:
    CleanCommand = None

BehaveTestCommand = behave_test

class ToxCommand(TestCommand):
    """
    Based on https://testrun.org/tox/latest/example/basic.html#integration-with-setuptools-distribute-test-commands
    """
    user_options = [('tox-args=', 'a', "Arguments to pass to tox")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.tox_args = None

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import tox
        import shlex
        errno = tox.cmdline(args=shlex.split(self.tox_args))
        sys.exit(errno)    


class LicenseHeaderCommand(Command):
    """
    Adds a standard copyright header to all source files.
    """
    description = 'add standard license header to all source files'
    user_options = [
        ('header-file', 'f', 'header license file'),
        ('extension', 'e', 'source file extension')
        ]

    def initialize_options(self):
        self.header_file = 'HEADER'
        self.extension = '.py'

    def finalize_options(self):
        assert self.header_file is not None, 'header_file is required'
        assert self.extension is not None, 'extension is required'

    def run(self):
        assert os.path.isfile(self.header_file), "header file '%s' is not a file" % self.header_file
        for filename in glob.iglob("**/*.py", recursive=True):
            print(filename)
            with open(filename, 'r') as file:
                lines = file.readlines()
            output = []
            phases = ('adding_hashbangs', 
                      'removing_previous_comments', 
                      'adding_header', 
                      'adding_source')
            phase = phases[0] 
            for line in lines:
                assert phase in phases, '%s not in %s' % (phase, phases)
                if phase == phases[0]:
                    if line.startswith('#!'):
                        output.append(line)
                    else:
                        phase = phases[1]
                if phase == phases[1]:
                    if line.startswith('#'):
                        pass
                    else:
                        phase = phases[2]
                if phase == phases[2]:
                    with open(self.header_file, 'r') as header_file:
                        output.extend(['# ' + l for l in header_file.readlines()])
                    phase = phases[3]
                if phase == phases[3]:
                    output.append(line)    
            print(output)
            
                    


from . import parser
from Naked.toolshed.shell import execute_js, muterun_js

parse('input.js')
success = execute_js('input.js')


#!/usr/bin/env python3
#
#  __init__.py
"""
CircuitPython library for controlling latching relays.
"""
#
#  Copyright © 2021 Dominic Davis-Foster <dominic@davis-foster.co.uk>
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
#  EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
#  MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
#  IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
#  DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
#  OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE
#  OR OTHER DEALINGS IN THE SOFTWARE.
#

# stdlib
import digitalio  # type: ignore  # nodep (CircuitPython builtin)
import time
from microcontroller import Pin  # type: ignore  # nodep (CircuitPython builtin)

__author__: str = "Dominic Davis-Foster"
__copyright__: str = "2021 Dominic Davis-Foster"
__license__: str = "MIT License"
__version__: str = "0.0.0"
__email__: str = "dominic@davis-foster.co.uk"

__all__ = ["LatchingRelay"]


class LatchingRelay:
	"""
	Represents a latching relay.

	:param on_pin: The pin which will turn the relay on when set high.
	:param off_pin: The pin which will turn the relay off when set high.
	"""

	def __init__(self, on_pin: Pin, off_pin: Pin):
		self._on = digitalio.DigitalInOut(on_pin)
		self._on.switch_to_output()

		self._off = digitalio.DigitalInOut(off_pin)
		self._off.switch_to_output()

	def turn_on(self) -> None:
		"""
		Turn the relay on.
		"""

		self._off.value = False
		self._on.value = True
		time.sleep(0.01)
		self._on.value = False

	def turn_off(self) -> None:
		"""
		Turn the relay off.
		"""

		self._on.value = False
		self._off.value = True
		time.sleep(0.01)
		self._off.value = False

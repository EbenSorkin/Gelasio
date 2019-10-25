from __future__ import print_function, division, absolute_import


class BooleanOperationsError(Exception):
    """Base BooleanOperations exception"""


class InvalidContourError(BooleanOperationsError):
    """Raised when any input contour is invalid"""


class InvalidSubjectContourError(InvalidContourError):
    """Raised when a 'subject' contour is not valid"""


class InvalidClippingContourError(InvalidContourError):
    """Raised when a 'clipping' contour is not valid"""


class OpenContourError(BooleanOperationsError):
    """Raised when any input contour is open"""


class ExecutionError(BooleanOperationsError):
    """Raised when clipping execution fails"""

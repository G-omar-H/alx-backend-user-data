#!/usr/bin/env python3
"""
filtered_logger.py
"""

import re
from typing import List
import logging


def filter_datum(
        fields: List[str],
        redaction: str,
        message: str,
        separator: str) -> str:
    """_summary_

    Args:
        fields (list): representing all fields to obfuscate
        redaction (str):representing by what the field will be obfuscated
        message (str): representing the log line
        separator (str):  by which character is separating all fields

    Returns:
        str: the log message obfuscated:
    """
    return re.sub(
        f'({"|".join(fields)})=[^{separator}]*',
        lambda m: f'{m.group(1)}={redaction}',
        message)


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        method to filter values in incoming log records
        using filter_datum. Values for
        fields in fields should be filtered.

        Args:
            record (logging.LogRecord): _description_

        Returns:
            str: _description_
        """
        message = super(RedactingFormatter, self).format(record)
        return filter_datum(
            self.fields,
            self.REDACTION,
            message,
            self.SEPARATOR)

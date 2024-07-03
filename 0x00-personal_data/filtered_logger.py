#!/usr/bin/env python3
"""
filtered_logger.py
"""

import re
from typing import List


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

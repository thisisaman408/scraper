"""
__init__.py file for my_scraper folder
"""

from .utils.logging import get_logger, set_verbosity_info

logger = get_logger(__name__)
set_verbosity_info()

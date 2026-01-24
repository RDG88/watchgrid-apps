"""
Data module for INTERCEPT.
Contains OUI database and other data utilities.
"""

from .oui import get_manufacturer, update_oui_database

__all__ = ['get_manufacturer', 'update_oui_database']

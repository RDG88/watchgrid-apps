"""
OUI (Organizationally Unique Identifier) lookup module for WiFi device manufacturers.
This module provides functionality to identify device manufacturers from MAC addresses.
"""

import os
import urllib.request
import logging

logger = logging.getLogger(__name__)

# OUI database - maps MAC prefixes to manufacturers
OUI_DATABASE = {}
OUI_FILE = os.path.join(os.path.dirname(__file__), 'oui.txt')
OUI_URL = 'http://standards-oui.ieee.org/oui/oui.txt'


def download_oui_database():
    """Download the latest OUI database from IEEE."""
    try:
        logger.info("Downloading OUI database from IEEE...")
        urllib.request.urlretrieve(OUI_URL, OUI_FILE)
        logger.info(f"OUI database downloaded to {OUI_FILE}")
        return True
    except Exception as e:
        logger.error(f"Failed to download OUI database: {e}")
        return False


def load_oui_database():
    """Load the OUI database from file."""
    global OUI_DATABASE
    
    if not os.path.exists(OUI_FILE):
        logger.warning(f"OUI database file not found at {OUI_FILE}")
        if not download_oui_database():
            logger.warning("Using empty OUI database")
            return
    
    try:
        with open(OUI_FILE, 'r', encoding='utf-8', errors='ignore') as f:
            for line in f:
                if '(hex)' in line:
                    parts = line.split('(hex)')
                    if len(parts) >= 2:
                        mac_prefix = parts[0].strip().replace('-', ':').lower()
                        manufacturer = parts[1].strip()
                        OUI_DATABASE[mac_prefix] = manufacturer
        
        logger.info(f"Loaded {len(OUI_DATABASE)} OUI entries")
    except Exception as e:
        logger.error(f"Failed to load OUI database: {e}")


def get_manufacturer(mac_address):
    """
    Get the manufacturer name for a given MAC address.
    
    Args:
        mac_address (str): MAC address in format XX:XX:XX:XX:XX:XX
        
    Returns:
        str: Manufacturer name or "Unknown" if not found
    """
    if not mac_address:
        return "Unknown"
    
    # Ensure OUI database is loaded
    if not OUI_DATABASE:
        load_oui_database()
    
    # Normalize MAC address format
    mac = mac_address.lower().replace('-', ':')
    
    # Extract the OUI (first 3 octets)
    parts = mac.split(':')
    if len(parts) < 3:
        return "Unknown"
    
    oui = ':'.join(parts[:3])
    
    # Look up manufacturer
    manufacturer = OUI_DATABASE.get(oui, "Unknown")
    
    return manufacturer


def update_oui_database():
    """Download and update the OUI database."""
    if download_oui_database():
        load_oui_database()
        return True
    return False


# Initialize the database on module import
try:
    load_oui_database()
except Exception as e:
    logger.error(f"Failed to initialize OUI database: {e}")

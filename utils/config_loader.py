# utils/config_loader.py
"""
This module loads configuration settings from the config file.
"""

import os
import json
from typing import Dict, Any

def load_config(config_path: str = None) -> Dict[str, Any]:
    """
    Load configuration settings from the config file.
    
    Args:
        config_path: Path to the configuration file. If None, defaults to 'config/config.json'.
        
    Returns:
        A dictionary containing configuration settings.
    """
    if config_path is None:
        config_path = os.path.join('config', 'config.json')
    
    # Check if config file exists
    if not os.path.exists(config_path):
        # Return default configuration if file doesn't exist
        return {
            "api_key": "mock_api_key",
            "model": "gpt-3.5-turbo",
            "temperature": 0.7,
            "max_tokens": 1000,
            "story_domains": ["sorting algorithms", "database indexing", "software design patterns", "software testing"]
        }
    
    # Load configuration from file
    try:
        with open(config_path, 'r', encoding='utf-8') as file:
            config = json.load(file)
        return config
    except (json.JSONDecodeError, UnicodeDecodeError, IOError) as e:
        print(f"Error loading configuration: {e}")
        # Return default configuration on error
        return {
            "api_key": "mock_api_key",
            "model": "gpt-3.5-turbo",
            "temperature": 0.7,
            "max_tokens": 1000,
            "story_domains": ["sorting algorithms", "database indexing", "software design patterns", "software testing"]
        }
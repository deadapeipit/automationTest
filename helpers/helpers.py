import yaml
import os

# Function to load configuration from YAML file
def load_config(config_file="config/config.yaml"):
    """Load and return the configuration from the YAML file."""
    if not os.path.exists(config_file):
        raise FileNotFoundError(f"Config file {config_file} not found!")

    with open(config_file, 'r') as file:
        config = yaml.safe_load(file)
        
    return config

# Example function to get the URL from config
def get_url(config):
    """Get the URL from the loaded config."""
    return config.get('url', 'https://default.com')

# Example function to get the timeout value from config
def get_timeout(config):
    """Get the timeout from the loaded config."""
    return config.get('timeout', 10)  # Default to 10 if not specified

# Example function to get headless option from config
def get_headless(config):
    """Get the headless mode option."""
    return config.get('headless', True)  # Default to True

# Example function to get the log file name from config
def get_logfile(config):
    """Get the log file path from the loaded config."""
    return config.get('logfile', 'test_log.log')

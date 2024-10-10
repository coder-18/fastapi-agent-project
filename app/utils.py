import yaml


def load_config(config_file):
    """
    Generic function to load configuration from a YAML file.

    Args:
        config_file (str): Path to the YAML configuration file.

    Returns:
        dict: Parsed configuration data from the YAML file,
        or None if an error occurs.
    """
    try:
        with open(config_file, "r") as file:
            config = yaml.safe_load(file)
        return config
    except FileNotFoundError:
        print(f"Error: {config_file} not found.")
        return None
    except yaml.YAMLError as e:
        print(f"Error parsing {config_file}: {e}")
        return None

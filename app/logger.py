import logging
import logging.config
import yaml


def setup_logging(default_path="logging_config.yaml"):
    """
    Setup logging configuration from a YAML file.

    Args:
        default_path (str): Path to the logging configuration file.
    """
    try:
        with open(default_path, "r") as f:
            config = yaml.safe_load(f.read())
        logging.config.dictConfig(config)
    except Exception as e:
        print(f"Error loading logging configuration: {e}")
        logging.basicConfig(level=logging.DEBUG)


# Call setup logging when the module is imported
setup_logging()

# Get a logger object
logger = logging.getLogger("app_logger")

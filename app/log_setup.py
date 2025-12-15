import logging

# Temporary static log level (we can wire env later)
LOG_LEVEL = "INFO"

# Basic logging config
logging.basicConfig(
    level=LOG_LEVEL,
    format="%(asctime)s [%(levelname)s] (%(name)s) %(message)s",
)

def get_logger(name: str) -> logging.Logger:
    """Return a logger with default configuration."""
    return logging.getLogger(name)

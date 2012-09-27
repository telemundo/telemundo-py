VERSION = (0, 1, 1, 'beta', 0)

def get_version(*args, **kwargs):
    # Don't litter telemundo/__init__.py with all the get_version stuff.
    # Only import if it's actually called.
    from telemundo.utils.version import get_version
    return get_version(*args, **kwargs)

# Reflector Integration in Archinstall

## Overview

This feature adds support for using **reflector** to automatically generate optimized mirrorlists during Arch Linux installation. Reflector is a Python script that can automatically retrieve and rank Arch Linux mirrors according to your preferences.

## Features

- **Automatic Mirror Selection**: Use reflector to automatically select the best mirrors based on your criteria
- **Country Selection**: Choose specific countries for mirror selection (e.g., Brazil, Chile)
- **Protocol Filtering**: Select preferred protocols (HTTP, HTTPS, FTP, RSYNC)
- **Freshness Control**: Set age limits to only use recently synchronized mirrors
- **Performance Optimization**: Sort mirrors by rate, score, delay, or other criteria
- **Customizable**: Configure number of mirrors, age limits, and sorting preferences

## Usage

### Through the GUI Menu

1. Run `archinstall`
2. Navigate to the **Mirror regions** menu
3. Select **"Use reflector"** option
4. Configure your preferences:
   - Enable/disable reflector
   - Select countries (e.g., Brazil, Chile, United States)
   - Choose protocols (HTTPS recommended)
   - Set age limit in hours
   - Set number of mirrors to use
   - Choose sorting method

### Command Line Equivalent

The reflector configuration generates commands equivalent to:

```bash
sudo reflector --verbose --country Brazil,Chile --protocol https --age 12 --latest 20 --sort rate --save /etc/pacman.d/mirrorlist
```

### Configuration Options

| Option | Description | Default | Example |
|--------|-------------|---------|---------|
| **Countries** | Comma-separated list of countries | None | Brazil,Chile,Germany |
| **Protocols** | Network protocols to use | HTTPS | https,http |
| **Age** | Maximum mirror age in hours | 12 | 12 |
| **Latest** | Number of mirrors to select | 20 | 20 |
| **Sort Order** | Sorting criteria | rate | rate, score, delay, age |

### Programming Interface

```python
from archinstall.lib.models.mirrors import (
    MirrorConfiguration,
    ReflectorConfiguration,
    ReflectorProtocol,
    ReflectorSortOrder,
)

# Create reflector configuration
reflector_config = ReflectorConfiguration(
    enabled=True,
    countries=['Brazil', 'Chile'],
    protocols=[ReflectorProtocol.HTTPS],
    age=12,
    latest=20,
    sort_order=ReflectorSortOrder.Rate,
    verbose=True
)

# Add to mirror configuration
mirror_config = MirrorConfiguration()
mirror_config.reflector = reflector_config

# Apply during installation
installer.set_mirrors(mirror_config)
```

## Benefits

1. **Automated Optimization**: No need to manually select and test mirrors
2. **Location-Aware**: Automatically prefer mirrors in selected countries
3. **Fresh Mirrors**: Only use recently synchronized mirrors
4. **Performance**: Automatically sort by connection speed or reliability
5. **Convenience**: Set-and-forget mirror configuration

## Requirements

- Reflector package (automatically installed if not present)
- Internet connection during installation
- Arch Linux installation environment

## Fallback Behavior

If reflector fails for any reason, the system automatically falls back to the traditional manual mirror selection method, ensuring your installation can continue.

## Example Configurations

### Basic Setup (User's Request)
- Countries: Brazil, Chile
- Protocol: HTTPS
- Age: 12 hours
- Latest: 20 mirrors
- Sort: By rate

### Performance-Focused
- Countries: Your local countries
- Protocol: HTTPS
- Age: 6 hours
- Latest: 10 mirrors
- Sort: By score

### Reliability-Focused
- Countries: Multiple nearby countries
- Protocols: HTTPS, HTTP
- Age: 24 hours
- Latest: 30 mirrors
- Sort: By delay

## Technical Details

The implementation includes:
- `ReflectorConfiguration` class for managing settings
- Integration with existing mirror management system
- Automatic reflector installation if needed
- Command generation and execution
- Error handling and fallback mechanisms
- Full integration with archinstall's configuration system

This feature makes mirror management much more user-friendly while providing the flexibility to customize according to specific needs and geographic locations.

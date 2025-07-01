#!/usr/bin/env python3
"""
Example usage of the new reflector functionality in archinstall.

This example shows how to configure and use reflector to automatically
generate an optimized mirrorlist based on selected countries.
"""

from archinstall.lib.models.mirrors import (
    MirrorConfiguration,
    ReflectorConfiguration,
    ReflectorProtocol,
    ReflectorSortOrder,
)


def example_reflector_configuration():
    """Example showing how to create a reflector configuration"""
    
    reflector_config = ReflectorConfiguration(
        enabled=True,
        countries=['Brazil', 'Chile'],
        protocols=[ReflectorProtocol.HTTPS],
        age=12,
        latest=20,
        sort_order=ReflectorSortOrder.Rate,
        verbose=True
    )
    
    mirror_config = MirrorConfiguration()
    mirror_config.reflector = reflector_config
    
    print("Reflector command that would be executed:")
    print(reflector_config.to_command_string())
    
    print("\nJSON configuration:")
    print(mirror_config.json())
    
    return mirror_config


def example_flexible_configuration():
    """Example showing a more flexible configuration"""
    
    reflector_config = ReflectorConfiguration(
        enabled=True,
        countries=['United States', 'Canada', 'Germany'],
        protocols=[ReflectorProtocol.HTTPS, ReflectorProtocol.HTTP],
        age=6,
        latest=10,
        sort_order=ReflectorSortOrder.Score, 
        verbose=True
    )
    
    mirror_config = MirrorConfiguration()
    mirror_config.reflector = reflector_config
    
    print("More flexible reflector configuration:")
    print(reflector_config.to_command_string())
    
    return mirror_config


if __name__ == "__main__":
    print("=== Archinstall Reflector Configuration Examples ===\n")
    
    print("1. Basic configuration (Brazil, Chile):")
    example_reflector_configuration()
    
    print("\n" + "="*50 + "\n")
    
    print("2. Flexible configuration (US, CA, DE):")
    example_flexible_configuration()
    
    print("\n=== How to use in archinstall ===")
    print("1. Run archinstall")
    print("2. Go to Mirror regions menu")
    print("3. Select 'Use reflector' option")
    print("4. Configure your countries and settings")
    print("5. The mirrorlist will be automatically generated during installation")

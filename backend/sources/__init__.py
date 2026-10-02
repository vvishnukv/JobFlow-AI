"""Plugin-based job source system for JobFlow-AI."""
from .registry import PluginRegistry, PluginConfig

__all__ = ["PluginRegistry", "PluginConfig"]

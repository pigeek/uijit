"""uijit - A2UI rendering for AI agents."""

__version__ = "0.1.0"

from uijit.canvas_manager import CanvasManager
from uijit.models import Surface, SurfaceState
from uijit.server import CanvasMCPServer

__all__ = [
    "CanvasManager",
    "CanvasMCPServer",
    "Surface",
    "SurfaceState",
]

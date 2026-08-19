from dataclasses import dataclass
from typing import Callable

from rfd.spd.airm import (
    airm_dist2,
    airm_exp,
    airm_parallel_transport,
)


@dataclass(frozen=True)
class GeometryOps:
    name: str
    exp: Callable
    transport: Callable
    dist2: Callable


AIRM_GEOMETRY = GeometryOps(
    name="airm",
    exp=airm_exp,
    transport=airm_parallel_transport,
    dist2=airm_dist2,
)

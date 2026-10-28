"""Riemannian Factor Dynamics: factor models for manifold-valued time series
whose baseline moves over time."""

from rfd._maths.geometry import AIRM_GEOMETRY, BW_GEOMETRY, SPHERE_GEOMETRY, GeometryOps
from rfd.model import RFDConfig, RFDFit, fit_rfd

__all__ = [
    "AIRM_GEOMETRY",
    "BW_GEOMETRY",
    "SPHERE_GEOMETRY",
    "GeometryOps",
    "RFDConfig",
    "RFDFit",
    "fit_rfd",
]

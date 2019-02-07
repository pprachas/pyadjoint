# flake8: noqa

import backend
from pyadjoint.adjfloat import AdjFloat
from .constant import Constant
from .dirichletbc import DirichletBC
if backend.__name__ != "firedrake":
    # Currently not implemented.
    from .expression import Expression, UserExpression, CompiledExpression
    # Shape AD specific imports, not implemented yet
    from .mesh import (Mesh, UnitSquareMesh,UnitIntervalMesh, IntervalMesh,
                       UnitCubeMesh, BoundaryMeshType)

from .function import Function

# Use pyadjoint AdjFloat for numpy.float64.
import numpy
from pyadjoint.overloaded_type import register_overloaded_type
from pyadjoint.adjfloat import AdjFloat
register_overloaded_type(AdjFloat, numpy.float64)


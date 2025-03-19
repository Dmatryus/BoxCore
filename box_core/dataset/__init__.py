"""__init__.py for the dataset module in the HypEx library.
This module defines data structures and roles used across the library for managing and manipulating experimental data.
"""

from .abstract import DatasetBase
from .dataset import Dataset, DatasetAdapter
from .roles import (
    InfoRole,
    DefaultRole,
    TargetRole,
    FeatureRole,
    GroupingRole,
    PreTargetRole,
    StatisticRole,
    StratificationRole,
    TreatmentRole,
    TempRole,
    TempTreatmentRole,
    TempGroupingRole,
    TempTargetRole,
    FilterRole,
    AdditionalMatchingRole,
    ABCRole,
    AdditionalTreatmentRole,
    AdditionalGroupingRole,
    AdditionalTargetRole,
    AdditionalPreTargetRole,
    default_roles,
)
from .experiment_data import ExperimentData
from .executor_state import ExecutorState, DatasetSpace

__all__ = [
    "Dataset",
    "ExperimentData",
    "InfoRole",
    "DefaultRole",
    "TargetRole",
    "FeatureRole",
    "GroupingRole",
    "PreTargetRole",
    "StratificationRole",
    "StatisticRole",
    "TreatmentRole",
    "FilterRole",
    "AdditionalMatchingRole",
    "TempRole",
    "TempTreatmentRole",
    "TempGroupingRole",
    "TempTargetRole",
    "AdditionalTreatmentRole",
    "AdditionalGroupingRole",
    "AdditionalTargetRole",
    "AdditionalPreTargetRole",
    "ABCRole",
    "default_roles",
    "DatasetBase",
    "DatasetAdapter",
    "ExecutorState",
    "DatasetSpace"
]

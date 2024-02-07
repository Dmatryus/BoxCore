from abc import ABC

import numpy as np

from hypex.utils.hypex_typings import (ABCRoleTypes, Any,
                                       StratificationRoleTypes,
                                       TargetRoleTypes, TreatmentRoleTypes)


class ABCRole(ABC):
    _role_name = "Abstract"

    def __init__(self, data_type: ABCRoleTypes = Any):
        self.data_type = data_type


class InfoRole(ABCRole):
    _role_name = "Info"


class StratificationRole(ABCRole):
    _role_name = "Stratification"

    def __init__(self, data_type: StratificationRoleTypes):
        super().__init__(data_type)


class GroupingRole(ABCRole):
    _role_name = "Grouping"


class TreatmentRole(ABCRole):
    _role_name = "Treatment"

    def __init__(self, data_type: TreatmentRoleTypes):
        super().__init__(data_type)


class TargetRole(ABCRole):
    _role_name = "Target"

    def __init__(self, data_type: TargetRoleTypes):
        super().__init__(data_type)


class FeatureRole(ABCRole):
    _role_name = "Feature"


class PreTargetRole(TargetRole):
    _role_name = "PreTarget"

    def __init__(self, data_type: TargetRoleTypes):
        super().__init__(data_type)


class DropRole(ABCRole):
    _role_name = "DropRole"


default_roles = {
    "info": InfoRole(),
    "feature": FeatureRole(),
    "treatment": TreatmentRole(np.float64),
    "grouping": GroupingRole(),
    "target": TargetRole(np.float64),
    "pretarget": PreTargetRole(np.float64),
    "drop": DropRole(),
    "stratification": StratificationRole(np.float64),
}
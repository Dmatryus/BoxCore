import enum


@enum.unique
class PipelineDataEnum(enum.Enum):
    groups = "groups"
    variables  =  "variables"
    additional_fields = "additional_fields"
    analysis_tables = "analysis_tables"

@enum.unique
class BackendsEnum(enum.Enum):
    pandas = "pandas"

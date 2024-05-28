import enum


@enum.unique
class PipelineDataEnum(enum.Enum):
    additional_fields = "additional_fields"
    analysis_tables = "analysis_tables"
    stats = "stats"


@enum.unique
class BackendsEnum(enum.Enum):
    pandas = "pandas"

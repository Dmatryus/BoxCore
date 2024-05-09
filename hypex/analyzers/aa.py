from typing import Dict, List, Any

from hypex.analyzers.abstract import Analyzer
from hypex.comparators import TTest, KSTest
from hypex.dataset import ExperimentData, Dataset
from hypex.dataset import StatisticRole
from hypex.utils import ExperimentDataEnum, BackendsEnum


class OneAASplitAnalyzer(Analyzer):
    def _set_value(self, data: ExperimentData, value, key=None) -> ExperimentData:
        return data.set_value(
            ExperimentDataEnum.analysis_tables,
            self.id,
            str(self.full_name),
            value,
        )

    def execute(self, data: ExperimentData) -> ExperimentData:
        analysis_tests: List[type] = [TTest, KSTest]
        executor_ids = data.get_ids(analysis_tests)

        analysis_data: Dict[str, float] = {}
        for c, spaces in executor_ids.items():
            analysis_ids = spaces.get("analysis_tables", [])
            if len(analysis_ids) > 0:
                t_data = data.analysis_tables[analysis_ids[0]].append(analysis_ids[1:])
                t_data.data.index = analysis_ids

                for f in ["p-value", "pass"]:
                    analysis_data[f"{c.__name__} {f}"] = t_data[f].mean()
        analysis_data["mean test score"] = (
            analysis_data["TTest p-value"] + 2 * analysis_data["KSTest p-value"]
        ) / 3
        analysis_data = Dataset.from_dict(
            [analysis_data],
            {f: StatisticRole() for f in analysis_data},
            BackendsEnum.pandas,
        )

        return self._set_value(data, analysis_data)

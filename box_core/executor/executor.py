from abc import abstractmethod, ABC
from copy import copy
from typing import Any, Dict, List, Optional, Sequence, Union, Tuple, Iterable

from ..dataset import (
    ABCRole,
    Dataset,
    ExperimentData,
    GroupingRole,
    FeatureRole,
    AdditionalMatchingRole,
    TargetRole,
    DatasetAdapter,
    ExecutorState,
    DatasetSpace,
)
from ..utils import (
    AbstractMethodError,
    ID_SPLIT_SYMBOL,
    SetParamsDictTypes,
    NotSuitableFieldError,
)
from ..utils.adapter import Adapter


class Executor(ABC):
    def _get_params_dict(self):
        return {k: str(v) for k, v in copy(self.__dict__).items()}

    def __init__(self, key: str = "", save_space: Optional[DatasetSpace] = None):
        self._state = ExecutorState(
            executor=self.__class__.__name__,
            parameters=self._get_params_dict(),
            key=key,
            save_space=save_space,
        )

    @property
    def state(self):
        return self._state

    def refresh_state(
        self, key: Optional[str] = None, save_space: Optional[DatasetSpace] = None
    ):
        if key is not None:
            self._state.key = key
        if save_space is not None:
            self._state.save_space = save_space
        self._state.set_params(self._get_params_dict())

    def check_and_setattr(self, params: Dict[str, Any]):
        for key, value in params.items():
            if key in self.__dir__():
                setattr(self, key, value)

    def set_params(self, params: SetParamsDictTypes) -> None:
        if isinstance(list(params)[0], str):
            self.check_and_setattr(params)
        elif isinstance(list(params)[0], type):
            for executor_class, class_params in params.items():
                if isinstance(self, executor_class):
                    self.check_and_setattr(class_params)
        else:
            raise ValueError(
                "params must be a dict of str to dict or a dict of class to dict"
            )
        self.refresh_state()

    def refresh_from_state(self, state: [ExecutorState, str]) -> None:
        self._state = ExecutorState.create_from_str(str(state))
        self.check_and_setattr(self._state.get_params_dict())

    @property
    def _is_transformer(self) -> bool:
        return False

    @abstractmethod
    def execute(self, data: ExperimentData) -> ExperimentData:
        raise AbstractMethodError


class Calculator(Executor, ABC):
    @classmethod
    def _pre_calc(cls, data: Dataset, **kwargs):
        return cls.calc(data, **kwargs)

    @staticmethod
    @abstractmethod
    def calc(data: Dataset, **kwargs) -> Any:
        raise AbstractMethodError

    def execute(self, data: ExperimentData) -> ExperimentData:
        return data.set_value(self.state, self._pre_calc(data.ds))


class Transformer(Executor, ABC):

    def __init__(
        self,
        reverse: bool = False,
        key: str = "",
        save_space: Optional[DatasetSpace] = None,
    ):
        super().__init__(key, save_space)
        self.reverse = reverse

    def _is_transformer(self) -> bool:
        return True

    @staticmethod
    @abstractmethod
    def transform(data: Dataset, **kwargs) -> Dataset:
        raise AbstractMethodError

    @staticmethod
    @abstractmethod
    def reverse_transform(data: Dataset, **kwargs) -> Dataset:
        raise AbstractMethodError

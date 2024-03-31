class RoleColumnError(Exception):
    def __init__(self, roles, columns):
        super().__init__(
            "Check your roles. All of them must be names of data columns. \n"
            f"Now roles have {roles} values and columns have {columns} values"
        )


class ConcatDataError(Exception):
    def __init__(self, data_type):
        super().__init__(f"Can only append Dataset to Dataset. Got {data_type}")


class ConcatBackendError(Exception):
    def __init__(self, other_backend, backend):
        super().__init__(
            f"Can only append datas with the same backends. Got {other_backend} expected {backend}"
        )


class SpaceError(Exception):
    def __init__(self, space):
        super().__init__(f"{space} is not a valid space")
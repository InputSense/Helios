from typing import Callable, Union


class persist:
    pass


def cv_ready() -> bool:
    pass


def cv_read(i: int, n: int = 0) -> Union[int, float]:
    pass


def set_val(button: int, val: float) -> None:
    pass


def set_val_for(self, button_val: Union[tuple, list[tuple]], duration: int = 0) -> None:
    pass


def get_actual(button: int) -> float:
    pass


def get_val(button: int) -> float:
    pass


def combo_run(combo: Callable) -> bool:
    pass


def system_time() -> float:
    pass


def elapsed_time() -> float:
    pass


def wait(ms: int) -> None:
    pass




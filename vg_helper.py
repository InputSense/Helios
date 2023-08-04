from typing import Callable, Union


# ======== Peristent memory types ========
class mem:
    pass


reg: dict



# ======== Virtual Gamepad specific ========


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


def get_prev(self, button: int) -> float:
    pass


def event_active(self, button: int) -> float:
    pass


def event_release(self, button: int) -> float:
    pass


def combo_run(combo: Callable) -> bool:
    pass


def system_time() -> float:
    pass


def elapsed_time() -> float:
    pass


def wait(ms: int) -> None:
    pass



# ======== Math functions ========


def abs(n: Union[int, float]) -> Union[int, float]:
    pass


def acos(n: float) -> float:
    pass


def asin(n: float) -> float:
    pass


def atan(n: float) -> float:
    pass


def atan2(n: float, m:float) -> float:
    pass


def ceil(n: Union[int, float]) -> int:
    pass


def clamp(n: Union[int, float], min_value: Union[int, float], max_value: Union[int, float]) -> Union[int, float]:
    pass


def cos(n: Union[int, float]) -> float:
    pass


def deg2rad(d: float) -> float:
    pass


def exp(n: Union[int, float]) -> Union[int, float]:
    pass


def floor(n: Union[int, float]) -> Union[int, float]:
    pass


def ilerp(a: float, b: float, t: float) -> float:
    pass


def lerp(a: float, b: float, t: float) -> float:
    pass


def log(n: float, b:float) -> float:
    pass


def log2(n: float) -> float:
    pass


def max(n) -> Union[int, float]:
    pass


def min(n) -> Union[int, float]:
    pass


def pow(n: Union[int, float], e: Union[int, float]) -> Union[int, float]:
    pass


def rad2deg(r: float) -> float:
    pass


def round(n: float, d: int) -> Union[int, float]:
    pass


def sin(n: float) -> float:
    pass


def sqrt(n: Union[int, float]) -> float:
    pass


def tan(n: Union[int, float]) -> float:
    pass









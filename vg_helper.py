from typing import Callable, Union


# ======== GUI specific ========


def label(title: str, text: str) -> None:
    pass


def checkbox(title: str, description: str = None, items: list = [], default_selection=0) -> list:
    pass


def radiobox(title: str, description: str = None, items: list = [], default_selection=0) -> int:
    pass


def combobox(title: str, description: str = None, items: list = []) -> str:
    pass


def spinbox(title: str, description: str = None, minimum: int = 0, maximum: int = 100, default_value: int = 50, step: int = 1) -> int:
    pass


def floatspinbox(title: str, description: str = None, minimum: float = 0.0, maximum: float = 100.0, default_value: float = 50.00, step: float = 0.1, decimals: int = 2) -> float:
    pass


def slider(title: str, description: str = None, orientation: str = "horizontal", minimum: int = 0, maximum: int = 100, default_value: int = 50) -> int:
    pass


def dial(title: str, description: str = None, minimum: int = 0, maximum: int = 100, default_value: int = 0) -> int:
    pass


def catalog(title: str, description: str = None, items: list = [], multi: bool = False) -> list:
    pass



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


def set_val_for(button_val: Union[tuple, list[tuple]], duration: int = 0) -> None:
    pass


def get_actual(button: int) -> float:
    pass


def get_val(button: int) -> float:
    pass


def get_prev(button: int) -> float:
    pass


def event_active(button: int) -> float:
    pass


def event_release(button: int) -> float:
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


def fmod(x: float, d: float) -> float:
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


def rand() -> float:
    pass


def round(n: float, d: int) -> Union[int, float]:
    pass


def sin(n: float) -> float:
    pass


def sqrt(n: Union[int, float]) -> float:
    pass


def tan(n: Union[int, float]) -> float:
    pass









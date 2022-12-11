from __future__ import annotations

__all__ = ["dataclass_transform"]

import typing


def dataclass_transform(
    *,
    eq_default: bool = True,
    order_default: bool = False,
    kw_only_default: bool = False,
    field_specifiers: tuple[typing.Type[typing.Any] | typing.Callable[..., typing.Any], ...] = (),
    **kwargs: typing.Any,
) -> typing.Callable[[typing.Any], typing.Any]:
    """Here is the source code ->
    https://github.com/python/cpython/blob/v3.11.0/Lib/typing.py#L3343."""

    def decorator(cls_or_fn):
        cls_or_fn.__dataclass_transform__ = {
            "eq_default": eq_default,
            "order_default": order_default,
            "kw_only_default": kw_only_default,
            "field_specifiers": field_specifiers,
            "kwargs": kwargs,
        }
        return cls_or_fn

    return decorator

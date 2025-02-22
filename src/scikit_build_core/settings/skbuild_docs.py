from __future__ import annotations

from .. import __version__
from .documentation import mk_docs
from .skbuild_model import ScikitBuildSettings

__all__ = ["mk_skbuild_docs"]


def __dir__() -> list[str]:
    return __all__


version = ".".join(__version__.split(".")[:2])


def mk_skbuild_docs() -> str:
    """
    Makes documentation for the skbuild model.
    """
    items = list(mk_docs(ScikitBuildSettings))
    for item in items:
        if item.name == "minimum-version":
            item.default = f'"{version}"  # current version'
        if item.name == "install.strip":
            item.default = "false"
        if item.name == "wheel.packages":
            item.default = '["src/<package>", "<package>"]'
    return "\n".join(str(item) for item in items)


if __name__ == "__main__":
    print(mk_skbuild_docs())  # noqa: T201

"""The application entry point."""

import argparse
from importlib.metadata import version
from typing import Final
from ._version import __version__


def app() -> None:
    """The application entry point."""

    parser: Final = argparse.ArgumentParser(
        description=(
            f"Python distribution example application "
            f"v{__version__}\n"
            "\n"
            "Copyright (c) 2025 maotek\n"
            "SPDX-License-Identifier: Apache-2.0\n"
            "\n"
            "https://github.com/maotek/package_example"
        ),
        formatter_class=argparse.RawTextHelpFormatter,
    )
    parser.add_argument(
        "-v",
        "--version",
        action="store_true",
        default=False,
        help="Display the version.",
    )
    parser.add_argument(
        "-i",
        "--input",
        action="store_true",
        default=False,
        help="Await any key before exiting.",
    )

    args: Final = parser.parse_args()

    if args.version is True:
        print(__version__)
        raise SystemExit(0)

    print("Hello, World!")

    if args.input is True:
        input("Press any key to exit...")

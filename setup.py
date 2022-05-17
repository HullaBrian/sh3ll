import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="sh3ll",
    version="1.2.2",  # Be sure to update the version in __init__.py as well
    description="An interactive shell application maker",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/HullaBrian/sh3ll.git",
    author="HullaBrian",
    author_email="",
    license="",
    classifiers=[],
    packages=["sh3ll"],
    include_package_data=True,
    install_requires=["art"],
    entry_points={
        "console_scripts": [
            "sh3ll=sh3ll.main:IS",
        ]
    },
)
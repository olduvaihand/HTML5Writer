from setuptools import setup, find_packages
import os

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, "README.txt")).read()
CHANGES = open(os.path.join(here, "CHANGES.txt")).read()

version = "1.0"

install_requires = [
    "docutils"
    ]

setup(
    name="HTML5Writer",
    version="0.1",
    description="HTML5 writer for docutils",
    long_description=README + "\n\n" + CHANGES,
    classifiers=[
        ],
    author="Ben Trofatter",
    author_email="bentrofatter@gmail.com",
    url="",
    packages=find_packages("lib"),
    package_dir={"": "lib"},
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    entry_points="""
    [console_scripts]
        rst2html5=html5writer.scripts:rst2html5
        test_html5=html5writer.scripts:test
    """
)

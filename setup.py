from setuptools import setup


def readme():
    """Open up the readme and use the text for the long description."""
    with open("README.md") as f:
        return f.read()


setup(
    name="projectdiffview",
    version="0.1.0",
    description="Utility to make managing project directories easier.",
    long_description=readme(),
    entry_points={
        "console_scripts": [
            "project-diff-cli=projectdiffview.cli:cli",
            "project-diff=projectdiffview.__main__:main",
        ],
    },
    packages=["projectdiffview",],
    package_dir={"projectdiffview": "projectdiffview"},
    include_package_data=True,
    install_requires=["Click", "PySide2"],
    license="MIT",
    zip_safe=False,
    keywords="projectdiffview",
    classifiers=["Programming Language :: Python :: 3", "Programming Language :: Python :: 3.7",],
)

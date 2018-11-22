from setuptools import setup, find_packages
import versioneer

tests_require = ["pytest", "pytest-runner", "pytest-cov", "coverage", "coveralls"]

dev_require = [
    "versioneer",
    "black",
    "nbstripout",
    "nbdime",
    "twine",
    "sphinx_rtd_theme",
    "sphinx-autodoc-annotation",
    #'mock',
]

db_require = ["pyodbc", "psycopg2"]

spatial_require = ["owslib", "geojson"]  # this needs pyproj -> C compiler

with open("README.md", "r") as src:
    LONG_DESCRIPTION = src.read()

setup(
    name="pyrolite",
    description="Tools for geochemical data analysis.",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    version=versioneer.get_version(),
    url="https://github.com/morganjwilliams/pyrolite",
    author="Morgan Williams",
    author_email="morgan.williams@csiro.au",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "Natural Language :: English",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Scientific/Engineering",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    packages=find_packages(exclude=["test*"]),
    install_requires=[
        "pathlib",
        "numpy",
        "scipy",
        "scikit-learn",
        "mpmath",
        "sympy",
        "pandas",
        "matplotlib",
        "periodictable",
        "xlrd",
        "python-ternary",
        "requests",
        "dicttoxml",
        "xmljson",
        "beautifulsoup4",
    ],
    extras_require={
        "dev": dev_require + tests_require,
        "spatial": spatial_require,
        "db": db_require,
    },
    tests_require=tests_require,
    test_suite="test",
    package_data={"pyrolite": ["data/*"]},
    include_package_data=True,
    license="CSIRO Modifed MIT/BSD",
    cmdclass=versioneer.get_cmdclass(),
)

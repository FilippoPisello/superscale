from setuptools import find_packages, setup

with open("README.md", "r") as file:
    long_description = file.read()

setup(
    name="measurehero",
    version="0.0.1",
    description="Extract measurement information from strings.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/FilippoPisello/MeasureHero",
    author="Filippo Pisello",
    author_email="filippo.pisello@live.it",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(exclude="tests"),
    include_package_data=True,
    python_requires=">=3.7",
)

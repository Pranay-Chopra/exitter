import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="exitter-Pranay-Chopra",
    version="1.0.1",
    author="Pranay Chopra",
    author_email="pranaychopra2007@gmail.com",
    description="A package which helps you code the exit loop in python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Pranay-Chopra/exitter",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=1.1',
)
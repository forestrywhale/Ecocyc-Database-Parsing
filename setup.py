import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name = 'Ecocyc_Parse',
    version = '0.0.1',
    url = 'https://github.com/kikyo91/Ecocyc-Database-Parsing',
    author = 'kikyo91',
    author_email = 'huijingwang91@gmail.com',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages = setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

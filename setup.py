import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="compareversion-likeclem30", # Replace with your own username
    version="0.0.1",
    author="William Aaron",
    author_email="likeclem30@gmail.com",
    description="Compare two version string",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/likeclem30/CompareVersionString",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
    
setuptools.setup(
    name="morpyengine",
    version="0.0.2",
    author="Morgiver",
    author_email="me@morgiver.net",
    description="A small Neural Network",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Morgiver/morpyneural",
    project_urls={
        "Bug Tracker": "https://github.com/Morgiver/morpyneural/issues",
    },
    install_requires=[
        'numpy',
        'numba'
    ],
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "Licence :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.9",
)

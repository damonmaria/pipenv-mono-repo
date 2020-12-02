import setuptools

setuptools.setup(
    name="local",
    version="1.0.0",
    description="Our local monorepo packages",
    packages=setuptools.find_packages(where="local"),
    package_dir={"": "local"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Other/Proprietary License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)

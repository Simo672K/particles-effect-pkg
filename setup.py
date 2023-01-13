import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description= fh.read()

setuptools.setup(
    name="particles-effect-pkg",
    version="0.0.1",
    author="Example Author",
    author_email="mohammed.hakmiii555@gmail.com",
    description="particles effect",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Simo672K/particles-effect-pkg",
    project_urls={
    "Bug Tracker": "https://github.com/Simo672K/particles-effect-pkg/issues",
    },
    classifiers=[
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
import setuptools

setuptools.setup(
    name="my_minipack",
    version="1.0.0",
    summary = "How to create a package in python",
    author="adconsta",
    author_email="adconsta@example.com",
    classifiers=[
        "Developpemnt Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Students",
        "Topic :: Education",
        "Topic :: Howto",
        "Topic :: Package",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3 :: Only",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)

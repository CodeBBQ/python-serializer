from setuptools import find_packages, setup

setup(
    name="serializer",
    version="1.0.0",
    description="""
      This is a package to serialize execution of code over multiple processes.
      """,
    author="Benjamin Bastian-Querner",
    author_email="benjamin.bastian@desy.de",
    packages=find_packages(),
    # scripts=["bin/ioblocker"],
)

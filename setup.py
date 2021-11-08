from setuptools import setup
import re

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

version = ""
with open("nextcord/ext/events/__init__.py") as f:
    version = re.search(r"^__version__\s*=\s*[\'\"]([^\'\"]*)[\'\"]", f.read(), re.MULTILINE).group(1)

with open("README.rst", encoding="utf-8") as f:
    readme = f.read()

setup(
    name="nextcord-ext-events",
    author="VincentRPS",
    python_requires=">=3.8.0",
    url="https://github.com/nextcord-ext/events",
    version=version,
    packages=["nextcord.ext.events"],
    license="Apache Software License",
    description="Custom events derived from events dispatched by Discord. ",
    long_description=readme,
    long_description_content_type="text/x-rst",
    include_package_data=True,
    install_requires=requirements,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.8",
        "Topic :: Internet",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
    ]
)

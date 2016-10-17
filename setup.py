# qtdd setup.py
from setuptools import setup, find_packages
from qtdd import _version_


def readme():
    with open('README.md') as f:
        return f.read()

setup(
    name="qtdd",
    scripts=['scripts/qtdd'],
    include_package_data=True,
    package_data = {"qtdd": ["ui/*"]},
    packages=find_packages(),
    version=_version_,
    description="QT frontend to dd, to write a disk image to an USB mass storage device.",
    author="Martin Groenholdt",
    author_email="martin.groenholdt@gmail.com",
    url="https://groenholdt.net",
    download_url="https://github.com/deadbok/qtdd/releases/python3-qtdd" + _version_ + ".tgz",
    keywords=["os", "usb", "iso", "disk image", "write"],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Development Status :: 4 - Beta",
        "Environment :: X11 Applications :: Qt",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: POSIX :: Linux",
        "Topic :: System :: Operating System",
        "Topic :: Utilities",
        ],
    long_description=readme()
)

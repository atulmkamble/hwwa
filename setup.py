"""Setup for the hwwa package."""

import setuptools

with open('README.md') as f:
    README = f.read()

setuptools.setup(
    author="Atul",
    author_email="kambleatulm@gmail.com",
    name='hwwa',
    license="MIT",
    description='hwwa is a python package for demonstrating package deployment.',
    version='v0.0.1',
    long_description=README,
    url='https://github.com/atulmkamble/hwwa',
    packages=setuptools.find_packages(),
    python_requires=">=3.5",
    classifiers=[
        # Trove classifiers
        # (https://pypi.python.org/pypi?%3Aaction=list_classifiers)
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Intended Audience :: Developers',
    ],
)

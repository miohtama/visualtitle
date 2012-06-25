"""

    Declare a Python package visualtitle

    See

    * http://wiki.python.org/moin/Distutils/Tutorial

    * http://packages.python.org/distribute/setuptools.html#developer-s-

    * http://plone.org/products/plone/roadmap/247

"""

import os
from setuptools import setup

setup(name="visualtitle",
    version="0.1",
    long_description=open("README.rst").read() + "\n\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
    description="Separate content and navigation titles for Plone CMS",
    author="Mikko Ohtamaa",
    author_email="mikko@opensourcehacker.com",
    url="http://opensourcehacker.com",
    install_requires=["five.grok", "archetypes.schemaextender"],
    packages=['visualtitle'],
    classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
    ],
    license="GPL2",
    include_package_data=True,
    entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
)

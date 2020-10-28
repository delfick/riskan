from setuptools import setup, find_packages
from riskan import VERSION

# fmt: off

setup(
      name = "riskan"
    , version = VERSION
    , packages = find_packages(include="riskan.*", exclude=["tests*"])

    , install_requires =
      [ "ibis-framework[postgres]"
      ]

    , entry_points =
      { 'console_scripts' :
        [ 'riskan = riskan.executor:main'
        ]
      }
    )

# fmt: on

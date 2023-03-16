from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in railway_ticket_booking/__init__.py
from railway_ticket_booking import __version__ as version

setup(
	name="railway_ticket_booking",
	version=version,
	description="online ticket site",
	author="Lalit",
	author_email="lalitpatil99799@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)

from setuptools import setup, find_packages

short_description = "Component-based Learned Intermolecular Force Field"

try:
    with open("README.md", "r") as handle:
        long_description = handle.read()
except:
    long_description = short_description

setup(
    name='cliff',
    author='Jeff Schriber',
    author_email='jschriber7@gatech.edu',
    description=short_description,
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    package_data={'cliff':['cliff/models/large/adens/*.tar', 'cliff/models/large/hirsh/*.tar','cliff/models/large/mtp/*.tar']},
)

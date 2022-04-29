from setuptools import setup, find_packages

setup(
    name='giit-calc',
    version='1.0',
    description='Simple calculator',
    author='G.I.I.T team',
    author_email='xvalach12@stud.fit.vutbr.cz',
    license='GPL3',
    install_requires= ["debhelper", "python3-all", "python3-tk", "idle"],
    packages=find_packages(),
    entry_points=dict(
        console_scripts=['rq=src.main:display_quote']
    )
)
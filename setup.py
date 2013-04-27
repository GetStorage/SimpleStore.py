from distutils.core import setup

setup(
    name='SimpleStore.py',
    version='0.0.1',
    packages=['store'],
    requires=['requests', 'configparser'],
    url='http://getstorage.net',
    license='Public Domain',
    author='clone1018',
    author_email='luke@axxim.net',
    description='A simple python app to store files on Storage'
)

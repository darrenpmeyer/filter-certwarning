from setuptools import setup

setup(
    name='filter-certwarning',
    version='0.2',
    packages=['filter_certwarning'],
    install_requires=['urllib3'],
    url='',
    license='BSD 2-clause',
    author='Darren P Meyer',
    author_email='darren-at-darrenpmeyer.com',
    description='Decorators for filtering InsecureRequestWarnings in requests and urllib3 apps'
)

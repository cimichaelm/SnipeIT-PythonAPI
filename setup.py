from setuptools import setup

with open("README.rst","r") as fh:
	long_description = fh.read()
	
setup(name='snipeit',
      version='1.3.1',
	  long_description=long_description,
      long_description_content_type="text/markdown",
      description=("Python library to access the SnipeIT API"),
      url='https://github.com/cimichaelm/SnipeIT-PythonAPI',
      author='Jared Bloomer (Cox Automotive Inc.)',
      author_email='jared.bloomer@coxautoinc.com',
      license='MIT',
      packages=['snipeit'],
      install_requires=['requests','simplejson'],
      zip_safe=False)

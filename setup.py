from setuptools import setup, find_packages
from os import path
 
setup(
     name='smooth-demo',              # This is the name of the PyPI-package.
     packages = ['smooth-demo'],
     install_requires=['docopt', 'termcolor'],
     version='0.1',            # Update the version number for new releases
     description = 'Tool to automate giving a demo on command line',
     author='William Cannon',
     author_email='William.Cannon+smoothdemo@gmail.com',
     license='GPLv3.0',
     url='https://github.com/wcannon/smooth-demo',
     download_url='https://github.com/wcannon/smooth-demo/archive/smooth-demo.0.1.tar.gz',
     classifiers=[
         'Development Status :: 4 - Beta',
         'Environment :: Console',
         'Intended Audience :: Information Technology',
         'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
         'Natural Language :: English',
         'Operating System :: OS Independent',
         'Programming Language :: Python',
         'Topic :: Utilities'
         ],
     keywords = ['smooth', 'demo', 'type', 'slow'],
     scripts=['bin/smooth-demo']
 )

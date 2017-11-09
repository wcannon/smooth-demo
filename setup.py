from setuptools import setup
 
setup(
     name='smooth-demo',              # This is the name of the PyPI-package.
     packages = ['smooth-demo'],
     version='0.1',            # Update the version number for new releases
     description = 'Tool to automate giving a demo on command line',
     author='William Cannon',
     author_email='William.Cannon+smooth-demo@gmail.com',
     url='https://github.com/wcannon/smooth-demo',
     download_url='https://github.com/wcannon/smooth-demo/archive/smooth-demo.0.1.tar.gz',
     keywords = ['smooth', 'demo', 'type', 'slow'],
     scripts=['smooth-demo.py']        # The name of the scipt, and also the command for calling it
 )

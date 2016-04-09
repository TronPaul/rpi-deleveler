from setuptools import setup, find_packages

setup(name='rpi-deleveler',
      version='0.0.1',
      packages=find_packages(),
      url='',
      license='MIT',
      author='Mark McGuire',
      author_email='mark.b.mcg@gmail.com',
      description='Check/Fix h.264 levels for RaspberryPi 2',
      entry_points={
          'console_scripts': [
              'level-check = rpi_deleveler.level_check:main',
              'delevel = rpi_deleveler.delevel:main'
          ]
      })

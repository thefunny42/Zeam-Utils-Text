from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='zeam.utils.text',
      version=version,
      description="Text field for zeam.form",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      classifiers=[
        "Framework :: Zope3",
        "Programming Language :: Python",
        "Programming Language :: Zope",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='zeam form text fields raw restructured',
      author='Sylvain Viollon',
      author_email='thefunny@gmail.com',
      url='',
      license='BSD',
      package_dir={'': 'src'},
      packages=find_packages('src'),
      namespace_packages=['zeam', 'zeam.utils'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'zeam.form.base',
          'zeam.form.ztk',
          ],
      )

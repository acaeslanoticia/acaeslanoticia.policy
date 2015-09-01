from setuptools import setup, find_packages
import os

version = '0.1'

setup(name='acaeslanoticia.policy',
      version=version,
      description="Plone Policy product for ACA es la Noticia",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='plone4 policy product acalanoticia website',
      author='Leonardo J. Caballero G.',
      author_email='leonardocaballero@gmail.com',
      url='https://github.com/acaeslanoticia/acaeslanoticia.policy',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['acaeslanoticia'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'plone.api==1.3.3',
          # -*- Extra requirements: -*-
          'Products.Doormat==1.0',
          'brasil.gov.tiles',
          # 'acaeslanoticia.theme',
          'brasil.gov.tiles',
          'collective.disqus==2.0rc1',
          # 'collective.googlenews==1.0rc3',
          'collective.opendata==1.0a2',
          'collective.upload==1.0rc1',
          'ftw.avatar',
          'sc.social.like==2.2',
      ],
      extras_require={
          'test': [
              'plone.app.robotframework',
              'plone.app.testing [robot] >=4.2.2',
              'plone.browserlayer',
              'plone.testing',
              'robotsuite',
          ],
      },
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      setup_requires=["PasteScript"],
      paster_plugins=["ZopeSkel"],
      )

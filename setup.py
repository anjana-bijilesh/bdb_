from setuptools import setup, find_packages

setup(name='bdb_kafka_',
      version='0.1',
      description='kafka connection',
      url='https://github.com/anjana-bijilesh/bdb_',
      download_url='https://github.com/anjana-bijilesh/bdb_/archive/refs/tags/v1.0.0.tar.gz',
      author=' ',
      author_email=' ',
      keywords=['kafka'],
      license='MIT',
      packages=setuptools.find_packages(include=['kafka_connection', 'kafka_connection.*'])
      install_requires=['requests', 'confluent_kafka', 'logger', 'concurrent', ],

      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'Topic :: Software Development :: Build Tools',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
          'Programming Language :: Python :: 3.9',
          'Programming Language :: Python :: 3.10'
      ],
      )

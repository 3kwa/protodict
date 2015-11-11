from setuptools import setup


setup(
    name='protodict',
    description='a small Python library for 2 ways conversion between dicts '
        'and protocol buffers.',
    version='1.0.1',
    author='Eugene Van den Bulke',
    author_email='eugene.vandenbulke@gmail.com',
    url='https://github.com/3kwa/protodict',
    license='Public Domain',
    keywords=['protobuf', 'dict'],
    install_requires=['protobuf>=2.3.0'],
    package_dir={'':'src'},
    py_modules=['protodict'],
    #setup_requires=['protobuf>=2.3.0', 'nose>=1.0', 'coverage', 'nosexcover'],
    #test_suite = 'nose.collector',
    classifiers=[
        'Programming Language :: Python',
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: Public Domain',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)

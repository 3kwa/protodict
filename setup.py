from setuptools import setup
import distutils.command.bdist_conda


setup(
    name='protodict',
    description='A teeny Python library for creating Python dicts from '
        'protocol buffers and the reverse. Useful as an intermediate step '
        'before serialisation (e.g. to JSON).',
    version='0.1.1',
    author='Ben Hodgson',
    author_email='ben@benhodgson.com',
    url='https://github.com/3kwa/protodict',
    license='Public Domain',
    keywords=['protobuf', 'dict'],
    install_requires=['protobuf>=2.3.0'],
    package_dir={'':'src'},
    py_modules=['protodict'],
    setup_requires=['protobuf>=2.3.0', 'nose>=1.0', 'coverage', 'nosexcover'],
    test_suite = 'nose.collector',
    classifiers=[
        'Programming Language :: Python',
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: Public Domain',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)

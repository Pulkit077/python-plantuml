from setuptools import setup

setup(
    name='plantuml',
    version='0.3.0',
    description='',
    long_description=open('README.md', 'r').read(),
    url='https://github.com/dougn/python-plantuml/',
    author='Doug Napoleone, Samuel Marks, Eric Frederich',
    author_email='doug.napoleone+plantuml@gmail.com',
    license='BSD',
    py_modules=['plantuml'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: BSD License',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Utilities',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    install_requires=['httplib2'],
    keywords=['plantuml', 'uml']
)

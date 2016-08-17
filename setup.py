"""
Mugabits - Sudoku
----------
A python package for playing sudoku.
Please refer to the online documentation for details.
Links
`````
* `documentation : README.md`
"""

from setuptools import setup

setup(
    name='Sudoku',
    version='0.1.0',
    url='',
    license='BSD',
    author='Jose Mugaburu',
    author_email='mugabits@gmail.com',
    maintainer='Jose Mugaburu',
    maintainer_email='mugabits@gmail.com',
    description='A python module for playing sudoku',
    long_description=__doc__,
    test_suite='',
    zip_safe=False,
    platforms='any',
    tests_require=[ ],
    classifiers=[
        'Development Status :: 1 - Alpha',
        'Natural Language :: English',
        'Environment :: Web Server',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
	'Programming Language :: Python :: 3.5',
        'Topic :: Gaming :: Libraries :: Python Modules',
        'Topic :: Games',
        'Topic :: Sudoku',
        'Topic :: Battle',
	'Topic :: Applications'
    ],
    keywords='Sudoku games online-gaming battle',
    install_requires=[ ],
    py_modules=[ 'random',
                 'os',
                 ]
)

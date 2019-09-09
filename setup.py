from setuptools import setup,find_packages

def readme():
    with open('README.rst') as f:
        return f.read()

setup(
	name = 'novainstrumentation',
	version = '0.3',
	description = 'Supporting code for Digital Instrumentation class at Universidade Nova de Lisboa.',
	url = 'https://github.com/hgamboa/novainstrumentation',
	author = 'hgamboa',
	packages=find_packages(),
	package_data = {'novainstrumentation' : ["data/*"]},
	install_requires = ['scipy','pandas','matplotlib','numpy'],
    zip_safe=False)

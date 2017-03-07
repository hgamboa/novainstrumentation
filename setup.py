from setuptools import setup,find_packages

def readme():
    with open('README.rst') as f:
        return f.read()

setup(
	name = 'novainstrumentation',
	version = '0.1.1',
	description = 'Supporting code for Digital Instrumentation class at Universidade Nova de Lisboa.',
	url = 'https://github.com/hgamboa/novainstrumentation',
	author = 'Hugo Gamboa',
    author_email = 'hgamboa@fct.unl.pt',
	packages=find_packages(),
	package_data = {'novainstrumentation' : ["data/*"]},
	install_requires = ['scipy','pandas','matplotlib','numpy'],
    zip_safe=False)

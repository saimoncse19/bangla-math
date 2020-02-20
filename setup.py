from distutils.core import setup

setup(
  name='banglamath',
  packages=['banglamath'],
  version='1.1',
  license='MIT',
  description='The Evaluator class in banglamath has two functions: bengali_to_english() that'
              'evaluates a Bengali math expression and return the result in English and bengali_to_bengali()'
              'that does the same thing as bengali_to_english() except that it returns the result '
              'in Bengali.',

  author='Saimon Hossain',
  author_email='saimoncse19@gmail.com',
  url='https://github.com/saimoncse19',
  download_url='https://github.com/user/reponame/archive/v_01.tar.gz',
  keywords=['math-converter', 'bangla math evaluator', 'math evaluator'],
  install_requires=[],
  classifiers=[
    'Development Status :: 5 - stable',
    'Intended Audience :: programmers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
  ],
)
from distutils.core import setup
setup(
  name = 'amerikana',         
  packages = ['amerikana'],  
  version = '0.2',      
  license='MIT',       
  description = '☕ a simpler imagenet class synset and decoder utility. pluggable and 100% tf.keras compatible',
   
  author = 'Glenn Wolfe',
  author_email = 'glennwolfe@protonmail.com',
  url = 'https://github.com/gWOLF3/amerikana',
  download_url = 'https://github.com/gWOLF3/amerikana/archive/0.2.tar.gz',
  keywords = ['keras', 'imagenet', 'labels', 'simple', 'american'], 
  install_requires=[           
          'tensorflow'
      ],
  classifiers=[
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)

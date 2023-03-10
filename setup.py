from distutils.core import setup
setup(
  name = 'PIE-PythonImageEditor',         # How you named your package folder (MyLib)
  packages = ['PIE-PythonImageEditor'],   # Chose the same as "name"
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'A simple function interface over the PIL image editing in python',   # Give a short description about your library
  author = 'Kevin George',                   # Type in your name
  url = 'https://github.com/kiwuthegamer',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/kiwuthegamer/PIE-PythonImageEditor/archive/refs/tags/v0.1.tar.gz',    # I explain this later on
  keywords = ['Images', 'PIL', 'Editing'],   # Keywords that define your package best
  install_requires=['PIL'],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12",
  ],
)

from setuptools import setup
setup(
    name='app_cli',
    version='0.1.0',
    py_modules=['app_cli'],
    install_requires=['Click,'],
    entry_points={'console_scripts': ['app_cli = appl_cli:cli']}
)


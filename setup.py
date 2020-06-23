from setuptools import setup

setup(
    name="okex-client",
    version="0.0.1",
    packages=['okex'],
    install_requires=['requests', 'websocket-client', 'urllib3']
)


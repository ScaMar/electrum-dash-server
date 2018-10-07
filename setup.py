from setuptools import setup

setup(
    name="electrum-deviant-server",
    version="1.0",
    scripts=['run_electrum_deviant_server','electrum-deviant-server'],
    install_requires=['plyvel >= 0.9, <=0.9','jsonrpclib', 'irc >= 11, <=14.0', 'x11_hash'],
    package_dir={
        'electrumserver':'src'
        },
    py_modules=[
        'electrumserver.__init__',
        'electrumserver.utils',
        'electrumserver.storage',
        'electrumserver.deserialize',
        'electrumserver.networks',
        'electrumserver.blockchain_processor',
        'electrumserver.server_processor',
        'electrumserver.processor',
        'electrumserver.version',
        'electrumserver.ircthread',
        'electrumserver.stratum_tcp'
    ],
    description="Deviant Electrum Server",
    author="",
    author_email="",
    license="MIT Licence",
    url="https://github.com/spesmilo/electrum-server/ , https://github.com/Deviantcoin/electrum-deviant-server/",
    long_description="""Server for the Electrum Lightweight Deviant Wallet"""
)

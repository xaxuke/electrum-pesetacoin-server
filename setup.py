from setuptools import setup

setup(
    name="electrum-peseta-server",
    version="0.9",
    scripts=['run_electrum_peseta_server','electrum-peseta-server'],
    install_requires=['plyvel','jsonrpclib', 'irc'],
    package_dir={
        'electrumpesetaserver':'src'
        },
    py_modules=[
        'electrumpesetaserver.__init__',
        'electrumpesetaserver.utils',
        'electrumpesetaserver.storage',
        'electrumpesetaserver.deserialize',
        'electrumpesetaserver.networks',
        'electrumpesetaserver.blockchain_processor',
        'electrumpesetaserver.server_processor',
        'electrumpesetaserver.processor',
        'electrumpesetaserver.version',
        'electrumpesetaserver.ircthread',
        'electrumpesetaserver.stratum_tcp',
        'electrumpesetaserver.stratum_http'
    ],
    description="Pesetacoin Electrum Server",
    author="Thomas Voegtlin & Pesetacoin Foundation",
    author_email="info@pesetacoin.info",
    license="GNU Affero GPLv3",
    url="https://github.com/electrumalt/electrum-peseta-server/",
    long_description="""Server for the Electrum Lightweight Pesetacoin Wallet"""
)

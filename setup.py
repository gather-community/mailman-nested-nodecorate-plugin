from setuptools import setup, find_packages


setup(
    name='nested-nodecorate-plugin',
    version='0.0.1',
    packages=find_packages('.'),
    description='suppress extra decorations on nested messages',
    maintainer='Steve Gaarder',
    maintainer_email='gaarder1@evi.earth',
    install_requires = [
        'mailman',
        'atpublic',
    ]
)

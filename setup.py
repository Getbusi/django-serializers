from distutils.core import setup

import django.serializers

README = open('README').read().strip() + "\n\n"
ChangeLog = \
    "What's new\n" + \
    "==========\n" + \
    "\n" + \
    open('ChangeLog').read().strip()

LONG_DESCRIPTION = README + ChangeLog

setup(
    name='django-serializers',
    version=django.serializers.__version__,
    description='Extended serializers for Django.',
    long_description=LONG_DESCRIPTION,
    author='Getbusi',
    author_email='info@getbusi.com',
    url='https://github.com/Getbusi/django-serializers/',
    download_url='https://github.com/Getbusi/django-serializers/tarball/modern-json',
    packages=(
        'django.serializers',
    ),
    keywords="django json serializer",
    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities',
        'Framework :: Django',
    ),
)

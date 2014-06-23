from setuptools import setup, find_packages
import drupalauth

setup(
    name = 'django-drupal-auth',
    version = drupalauth.__version__,
    packages = find_packages(),

    author = 'Fei Tao',
    author_email = 'filia.tao@gmail.com',
    license = 'GPLv3',
    description = 'Django Auth backend using a drupal database',
    url='https://github.com/ftao/django-drupal-auth',
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GPL License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    install_requires=[
    ],
    #test_suite='tests.main',
    zip_safe = False,
)

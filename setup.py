from setuptools import setup, find_packages

setup(
    name='mi_paquete',
    version='0.1.0',
    author='AlvaroWau',
    author_email='alvarobajo893@gmail.com',
    description='Paquete con el contenido de la carpeta mypackage',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/alvarowau/tarea_cinco_sge',
    packages=['mypackage', 'mypackage.parte_dos_cuatro', 'mypackage.parte_uno'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    python_requires='>=3.6',
)

from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='deepcfd_extended',
    version='0.1',
    description='This is an extended edition of the original DeepCFD: Efficient Steady-State Laminar Flow'
        'Approximation with Deep Convolutional Neural Networks',
    researcher='Alper Saydam',
    researcher_email='asaydam21@ku.edu.tr',
    original_author='Mateus Dias Ribeiro, Carlos Peña Monferrer',
    original_author_email='mateusdiasbr@gmail.com',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/ASaydam/DeepCFD_Extended',
    original_url='https://github.com/mdribeiro/DeepCFD',
    packages=['deepcfd', 'deepcfd.models'],
    package_dir={'': 'src'},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "torch==2.0.0",
        "torchvision==0.15.1",
        "matplotlib>=3.0.0,<=3.7.1"
    ],
)

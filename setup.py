from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="task-manager",
    version="0.0.1",
    author="Igor Dantas de Aguiar",
    author_email="igordantas91@icloud.com",
    description="Task manager celery to django",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='MIT',
    url="https://gitlab.com/brain/python/packages/task-manager.git",
    packages=find_packages(exclude=['tests*']),
    install_requires=[
        'Django>=3',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
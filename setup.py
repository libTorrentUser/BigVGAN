import setuptools

long_description = 'lol'

setuptools.setup(
    name="BigVGAN",
    packages=setuptools.find_packages(),
    version="0.0.1",
    author="Nvidia",
    author_email="54623771+152334H@users.noreply.github.com",
    description="BigVGAN for tortoise-tts",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/152334H/BigVGAN",
    project_urls={},
    scripts=[
        "./inference_e2e.py",
        "./inference.py",
    ],
    include_package_data=True,
    install_requires=[
        "torch",
        "numpy",
        "librosa==0.8.1",
        "scipy",
        #"tensorboard",
        "soundfile",
        "matplotlib",
        "pesq",
        "auraloss",
        "tqdm",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    python_requires=">=3.6",
)

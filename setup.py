import setuptools

long_description = 'lol'
setuptools.setup(
    name="BigVGAN",
    packages=setuptools.find_packages(),
    version="0.0.1",
    author="Nvidia",
    author_email="null@null.com",
    description="BigVGAN for tortoise-tts",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/libTorrentUser/BigVGAN",
    project_urls={},
    include_package_data=True,
    install_requires=[
        "torch",
        "numpy",
        "librosa",
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

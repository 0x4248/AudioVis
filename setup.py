# AudioVis
# Visualize audio with graphs.
# Github: https://www.github.com/lewisevans2007/AudioVis
# Licence: GNU General Public License v3.0
# By: Lewis Evans

from setuptools import setup

setup(
    name="audiovis",
    version="0.1",
    packages=["audiovis"],
    install_requires=[
        "librosa",
        "matplotlib"
    ],
)

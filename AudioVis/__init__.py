# AudioVis
# Visualize audio with graphs.
# Github: https://www.github.com/0x4248/AudioVis
# Licence: GNU General Public License v3.0
# By: 0x4248

import librosa
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def time_pitch_volume_3d(audio_file):
    """Plots the time, pitch, and volume of an audio file in 3D.

    Args:
        audio_file (string): Path to the audio file.
    """

    y, sr = librosa.load(audio_file)


    pitches, magnitudes = librosa.piptrack(y=y, sr=sr)
    pitch = pitches.mean(axis=0)
    volume = magnitudes.mean(axis=0)


    time = librosa.times_like(pitches)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.scatter(time, volume, pitch, c=pitch, cmap=plt.cm.viridis)


    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Volume')
    ax.set_zlabel('Pitch')

    plt.show()



def time_volume_2d(audio_file):
    """Plots the time and volume of an audio file in 2D.

    Args:
        audio_file (string): Path to the audio file.
    """

    y, sr = librosa.load(audio_file)

    volume = librosa.feature.rms(y=y)
    time = librosa.times_like(volume)

    plt.plot(time, volume[0])
    plt.show()

def time_pitch_2d(audio_file):
    """Plots the time and pitch of an audio file in 2D.

    Args:
        audio_file (string): Path to the audio file.
    """

    y, sr = librosa.load(audio_file)

    pitches, magnitudes = librosa.piptrack(y=y, sr=sr)
    pitch = pitches.mean(axis=0)
    time = librosa.times_like(pitch)

    plt.plot(time, pitch)
    plt.show()
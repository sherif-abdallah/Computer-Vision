from subprocess import call


def changeVolume(volume):
    call(["amixer", "-D", "pulse", "sset", "Master", str(volume)+"%"])
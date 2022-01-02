import find.findTokensLinux as linux
import find.findTokensMisc as misc
import find.findTokensWindows as win

windowsNames = ["nt", "win32", "windows"]
linuxNames = ["linux", "linux2", "posix"]

def getTokens(platform, getJson):
    platform = platform.lower()

    try:
        if windowsNames.__contains__(platform):
            return win.locateTokens(getJson)
        elif linuxNames.__contains__(platform):
            return linux.locateTokens(getJson)
        else:
            return misc.locateTokens(getJson)
    except BaseException:
        return misc.locateTokens(getJson)
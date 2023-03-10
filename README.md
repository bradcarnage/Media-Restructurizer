# Media-Restructurizer
bridges the gap between [jellyfin](https://github.com/jellyfin) and [flood](https://github.com/jesec/flood)

# What does this do?
Flood doesn't allow for renaming files. Why not make my life easier!

This tool scans a library folder, and structurizes it somewheere else (with symlinks). It still requires you to put stuff under a `ShowName`, however.

For example, `/mnt/bigstore/MediaStorage/ShowName/blahblah/blahblah2/S01COMPLETE/S01E05-whatever-WHATEVERELSE-ENGLISH.mkv`
gets symlink'd to 
`/mnt/bigstore/MediaLibrary/ShowName/Season 1/Episode 5.mkv`
Much neater!

There's also functionality to remove empty symlinks & folders.

# VideoSlice

Application for converting video frames to a mosaic

## Getting Started

#### Installing

* [Download](https://github.com/Skeibol/VideoSlice/raw/refs/heads/main/dist/VideoSlicer.exe)
* Put inside a folder

#### Executing program

* Navigate to VideoSlicer.exe folder
* Open the folder in CMD prompt
* Example:
```
C:\Users\<User>\Documents\VideoSlice
```
* If using for the first time, run
```console
C:\Users\<User>\Documents\VideoSlice> videoslice
```
* Place mp4 inside the videos folder (Needs to be 4:3. Use sample video from videos folder).
* type this command into the prompt:
```console
C:\Users\<User>\Documents\VideoSlice> videoslice -file <video_name.mp4>
```

## More options

```console
usage: main [-file SRC] [-out OUT] [-w WIDTH] [-h HEIGHT] [-rows ROWS] [-cols COLS] [-help]

options:
  -file SRC      video name (in videos folder)
  -out OUT       output file name
  -w WIDTH       width of mosaic frames(default 80)
  -h HEIGHT      height of mosaic frames(default 60)
  -rows ROWS     no. of rows(default 12)
  -cols COLS     no. of cols(default 10
  -help, --help  Show this help message and exit.
```

## Help

Use the -help flag to bring up help and more options.
```console
C:\Users\<User>\Documents\VideoSlice> videoslice -help
```

## Authors

* [skeibol](https://github.com/Skeibol/)
* [mr. klanax](https://hr.linkedin.com/in/karlo-klanac-3b14b7186)

## Version History

* 0.1
    * Couldnt even run it lmao
    * See [commit change](https://github.com/Skeibol/VideoSlice/commit/a53b4111529420a312c511aa78ac747233cccd49) or See [release history](https://github.com/Skeibol/VideoSlice/commits/main/)
* 0.1
    * Magically works

## License

This project is licensed under the MIT License - see the LICENSE.md file for details


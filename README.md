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

* 0.2
    * Various bug fixes and optimizations
    * See [commit change]() or See [release history]()
* 0.1
    * Initial Release

## License

This project is licensed under the MIT License - see the LICENSE.md file for details


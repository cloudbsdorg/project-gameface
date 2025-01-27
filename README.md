# Project Gameface
Project Gameface helps gamers control their mouse cursor using their head movement and facial gestures.

# This is a Multiplatform build 
> :warning:  Still under heavy development and has issues!

This will run on Windows AMD64, Apple MacOS, and Linux AMD64.

> :warning:  For those using MacOS on Apple Silicon ( M1, M2, *NOT INTEL* ):

You may need to completely reinstall Python from an official Python Package from: 
https://www.python.org/downloads/

# Model used
MediaPipe Face Landmark Detection API [Task Guide](https://developers.google.com/mediapipe/solutions/vision/face_landmarker)  
[MediaPipe BlazeFace Model Card](https://storage.googleapis.com/mediapipe-assets/MediaPipe%20BlazeFace%20Model%20Card%20(Short%20Range).pdf)  
[MediaPipe FaceMesh Model Card](https://storage.googleapis.com/mediapipe-assets/Model%20Card%20MediaPipe%20Face%20Mesh%20V2.pdf)  
[Mediapipe Blendshape V2 Model Card](https://storage.googleapis.com/mediapipe-assets/Model%20Card%20Blendshape%20V2.pdf)  



# Application
- Control mouse cursor in games.
- Intended users are people who choose to use face-control and head movement for gaming purposes.

# Out-of-Scope Applications
* This project is not intended for human life-critical decisions 
* Predicted face landmarks do not provide facial recognition or identification and do not store any unique face representation.


# Python application

## Installation
> Environment
>- Windows - AMD64
>- Linux - AMD64
>- Apple MacOS - All Architectures (Intel / AMD64, Apple Silicon M1 and M2 )
>- Python 3.9
```
pip install -r requirements.txt
```

## Quick start
1. Run main application
    ```
    python project_gameface.py
    ```


# Configs
## Basic config

>[cursor.json](configs/default/cursor.json)  

|           |                                       |
|-----------|---------------------------------------|
| camera_id | Default camera index on your machine. |
| tracking_vert_idxs | Tracking points for controlling cursor ([see](assets/images/uv_unwrap_full.png)) |
| spd_up    | Cursor speed in the upward direction  |
| spd_down  | Cursor speed in downward direction    |
| spd_left  | Cursor speed in left direction        |
| spd_right | Cursor speed in right direction       |
| pointer_smooth  | Amount of cursor smoothness           |
| shape_smooth  | Reduces the flickering of the action           |
| hold_trigger_ms  | Hold action trigger delay in milliseconds           |
| auto_play  | Automatically begin playing when you launch the program           |
| mouse_acceleration  | Make the cursor move faster when the head moves quickly        |
| use_transformation_matrix  | Control cursor using head direction (tracking_vert_idxs will be ignored)   |
 

## Keybinds configs
>[mouse_bindings.json](configs/default/mouse_bindings.json)  
>[keyboard_bindings.json](configs/default/keyboard_bindings.json) 

The config parameters for keybinding configuration are in this structure.
```
gesture_name: [device_name, action_name, threshold, trigger_type]
```


|              |                                                                                           |
|--------------|-------------------------------------------------------------------------------------------|
| gesture_name | Face expression name, see the [list](src/shape_list.py#L16)       |
| device_name  | "mouse" or "keyboard"                                                                     |
| action_name  | "left", "right" and "middle" for mouse. "" for keyboard, for instance, "w" for the W key. |
| threshold    | The action trigger threshold has values ranging from 0.0 to 1.0.        |
| trigger_type | Action trigger type, use "single" for a single trigger, "hold" for ongoing action.                                 |





# Build Package on Windows
```
    pyinstaller build.spec
```


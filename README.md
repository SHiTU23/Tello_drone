# Tello_drone
Controlling Tello Drone and do cool projects with it

+ ***Depencensies***\
    for using `djitellopy` package, some specific versions of numpy and pillow is needed. So better to create a virtual environment and install the [requirements.txt](./requirements.txt)

    ```shell
    pip install -r requirements.txt
    ```

## Control the drone

[python script](./src/control_and_capture.py)

### Keyboard Commands:
+ `s` : for saving frames
+ `pgUp`: Take off the drone
+ `PgDn`: Land the drone

    **All movments are relative to the drone itself** 

+ `Left arrow`: Rotate 10 degrees to the left
+ `Right arrow`: Rotate 10 degrees to the right
+ `w`: Move 20cm forward
+ `z`: Move 20cm backeward 
+ `a`: Move 20cm to the left
+ `d`: Move 20cm to the right
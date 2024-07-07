<h1 align="center"> Auto-Emptor - Your Own Shop Dog</h1>
<br>
<br>
<h2 align="center">SEMESTER-4 [TERM PROJECT]</h2>
<br>
<h1 align="center">Hi 👋,This side Team 1 of Batch A</h1>
<h3 align="center">Students at Amrita Vishwa Vidyapeetham, Coimbatore🌟.</h3>
<br>
<h4 align="center">Our Project is performed by the utilization of ROS2 [ver:Humble Hawksbill] and Gazebo, primarily. Other than that, we have utilized OpenCV, cv_bridge, Pyzbar and RVIZ2 for our Project Work.</h4>
<br>

## Group Members
* Aman Sirohi [CB.EN.U4AIE21003]
* Vikhyat Bansal [CB.EN.U4AIE21076]
* Rakhil ML [CB.EN.U4AIE21048]
* R Sriviswa [CB.EB.U4AIE21046]
  <br>
  
## Contents
* [Spawner Package](https://github.com/ErAgOn-AmAnSiRoHi/Auto-Emptor/tree/main/warehouse_robot_spawner_pkg)
* [Controller Package](https://github.com/ErAgOn-AmAnSiRoHi/Auto-Emptor/tree/main/warehouse_robot_controller_pkg)

* [QR-CODE MODEL](https://github.com/ErAgOn-AmAnSiRoHi/Auto-Emptor/tree/main/QR_Code_Model/texture)

* [PPT](https://github.com/ErAgOn-AmAnSiRoHi/Auto-Emptor/blob/main/ROS_TEAM_1_BATCH_A_END_TERM.pptx)

## Tools and Libraries
* Gazebo
  > ```sudo apt install ros-$ROS_DISTRO-gazebo-ros-pkgs```
* OpenCV
  > ```sudo apt-get install libopencv-dev python3-opencv```
* PyZBar
  > ```pip install pyzbar```
* cv_bridge
  > ```sudo apt-get install ros-$ROS_DISTRO-vision-opencv```   
  >    ```sudo apt-get install ros-$ROS_DISTRO-cv-bridge```

## How to Run
* After creating the desired packages, go to the ros workspace directory.
* There, do ```colcon build``` or ```colcon build --packages-select <pkg_name>``` if you want to build a specific package instead of all the packages in the workspace.
* Now, being in the workspace directory, do ```source install/setup.bash```
* Now, in a terminal window, simply type ```ros2 launch <pkg_name> <launch_file_name>```
* * So, in our case, since we have two packages, you will have to start two terminals and initially run:   
  > ```ros2 launch warehouse_robot_spawner_pkg gazebo_world.launch.py```   
* *  After the Gazebo simulation has started successfully, we need to run:   
  > ```ros2 launch warehouse_robot_controller_pkg controller_estimator.launch.py```   
* *  Then in one more terminal window, we need to run:   
  > ```ros2 run warehouse_robot_spawner_pkg decode_qr```

## Simulation Video (Basic Layout of a Mart)
https://amritavishwavidyapeetham-my.sharepoint.com/:v:/g/personal/cb_en_u4aie21003_cb_students_amrita_edu/EaNcJRI3JM1JioUTcdLq7oMBysudWm0ew7rwrRGFZMmaBg?e=qW20nr   
<br>
* * * Better Layout of the Mart (with Human Models added as extra obstacles and extra models for decoration sake)   
https://amritavishwavidyapeetham-my.sharepoint.com/:v:/g/personal/cb_en_u4aie21003_cb_students_amrita_edu/EZjKWvG0IzVNvWs4TzDx7ggB86gl3PUX3uX1kzanuVWfxQ?e=KH0Rgi

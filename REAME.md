1. Clone robocup atwork commander

2. Clone this repo in the same workspace!

3. Clone https://github.com/JeroenBongers96/suii_communication_ros1.git 

4. clone https://github.com/JeroenBongers96/nav_test_package.git 

3. source env.

4. Refbox
    • roslaunch atwork_commander atwork_commander.launch multimaster:=false
    • roslaunch atwork_commander generate.launch task:=BMT
    • rosrun nav_test_package nav_manager_server_test.py 
    • roslaunch atwork_commander_client suii_robot.launch multimaster:=false 
    • roslaunch atwork_commander start.launch 
    • roslaunch atwork_commander forward.launch [ to start immediately ]
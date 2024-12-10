with open("/home/clover/catkin_ws/src/clover/clover/launch/aruco.launch", "r") as f:
    root = f.read()

root = root.replace('<arg name="aruco_map" default="false"/>', '<arg name="aruco_map" default="true"/>', 1)
root = root.replace('<arg name="aruco_vpe" default="false"/>', '<arg name="aruco_vpe" default="true"/>', 1)
m = input("Enter the name of the marker map you are using (if you want to use the default map, enter any character)\n")
try:
    with open(f"/home/clover/catkin_ws/src/clover/aruco_pose/map/{m}", "r") as file:
        w = file.read().split()
        z = w[10]
        root = root.replace("map.txt", m, 1)
        root = root.replace('<arg name="length" default="0.22"/>', f'<arg name="length" default="{z}"/>', 1)
except:
    root = root.replace("map.txt", "cmit.txt", 1)
    root = root.replace('<arg name="length" default="0.22"/>', '<arg name="length" default="0.33"/>', 1)

with open("/home/clover/catkin_ws/src/clover/clover/launch/aruco.launch", "w") as f:
    f.write(root)



with open("/home/clover/catkin_ws/src/clover/clover/launch/clover.launch", "r") as f:
    r = f.read()
r = r.replace('<arg name="aruco" default="false"/>', '<arg name="aruco" default="true"/>', 1)
r = r.replace('<arg name="simulator" default="false"/>', '<arg name="simulator" default="true"/>', 1)
with open("/home/clover/catkin_ws/src/clover/clover/launch/clover.launch", "w") as f:
    f.write(r)
import random

with open("/home/clover/catkin_ws/src/clover/clover_simulation/resources/worlds/clover_aruco.world", "r") as f:
    r = f.read()
m = ["blue", "green", "red", "yellow"]
def dr():
    a = str(random.randint(0,9))
    if a == "0":
        return a + "." + str(random.randint(5,9))
    if a == "9":
        return a + "." + "0"
    return a + "." + str(random.randint(0, 9))

text_my = f"<uri>model://aruco_cmit_txt</uri></include><include><name>d1</name><uri>model://dronepoint_{random.choice(m)}</uri><pose>{dr()} {dr()} 0 0 0 0</pose></include><include><name>d2</name><uri>model://dronepoint_{random.choice(m)}</uri><pose>{dr()} {dr()} 0 0 0 0</pose></include><include><name>d3</name><uri>model://dronepoint_{random.choice(m)}</uri><pose>{dr()} {dr()} 0 0 0 0</pose></include><include><name>d4</name><uri>model://dronepoint_{random.choice(m)}</uri><pose>{dr()} {dr()} 0 0 0 0</pose></include><include><name>d4</name><uri>model://dronepoint_{random.choice(m)}</uri><pose>{dr()} {dr()} 0 0 0 0</pose>"
r = r.replace('<uri>model://aruco_cmit_txt</uri>', text_my, 1)
with open("/home/clover/catkin_ws/src/clover/clover_simulation/resources/worlds/clover_aruco.world", "w") as f:
    f.write(r)
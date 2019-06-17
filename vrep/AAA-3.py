import vrep
import keyboard
import time
import sys, math     
# child threaded script: 
# 內建使用 port 19997 若要加入其他 port, 在  serve 端程式納入
#simExtRemoteApiStart(19999)
  
vrep.simxFinish(-1)


clientID = vrep.simxStart('127.0.0.1', 19997, True, True, 5000, 5)
KickBallV = 360
Move_Minus =-0.1        
Move_Plus =0.1
n=1
R_KickBallVel = (math.pi/180)*KickBallV
B_KickBallVel = -(math.pi/180)*KickBallV
if clientID!= -1:
    print("Connected to remote server")
else:
    print('Connection not successful')
    sys.exit('Could not connect')
    

errorCode,P1_handle=vrep.simxGetObjectHandle(clientID,'P1',vrep.simx_opmode_oneshot_wait)
errorCode,R1_handle=vrep.simxGetObjectHandle(clientID,'R1',vrep.simx_opmode_oneshot_wait)
errorCode,R2_handle=vrep.simxGetObjectHandle(clientID,'R2',vrep.simx_opmode_oneshot_wait)

vrep.simxSetJointTargetVelocity(clientID,P1_handle,0,vrep.simx_opmode_oneshot_wait)
vrep.simxSetJointTargetVelocity(clientID,R1_handle,0,vrep.simx_opmode_oneshot_wait)
vrep.simxSetJointTargetVelocity(clientID,R2_handle,0,vrep.simx_opmode_oneshot_wait)

def speed(handle,speed):
    errorCode = vrep.simxSetJointTargetVelocity(clientID,handle,speed,vrep.simx_opmode_oneshot_wait)

vrep.simxStartSimulation(clientID,vrep.simx_opmode_oneshot_wait)
while True:
    try:
            if keyboard.is_pressed('a'): 
                speed(R1_handle,R_KickBallVel)
            else:  
                speed(R1_handle,B_KickBallVel)
            
            if keyboard.is_pressed('UP arrow'):  
                speed(P1_handle,-1000)
            else: 
                speed(P1_handle,500)

            if keyboard.is_pressed('l'):  
                speed(R2_handle,B_KickBallVel)
            else:
                speed(R2_handle,R_KickBallVel)
            
    except:
            break

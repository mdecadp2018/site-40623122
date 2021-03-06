import vrep
import keyboard    #導入鍵盤
import time
import sys, math     
# child threaded script: 
# 內建使用 port 19997 若要加入其他 port, 在  serve 端程式納入
#simExtRemoteApiStart(19999)
  
vrep.simxFinish(-1)


clientID = vrep.simxStart('127.0.0.1', 19997, True, True, 5000, 5)

KickBallV = 360     #轉軸角度

R_KickBallVel = (math.pi/180)*KickBallV   
B_KickBallVel = -(math.pi/180)*KickBallV

if clientID!= -1:
    print("Connected to remote server")
else:
    print('Connection not successful')
    sys.exit('Could not connect')                                  #以上為連動程式
    
errorCode,P1_handle=vrep.simxGetObjectHandle(clientID,'P1',vrep.simx_opmode_oneshot_wait)
errorCode,P2_handle=vrep.simxGetObjectHandle(clientID,'P2',vrep.simx_opmode_oneshot_wait)
errorCode,R1_handle=vrep.simxGetObjectHandle(clientID,'R1',vrep.simx_opmode_oneshot_wait)
errorCode,R2_handle=vrep.simxGetObjectHandle(clientID,'R2',vrep.simx_opmode_oneshot_wait)
 
vrep.simxSetJointTargetVelocity(clientID,P1_handle,0,vrep.simx_opmode_oneshot_wait)
vrep.simxSetJointTargetVelocity(clientID,P2_handle,0,vrep.simx_opmode_oneshot_wait)
vrep.simxSetJointTargetVelocity(clientID,R1_handle,0,vrep.simx_opmode_oneshot_wait)
vrep.simxSetJointTargetVelocity(clientID,R2_handle,0,vrep.simx_opmode_oneshot_wait)

def speed(handle,speed):    #定義速度
    errorCode = vrep.simxSetJointTargetVelocity(clientID,handle,speed,vrep.simx_opmode_oneshot_wait)

vrep.simxStartSimulation(clientID,vrep.simx_opmode_oneshot_wait)

while True:
    try:
            if keyboard.is_pressed('s'): 
                speed(R1_handle,R_KickBallVel)
            elif keyboard.is_pressed('w'):  
                speed(R1_handle,B_KickBallVel)
            else:
                speed(R1_handle,0)
            if keyboard.is_pressed('a'):  
                speed(P1_handle,0.1)
            elif keyboard.is_pressed('d'):  
                speed(P1_handle,-0.1)
            else:
                speed(P1_handle,0)
            if keyboard.is_pressed('8'): 
                speed(R2_handle,R_KickBallVel)
            elif keyboard.is_pressed('5'):  
                speed(R2_handle,B_KickBallVel)
            else:
                speed(R2_handle,0)
            if keyboard.is_pressed('6'):  
                speed(P2_handle,0.1)
            elif keyboard.is_pressed('4'):  
                speed(P2_handle,-0.1)
            else:
                speed(P2_handle,0)
    except:
            break

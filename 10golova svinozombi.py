from mcpi.minecraft import Minecraft
from time import sleep
mc = Minecraft.create()
x,y,z = mc.player.getPos()
sleep(5)
mc.setBlocks(x,y,z,x+7,y+7,z+7,35,6)
mc.setBlocks(x+1,y+5,z,x+2,y+6,z,35,8)
mc.setBlocks(x,y,z,x+2,y+5,z+7,35,6)
mc.setBlocks(x+1,y+4,z,x+2,y+6,z,35,8)


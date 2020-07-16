from mcpi.minecraft import Minecraft
from time import sleep
mc = Minecraft.create()
x,y,z = mc.player.getPos()
sleep(5)
mc.setBlocks(x,y,z,x+9,y+1,z+9,80)
mc.setBlocks(x,y+2,z,x+9,y+2,z+9,86)

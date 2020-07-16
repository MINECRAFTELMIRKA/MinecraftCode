from mcpi.minecraft import Minecraft
from time import sleep
mc = Minecraft.create()
x,y,z = mc.player.getPos()
sleep(5)
mc.setBlock(x,y-1,z,18,1)
mc.setBlocks(x-1,y-2,z-1,x+1,y-2,z+1,18,1)
mc.setBlocks(x-3,y-4,z-3,x+3,y-4,z+3,18,1)
mc.setBlocks(x-4,y-5,z-4,x+4,y-5,z+4,18,1)
mc.setBlock(x,y-2,z,18,1)
mc.setBlocks(x,y-3,z,x,y-13,z,162,1)


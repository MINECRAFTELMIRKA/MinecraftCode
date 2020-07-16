from mcpi.minecraft import Minecraft
from time import sleep
mc = Minecraft.create()
x,y,z = mc.player.getPos()
sleep(5)
mc.setBlock(x,y-1,z,138)
mc.setBlocks(x-1,y-2,z-1,x+1,y-2,z+1,57)
mc.setBlocks(x-2,y-3,z-2,x+2,y-3,z+2,57)
mc.setBlocks(x-3,y-4,z-3,x+3,y-4,z+3,57)
mc.setBlocks(x-4,y-5,z-4,x+4,y-5,z+4,57)



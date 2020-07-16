from mcpi.minecraft import Minecraft
from time import sleep
mc = Minecraft.create()
x,y,z = -1658,64,-716
#x,y,z = mc.player.getPos()
sleep(5)
mc.setBlocks(x+2,y-1,z+2,x-2,y-1,z-2,162)
mc.setBlocks(x+3,y,z+3,x-3,y+2,z-3,5,3)
mc.setBlocks(x+2,y,z+2,x-2,y+2,z-2,0)

mc.setBlock(x,y+7,z,5,5)
mc.setBlocks(x-1,y+6,z-1,x+1,y+6,z+1,5,5)
mc.setBlocks(x-2,y+5,z-2,x+2,y+5,z+2,5,5)
mc.setBlocks(x-3,y+4,z-3,x+3,y+4,z+3,5,5)
mc.setBlocks(x-4,y+3,z-4,x+4,y+3,z+4,5,5)

mc.setBlocks(x+3,y,z,x+3,y+1,z,0)

mc.setBlock(x+3,y+1,z+2,20)
mc.setBlock(x+3,y+1,z-2,20)

mc.setBlock(x,y+3,z,89)
mc.setBlock(x-3,y,z,89)

mc.setBlock(x-2,y,z+2,54)

















   

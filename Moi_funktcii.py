from mcpi.minecraft import Minecraft
from time import sleep
mc = Minecraft.create()
x,y,z = mc.player.getPos()
sleep (5)
def vodopad(x,y,z):
    mc.setBlock(x,y,z,213)
    mc.setBlock(x,y+1,z,213)
    mc.setBlock(x,y+2,z,213)
    mc.setBlock(x,y+3,z,213)
    mc.setBlock(x,y+4,z,213)
    mc.setBlock(x,y+5,z,8)


def drawCircleY(x0, y, z0, radius, blockType, blockData=0):
    for x in range(-radius, radius):
        for z in range(-radius, radius):
            if x**2 + z**2 < radius**2:
                mc.setBlock(x+x0,y,z+z0,blockType, blockData)
               

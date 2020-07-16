from mcpi.minecraft import Minecraft
from time import sleep
mc = Minecraft.create()
x,y,z = mc.player.getPos()
sleep (5)
def vodopad(x,y,z):
    mc.setBlock(x,y,z,86)
    mc.setBlock(x,y+1,z,86)
    mc.setBlock(x,y+2,z,86)
    mc.setBlock(x,y+3,z,86)
    mc.setBlock(x,y+4,z,86)
    mc.setBlock(x,y+5,z,8)

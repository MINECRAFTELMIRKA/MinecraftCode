from mcpi.minecraft import Minecraft
from time import sleep
mc = Minecraft.create()
x,y,z = mc.player.getPos()
sleep (5)
mc.setBlock(x,y,z,80)#ноги снеговика
mc.setBlock(x,y+1,z,80)#грудь снеговика
mc.setBlock(x,y+2,z,86)#голова снеговика


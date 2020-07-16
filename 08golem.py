from mcpi.minecraft import Minecraft
from time import sleep
mc = Minecraft.create()
x,y,z = mc.player.getPos()
sleep (5)
mc.setBlock(x,y,z,42)#ноги голема
mc.setBlock(x,y+1,z,42)#грудь голема
mc.setBlock(x+1,y+1,z,42)#левая рука голема
mc.setBlock(x-1,y+1,z,42)#правая рука голема
mc.setBlock(x,y+2,z,86)#голова голема

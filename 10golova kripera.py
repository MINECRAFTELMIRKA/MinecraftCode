from mcpi.minecraft import Minecraft
from time import sleep
mc = Minecraft.create()
x,y,z = mc.player.getPos()
sleep(5)
mc.setBlocks(x,y,z,x+7,y+7,z+7,251,5)#голова из зелёной шерсти
mc.setBlocks(x+1,y+4,z,x+2,y+5,z,251,15)#правый глаз
mc.setBlocks(x+5,y+4,z,x+6,y+5,z,251,15)#левый глаз
mc.setBlocks(x+3,y+1,z,x+4,y+3,z,251,15)#рот
mc.setBlocks(x+2,y,z,x+2,y+2,z,251,15)#правый ус
mc.setBlocks(x+5,y,z,x+5,y+2,z,251,15)#левый ус

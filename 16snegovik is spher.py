from mcpi.minecraft import Minecraft
from time import sleep
from minecraftstuff.minecraftstuff import MinecraftDrawing
mc = Minecraft.create()
md = MinecraftDrawing(mc)
x,y,z = mc.player.getPos()
sleep(15)
md.drawSphere(x,y,z,15,80)
sleep(20)
md.drawSphere(x,y+15,z,10,80)
sleep(20)
md.drawSphere(x,y+27,z,7,80)
sleep(20)
mc.setBlocks(x+6,y+27,z+1,x+6,y+28,z+2,173)
mc.setBlocks(x+6,y+27,z-1,x+6,y+28,z-2,173)
mc.setBlocks(x+6,y+25,z,x+9,y+25,z)

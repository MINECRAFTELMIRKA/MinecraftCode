from mcpi.minecraft import Minecraft
from time import sleep
from minecraftstuff.minecraftstuff import MinecraftDrawing
mc = Minecraft.create()
md = MinecraftDrawing(mc)
x,y,z = mc.player.getPos()
sleep(5)
md.drawSphere(x,y,z,10,41)


md.drawSphere(x+25,y,z,10,22)
#md.drawHollowSphere(x,y,z,10,41)

md.drawSphere(x,y,z+25,10,5,5)

md.drawSphere(x,y+25,z,10,133)

md.drawSphere(x+25,y,z+25,10,213)
              

from mcpi.minecraft import Minecraft
from time import sleep
from minecraftstuff.minecraftstuff import MinecraftDrawing
mc = Minecraft.create()
md = MinecraftDrawing(mc)
x,y,z = mc.player.getPos()
x,y,z = -1555,90,-900
sleep(5)
md.drawSphere(x,y,z,20,42)
md.drawSphere(x,y,z,10,0)
md.drawSphere(x+15,y+15,z+15,10,0)

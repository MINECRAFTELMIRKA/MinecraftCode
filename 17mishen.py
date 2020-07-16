from mcpi.minecraft import Minecraft
from time import sleep
from minecraftstuff.minecraftstuff import MinecraftDrawing
mc = Minecraft.create()
md = MinecraftDrawing(mc)
x,y,z = mc.player.getPos()
md.drawCircle(x,y,z,20,41)
md.drawCircle(x,y,z,18,214)
md.drawCircle(x,y,z,16,214)
md.drawCircle(x,y,z,11,57)
md.drawCircle(x,y,z,9,133)
md.drawCircle(x,y,z,5,173)

from mcpi.minecraft import Minecraft
from mcpi.minecraftstuff import MinecraftTurtle
from time import sleep
mc = Minecraft.create()
pos = mc.player.getTilePos()
sleep(10)
kukux=MinecraftTurtle(mc,pos)
kukux.forward (5)

from mcpi.minecraft import Minecraft
from mcpi.minecraftstuff import MinecraftTurtle
from time import sleep
mc = Minecraft.create()

kukux=MinecraftTurtle(mc)
sleep(3)
kukux.setposition(-3509,72,620)
kukux.left(90)
kukux.penblock(152)
kukux.forward(20)

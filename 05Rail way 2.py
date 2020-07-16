from mcpi.minecraft import Minecraft
from mcpi.minecraftstuff import MinecraftTurtle
from time import sleep
mc = Minecraft.create()

kukux=MinecraftTurtle(mc)
sleep(10)
kukux.setposition(-3368,87,773)
kukux.left(90)
kukux.penblock(27)
kukux.forward(200)

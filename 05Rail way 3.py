from mcpi.minecraft import Minecraft
from mcpi.minecraftstuff import MinecraftTurtle
from time import sleep
mc = Minecraft.create()

kukux=MinecraftTurtle(mc)
sleep(10)
kukux.setposition(-3368,86,572)
kukux.left(90)
kukux.down(45)
kukux.penblock(152)
kukux.forward(19)

kukux.setposition(-3368,87,572)
kukux.penblock(27)
kukux.forward(19)

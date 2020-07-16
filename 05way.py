from mcpi.minecraft import Minecraft
from mcpi.minecraftstuff import MinecraftTurtle
from time import sleep
mc = Minecraft.create()

kukux=MinecraftTurtle(mc)
kukux.speed (10)
sleep(3)
kukux.setposition(-3509,73,620)
kukux.left(90)
kukux.penblock(27)
kukux.forward(20)
kukux.up(45)
kukux.forward(100)
kukux.down(45)
kukux.forward(20)
kukux.down(45)
kukux.forward(130)
kukux.up(45)
kukux.forward(2)
kukux.right(90)
kukux.forward(20)


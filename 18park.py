from mcpi.minecraft import Minecraft
from mcpi.minecraftstuff import MinecraftTurtle
from time import sleep
from minecraftstuff.minecraftstuff import MinecraftDrawing
from Moi_funktcii import vodopad,drawCircleY
mc = Minecraft.create()
md = MinecraftDrawing(mc)
x,y,z = -1338,65,-988
mc.setBlocks(x+20,y,z+20,x-20,y+5,z-20,0)
md.drawHorizontalCircle(x,y,z,20,41)
md.drawHorizontalCircle(x,y,z,19,214)
md.drawHorizontalCircle(x,y,z,18,57)
md.drawHorizontalCircle(x,y,z,17,133)
md.drawHorizontalCircle(x,y,z,16,173)
vodopad(x,y,z)
drawCircleY(x,y,z,15,95,5)
kukux=MinecraftTurtle(mc)
kukux.speed (10)
sleep(3)
kukux.setposition(x-7,y,z+7)
kukux.penblock(139)
kukux.forward(15)
kukux.left(90)
kukux.forward(15)
kukux.left(90)
kukux.forward(15)
kukux.left(90)
kukux.forward(15)
kukux.left(90)
kukux.forward(15)



                        

                        
                
                                                                    
                            

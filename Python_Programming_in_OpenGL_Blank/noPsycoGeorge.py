#tr0.py 
#based on lorenz.py by Stan Blank 22mar05
#OpenGL by Alex Bourd and Matthew Stiak 9oct96
#IrisGL by G Francis 9apr89, last revision 9sep96
# written gkf 6apr05
# there is still a python type error in here but it works as intended.
# but actually, it can't work right this way ! what gives?
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import *
import sys

#import psyco
#psyco.full()

# Bryn Keller's version of (cond?expr1:expr2)
def C(u): return cos(u*0.01745)
def S(u): return sin(u*0.01745)
def T(u): return tan(u*0.01745)

# Need to be declared so functions can assign new values to them
global wd
global ht
global MouseX
global MouseY
global aff

aff = ([1.0, 0.0, 0.0, 0.0,
       0.0, 1.0, 0.0, 0.0,
       0.0, 0.0, 1.0, 0.0,
       0.0, 0.0, 0.0, 1.0])
    
def drawvert(th,ta):
   n0= C(th)*C(ta)
   n1= S(th)*C(ta)
   n2=       S(ta)

   glColor3f(tan(n0*n0), tan(n1*n1), tan(n2*n2))
   glVertex3f(n0, n1, n2)
#end drawvert

def drawtor():
   glBegin(GL_TRIANGLE_STRIP) 
   for th in range(0,349,12):
      for ta in range (0,349, 12): 
         drawvert(th,ta); drawvert(th+12,ta) 
   glEnd() 
#end drawtor

#assign initial window and mouse settings
wd = 800
ht = 800
MouseX = wd/2
MouseY = ht/2

brake = 512. 

def display():
   glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
   glMatrixMode(GL_MODELVIEW)
   glLoadIdentity()
   glMultMatrixf(aff)
   drawtor()
   glutSwapBuffers()
#end display()

#typical keyboard callback 
def keyboard(key, x, y):
   if key == chr(27) or key == 'q':
     sys.exit(0)
   glutPostRedisplay()
#end keyboard()

#Note that we must declare the globals again
def chaptrack():
   global MouseX
   global MouseY
   global wd
   global ht
   global aff
   lightPos = (-5.0, 5.0, 5.0, 1.0) 
   dx = (MouseX-wd/2)/brake  
   dy = (MouseY-ht/2)/brake
   glMatrixMode(GL_MODELVIEW)
   glPushMatrix()
   glLoadIdentity()
   glRotatef(dx,0,1.0,0.0)
   glRotatef(dy,1.0,0.0,0.0)
   glMultMatrixf(aff)
   aff = glGetFloatv(GL_MODELVIEW_MATRIX)
   glLightfv(GL_LIGHT0, GL_POSITION, lightPos)
   glPopMatrix()
#end chaptrack()

#traditional idle
def idle():
   chaptrack()
   glutPostRedisplay()
#end idle()

#ditto traditional mousemotion
#Note globals
def mousemotion(x,y):
   global MouseX
   global MouseY
   MouseX = x
   MouseY = y
#end mousemotion()

def init():
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_COLOR_MATERIAL)
    glShadeModel(GL_SMOOTH)
    glClearColor(0.0, 0.0, 0.0, 1.0)

#Traditional main subroutine
def main() :
   global wd
   global ht
   glutInitDisplayMode(GLUT_RGB | GLUT_DEPTH | GLUT_DOUBLE)
   glutInitWindowPosition(50, 50)
   glutInitWindowSize(wd, ht)
   glutInit([])
   glutCreateWindow("Octahedron")
   glutKeyboardFunc(keyboard)
   glutDisplayFunc(display)
   glutIdleFunc(idle)
   glutPassiveMotionFunc(mousemotion)
   glEnable(GL_DEPTH_TEST)
   glShadeModel(GL_SMOOTH)
   glMatrixMode(GL_PROJECTION)
   glLoadIdentity()
   glOrtho(-2.0,2.0,-2.0,2.0,-2.0,2.0)
   
   init()
   glutMainLoop()

#Necessary if we want to this program to run
main()

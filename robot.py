import matplotlib.pyplot as plt
from pyrosim import PYROSIM
import constants as c

import random

###### Variables ######
pi = c.pi

###### Model setup ######
class ROBOT:

    def __init__( self, sim, wts ):

        self.Send_Object(sim)
        self.Send_Joints(sim)
        #self.Send_Sensors(sim)
        #self.Send_Neurons(sim)
        #self.Send_Synapses(sim, wts)
        #self.Debug_Tester(sim)

    def Send_Object(self, sim):

        ###### Body ######
        sim.Send_Box( objectID=0,
                      x=0, y=0, z=c.L + c.R,
                      length=2*c.H, width=2*c.H, height=c.R * 2,
                      r=0.5, g=0.5, b=0.5)

        ###### Horizontal Legs ######
        sim.Send_Cylinder(objectID=1,
                          x=0, y= (c.H + c.L / 2), z=c.L + c.R,
                          length=c.L, radius=c.R,
                          r1=0, r2=1, r3=0,
                          r=1, g=0, b=0)

        sim.Send_Cylinder(objectID=2,
                          x= (c.H + c.L / 2), y=0, z=c.L + c.R,
                          length=c.L, radius=c.R,
                          r1=1, r2=0, r3=0,
                          r=0, g=1, b=0)

        sim.Send_Cylinder(objectID=3,
                          x=0, y= -(c.H + c.L / 2), z=c.L + c.R,
                          length=c.L, radius=c.R,
                          r1=0, r2=1, r3=0,
                          r=0,g=0, b=1)

        sim.Send_Cylinder(objectID=4,
                          x= -(c.H + c.L / 2), y=0, z=c.L + c.R,
                          length=c.L, radius=c.R,
                          r1=1, r2=0, r3=0,
                          r=1, g=0, b=1)

        ###### Vertical Legs ######
        sim.Send_Cylinder(objectID=5,
                          x=0, y= ( c.H + c.L ), z= (c.L / 2 + c.R),
                          length=c.L, radius=c.R,
                          r=1, g=0, b=0)

        sim.Send_Cylinder(objectID=6,
                          x= ( c.H + c.L ), y=0, z= (c.L / 2 + c.R),
                          length=c.L, radius=c.R,
                          r=0, g=1, b=0)

        sim.Send_Cylinder(objectID=7,
                          x=0, y= -( c.H + c.L ), z= (c.L / 2 + c.R),
                          length=c.L, radius=c.R,
                          r=0,g=0, b=1)

        sim.Send_Cylinder(objectID=8,
                          x=  -( c.H + c.L ), y=0, z= (c.L / 2 + c.R),
                          length=c.L, radius=c.R,
                          r=1, g=0, b=1)

    def Send_Joints(self, sim):

        ####### Legs to Body ######
        sim.Send_Joint(jointID=0,
                       firstObjectID=0, secondObjectID=1,
                       x=0, y=c.H, z=c.L + c.R,
                       n1=-1, n2=0, n3=0,
                       lo=-pi / 2, hi=pi / 2)

        sim.Send_Joint(jointID=1,
                       firstObjectID=0, secondObjectID=2,
                       x=c.H, y=0, z=c.L + c.R,
                       n1=0, n2=-1, n3=0,
                       lo=-pi / 2, hi=pi /2)

        sim.Send_Joint(jointID=2,
                       firstObjectID=0, secondObjectID=3,
                       x=0, y=-c.H, z=c.L + c.R,
                       n1=1, n2=0, n3=0,
                       lo=-pi / 2, hi=pi / 2)

        sim.Send_Joint(jointID=3,
                       firstObjectID=0, secondObjectID=4,
                       x=-c.H, y=0, z=c.L + c.R,
                       n1=0, n2=1, n3=0,
                       lo=-pi / 2, hi=pi / 2)

        ####### Legs to Leg ######
        sim.Send_Joint(jointID=4,
                       firstObjectID=1, secondObjectID=5,
                       x=0, y= c.H + c.L, z=c.L + c.R,
                       n1=-1, n2=0, n3=0,
                       lo=-pi / 2, hi=pi / 2)

        sim.Send_Joint(jointID=5,
                       firstObjectID=2, secondObjectID=6,
                       x= c.H + c.L, y=0, z=c.L + c.R,
                       n1=0, n2=-1, n3=0,
                       lo=-pi / 2, hi=pi / 2)

        sim.Send_Joint(jointID=6,
                       firstObjectID=3, secondObjectID=7,
                       x=0, y= -(c.H + c.L), z=c.L + c.R,
                       n1=1, n2=0, n3=0,
                       lo=-pi / 2, hi=pi / 2)

        sim.Send_Joint(jointID=7,
                       firstObjectID=4, secondObjectID=8,
                       x= -(c.H + c.L), y=0, z=c.L + c.R,
                       n1=0, n2=1, n3=0,
                       lo=-pi / 2, hi=pi / 2)

    def Send_Sensors(self, sim):

        sim.Send_Touch_Sensor( sensorID=0, objectID=5 )
        sim.Send_Touch_Sensor( sensorID=1, objectID=6 )
        sim.Send_Touch_Sensor( sensorID=2, objectID=7 )
        sim.Send_Touch_Sensor( sensorID=3, objectID=8 )
        sim.Send_Light_Sensor( sensorID=4, objectID=0 )
        sim.Send_Position_Sensor( sensorID=5, objectID=0 )

    def Send_Neurons(self, sim):

        for s in range(0, 5):

            sim.Send_Sensor_Neuron( neuronID=s, sensorID=s )

        for m in range(0, 8):

            sim.Send_Motor_Neuron( neuronID=5 + m, jointID=m, tau=c.tau ) # Tau means the rate of response

        for h in range(0, c.numHidNeurons):

            sim.Send_Hidden_Neuron( neuronID=13 + h )

    def Send_Synapses(self, sim, wts):

        # for s in range(0, 5):       # Sensor Neurons
        #
        #     for m in range(0, 8):   # Motor Neurons
        #
        #         sim.Send_Synapse(sourceNeuronID=s, targetNeuronID=5 + m, weight=wts[s, m])

        for h in range(0,c.numHidNeurons):

            for s in range(0, 5):       # Sensors to hidden layer

                bias = random.uniform( c.biasSensor, -c.biasSensor )
                sim.Send_Synapse(sourceNeuronID=s, targetNeuronID=13 + h, weight=wts[0][h, s] + bias)

            for m in range(0, 8):       # hidden layer to motors

                bias = random.uniform( c.biasMotor, -c.biasMotor )
                sim.Send_Synapse(sourceNeuronID=13 + h, targetNeuronID=m, weight=wts[1][h, m] + bias)

            for r in range(0,c.numHidNeurons):        # hidden layer (recurrent)

                bias = random.uniform( c.biasNeuron, c.biasNeuron )
                sim.Send_Synapse(sourceNeuronID=13 + h, targetNeuronID=13 + r, weight=wts[2][h, r] + bias )

    def Debug_Tester(self, sim):

        sim.Send_Box(objectID = 9 ,
                     x = 0 , y = 5 , z = 1 ,
                     length = 1 , width = 1 , height = 1 ,
                     r = 0 , g = 1 , b = 1 )

        sim.Send_Light_Source( objectIndex = 9 )

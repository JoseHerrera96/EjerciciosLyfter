class Human:
    def __init__(self, head, torso, arms, hands, legs, feet, weight, height, skin_color):
        self.head = head
        self.torso = torso
        self.arms = arms
        self.hands = hands
        self.legs = legs
        self.feet = feet
        self.weight = weight
        self.height = height
        self.skin_color = skin_color
    
class Head:
    def __init__(self, eyes_color, hair_color, hair_length, skin_type, face_shape, facial_hair_type):
        self.eyes_color = eyes_color
        self.hair_color = hair_color
        self.hair_length = hair_length
        self.skin_type = skin_type
        self.face_shape = face_shape
        self.facial_hair_type = facial_hair_type

class Torso:
    def __init__(self, body_shape, right_arm, left_arm, left_leg, right_leg, head):
        self.body_shape = body_shape
        self.right_arm = right_arm
        self.left_arm = left_arm
        self.left_leg = left_leg
        self.right_leg = right_leg
        self.head = head
    
class Arm:
    def __init__(self, arm_length, arm_shape, hand):
        self.arm_length = arm_length
        self.arm_shape = arm_shape
        self.hand = hand

class Hand:
    def __init__(self, hand_type, hand_shape):
        self.hand_type = hand_type
        self.hand_shape = hand_shape

class Leg:
    def __init__(self, leg_length, leg_shape, foot):
        self.leg_length = leg_length
        self.leg_shape = leg_shape
        self.foot = foot

class Feet:
    def __init__(self, feet_size, feet_shape):
        self.feet_size = feet_size
        self.feet_shape = feet_shape

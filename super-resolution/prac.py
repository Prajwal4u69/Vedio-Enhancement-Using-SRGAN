from model.srgan import generator

model = generator()
model.load_weights('D:/IIITD/ComputerVision/major project/weights/srgan/pre_generator.h5')
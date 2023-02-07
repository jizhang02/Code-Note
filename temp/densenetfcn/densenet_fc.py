from keras_contrib.applications.densenet import DenseNetFCN
from data import *
from utils import *
#hyper-parameters:
data_aug = dict(rotation_range=0.2, width_shift_range=0.05, height_shift_range=0.05, shear_range=0.05,
                    zoom_range=0.05, horizontal_flip=True, fill_mode='nearest')#with data augmentation
no_data_aug = dict()#without data augmentation
batchsize = 1
loss = 'mse'
train_path = "./data/melanoma2/train"
test_path = "./data/melanoma2/test"
predict_path = "data/melanoma2/test/image"
save_path = "./data/melanoma2/test/predict"
model_save_path = './models/densefcn_model.hdf5'
step_epoch = 1
epochs = 3
learning_rate = 1e-5
input_shape = (256,256,1)

#train stage
model = DenseNetFCN(input_shape)
model.compile(optimizer='adam', loss='mse', metrics=['accuracy'])
model.summary()
tensorboard = TensorBoard(log_dir='./logs', histogram_freq=0,write_graph=True, write_images=False)
model_checkpoint = ModelCheckpoint(model_save_path, monitor='loss',verbose=1, save_best_only=True)
trainGene = trainGenerator(batchsize,train_path,'image','label',data_aug,save_to_dir = None)
hist = model.fit_generator(trainGene,steps_per_epoch=step_epoch,epochs=epochs)
print(hist.history)

#predict stage
testGene = testGenerator(predict_path)
results = model.predict_generator(testGene,20,verbose=0)#return probability
saveResult(save_path,results)

#test stage
evaluateGene = validGenerator(1,test_path,'image','label',no_data_aug,save_to_dir = None)
score = model.evaluate_generator(evaluateGene,20, verbose=1)
print(model.metrics_names)
print(score[0], score[1])

# Save results
import json
with open('seg_result.json', 'w') as f:
    json.dump(str(hist.history), f)
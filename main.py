from model import *
from data import *
from keras.callbacks import TensorBoard
#os.environ["CUDA_VISIBLE_DEVICES"] = "0"#only 0 is visible in this programme.

#train stage
data_gen_args = dict(rotation_range=0.2, width_shift_range=0.05, height_shift_range=0.05, shear_range=0.05,
                    zoom_range=0.05, horizontal_flip=True, fill_mode='nearest')
trainGene = trainGenerator(1,'./data/melanoma2/train','image','label',data_gen_args,save_to_dir = None)
model = unet()
tensorboard = TensorBoard(log_dir='./logs', histogram_freq=0,write_graph=True, write_images=False)
model_checkpoint = ModelCheckpoint('./models/unet_model.hdf5', monitor='loss',verbose=1, save_best_only=True)
history = model.fit_generator(trainGene,steps_per_epoch=100,epochs=2,callbacks=[model_checkpoint,tensorboard])
print("model history",history.history)
print("mean loss: ",np.mean(history.history['loss']))
print("std of loss: ",np.std(history.history['loss']))
print("mean accuracy: ",np.mean(history.history['acc']))
print("std of accuracy: ",np.std(history.history['acc']))
print("mean IOU: ",np.mean(history.history['IOU']))
print('std of IOU: ',np.std(history.history['IOU']))
print("number of epoch",history.epoch)



#predict stage
testGene = testGenerator("data/melanoma2/test/image")
results = model.predict_generator(testGene,20,verbose=0)#return probability
saveResult("data/melanoma2/test/predict",results)

#teatime stage
data_gen_args = dict(rotation_range=0.2, width_shift_range=0.05, height_shift_range=0.05, shear_range=0.05,
                    zoom_range=0.05, horizontal_flip=True, fill_mode='nearest')
evaluateGene = validGenerator(1,'./data/melanoma1/test','image','label',data_gen_args,save_to_dir = None)
score = model.evaluate_generator(evaluateGene,20, verbose=1)
print(model.metrics_names)
print(score[0], score[1],score[2])
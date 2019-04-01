from keras.models import load_model
from data import *
from model import *
def dice_coef(y_true, y_pred):
    smooth = 1
    y_true_f = K.flatten(y_true)
    y_pred_f = K.flatten(y_pred)
    intersection = K.sum(y_true_f * y_pred_f)
    return (2. * intersection +smooth) / (K.sum(y_true_f) + K.sum(y_pred_f) +smooth)

def dice_coef_loss(y_true, y_pred):
    print("dice loss")
    return 1-dice_coef(y_true, y_pred)

def focal_loss(gamma=2, alpha=0.75):
    def focal_loss_fixed(y_true, y_pred):#with tensorflow
        eps = 1e-12
        y_pred=K.clip(y_pred,eps,1.-eps)#improve the stability of the focal loss and see issues 1 for more information
        pt_1 = tf.where(tf.equal(y_true, 1), y_pred, tf.ones_like(y_pred))
        pt_0 = tf.where(tf.equal(y_true, 0), y_pred, tf.zeros_like(y_pred))
        return -K.mean(alpha * K.pow(1. - pt_1, gamma) * K.log(pt_1))-K.mean((1-alpha) * K.pow( pt_0, gamma) * K.log(1. - pt_0))
    return focal_loss_fixed

def jaccard_distance_loss(y_true, y_pred, smooth=1):
    intersection = K.sum(K.abs(y_true * y_pred), axis=-1)
    sum_ = K.sum(K.abs(y_true) + K.abs(y_pred), axis=-1)
    jac = (intersection + smooth) / (sum_ - intersection + smooth)
    return (1 - jac) * smooth

custom_objects = {
    'focal_loss': focal_loss,
     'focal_loss_fixed': focal_loss(),
     'jaccard_distance_loss': jaccard_distance_loss,
     'dice_coef':dice_coef,
     'dice_coef_loss':dice_coef_loss
     }
model = load_model('../data from server/notmelanomaCE/unet_model1.hdf5', custom_objects)

print('Load done')
#path to images which you want to seg
    #./data/GlandCeildata/test/image/
    #./data/membrane/test/image/
    #./data/melanoma/test/image/
    #./data/notmelanoma/test/image/

testGene = testGenerator("./data/melanoma/test/image/")
results = model.predict_generator(testGene,5,verbose=1)

#save the predict images
    # ./data/GlandCeildata/test/predict/
    # ./data/membrane/test/predict/
    # ./data/melanoma/test/predict/
    # ./data/notmelanoma/test/predict/
saveResult("./data/melanoma/test/predict/",results)

# valid your model
# path to images which you want to evaluate
# ./data/GlandCeildata/train ./data/GlandCeildata/valid ./data/GlandCeildata/valid2
# ./data/membrane/valid
# ./data/melanoma/train ./data/melanoma/valid ./data/melanoma/valid2
# ./data/notmelanoma/train ./data/notmelanoma/valid
data_gen_args = dict(rotation_range=0.2, width_shift_range=0.05, height_shift_range=0.05, shear_range=0.05,
                    zoom_range=0.05, horizontal_flip=True, fill_mode='nearest')
evaluateGene = validGenerator(1,'./data/melanoma/test','image','label',data_gen_args,save_to_dir = None)
score = model.evaluate_generator(evaluateGene,1, verbose=1)
print(model.metrics_names)
print(score[0], score[1],score[2])
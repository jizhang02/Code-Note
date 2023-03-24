'''
Title: Multi-task-u-net:segmentation branch, regression branch
Date: 2021-03-23
Author: Jing Zhang
'''
from keras.models import *
from keras.layers import *

def Multi_task_unet(input_size = (256,256,1),filters = 16,num_class=1):
    # input layer
    inputs = Input(input_size)
    print(inputs.get_shape())
    # Level 1
    conv1 = Conv2D(filters, 3, activation='relu', padding='same', kernel_initializer='he_normal')(inputs)
    print(conv1.get_shape())
    conv1 = BatchNormalization()(conv1)
    conv1 = Conv2D(filters, 3, activation='relu', padding='same', kernel_initializer='he_normal')(conv1)
    conv1 = BatchNormalization()(conv1)
    pool1 = MaxPooling2D(pool_size=(2, 2))(conv1)

    # Level 2
    conv2 = Conv2D(filters * 2, 3, activation='relu', padding='same', kernel_initializer='he_normal')(pool1)
    conv2 = BatchNormalization()(conv2)
    conv2 = Conv2D(filters * 2, 3, activation='relu', padding='same', kernel_initializer='he_normal')(conv2)
    conv2 = BatchNormalization()(conv2)
    pool2 = MaxPooling2D(pool_size=(2, 2))(conv2)

    # Level 3
    conv3 = Conv2D(filters * 4, 3, activation='relu', padding='same', kernel_initializer='he_normal')(pool2)
    conv3 = BatchNormalization()(conv3)
    conv3 = Conv2D(filters * 4, 3, activation='relu', padding='same', kernel_initializer='he_normal')(conv3)
    conv3 = BatchNormalization()(conv3)
    pool3 = MaxPooling2D(pool_size=(2, 2))(conv3)

    # Level 4
    conv4 = Conv2D(filters * 8, 3, activation='relu', padding='same', kernel_initializer='he_normal')(pool3)
    conv4 = BatchNormalization()(conv4)
    conv4 = Conv2D(filters * 8, 3, activation='relu', padding='same', kernel_initializer='he_normal')(conv4)
    conv4 = BatchNormalization()(conv4)
    drop4 = Dropout(0.5)(conv4)
    pool4 = MaxPooling2D(pool_size=(2, 2))(drop4)

    # Level 5:bottom
    conv5 = Conv2D(filters * 16, 3, activation='relu', padding='same', kernel_initializer='he_normal')(pool4)
    conv5 = BatchNormalization()(conv5)
    conv5 = Conv2D(filters * 16, 3, activation='relu', padding='same', kernel_initializer='he_normal')(conv5)
    conv5 = BatchNormalization()(conv5)
    drop5 = Dropout(0.5)(conv5)

    # Level 1' up
    up6 = Conv2D(filters * 8, 2, activation='relu', padding='same', kernel_initializer='he_normal')(
            UpSampling2D(size=(2, 2))(drop5))
    merge6 = concatenate([drop4, up6], axis=3)
    conv6 = Conv2D(filters * 8, 3, activation='relu', padding='same', kernel_initializer='he_normal')(merge6)
    conv6 = BatchNormalization()(conv6)
    conv6 = Conv2D(filters * 8, 3, activation='relu', padding='same', kernel_initializer='he_normal')(conv6)
    conv6 = BatchNormalization()(conv6)
    #print(conv3.get_shape())

    # Level 2' up
    up7 = Conv2D(filters * 4, 2, activation='relu', padding='same', kernel_initializer='he_normal')(
            UpSampling2D(size=(2, 2))(conv6))
    #print(up7.get_shape())

    merge7 = concatenate([conv3, up7], axis=3)
    conv7 = Conv2D(filters * 4, 3, activation='relu', padding='same', kernel_initializer='he_normal')(merge7)
    conv7 = BatchNormalization()(conv7)
    conv7 = Conv2D(filters * 4, 3, activation='relu', padding='same', kernel_initializer='he_normal')(conv7)
    conv7 = BatchNormalization()(conv7)

    # Level 3' up
    up8 = Conv2D(filters * 2, 2, activation='relu', padding='same', kernel_initializer='he_normal')(
            UpSampling2D(size=(2, 2))(conv7))
    merge8 = concatenate([conv2, up8], axis=3)
    conv8 = Conv2D(filters * 2, 3, activation='relu', padding='same', kernel_initializer='he_normal')(merge8)
    conv8 = BatchNormalization()(conv8)
    conv8 = Conv2D(filters * 2, 3, activation='relu', padding='same', kernel_initializer='he_normal')(conv8)
    conv8 = BatchNormalization()(conv8)

    # Level 4' up
    up9 = Conv2D(filters, 2, activation='relu', padding='same', kernel_initializer='he_normal')(
            UpSampling2D(size=(2, 2))(conv8))
    merge9 = concatenate([conv1, up9], axis=3)
    conv9 = Conv2D(filters, 3, activation='relu', padding='same', kernel_initializer='he_normal')(merge9)
    conv9 = BatchNormalization()(conv9)
    conv9 = Conv2D(filters, 3, activation='relu', padding='same', kernel_initializer='he_normal')(conv9)
    conv9 = BatchNormalization()(conv9)

    # final layer
    seg_branch = Conv2D(num_class, 1, activation='sigmoid', name='seg_output')(conv9)
    print(seg_branch.get_shape())

    # multi-task, another task is regression
    reg_branch = Flatten()(conv9)
    reg_branch = Dense(32)(reg_branch)
    reg_branch = Activation('relu')(reg_branch)
    reg_branch = Dropout(0.3)(reg_branch)
    reg_branch = Dense(3, activation='linear', name='reg_output')(reg_branch)
    model = Model(inputs = inputs, outputs= [seg_branch, reg_branch])
    return model

'''
Title: N-net:segmentation branch, regression CNN branch
Date: 2021-03-23
Author: Jing Zhang
'''

# u-net model
def N_net(input_size = (256,256,1),filters = 16,num_class=1):
        # input layer
        inputs = Input(input_size)
        print(inputs.get_shape())
        # Level 1
        conv1 = Conv2D(filters, 3, activation='relu', padding='same', kernel_initializer='he_normal')(inputs)
        print(conv1.get_shape())
        conv1 = BatchNormalization()(conv1)
        conv1 = Conv2D(filters, 3, activation='relu', padding='same', kernel_initializer='he_normal')(conv1)
        conv1 = BatchNormalization()(conv1)
        pool1 = MaxPooling2D(pool_size=(2, 2))(conv1)

        # Level 2
        conv2 = Conv2D(filters * 2, 3, activation='relu', padding='same', kernel_initializer='he_normal')(pool1)
        conv2 = BatchNormalization()(conv2)
        conv2 = Conv2D(filters * 2, 3, activation='relu', padding='same', kernel_initializer='he_normal')(conv2)
        conv2 = BatchNormalization()(conv2)
        pool2 = MaxPooling2D(pool_size=(2, 2))(conv2)

        # Level 3
        conv3 = Conv2D(filters * 4, 3, activation='relu', padding='same', kernel_initializer='he_normal')(pool2)
        conv3 = BatchNormalization()(conv3)
        conv3 = Conv2D(filters * 4, 3, activation='relu', padding='same', kernel_initializer='he_normal')(conv3)
        conv3 = BatchNormalization()(conv3)
        pool3 = MaxPooling2D(pool_size=(2, 2))(conv3)

        # Level 4
        conv4 = Conv2D(filters * 8, 3, activation='relu', padding='same', kernel_initializer='he_normal')(pool3)
        conv4 = BatchNormalization()(conv4)
        conv4 = Conv2D(filters * 8, 3, activation='relu', padding='same', kernel_initializer='he_normal')(conv4)
        conv4 = BatchNormalization()(conv4)
        drop4 = Dropout(0.5)(conv4)
        pool4 = MaxPooling2D(pool_size=(2, 2))(drop4)

        # Level 5:bottom
        conv5 = Conv2D(filters * 16, 3, activation='relu', padding='same', kernel_initializer='he_normal')(pool4)
        conv5 = BatchNormalization()(conv5)
        conv5 = Conv2D(filters * 16, 3, activation='relu', padding='same', kernel_initializer='he_normal')(conv5)
        conv5 = BatchNormalization()(conv5)
        drop5 = Dropout(0.5)(conv5)

        # Level 1' up
        up6 = Conv2D(filters * 8, 2, activation='relu', padding='same', kernel_initializer='he_normal')(
                UpSampling2D(size=(2, 2))(drop5))
        merge6 = concatenate([drop4, up6], axis=3)
        conv6 = Conv2D(filters * 8, 3, activation='relu', padding='same', kernel_initializer='he_normal')(merge6)
        conv6 = BatchNormalization()(conv6)
        conv6 = Conv2D(filters * 8, 3, activation='relu', padding='same', kernel_initializer='he_normal')(conv6)
        conv6 = BatchNormalization()(conv6)

        # Level 2' up
        up7 = Conv2D(filters * 4, 2, activation='relu', padding='same', kernel_initializer='he_normal')(
                UpSampling2D(size=(2, 2))(conv6))
        merge7 = concatenate([conv3, up7], axis=3)
        conv7 = Conv2D(filters * 4, 3, activation='relu', padding='same', kernel_initializer='he_normal')(merge7)
        conv7 = BatchNormalization()(conv7)
        conv7 = Conv2D(filters * 4, 3, activation='relu', padding='same', kernel_initializer='he_normal')(conv7)
        conv7 = BatchNormalization()(conv7)

        # Level 3' up
        up8 = Conv2D(filters * 2, 2, activation='relu', padding='same', kernel_initializer='he_normal')(
                UpSampling2D(size=(2, 2))(conv7))
        merge8 = concatenate([conv2, up8], axis=3)
        conv8 = Conv2D(filters * 2, 3, activation='relu', padding='same', kernel_initializer='he_normal')(merge8)
        conv8 = BatchNormalization()(conv8)
        conv8 = Conv2D(filters * 2, 3, activation='relu', padding='same', kernel_initializer='he_normal')(conv8)
        conv8 = BatchNormalization()(conv8)

        # Level 4' up
        up9 = Conv2D(filters, 2, activation='relu', padding='same', kernel_initializer='he_normal')(
                UpSampling2D(size=(2, 2))(conv8))
        merge9 = concatenate([conv1, up9], axis=3)
        conv9 = Conv2D(filters, 3, activation='relu', padding='same', kernel_initializer='he_normal')(merge9)
        conv9 = BatchNormalization()(conv9)
        conv9 = Conv2D(filters, 3, activation='relu', padding='same', kernel_initializer='he_normal')(conv9)
        conv9 = BatchNormalization()(conv9)

        # final layer
        seg_branch = Conv2D(num_class, 1, activation='sigmoid', name='seg_output')(conv9)


        ### The N-Net

        # Level 3''
        conv10 = Conv2D(filters * 2, 3, activation='relu', padding='same', kernel_initializer='he_normal')(conv9)
        conv10 = BatchNormalization()(conv10)
        conv10 = Conv2D(filters * 2, 3, activation='relu', padding='same', kernel_initializer='he_normal')(conv10)
        conv10 = BatchNormalization()(conv10)
        pool10 = MaxPooling2D(pool_size=(2, 2))(conv10)

        # Level 2''
        conv11 = Conv2D(filters * 4, 3, activation='relu', padding='same', kernel_initializer='he_normal')(pool10)
        conv11 = BatchNormalization()(conv11)
        conv11 = Conv2D(filters * 4, 3, activation='relu', padding='same', kernel_initializer='he_normal')(conv11)
        conv11 = BatchNormalization()(conv11)
        pool11 = MaxPooling2D(pool_size=(2, 2))(conv11)

        # Level 1''
        conv12 = Conv2D(filters * 8, 3, activation='relu', padding='same', kernel_initializer='he_normal')(pool11)
        conv12 = BatchNormalization()(conv12)
        conv12 = Conv2D(filters * 8, 3, activation='relu', padding='same', kernel_initializer='he_normal')(conv12)
        conv12 = BatchNormalization()(conv12)
        drop12 = Dropout(0.5)(conv12)
        pool12 = MaxPooling2D(pool_size=(2, 2))(drop12)

        # Level 5:bottom
        conv13 = Conv2D(filters * 16, 3, activation='relu', padding='same', kernel_initializer='he_normal')(pool12)
        conv13 = BatchNormalization()(conv13)
        conv13 = Conv2D(filters * 16, 3, activation='relu', padding='same', kernel_initializer='he_normal')(conv13)
        conv13 = BatchNormalization()(conv13)
        drop13 = Dropout(0.5)(conv13)

        # Final layer
        reg_branch = Flatten()(drop13)
        reg_branch = Dense(32)(reg_branch)
        reg_branch = Activation('relu')(reg_branch)
        reg_branch = Dropout(0.3)(reg_branch)
        reg_branch = Dense(3, activation='linear', name='reg_output')(reg_branch)
        model = Model(inputs = inputs, outputs= [seg_branch, reg_branch])
        return model
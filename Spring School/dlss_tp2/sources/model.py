from keras.models import Model
from keras.layers import *


def unet(input_size=(256, 256, 1), ori_nb_fm=16, pretrained_weights=None, use_bn=True, show_summary=False):

    if not use_bn:
        # input layer
        input = Input(input_size)

        # Level 1
        conv1 = Convolution2D(ori_nb_fm, (3, 3), padding='same', kernel_initializer='he_normal')(input)
        conv1 = Activation('relu')(conv1)
        conv1 = Convolution2D(ori_nb_fm, (3, 3), padding='same', kernel_initializer='he_normal')(conv1)
        conv1 = Activation('relu')(conv1)
        pool1 = MaxPooling2D(pool_size=(2, 2))(conv1)

        # Level 2
        conv2 = Convolution2D(ori_nb_fm*2, (3, 3), padding='same', kernel_initializer='he_normal')(pool1)
        conv2 = Activation('relu')(conv2)
        conv2 = Convolution2D(ori_nb_fm*2, (3, 3), padding='same', kernel_initializer='he_normal')(conv2)
        conv2 = Activation('relu')(conv2)
        pool2 = MaxPooling2D(pool_size=(2, 2))(conv2)

        # level 3
        conv3 = Convolution2D(ori_nb_fm*4, (3, 3), padding='same', kernel_initializer='he_normal')(pool2)
        conv3 = Activation('relu')(conv3)
        conv3 = Convolution2D(ori_nb_fm*4, (3, 3), padding='same', kernel_initializer='he_normal')(conv3)
        conv3 = Activation('relu')(conv3)
        pool3 = MaxPooling2D(pool_size=(2, 2))(conv3)

        # Level 4
        conv4 = Convolution2D(ori_nb_fm*8, (3, 3), padding='same', kernel_initializer='he_normal')(pool3)
        conv4 = Activation('relu')(conv4)
        conv4 = Convolution2D(ori_nb_fm*8, (3, 3), padding='same', kernel_initializer='he_normal')(conv4)
        conv4 = Activation('relu')(conv4)
        pool4 = MaxPooling2D(pool_size=(2, 2))(conv4)

        # Level 5 :  bottom
        conv5 = Convolution2D(ori_nb_fm*16, (3, 3), padding='same', kernel_initializer='he_normal')(pool4)
        conv5 = Activation('relu')(conv5)
        conv5 = Convolution2D(ori_nb_fm*16, (3, 3), padding='same', kernel_initializer='he_normal')(conv5)
        conv5 = Activation('relu')(conv5)
        up6 = UpSampling2D(size=(2, 2))(conv5)

        # Level 1'
        merge6 = Concatenate()([conv4, up6])
        conv6 = Convolution2D(ori_nb_fm*8, (3, 3), padding='same', kernel_initializer='he_normal')(merge6)
        conv6 = Activation('relu')(conv6)
        conv6 = Convolution2D(ori_nb_fm*8, (3, 3), padding='same', kernel_initializer='he_normal')(conv6)
        conv6 = Activation('relu')(conv6)
        up7 = UpSampling2D(size=(2,2))(conv6)

        # Level 2'
        merge7 = Concatenate()([conv3, up7])
        conv7 = Convolution2D(ori_nb_fm*4, (3, 3), padding='same', kernel_initializer='he_normal')(merge7)
        conv7 = Activation('relu')(conv7)
        conv7 = Convolution2D(ori_nb_fm*4, (3, 3), padding='same', kernel_initializer='he_normal')(conv7)
        conv7 = Activation('relu')(conv7)
        up8 = UpSampling2D(size=(2,2))(conv7)

        # Level 3'
        merge8 = Concatenate()([conv2, up8])
        conv8 = Convolution2D(ori_nb_fm*2, (3, 3), padding='same', kernel_initializer='he_normal')(merge8)
        conv8 = Activation('relu')(conv8)
        conv8 = Convolution2D(ori_nb_fm*2, (3, 3), padding='same', kernel_initializer='he_normal')(conv8)
        conv8 = Activation('relu')(conv8)
        up9 = UpSampling2D(size=(2, 2))(conv8)

        # Level 4'
        merge9 = Concatenate()([conv1, up9])
        conv9 = Convolution2D(ori_nb_fm, (3, 3), padding='same', kernel_initializer='he_normal')(merge9)
        conv9 = Activation('relu')(conv9)
        conv9 = Convolution2D(ori_nb_fm, (3, 3), padding='same', kernel_initializer='he_normal')(conv9)
        conv9 = Activation('relu')(conv9)

        # final layer
        output = Convolution2D(4, (1, 1), activation='softmax')(conv9)

        # define as a sequential model in keras, from input to output
        model = Model(inputs=input, outputs=output)

    else:
        # input layer
        input = Input(input_size)

        # Level 1
        conv1 = Convolution2D(ori_nb_fm, (3, 3), padding='same', kernel_initializer='he_normal')(input)
        conv1 = BatchNormalization()(conv1)
        conv1 = Activation('relu')(conv1)
        conv1 = Convolution2D(ori_nb_fm, (3, 3), padding='same', kernel_initializer='he_normal')(conv1)
        conv1 = BatchNormalization()(conv1)
        conv1 = Activation('relu')(conv1)
        pool1 = MaxPooling2D(pool_size=(2, 2))(conv1)

        # Level 2
        conv2 = Convolution2D(ori_nb_fm * 2, (3, 3), padding='same', kernel_initializer='he_normal')(pool1)
        conv2 = BatchNormalization()(conv2)
        conv2 = Activation('relu')(conv2)
        conv2 = Convolution2D(ori_nb_fm * 2, (3, 3), padding='same', kernel_initializer='he_normal')(conv2)
        conv2 = BatchNormalization()(conv2)
        conv2 = Activation('relu')(conv2)
        pool2 = MaxPooling2D(pool_size=(2, 2))(conv2)

        # level 3
        conv3 = Convolution2D(ori_nb_fm * 4, (3, 3), padding='same', kernel_initializer='he_normal')(pool2)
        conv3 = BatchNormalization()(conv3)
        conv3 = Activation('relu')(conv3)
        conv3 = Convolution2D(ori_nb_fm * 4, (3, 3), padding='same', kernel_initializer='he_normal')(conv3)
        conv3 = BatchNormalization()(conv3)
        conv3 = Activation('relu')(conv3)
        pool3 = MaxPooling2D(pool_size=(2, 2))(conv3)

        # Level 4
        conv4 = Convolution2D(ori_nb_fm * 8, (3, 3), padding='same', kernel_initializer='he_normal')(pool3)
        conv4 = BatchNormalization()(conv4)
        conv4 = Activation('relu')(conv4)
        conv4 = Convolution2D(ori_nb_fm * 8, (3, 3), padding='same', kernel_initializer='he_normal')(conv4)
        conv4 = BatchNormalization()(conv4)
        conv4 = Activation('relu')(conv4)
        pool4 = MaxPooling2D(pool_size=(2, 2))(conv4)

        # Level 5 :  bottom
        conv5 = Convolution2D(ori_nb_fm * 16, (3, 3), padding='same', kernel_initializer='he_normal')(pool4)
        conv5 = BatchNormalization()(conv5)
        conv5 = Activation('relu')(conv5)
        conv5 = Convolution2D(ori_nb_fm * 16, (3, 3), padding='same', kernel_initializer='he_normal')(conv5)
        conv5 = BatchNormalization()(conv5)
        conv5 = Activation('relu')(conv5)
        up6 = UpSampling2D(size=(2, 2))(conv5)

        # Level 1'
        merge6 = Concatenate()([conv4, up6])
        conv6 = Convolution2D(ori_nb_fm * 8, (3, 3), padding='same', kernel_initializer='he_normal')(merge6)
        conv6 = BatchNormalization()(conv6)
        conv6 = Activation('relu')(conv6)
        conv6 = Convolution2D(ori_nb_fm * 8, (3, 3), padding='same', kernel_initializer='he_normal')(conv6)
        conv6 = BatchNormalization()(conv6)
        conv6 = Activation('relu')(conv6)
        up7 = UpSampling2D(size=(2, 2))(conv6)

        # Level 2'
        merge7 = Concatenate()([conv3, up7])
        conv7 = Convolution2D(ori_nb_fm * 4, (3, 3), padding='same', kernel_initializer='he_normal')(merge7)
        conv7 = BatchNormalization()(conv7)
        conv7 = Activation('relu')(conv7)
        conv7 = Convolution2D(ori_nb_fm * 4, (3, 3), padding='same', kernel_initializer='he_normal')(conv7)
        conv7 = BatchNormalization()(conv7)
        conv7 = Activation('relu')(conv7)
        up8 = UpSampling2D(size=(2, 2))(conv7)

        # Level 3'
        merge8 = Concatenate()([conv2, up8])
        conv8 = Convolution2D(ori_nb_fm * 2, (3, 3), padding='same', kernel_initializer='he_normal')(merge8)
        conv8 = BatchNormalization()(conv8)
        conv8 = Activation('relu')(conv8)
        conv8 = Convolution2D(ori_nb_fm * 2, (3, 3), padding='same', kernel_initializer='he_normal')(
            conv8)
        conv8 = BatchNormalization()(conv8)
        conv8 = Activation('relu')(conv8)
        up9 = UpSampling2D(size=(2, 2))(conv8)

        # Level 4'
        merge9 = Concatenate()([conv1, up9])
        conv9 = Convolution2D(ori_nb_fm, (3, 3), padding='same', kernel_initializer='he_normal')(merge9)
        conv9 = BatchNormalization()(conv9)
        conv9 = Activation('relu')(conv9)
        conv9 = Convolution2D(ori_nb_fm, (3, 3), padding='same', kernel_initializer='he_normal')(conv9)
        conv9 = BatchNormalization()(conv9)
        conv9 = Activation('relu')(conv9)

        # final layer
        output = Convolution2D(4, (1, 1), activation='softmax')(conv9)

        # define as a sequential model in keras, from input to output
        model = Model(inputs=input, outputs=output)

    # Display the architecture of the obtained model
    if show_summary:
        model.summary()

    # Initialize the model with a predefinite set of parameters
    if pretrained_weights:

        model.load_weights(pretrained_weights)
        print('Model loaded with pretrained weights')

    return model


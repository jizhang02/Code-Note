"""
Diogo Amorim, 2018-07-10
V-Net implementation in Keras 2
https://arxiv.org/pdf/1606.04797.pdf
"""
from keras.layers import *
from keras import backend as K
from keras.layers import Conv3D, Input
from keras.models import Model
from keras.layers.advanced_activations import PReLU

def vnet(input_size=(128, 128, 64, 1),filters = 16, batch_norm = True):
    if batch_norm:
        # Layer 1
        input = Input(input_size)
        print("the input tensor:",input.get_shape())
        conv1 = Conv3D(filters, kernel_size=(5, 5, 5), strides=1, padding='same', data_format = 'channels_last',kernel_initializer='he_normal')(input)
        print("the conv1 tensor:",conv1.get_shape())
        conv1 = PReLU()(conv1)
        print("the conv1 tensor after PReLU:",conv1.get_shape())
        add1 = add([input,conv1])
        down1 = Conv3D(filters*2, 2, strides=2, padding='same', data_format = 'channels_last',kernel_initializer='he_normal')(add1)
        down1 = PReLU()(down1)
        down1 = BatchNormalization()(down1)
        print("the down1 tensor:",down1.get_shape())
        # Layer 2
        conv2_1 = Conv3D(filters*2, kernel_size=5, padding='same', data_format = 'channels_last',kernel_initializer='he_normal')(down1)
        conv2 = PReLU()(conv2_1)
        conv2 = Conv3D(filters*2, kernel_size=5, padding='same', data_format = 'channels_last',kernel_initializer='he_normal')(conv2)
        conv2 = PReLU()(conv2)
        add2 = add([conv2_1,conv2])
        down2 = Conv3D(filters*4,2, strides=2, padding='same', data_format = 'channels_last',kernel_initializer='he_normal')(add2)
        down2 = PReLU()(down2)
        down2 = BatchNormalization()(down2)
        print("the down2 tensor:", down2.get_shape())
        # Layer 3
        conv3_1 = Conv3D(filters*4, kernel_size=5, padding='same', data_format = 'channels_last',kernel_initializer='he_normal')(down2)
        conv3 = PReLU()(conv3_1)
        conv3 = Conv3D(filters*4, kernel_size=5, padding='same',data_format = 'channels_last', kernel_initializer='he_normal')(conv3)
        conv3 = PReLU()(conv3)
        conv3 = Conv3D(filters*4, kernel_size=5, padding='same', data_format = 'channels_last',kernel_initializer='he_normal')(conv3)
        conv3 = PReLU()(conv3)
        add3 = add([conv3_1,conv3])
        down3 = Conv3D(filters*8,2, strides=2, padding='same', data_format = 'channels_last',kernel_initializer='he_normal')(add3)
        down3 = PReLU()(down3)
        down3 = BatchNormalization()(down3)
        print("the down3 tensor:", down3.get_shape())

        # Layer 4
        conv4_1 = Conv3D(filters*8, kernel_size=5, padding='same', data_format = 'channels_last',kernel_initializer='he_normal')(down3)
        conv4 = PReLU()(conv4_1)
        conv4 = Conv3D(filters*8, kernel_size=5, padding='same', data_format = 'channels_last',kernel_initializer='he_normal')(conv4)
        conv4 = PReLU()(conv4)
        conv4 = Conv3D(filters*8, kernel_size=5, padding='same', data_format = 'channels_last',kernel_initializer='he_normal')(conv4)
        conv4 = PReLU()(conv4)
        add4 = add([conv4_1,conv4])
        down4 = Conv3D(filters*16,2, strides=2, padding='same', data_format = 'channels_last',kernel_initializer='he_normal')(add4)
        down4 = PReLU()(down4)
        down4 = BatchNormalization()(down4)
        print("the down4 tensor:", down4.get_shape())

        # Layer 5:Bottom
        conv5_1 = Conv3D(filters*16, kernel_size=(5, 5, 5), padding='same', data_format = 'channels_last',kernel_initializer='he_normal')(down4)
        conv5 = PReLU()(conv5_1)
        conv5 = Conv3D(filters*16, kernel_size=(5, 5, 5), padding='same', data_format = 'channels_last',kernel_initializer='he_normal')(conv5)
        conv5 = PReLU()(conv5)
        conv5 = Conv3D(filters*16, kernel_size=(5, 5, 5), padding='same', data_format = 'channels_last',kernel_initializer='he_normal')(conv5)
        conv5 = PReLU()(conv5)
        add5 = add([conv5_1, conv5])
        up5 = Deconvolution3D(filters*16, kernel_size=(2, 2, 2), padding='same', data_format = 'channels_last',strides=(2, 2, 2))(add5)
        up5 = PReLU()(up5)
        up5 = BatchNormalization()(up5)
        print("the up5 tensor:", up5.get_shape())

        # Layer 6
        merge6 = concatenate([add4,up5], axis=4)
        conv6_1 = Conv3D(filters*16,kernel_size=(5, 5, 5), padding='same', data_format = 'channels_last',kernel_initializer='he_normal')(merge6)
        conv6 = PReLU()(conv6_1)
        conv6 = Conv3D(filters*16, kernel_size=(5, 5, 5), padding='same', data_format = 'channels_last',kernel_initializer='he_normal')(conv6)
        conv6 = PReLU()(conv6)
        conv6 = Conv3D(filters*16, kernel_size=(5, 5, 5), padding='same', data_format = 'channels_last',kernel_initializer='he_normal')(conv6)
        conv6 = PReLU()(conv6)
        add6 = add([conv6_1,conv6])
        up6 = Deconvolution3D(filters*8, kernel_size=(2, 2, 2), padding='same', data_format = 'channels_last',strides=(2, 2, 2))(add6)
        up6 = PReLU()(up6)
        up6 = BatchNormalization()(up6)
        print("the up6 tensor:", up6.get_shape())

        # Layer7
        merge7 = concatenate([add3,up6],axis=4)
        conv7_1 = Conv3D(filters*8, kernel_size=(5, 5, 5), padding='same', data_format = 'channels_last',kernel_initializer='he_normal')(merge7)
        conv7 = PReLU()(conv7_1)
        conv7 = Conv3D(filters*8, kernel_size=(5, 5, 5), padding='same', data_format = 'channels_last',kernel_initializer='he_normal')(conv7)
        conv7 = PReLU()(conv7)
        conv7 = Conv3D(filters*8, kernel_size=(5, 5, 5), padding='same', data_format = 'channels_last',kernel_initializer='he_normal')(conv7)
        conv7 = PReLU()(conv7)
        add7 = add([conv7_1, conv7])
        up7 = Deconvolution3D(filters*4, kernel_size=(2, 2, 2), padding='same', data_format = 'channels_last',strides=(2, 2, 2))(add7)
        up7 = PReLU()(up7)
        up7 = BatchNormalization()(up7)
        print("the up7 tensor:", up7.get_shape())

        # Layer8
        merge8 = concatenate([add2,up7],axis=4)
        conv8_1 = Conv3D(filters*4, kernel_size=(5, 5, 5), padding='same', data_format = 'channels_last',kernel_initializer='he_normal')(merge8)
        conv8 = PReLU()(conv8_1)
        conv8 = Conv3D(filters*4, kernel_size=(5, 5, 5), padding='same', data_format = 'channels_last',kernel_initializer='he_normal')(conv8)
        conv8 = PReLU()(conv8)
        add8 = add([conv8_1, conv8])
        up8 = Deconvolution3D(filters*2, kernel_size=(2, 2, 2), padding='same', data_format = 'channels_last',strides=(2, 2, 2))(add8)
        up8 = PReLU()(up8)
        up8 = BatchNormalization()(up8)
        print("the up8 tensor:", up8.get_shape())

        # Layer 9
        merged9 = concatenate([add1,up8], axis=4)
        conv9_1 = Conv3D(filters*2, kernel_size=(5, 5, 5), padding='same', data_format = 'channels_last',kernel_initializer='he_normal')(merged9)
        conv9 = PReLU()(conv9_1)
        add9 = add([conv9_1,conv9])
        conv9 = Conv3D(2, kernel_size=(1, 1, 1), padding='same', data_format = 'channels_last',kernel_initializer='he_normal')(add9)
        conv9 = BatchNormalization()(conv9)

        sigmoid = Conv3D(1, kernel_size=(1, 1, 1), padding='same', data_format = 'channels_last',kernel_initializer='he_normal',activation='sigmoid')(conv9)
        #softmax = Conv3D(5, kernel_size=(1, 1, 1), padding='same', kernel_initializer='he_normal',activation='softmax')(conv9)
        print("the final sigmoid tensor:", sigmoid.get_shape())
        #print("the final softmax tensor:", softmax.get_shape())


        model = Model(inputs = input, outputs = sigmoid)
    else:
        # Layer 1
        input = Input(input_size)
        print("the input tensor:", input.get_shape())
        conv1 = Conv3D(filters, kernel_size=(5, 5, 5), strides=1, padding='same', data_format='channels_last',
                       kernel_initializer='he_normal')(input)
        print("the conv1 tensor:", conv1.get_shape())
        conv1 = PReLU()(conv1)
        print("the conv1 tensor after PReLU:", conv1.get_shape())
        add1 = add([input, conv1])
        down1 = Conv3D(filters*2, 2, strides=2, padding='same', data_format='channels_last', kernel_initializer='he_normal')(
            add1)
        down1 = PReLU()(down1)
        print("the down1 tensor:", down1.get_shape())
        # Layer 2
        conv2_1 = Conv3D(filters*2, kernel_size=5, padding='same', data_format='channels_last',
                         kernel_initializer='he_normal')(down1)
        conv2 = PReLU()(conv2_1)
        conv2 = Conv3D(filters*2, kernel_size=5, padding='same', data_format='channels_last',
                       kernel_initializer='he_normal')(conv2)
        conv2 = PReLU()(conv2)
        add2 = add([conv2_1, conv2])
        down2 = Conv3D(filters*4, 2, strides=2, padding='same', data_format='channels_last', kernel_initializer='he_normal')(
            add2)
        down2 = PReLU()(down2)
        print("the down2 tensor:", down2.get_shape())
        # Layer 3
        conv3_1 = Conv3D(filters*4, kernel_size=5, padding='same', data_format='channels_last',
                         kernel_initializer='he_normal')(down2)
        conv3 = PReLU()(conv3_1)
        conv3 = Conv3D(filters*4, kernel_size=5, padding='same', data_format='channels_last',
                       kernel_initializer='he_normal')(conv3)
        conv3 = PReLU()(conv3)
        conv3 = Conv3D(filters*4, kernel_size=5, padding='same', data_format='channels_last',
                       kernel_initializer='he_normal')(conv3)
        conv3 = PReLU()(conv3)
        add3 = add([conv3_1, conv3])
        down3 = Conv3D(filters*8, 2, strides=2, padding='same', data_format='channels_last', kernel_initializer='he_normal')(
            add3)
        down3 = PReLU()(down3)
        print("the down3 tensor:", down3.get_shape())

        # Layer 4
        conv4_1 = Conv3D(filters*8, kernel_size=5, padding='same', data_format='channels_last',
                         kernel_initializer='he_normal')(down3)
        conv4 = PReLU()(conv4_1)
        conv4 = Conv3D(filters*8, kernel_size=5, padding='same', data_format='channels_last',
                       kernel_initializer='he_normal')(conv4)
        conv4 = PReLU()(conv4)
        conv4 = Conv3D(filters*8, kernel_size=5, padding='same', data_format='channels_last',
                       kernel_initializer='he_normal')(conv4)
        conv4 = PReLU()(conv4)
        add4 = add([conv4_1, conv4])
        down4 = Conv3D(filters*16, 2, strides=2, padding='same', data_format='channels_last', kernel_initializer='he_normal')(
            add4)
        down4 = PReLU()(down4)
        print("the down4 tensor:", down4.get_shape())

        # Layer 5
        conv5_1 = Conv3D(filters*16, kernel_size=(5, 5, 5), padding='same', data_format='channels_last',
                         kernel_initializer='he_normal')(down4)
        conv5 = PReLU()(conv5_1)
        conv5 = Conv3D(filters*16, kernel_size=(5, 5, 5), padding='same', data_format='channels_last',
                       kernel_initializer='he_normal')(conv5)
        conv5 = PReLU()(conv5)
        conv5 = Conv3D(filters*16, kernel_size=(5, 5, 5), padding='same', data_format='channels_last',
                       kernel_initializer='he_normal')(conv5)
        conv5 = PReLU()(conv5)
        add5 = add([conv5_1, conv5])
        up5 = Deconvolution3D(filters*16, kernel_size=(2, 2, 2), padding='same', data_format='channels_last',
                              strides=(2, 2, 2))(add5)
        up5 = PReLU()(up5)
        print("the up5 tensor:", up5.get_shape())

        # Layer 6
        merge6 = concatenate([add4, up5], axis=4)
        conv6_1 = Conv3D(filters*16, kernel_size=(5, 5, 5), padding='same', data_format='channels_last',
                         kernel_initializer='he_normal')(merge6)
        conv6 = PReLU()(conv6_1)
        conv6 = Conv3D(filters*16, kernel_size=(5, 5, 5), padding='same', data_format='channels_last',
                       kernel_initializer='he_normal')(conv6)
        conv6 = PReLU()(conv6)
        conv6 = Conv3D(filters*16, kernel_size=(5, 5, 5), padding='same', data_format='channels_last',
                       kernel_initializer='he_normal')(conv6)
        conv6 = PReLU()(conv6)
        add6 = add([conv6_1, conv6])
        up6 = Deconvolution3D(filters*8, kernel_size=(2, 2, 2), padding='same', data_format='channels_last',
                              strides=(2, 2, 2))(add6)
        up6 = PReLU()(up6)
        print("the up6 tensor:", up6.get_shape())

        # Layer7
        merge7 = concatenate([add3, up6], axis=4)
        conv7_1 = Conv3D(filters*8, kernel_size=(5, 5, 5), padding='same', data_format='channels_last',
                         kernel_initializer='he_normal')(merge7)
        conv7 = PReLU()(conv7_1)
        conv7 = Conv3D(filters*8, kernel_size=(5, 5, 5), padding='same', data_format='channels_last',
                       kernel_initializer='he_normal')(conv7)
        conv7 = PReLU()(conv7)
        conv7 = Conv3D(filters*8, kernel_size=(5, 5, 5), padding='same', data_format='channels_last',
                       kernel_initializer='he_normal')(conv7)
        conv7 = PReLU()(conv7)
        add7 = add([conv7_1, conv7])
        up7 = Deconvolution3D(filters*4, kernel_size=(2, 2, 2), padding='same', data_format='channels_last',
                              strides=(2, 2, 2))(add7)
        up7 = PReLU()(up7)
        print("the up7 tensor:", up7.get_shape())

        # Layer8
        merge8 = concatenate([add2, up7], axis=4)
        conv8_1 = Conv3D(filters*4, kernel_size=(5, 5, 5), padding='same', data_format='channels_last',
                         kernel_initializer='he_normal')(merge8)
        conv8 = PReLU()(conv8_1)
        conv8 = Conv3D(filters*4, kernel_size=(5, 5, 5), padding='same', data_format='channels_last',
                       kernel_initializer='he_normal')(conv8)
        conv8 = PReLU()(conv8)
        add8 = add([conv8_1, conv8])
        up8 = Deconvolution3D(filters*4, kernel_size=(2, 2, 2), padding='same', data_format='channels_last',
                              strides=(2, 2, 2))(add8)
        up8 = PReLU()(up8)
        print("the up8 tensor:", up8.get_shape())

        # Layer 9
        merged9 = concatenate([add1, up8], axis=4)
        conv9_1 = Conv3D(filters*2, kernel_size=(5, 5, 5), padding='same', data_format='channels_last',
                         kernel_initializer='he_normal')(merged9)
        conv9 = PReLU()(conv9_1)
        add9 = add([conv9_1, conv9])
        conv9 = Conv3D(2, kernel_size=(1, 1, 1), padding='same', data_format='channels_last',
                       kernel_initializer='he_normal')(add9)

        sigmoid = Conv3D(1, kernel_size=(1, 1, 1), padding='same', data_format='channels_last',
                         kernel_initializer='he_normal', activation='sigmoid')(conv9)
        #softmax = Conv3D(1, kernel_size=(1, 1, 1), padding='same', data_format='channels_last',kernel_initializer='he_normal',activation='softmax')(conv9)
        #print("the final sigmoid tensor:", sigmoid.get_shape())

        model = Model(inputs=input, outputs=sigmoid)

    return model
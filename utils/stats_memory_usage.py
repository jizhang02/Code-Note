'''
-----------------------------------------------
File Name: stats_memory_usage.py
Description: memroy usage in theory
Author: Jing
Date: 9/28/2021
-----------------------------------------------
'''
def get_model_memory_usage(batch_size, model):
    import numpy as np
    try:
        from keras import backend as K
    except:
        from tensorflow.keras import backend as K

    shapes_mem_count = 0
    internal_model_mem_count = 0
    for l in model.layers:
        layer_type = l.__class__.__name__
        if layer_type == 'Model':
            internal_model_mem_count += get_model_memory_usage(batch_size, l)
        single_layer_mem = 1
        out_shape = l.output_shape
        print('the type of outputshape is:',type(out_shape)) # <class 'tuple'>
        if type(out_shape) is list:
            out_shape = out_shape[0]
            print('the shape of current layer:',out_shape)
        for s in out_shape:
            if s is None:
                continue
            #print('s in this layer is:',s)
            single_layer_mem *= s
            #print('the memory in this layer is:',single_layer_mem)
        shapes_mem_count += single_layer_mem

    trainable_count = np.sum([K.count_params(p) for p in model.trainable_weights])
    non_trainable_count = np.sum([K.count_params(p) for p in model.non_trainable_weights])

    number_size = 4.0
    if K.floatx() == 'float16':
        number_size = 2.0
    if K.floatx() == 'float64':
        number_size = 8.0

    print('internal_model_mem_count',internal_model_mem_count)
    total_memory = number_size * (batch_size * shapes_mem_count + trainable_count + non_trainable_count)
    gbytes = np.round(total_memory / (1024.0 ** 3), 3) + internal_model_mem_count
    return gbytes
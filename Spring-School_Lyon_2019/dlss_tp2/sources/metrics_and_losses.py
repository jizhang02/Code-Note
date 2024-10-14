from keras import backend as k


def _dice(y_true, y_pred):
    """ Binary dice indice adapted to keras tensors """

    flat_y_true = k.flatten(y_true)
    flat_y_pred = k.flatten(y_pred)

    intersect = k.sum(flat_y_true * flat_y_pred)

    s_true = k.sum(flat_y_true)
    s_pred = k.sum(flat_y_pred)

    return (2. * intersect + 1.) / (s_true + s_pred + 1.)


def multiclass_dice(y_true, y_pred):
    """Extension of the dice to a 4 class problem"""

    res = k.variable(0., name='dice_classes')

    for i in range(4):
        res = res + _dice(y_true[:, :, :, i], y_pred[:, :, :, i])

    return res / 4

def classes_dice_loss(y_true, y_pred):
    """Loss based on the dice : scales between [0, 1], optimized when minimized"""

    return 1 - multiclass_dice(y_true, y_pred)


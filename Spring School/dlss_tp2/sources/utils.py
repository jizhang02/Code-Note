import matplotlib
import matplotlib.pyplot as plt
import keras
from keras.callbacks import *


def display_dataset_samples(nb_examples, x, y):

    """Display nb_examples images and segmentation masks stored in lists x and y"""

    # random selection of indices of images to be displayed
    im_id = np.random.randint(0, x.shape[0], nb_examples)

    # Plot of the selected images
    plt.figure(figsize=(15, 7), dpi=200)
    for i, ind in enumerate(im_id):

        # image
        us_image = x[ind, :, :, 0]
        plt.subplot(2, nb_examples, i+1)
        plt.axis('off')
        plt.title('Image ' + str(ind))
        plt.imshow(us_image, cmap='gray')

        # mask
        mask = y[ind, :, :, :]
        plt.subplot(2, nb_examples, i+1 + nb_examples)
        plt.axis('off')
        plt.title('Corresponding mask')
        plt.imshow(us_image, cmap='gray')
        plt.imshow(np.argmax(mask, axis=-1), cmap='jet', alpha=0.3)

    plt.show()


def display_dataset_samples_with_estimation(nb_examples, x_ref, y_ref, segs, res):

    """Display nb_examples images, groundtruth masks and predictions stored in lists x_ref, y_ref and segs,
       as well as geometric performance """

    # get random indices
    im_id = np.random.randint(0, x_ref.shape[0], nb_examples)

    # Sample examples from the training set
    plt.figure(figsize=(15, 12), dpi=200)
    for i, ind in enumerate(im_id):

        # images
        us_image = x_ref[ind, :, :, 0]
        plt.subplot(3, nb_examples, i + 1)
        plt.axis('off')
        plt.title('Image ' + str(ind))
        plt.imshow(us_image, cmap='gray')

        # reference
        mask = y_ref[ind, :, :, :]
        plt.subplot(3, nb_examples, i + 1 + nb_examples)
        plt.axis('off')
        plt.title('Groundtruth ' + str(ind))
        plt.imshow(us_image, cmap='gray')
        plt.imshow(np.argmax(mask, axis=-1), cmap='jet', alpha=0.3)

        # Prediction
        pred = segs[ind, :, :, :]
        plt.subplot(3, nb_examples, i + 1 + 2 * nb_examples)
        plt.axis('off')
        plt.title('Prediction ' + str(ind) + '\n' + 'Dice' + str(np.around(res[ind, :, 0], 2)) + '\n' + 'HD' + str(
            np.around(res[ind, :, 1], 2)))
        plt.imshow(us_image, cmap='gray')
        plt.imshow(np.argmax(pred, axis=-1), cmap='jet', alpha=0.3)

    plt.show()


def display_loss_metric_curves(nb_epochs, history, save_fig_dir, save_fig_filename):

    """Display nb_examples images, groundtruth masks and predictions stored in lists x_ref, y_ref and segs,
       as well as geometric performance """

    # Retrieve values from the log
    time_steps = range(nb_epochs)
    train_loss = history.train_losses
    val_loss = history.val_losses
    train_dice = history.train_metrics
    val_dice = history.val_metrics

    if not os.path.isdir(save_fig_dir):
        os.makedirs(save_fig_dir)

    # Display loss and metrics curves
    fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(12, 4), dpi=200)
    ax[0].plot(time_steps, train_loss, 'r', label='Train')
    ax[0].plot(time_steps, val_loss, 'g', label='Valid')
    ax[0].legend()
    ax[0].set_xlabel('Epoch')
    ax[0].set_ylabel('Value')
    ax[0].set_title('Losses')

    ax[1].plot(time_steps, train_dice, 'm', label='Train')
    ax[1].plot(time_steps, val_dice, 'b', label='Valid')
    ax[1].legend()
    ax[1].set_xlabel('Epoch')
    ax[1].set_ylabel('Value')
    ax[1].set_title('Metrics')

    fig.tight_layout()
    fig.savefig(os.path.join(save_fig_dir, save_fig_filename), dpi=200, orientation='landscape', format='png')

def display_model_weights(first_weights, nb_feat):

    print('\nFilters')
    kernel_size = first_weights.shape[2]
    conv_shape = first_weights.shape[0]

    if conv_shape ==3:
        if kernel_size > 1:
            print("We only display weights applied to the first previous feature maps for convenience")

        plt.figure(figsize=(15, 15), dpi=200)
        for i in range(nb_feat):
            plt.subplot(nb_feat / 2, nb_feat / 2, i + 1)
            plt.axis('off')
            #plt.colorbar()
            plt.imshow(first_weights[:, :, 0, i], cmap='gray')
        plt.show()

    else:
        " We do not display the weights for conv(1, 1) as they are hard (impossible?) to interpret "


def display_model_feature_maps(feat_maps, nb_feat):

    print('\nFeature maps')
    plt.figure(figsize=(15, 15), dpi=200)
    for i in range(nb_feat):
        plt.subplot(nb_feat / 2, nb_feat / 2, i + 1)
        plt.axis('off')
        plt.imshow(feat_maps[:, :, i], cmap='gray')
    plt.show()


class LossHistory(keras.callbacks.Callback):

    """Keras callback to store losses and metrics values after each epoch"""

    def on_train_begin(self, logs={}):
        self.train_losses = []
        self.val_losses = []
        self.train_metrics = []
        self.val_metrics = []

    def on_epoch_end(self, epoch, logs={}):
        self.train_losses.append(logs.get('loss'))
        self.val_losses.append(logs.get('val_loss'))
        self.train_metrics.append(logs.get('multiclass_dice'))
        self.val_metrics.append(logs.get('val_multiclass_dice'))





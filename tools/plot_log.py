import re
import sys
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.ndimage.interpolation import shift

patterns = { 'train_niters': re.compile('Iteration (\d+), loss = \d+[.]*\d*'),
        'train_loss': re.compile('Iteration \d+, loss = (\d+[.]*\d*)'),
        'train_acc': re.compile('Train net output #0: accuracy = (\d+[.]*\d*)'),
        'val_niters': re.compile('Iteration (\d+), Testing net'),
        'val_acc': re.compile('Test net output #0: accuracy = (\d+[.]*\d*)')
        }

def parse_log(log_file):
    extracted_data = {}

    # initialization
    for p in patterns:
        extracted_data[p] = []


    with open(log_file) as lf:
        for line in lf.readlines():
            for p in patterns:
                match = patterns[p].search(line)
                if match:
                    num = match.group(1)
                    if '.' in num:
                        num = float(num)
                    else:
                        num = int(num)
                    extracted_data[p].append(num)

    # sanity check
    #for split in ['train', 'val']:
    #    for p in patterns:
    #        if split not in p or 'niters' in p:
    #            continue
    #        niters = extracted_data[split + '_niters']
    #        data = extracted_data[p]
    #        while len(niters) != len(data):
    #            min_len = min(len(niters), len(data))
    #            for i in range(min_len, len(niters)):
    #                niters.pop()
    #            for i in range(min_len, len(data)):
    #                data.pop()

    return extracted_data

def smooth(seq):

    smooth = []
    smooth_len = max(10, len(seq) / 20)
    #smooth = np.cumsum(np.array(seq)) / (np.arange(len(seq)) + 1)
    smooth = np.cumsum(seq) / smooth_len
    smooth = smooth - shift(smooth, smooth_len, cval=0)
    smooth[:smooth_len] = np.cumsum(seq[:smooth_len]) / (np.arange(smooth_len) + 1)

    return smooth



def plot_log(train_niters, train_loss, train_acc=None, val_niters=None, val_acc=None, path=None, ylim='[0, 1]'):

    assert len(train_niters) == len(train_loss), 'length niters and loss is ' +\
           'different: {:d} vs. {:d}'.format(len(train_niters), len(train_loss))
    assert train_loss is not None and len(train_loss) != 0, 'illegal train_loss'

    # first axis
    _, ax1 = plt.subplots()
    ax1.set_axisbelow(True)
    ax1.yaxis.grid(color='gray', linestyle='dashed')
    ax1.set_xlabel('Iterations')
    #ax1.set_yscale('log')
    ax1.set_ylabel('Train loss')

    # plot the loss
    loss_plot, =    ax1.plot(   train_niters, train_loss,
                                '#88cb88', linewidth=1,
                                label='Loss (left axis)')
    loss_smth, =    ax1.plot(   train_niters, smooth(train_loss),
                                '#287657', linewidth=2,
                                label='Train Loss (left axis)')
    legend = [loss_smth]

    # plot the accuracy
    ax2 = None
    if train_acc is not None and len(train_acc) > 0:
        ax2 = ax1.twinx()
        #ax2.set_yscale('log')
        ax2.set_ylabel('Accuracy')
        ax2.set_ylim(eval(ylim))
        #ax2.set_xlim((0,50000))

        tracc_plot, = ax2.plot( train_niters, train_acc,
                                '#9fc3ff', linewidth=1,
                                label='Train Accuracy (right axis)')
        tracc_smth, = ax2.plot( train_niters, smooth(train_acc),
                                '#0060ff', linewidth=2,
                                label='Train Accuracy (right axis)')
        legend += [tracc_smth]

    # plot validation accuracy if any
    if val_acc is not None and len(val_acc) > 0:
        if ax2 is None:
            ax2 = ax1.twinx()
            #ax2.set_yscale('log')
            ax2.set_ylabel('Accuracy')
            ax2.set_ylim([0, 1])

        val_plot, = ax2.plot( val_niters, val_acc,
                                '#ff0000', linewidth=2,
                                label='Validation Accuracy (right axis)')
        legend += [val_plot]

    plt.legend(handles=legend, loc='best', fancybox=True, framealpha=.4)

    # output
    if path is None:
        plt.show()
    else:
        plt.savefig(path, bbox_inches='tight')
    plt.close('all')


if __name__ == '__main__':
    if len(sys.argv) == 2:
        plot_log(**parse_log(sys.argv[1]))
    if len(sys.argv) == 3:
        plot_log(path=sys.argv[2], **parse_log(sys.argv[1]))
    if len(sys.argv) == 4:
        plot_log(path=sys.argv[2], ylim=sys.argv[3], **parse_log(sys.argv[1]))


import matplotlib as mpl
mpl.use('agg')
import matplotlib.pyplot as plt
from math import sqrt, pi, acos
import numpy as np

class Evaluator(object):

    def __init__(self):
        self.perimg = list()
        self.stat_all = None
        pass

    def __str__(self):
        pass

    def get_header(self, is_perimg):
        header = ['pr', 'gt'] + self.metrics if is_perimg else self.metrics
        headers = [' | '.join(header), ' | '.join(['-'*len(t) for t in header])]
        return '\n'.join(headers)

    def eval_perimg(self, pr_dict, gt_dict):
        pass

    def eval_all(self):
        pass

    def report_perimg(self):
        if len(self.perimg) == 0:
            return None
        perimg = sorted(self.perimg, key=lambda x:x[2][self.sorted])
        perimg_strs = list()
        for pr_name, gt_name, stat in perimg:
            perimg_str  = ' | '.join([pr_name, gt_name])
            perimg_str +=(' | {:.4f}'*len(self.metrics)).format(*[stat[t] for t in self.metrics])
            perimg_strs.append(perimg_str)
        return '\n'.join([self.get_header(is_perimg=True)] + perimg_strs)

    def report_all(self):
        if self.stat_all is None:
            return None
        stat = self.stat_all
        self.report_str = ' | '.join(['{:.4f}'.format(stat[t]) for t in self.metrics])
        return '\n'.join([self.get_header(is_perimg=False), self.report_str])

    def extra_report(self, cache_dir, report_file):
        pass


class Flow(Evaluator):

    def __init__(self):
        Evaluator.__init__(self)
        self.metrics = ['epe', 'aae']
        self.sorted = 'epe'
        self.unknown_thresh = 1e7

    # Calculate average end point error
    def epe(self, FG, FP):
        """
        """
        smallflow = 0.0
        '''
        stu = tu[bord+1:end-bord,bord+1:end-bord]
        stv = tv[bord+1:end-bord,bord+1:end-bord]
        su = u[bord+1:end-bord,bord+1:end-bord]
        sv = v[bord+1:end-bord,bord+1:end-bord]
        '''

        stu = FG[..., 0]
        stv = FG[..., 1]
        su = FP[..., 0]
        sv = FP[..., 1]

        idxUnknow = (abs(stu) > self.unknown_thresh) | (abs(stv) > self.unknown_thresh)
        stu[idxUnknow] = 0
        stv[idxUnknow] = 0
        su[idxUnknow] = 0
        sv[idxUnknow] = 0

        ind2 = [(np.absolute(stu) > smallflow) | (np.absolute(stv) > smallflow)]

        epe = np.sqrt((stu - su) ** 2 + (stv - sv) ** 2)
        epe = epe[ind2]
        return np.mean(epe)

    def aae(self, FG, FP):

        valid_counter = 0
        AAE_sum = 0.0
        W, H, _ = FG.shape
        for x in range(W):
          for y in range(H):
            uc, vc = FG[x,y,0], FG[x,y,1]
            ue, ve = FP[x,y,0], FP[x,y,1]
            if (np.isnan(uc) or np.isnan(vc) or \
                np.isnan(ue) or np.isnan(ve) or \
                abs(uc) > 2048    or abs(vc) > 2048):
              continue
            aux = (uc*ue+vc*ve+1.)/sqrt((uc*uc+vc*vc+1.)*(ue*ue+ve*ve+1.))
            if aux > 1.0:
              aux = 1.0
            elif (aux < -1.0):
              aux = -1.0
            AAE_sum += (180./pi)*acos(aux)
            valid_counter += 1

        return AAE_sum/valid_counter


    def eval_perimg(self, pr_dict, gt_dict):
        """
            pr_dict['data'], and gt_dict['data'] is the raw blob data
            where the first channel (batch channel) is always 1
        """

        pr_name = pr_dict['path']
        pr = pr_dict['data'].squeeze()
        gt_name = gt_dict['path']
        gt = gt_dict['data'].squeeze()

        # flow data have the third channel reversed (just as RGB image -> BGR)
        pr = pr[::-1, ...].transpose((1, 2, 0))
        gt = gt[::-1, ...].transpose((1, 2, 0))

        stat = {'epe': self.epe(pr, gt),
                'aae': self.aae(pr, gt)}

        self.perimg.append((pr_name, gt_name, stat))

        return (pr, gt)

    def eval_all(self):

        if len(self.perimg) == 0:
            return None

        stat = list(zip(*self.perimg)[2])
        self.stat_all = {'epe': np.mean([st['epe'] for st in stat]),
                'aae': np.mean([st['aae'] for st in stat])}

        return self.stat_all


class Seg(Evaluator):

    def __init__(self, nclasses, void_label=None, mapping=None):
        Evaluator.__init__(self)

        self.count_mat = np.zeros((nclasses, nclasses), np.float)
        self.nclasses = nclasses

        self.void_label = void_label if void_label is not None else nclasses
        #self.mapping = dict((v, k) for k, v in mapping.iteritems()) if mapping is not None \
        #        else dict(zip(xrange(nclasses), xrange(nclasses)))
        # for report
        self.metrics = ['global', 'class', 'miou']
        self.sorted = 'miou'

    def seg_stat(self, count_mat):
        if np.sum(count_mat) == 0:
            return None

        # compute global accuracy
        global_acc = np.sum(np.diag(count_mat)) / np.sum(count_mat).astype(np.float)

        # BE CAUTIOUS HERE, without dim extension,
        # the division is columns-wise (but we want it to be row-wise)
        gt = count_mat.sum(axis=1)
        npred_pc = count_mat.sum(axis=0) # npixels predicted per class
        conf_mat_fp = count_mat / (npred_pc + (npred_pc == 0))
        conf_mat_fn = count_mat / (gt[..., None] + (gt[..., None] == 0))
        # compute class accuracy
        class_acc = np.sum(np.diag(conf_mat_fn)) / np.count_nonzero(gt)

        # compute mean intersection over union for each class
        diag = np.diag(count_mat)
        denom = np.sum(count_mat, axis=0) + np.sum(count_mat, axis=1) - diag
        miou_pc = diag / (denom + (denom == 0)) # TP / (TP + FP + FN)
        miou = np.sum(miou_pc) / np.count_nonzero(gt)

        return {'global': global_acc,
                'class': class_acc,
                'miou': miou,
                'confmat_fp': conf_mat_fp,
                'confmat_fn': conf_mat_fn,
                'miou_pc': miou_pc}

    #def map_im(self, lhs, mapping):
    #    # unknown label to be the largest value
    #    unknown_label = max(mapping.values())
    #    rhs = np.zeros(lhs.shape[:2], dtype=np.uint8) + unknown_label
    #    for k in mapping:
    #        rhs[lhs == k] = mapping[k]
    #    return rhs

    def eval_perimg(self, pr_dict, gt_dict):

        pr_name = pr_dict['path']
        pr = pr_dict['data'].squeeze()
        gt_name = gt_dict['path']
        gt = gt_dict['data'].squeeze()

        pr = pr.argmax(axis=0) #self.map_im(pr.argmax(axis=0), self.mapping)
        pr[gt == self.void_label] = self.void_label

        # [j, k] = number of pixels which predict label k while it should be j
        # hence the rows are ground truth labels
        # while the colums are predicted labels
        count_mat = np.zeros_like(self.count_mat)
        for j in range(self.nclasses):
            for k in range(self.nclasses):
                cl = gt == j
                clp = pr == k
                index = cl * clp
                count_mat[j, k] += np.sum(index)
        self.count_mat += count_mat

        # evaluation
        stat = self.seg_stat(count_mat)
        self.perimg.append((pr_name, gt_name, stat))

        return (pr, gt)

    def eval_all(self):

        if len(self.perimg) == 0:
            return None

        # evaluation
        self.stat_all = self.seg_stat(self.count_mat)
        return self.stat_all

    def extra_report(self, cache_dir, report_file):
        # output confusion matrix
        results = self.stat_all
        report_txt = ''
        for cfm_name in ['confmat_fn', 'confmat_fp']:
            fig, ax = plt.subplots()
            cax = ax.imshow(results[cfm_name], interpolation='none', cmap='jet')
            fig.colorbar(cax)
            ax.set_xticks(np.arange(0, results[cfm_name].shape[1]))
            ax.set_yticks(np.arange(0, results[cfm_name].shape[0]))
            ax.set_ylabel('Ground truth class')
            ax.set_xlabel('Predicted class')
            plt.tight_layout()
            plt.savefig(cache_dir + '/' + cfm_name+'.png')

        report_txt += '\n\n- *Confusion matrix* : False Negative | False Positive\n\n'
        report_txt += '![conf_mat_fn](confmat_fn.png) | '
        report_txt += '![conf_mat_fp](confmat_fp.png)'

        report_file.write(report_txt)


class Norm(Evaluator):

    def __init__(self):
        Evaluator.__init__(self)
        self.metrics = ['mean', 'median', 'rmse', '11.25', '22.5', '30']
        self.sorted = 'mean'
        pass

    # Calculate average end point error
    def norm_stat(self, NG, NP):
        NG = NG / np.sqrt(np.power(NG, 2).sum(axis=2, keepdims=True))
        NP = NP / np.sqrt(np.power(NP, 2).sum(axis=2, keepdims=True))
        DP = (NG * NP).sum(axis=2)
        T = np.minimum(1, np.maximum(-1, DP))

        E = np.rad2deg(np.arccos(T))
        return {'error': E,
                'mean': np.mean(E),
                'median': np.median(E),
                'rmse': np.sqrt(np.mean(np.power(E,2))),
                '11.25': np.mean(E < 11.25) * 100,
                '22.5': np.mean(E < 22.5) * 100,
                '30': np.mean(E < 30) * 100}

    def eval_perimg(self, pr_dict, gt_dict):

        pr_name = pr_dict['path']
        pr = pr_dict['data'].squeeze()
        gt_name = gt_dict['path']
        gt = gt_dict['data'].squeeze()

        pr = pr[::-1, ...].transpose((1, 2, 0))
        gt = gt[::-1, ...].transpose((1, 2, 0))

        stat = self.norm_stat(pr, gt)
        self.perimg.append((pr_name, gt_name, stat))

        return (pr, gt)

    def eval_all(self):
        if len(self.perimg) == 0:
            return None

        E = zip(*self.perimg)[2]
        self.stat_all = {'mean': np.mean([x['error'] for x in E]),
                'median': np.median([x['error'] for x in E]),
                'rmse': np.sqrt(np.mean(np.power([x['error'] for x in E],2))),
                '11.25': np.mean(np.array([x['error'] for x in E]) < 11.25) * 100,
                '22.5': np.mean(np.array([x['error'] for x in E]) < 22.5) * 100,
                '30': np.mean(np.array([x['error'] for x in E]) < 30) * 100}
        return self.stat_all


class Depth(Evaluator):

    def __init__(self):
        pass

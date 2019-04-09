import copy
import yaml

datasets = ['vkitti.yaml', 'gdxtracted.yaml']
types = ['gt', 'pr']
modalities = ['seg', 'flow', 'norm']


def single():

    for d in datasets:
        config = dict()
        config['INPUT'] = dict()
        config['INPUT']['DATASET'] = d
        for target in modalities:
            config['INPUT']['LAYOUT'] = list()
            config['REFINE'] = dict()
            config['REFINE']['TARGETS'] = target
            config['INPUT']['LAYOUT'].append('pr'+target)
            n_supps = 1
            fname_tar = d.split('.')[0] + '-' + 'rf_'+target + '-' + 'pr'+target
            layout = copy.copy(config['INPUT']['LAYOUT'])
            for supp in modalities:
                if supp == target:
                    continue
                for br_t in types:
                    for br in range(0, n_supps+1):
                        config['INPUT']['LAYOUT'] = copy.copy(layout)
                        if br > len(config['INPUT']['LAYOUT'])-1:
                            config['INPUT']['LAYOUT'].append(br_t+supp)
                            fname_sup = '-'+br_t+supp
                        else:
                            config['INPUT']['LAYOUT'][br] += ', ' + br_t + supp
                            fname_sup='_'+br_t+supp

                        print config
                        yaml.dump(config,
                                open('../experiments/' + fname_tar+fname_sup+'.yaml','w'),
                                default_flow_style=False)

def double():

    for d in datasets:
        config = dict()
        config['INPUT'] = dict()
        config['INPUT']['DATASET'] = d
        for target in modalities:
            config['INPUT']['LAYOUT'] = list()
            config['REFINE'] = dict()
            config['REFINE']['TARGETS'] = target
            config['INPUT']['LAYOUT'].append('pr'+target)
            n_supps = 2
            fname_tar = d.split('.')[0] + '-' + 'rf_'+target + '-' + 'pr'+target
            layout = copy.copy(config['INPUT']['LAYOUT'])

            for i, supp in enumerate(modalities):
                if supp == target:
                    continue
                for br_t in types:
                    for br in range(n_supps):
                        config['INPUT']['LAYOUT'] = copy.copy(layout)
                        if br > len(config['INPUT']['LAYOUT'])-1:
                            config['INPUT']['LAYOUT'].append(br_t+supp)
                            fname_sup = '-'+br_t+supp
                        else:
                            config['INPUT']['LAYOUT'][br] += ', ' + br_t + supp
                            fname_sup='_'+br_t+supp

                        layout1 = copy.copy(config['INPUT']['LAYOUT'])
                        for j in range(i+1, len(modalities)):
                            supp1 = modalities[j]
                            if supp1 == target:
                                continue
                            for k in range(n_supps+1):
                                if k > len(layout1):
                                    continue
                                config['INPUT']['LAYOUT'] = copy.copy(layout1)


                                if k > len(config['INPUT']['LAYOUT'])-1:
                                    config['INPUT']['LAYOUT'].append(br_t+supp1)
                                    fname_sup2 = '-'+br_t+supp1
                                else:
                                    config['INPUT']['LAYOUT'][k] += ', ' + br_t + supp1
                                    fname_sup2='_'+br_t+supp1

                                print config
                                yaml.dump(config,
                                        open('../experiments/' + fname_tar+fname_sup+fname_sup2+'.yaml','w'),
                                        default_flow_style=False)

single()
double()

def avail(all_layouts, layout):

    for l in all_layouts:
        if l == layout:
            return False
    return True

def double3(all_layouts, layout, nsups, target):
    if nsups < 0:
        if avail(all_layouts, layout):
            all_layouts.append(layout)
        return
    for m in modalities:
        if m == target:
            continue
        for i in range(nsups+1):
            if i > len(layout):
                layout.add(frozenset([m]))
            else:
                fs = layout.pop()
                temp = set([s for s in fs])
                temp.add(m)
                layout.add(frozenset(temp))
            double3(all_layouts, layout, nsups-1, target)

#for m in modalities:
#    all_layouts = list()
#    layout = set()
#    fs = frozenset([m])
#    layout.add(fs)
#    double3(all_layouts, layout, 2, m)
#    print all_layouts


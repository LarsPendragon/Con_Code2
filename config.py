# coding=utf-8
import os
import platform

os_name = platform.system().lower()


def is_mac():
    return os_name.startswith('darwin')


def is_windows():
    return os_name.startswith('windows')


def is_linux():
    return os_name.startswith('linux')


def parse_weigths(weights):
    if not weights \
            or not weights.endswith('.h5') \
            or not weights.__contains__('/') \
            or not weights.__contains__('-'):
        return None
    try:
        weights_info = weights.split(os.path.sep)[-1].replace('.h5', '').split('-')
        if len(weights_info) != 3:
            return None
        epoch = int(weights_info[0])
        val_loss = float(weights_info[1])
        val_acc = float(weights_info[2])
        return epoch, val_loss, val_acc
    except Exception as e:
        raise Exception('Parse weights failure: %s', str(e))


def CONTEXT(name, **kwargs):
    return {
        'weights': 'params/%s/{epoch:05d}-{val_loss:.4f}-{val_acc:.4f}.h5' % name,
        'summary': 'log/%s' % name,
        'predictor_cache_dir': 'cache/%s' % name,
        'load_imagenet_weights': is_windows(),
        'path_json_dump': 'eval_json/%s/result%s.json' % (
            name, ('_' + kwargs['policy']) if kwargs.__contains__('policy') else ''),
    }


# image path
if is_windows():
    PATH_TRAIN_BASE = 'D:/BaiduNetdiskDownload/dataset/ai_challenger_scene_train_20170904'
    PATH_VAL_BASE = 'D:/BaiduNetdiskDownload/dataset/ai_challenger_scene_validation_20170908'
    PATH_TEST_B = ''
elif is_mac():
    PATH_TRAIN_BASE = '/Users/zijiao/Desktop/ai_challenger_scene_train_20170904'
    PATH_VAL_BASE = '/Users/zijiao/Desktop/ai_challenger_scene_validation_20170908'
    PATH_TEST_B = ''
elif is_linux():
    PATH_TRAIN_BASE = ''
    PATH_VAL_BASE = ''
    PATH_TEST_B = ''
else:
    raise Exception('No images configured on %s' % os_name)

PATH_TRAIN_IMAGES = os.path.join(PATH_TRAIN_BASE, 'classes')
PATH_TRAIN_JSON = os.path.join(PATH_TRAIN_BASE, 'scene_train_annotations_20170904.json')

PATH_VAL_IMAGES = os.path.join(PATH_VAL_BASE, 'classes')
PATH_VAL_JSON = os.path.join(PATH_VAL_BASE, 'scene_validation_annotations_20170908.json')

PATH_JSON_DUMP = 'eval_json/resnet.json'

# train info
IM_SIZE_299 = 299
IM_SIZE_224 = 224
BATCH_SIZE = 32
CLASSES = len(os.listdir(PATH_TRAIN_IMAGES))
EPOCH = 10

if __name__ == '__main__':
    print(PATH_TRAIN_IMAGES)
    print(CONTEXT('test').values())

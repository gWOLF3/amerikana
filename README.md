### ☕ amerikana: [tf.keras](https://www.tensorflow.org/guide/keras) prediction decoder for [imagenet-simple-labels](https://github.com/anishathalye/imagenet-simple-labels)

a simpler, more human readable imagenet synset for keras. 


comparison:

| ID | ImageNet | Keras | Simple (this repo) |
| --- | --- | --- | --- |
| 87 | African grey, African gray, Psittacus erithacus | African_grey | grey parrot |
| 97 | drake | drake | duck |
| 913 | wreck | wreck | shipwreck |
| 930 | French loaf | French_loaf | baguette |


#### quickstart:

should be used as a drop in replacement for [tf.keras.applications.imagenet_utils.decode_predictions](https://www.tensorflow.org/api_docs/python/tf/keras/applications/imagenet_utils/decode_predictions)

install with pip:
```
pip install amerikana
```

import:

```
from amerikana import decode_predictions
```

instead of:

```
from tensorflow.keras.applications.imagenet_utils import decode_predictions
```

example use:

```
predictions = model.predict(processed_image)
labels = decode_predictions(predictions)
print(labels)
```


#### credit: 

- simplified labels list: [imagenet-simple-labels](https://github.com/anishathalye/imagenet-simple-labels). see information and comparison for simplified labels there.

- the module code used in this project is a derivative of tf.keras [imagenet_utils](https://github.com/tensorflow/tensorflow/blob/1a9dcb0b4844007f0943581f4fbeaa7fc8628bd6/tensorflow/python/keras/applications/imagenet_utils.py).


#### enjoy!

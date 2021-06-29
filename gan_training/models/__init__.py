from gan_training.models import (
    mlnet
)

generator_dict = {
    'mlnet' : mlnet.Generator
}

discriminator_dict = {
    'mlnet' : mlnet.Discriminator
}

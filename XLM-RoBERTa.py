import torch
xlmr = torch.hub.load('pytorch/fairseq:main', 'xlmr.large')
xlmr.eval()  # disable dropout (or leave in train mode to finetune)

# Download xlmr.large model
wget https://dl.fbaipublicfiles.com/fairseq/models/xlmr.large.tar.gz
tar -xzvf xlmr.large.tar.gz

# Load the model in fairseq
from fairseq.models.roberta import XLMRModel
xlmr = XLMRModel.from_pretrained('/path/to/xlmr.large', checkpoint_file='model.pt')
xlmr.eval()  # disable dropout (or leave in train mode to finetune)


ar_tokens = xlmr.encode('مرحبا بالعالم')
assert ar_tokens.tolist() == [0, 665, 193478, 258, 1705, 77796, 2]
xlmr.decode(ar_tokens) # 'مرحبا بالعالم'


# Extract the last layer's features
last_layer_features = xlmr.extract_features(zh_tokens)
assert last_layer_features.size() == torch.Size([1, 6, 1024])

# Extract all layer's features (layer 0 is the embedding layer)
all_layers = xlmr.extract_features(zh_tokens, return_all_hiddens=True)
assert len(all_layers) == 25
assert torch.all(all_layers[-1] == last_layer_features)

@article{conneau2019unsupervised,
  title={Unsupervised Cross-lingual Representation Learning at Scale},
  author={Conneau, Alexis and Khandelwal, Kartikay and Goyal, Naman and Chaudhary, Vishrav and Wenzek, Guillaume and Guzm{\'a}n, Francisco and Grave, Edouard and Ott, Myle and Zettlemoyer, Luke and Stoyanov, Veselin},
  journal={arXiv preprint arXiv:1911.02116},
  year={2019}
}

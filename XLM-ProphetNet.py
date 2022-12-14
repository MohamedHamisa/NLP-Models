from transformers import XLMProphetNetTokenizer, XLMProphetNetForCausalLM
import torch

tokenizer = XLMProphetNetTokenizer.from_pretrained("microsoft/xprophetnet-large-wiki100-cased")
model = XLMProphetNetForCausalLM.from_pretrained("microsoft/xprophetnet-large-wiki100-cased")
assert model.config.is_decoder, f"{model.__class__} has to be configured as a decoder."
inputs = tokenizer("Hello, my dog is cute", return_tensors="pt")
outputs = model(**inputs)

logits = outputs.logits

# Model can also be used with EncoderDecoder framework
from transformers import EncoderDecoderModel, XLMProphetNetTokenizer, XLMRobertaTokenizer
import torch

tokenizer_enc = XLMRobertaTokenizer.from_pretrained("xlm-roberta-large")
tokenizer_dec = XLMProphetNetTokenizer.from_pretrained("microsoft/xprophetnet-large-wiki100-cased")
model = EncoderDecoderModel.from_encoder_decoder_pretrained(
    "xlm-roberta-large", "microsoft/xprophetnet-large-wiki100-cased"
)

ARTICLE = (
    "the us state department said wednesday it had received no "
    "formal word from bolivia that it was expelling the us ambassador there "
    "but said the charges made against him are `` baseless ."
)
input_ids = tokenizer_enc(ARTICLE, return_tensors="pt").input_ids
labels = tokenizer_dec("us rejects charges against its ambassador in bolivia", return_tensors="pt").input_ids
outputs = model(input_ids=input_ids, decoder_input_ids=labels[:, :-1], labels=labels[:, 1:])

loss = outputs.loss

#!pip install transformers -U -q
#an unsupervised text tokenizer and detokenizer mainly for Neural Network-based text generation systems
#where the vocabulary size is predetermined prior to the neural model training
! pip install sentencepiece
!pip freeze | grep transformers 
#adding the possibility of "freezing" the connector and transformer wires to prevent other connector wires from connecting to them
from transformers import MBartForConditionalGeneration, MBart50TokenizerFast

model = MBartForConditionalGeneration.from_pretrained("facebook/mbart-large-50-one-to-many-mmt")
tokenizer = MBart50TokenizerFast.from_pretrained("facebook/mbart-large-50-one-to-many-mmt", src_lang="en_XX")
article_en = "U.N encourages wearing masks"
model_inputs = tokenizer(article_en, return_tensors="pt")

generated_tokens = model.generate(
    **model_inputs,
    forced_bos_token_id=tokenizer.lang_code_to_id["ar_AR"]
)
translation = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)

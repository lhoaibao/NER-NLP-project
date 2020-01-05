import torch
import numpy as np
from pytorch_pretrained_bert import BertTokenizer
from keras.preprocessing.sequence import pad_sequences

class ParseData():
    def __init__(self, txt):
        self.sentence = txt
        self.tags_vals = ['B-org',
        'B-gpe',
        'I-art',
        'I-tim',
        'I-eve',
        'B-eve',
        'I-org',
        'B-per',
        'I-nat',
        'B-art',
        'I-per',
        'B-nat',
        'I-geo',
        'B-tim',
        'B-geo',
        'I-gpe',
        'O']

    def process(self):
        model = torch.load("./ner.pt", map_location=torch.device('cpu'))
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        predictions = []
        tokenizer = BertTokenizer.from_pretrained('bert-base-uncased', do_lower_case=True)
        tokenized_txt = [tokenizer.tokenize(self.sentence)]
        input_id = pad_sequences([tokenizer.convert_tokens_to_ids(self.sentence) for self.sentence in tokenized_txt],
                                maxlen=75, dtype="long", truncating="post", padding="post")
        input_id = torch.tensor(input_id).to(device)
        attention_mask1 = [[float(i>0) for i in ii] for ii in input_id]
        attention_mask1 = torch.tensor(attention_mask1).to(device)
        logits = model(input_id, token_type_ids=None,
                            attention_mask=attention_mask1)
        logits = logits.detach().cpu().numpy()
        predictions.extend([list(p) for p in np.argmax(logits, axis=2)])
        pred_tags = [[self.tags_vals[p_i] for p_i in p] for p in predictions]
        return [{"word":tokenized_txt[0][i], "label":x} for i, x in enumerate(pred_tags[0]) if i < len(tokenized_txt[0]) and x != 'O']
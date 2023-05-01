import torch
from transformers import BertModel, BertTokenizer, ElectraModel, ElectraTokenizer
#
# # BERT tokenizer와 model 로드
# tokenizer = ElectraTokenizer.from_pretrained("monologg/koelectra-base-v3-discriminator" )
# model = ElectraModel.from_pretrained("monologg/koelectra-base-v3-discriminator", output_hidden_states=True)
#
# model2 = ElectraModel.from_pretrained("monologg/koelectra-base-v3-discriminator", output_hidden_states=True)
# # model2.load_state_dict(torch.load('/data/KLUE-baseline/dp/klue_output0000/klue-dp/version_1/checkpoint/epoch=09-step=4064=valid/las_macro_f1=81.13.ckpt'), strict=False)
# model3 = torch.load("/data/KLUE-baseline/dp/klue_output_full/klue-dp/version_0/checkpoint/epoch=08-step=3543=valid/las_macro_f1=81.92.ckpt")
#
# for n, p in model.named_parameters():
#     print(n)
#
# for pt in model3['state_dict']:
#     print(pt)
# # print(model3)
# input()
#
# # 입력 문장 인코딩
# input_text = "세상에 비호감 딱 두 명있대"
# inputs = tokenizer(input_text, return_tensors='pt')
# input_ids = inputs['input_ids']
#
# # BERT 모델에 입력 문장 인코딩 후 전달
# outputs = model(input_ids, output_hidden_states=True)
# outputs2 = model2(input_ids, output_hidden_states=True)
#
# # hidden state 값 추출
# hidden_states = outputs[2]
# hidden_states2 = outputs2[2]
#
#
# # 첫 번째 레이어의 hidden state 값 출력
# print(hidden_states[0]==hidden_states2[0])

import os
os.environ["CUDA_VISIBLE_DEVICES"] = "0"
model_ = BertModel.from_pretrained('klue/bert-base')

# self.model.load_state_dict(torch.load(r"/data/KLUE-baseline/dp/klue_output111/klue-dp/version_3/checkpoint/epoch=09-step=4168=valid/las_macro_f1=87.41.ckpt"), strict=False)
# self.model_.load_state_dict(torch.load(r"/data/KLUE-baseline/dp/bert_all_train/klue-dp/version_0/checkpoint/epoch=04-step=2083=valid/las_macro_f1=87.83.ckpt"),strict=False)

model_.load_state_dict(torch.load(r"/data/KLUE-baseline/dp/bert_all_train/klue-dp/version_0/checkpoint/epoch=04-step=2083=valid/las_macro_f1=87.83.ckpt"),strict=False)

no_update = ["layer.0."]
#
# Frozen
for n, p in model_.named_parameters():
    for layer in no_update:
        if layer in n:
            print(n, p)
            input()
            p.requires_grad = False
# Layer-wise_Fine-tuning_Based_Pre-trained-Language-Model-Knowledge
✏ KIICE2023 논문 repo

#### 이 논문은 [KLUE-baseline](https://github.com/KLUE-benchmark/KLUE-baseline) 을 기반하여 실험했습니다.

## File Direcotry
```bash
├── data/klue_benchmark
│   ├── klue-dp-v1.1
│   └── klue-dp-v1.1
├── klue-baseline
│   ├── data
│   │  ├── base.py
│   │  ├── klue_dp.py
│   │  ├── klue_mrc.py
│   │  ├── klue_ner.py
│   │  ├── klue_nli.py
│   │  ├── klue_re.py
│   │  ├── klue_sts.py
│   │  ├── utils.py
│   │  ├── wos.py
│   │  └── ynat.py
│   ├── metrics
│   │  ├── init.py
│   │  ├── base.py
│   │  ├── functional.py
│   │  └── utils.py
│   ├── models
│   └── utils
│   ├── models
│   │  ├── __init__.py
│   │  ├── dependecny_parsing.py
│   │  ├── dialogue_state_tracking.py
│   │  ├── **lightning_base.py**
│   │  ├── machine_reading_comprehension.py
│   │  ├── mode.py
│   │  ├── named_entity_recognition.py
│   │  ├── relation_extraction.py
│   │  ├── semantic_textual_similarity.py
│   │  └── sequence_calssification.py
│   ├── utils
│   │  ├── __init__.py
│   │  └── task.py
├── mypy.ini
├── pyproject.toml
├── requirements-dev.txt
├── requirements-dev.txt
├── run_all.sh
├── run_klue.sh
├── setup.cfg
└── test.py
``` 

# Abstract
Pre-trained language models make it easier to perform a variety of natural language processing tasks. Typically, the model is further trained and used through a task-specific fine-tuning process, and due to the structure of the pre-trained language model, training occurs through the interaction of multiple deep learning layers. In order to reduce the gap between adjacent layers, traditional models refine the model only for that task when performing any one task.
In this paper, we propose a new paradigm for this traditional training approach. Previous studies has shown that higher ans lower layers within a model can play different roles as the model trains data. Based on this, we propose a model learning approach that injects morphological information into lower layers and then fine-tunes semantic tasks based on the injected information. In this study, we found that the proposed method improved performance on three tasks in the KLUE benchmark: MRC, NLI, and STS. The methodology presented can provide more flexible insights for fine-tuning, and further performance gains can be expected through techniques to handle the injected information more efficiently.

---
# Model
<img src="https://github.com/HyeLynnKIM/Layer-wise_Fine-tuning_Based_Pre-trained-Language-Model-Knowledge/assets/64192139/2ca5bc54-3755-4485-b0bf-37d180588b01" width=40%>

#### [그림 1] 모델 학습 구조도 (MRC 기준)

---
# Version
```bash
pip install -r requirements.txt
``` 

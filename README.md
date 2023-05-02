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
│   │  ├── *lightning_base.py*
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


---
# Version
'''
pip install -r requirements.txt
'''

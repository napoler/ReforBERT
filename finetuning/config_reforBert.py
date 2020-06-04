# coding=utf-8
# Copyright 2018 The Google AI Language Team Authors and The HuggingFace Inc. team.
# Copyright (c) 2018, NVIDIA CORPORATION.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
""" reforBERT model configuration """
import logging
from transformers.configuration_utils import PretrainedConfig

logger = logging.getLogger(__name__)

reforBERT_PRETRAINED_CONFIG_ARCHIVE_MAP = {
    "reforBert-base": "./config/reforBert-config.json",
}

class ReforBertConfig(PretrainedConfig):
    pretrained_config_archive_map = reforBERT_PRETRAINED_CONFIG_ARCHIVE_MAP
    model_type = "reforBert"

    def __init__(
        self,
        vocab_size=8007,  # vocab 크기
        hidden_size=768,   # 임베딩 사이즈
        max_seq_len = 512,  # 최대 입력 길이
        depth = 6,  # reformer depth
        heads = 8,  # reformer heads
        causal=True,
        **kwargs
    ):
        super().__init__(**kwargs)

        self.vocab_size = vocab_size
        self.hidden_size = hidden_size
        self.max_seq_len = max_seq_len
        self.depth = depth
        self.heads = heads
        self.causal = causal
